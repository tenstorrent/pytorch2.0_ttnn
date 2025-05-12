# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._to_copy.default          |                 11 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten._unsafe_view.default      |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.add.Tensor                |                 11 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.addmm.default             |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.bmm.default               |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.cat.default               |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.clone.default             |                 10 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.cumsum.default            |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.div.Tensor                |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.embedding.default         |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.eq.Scalar                 |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.expand.default            |                 12 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.gt.Scalar                 |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.index.Tensor              |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.masked_fill.Scalar        |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.mm.default                |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.mul.Tensor                |                 13 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.native_layer_norm.default |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.neg.default               |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.new_ones.default          |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.permute.default           |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.pow.Tensor_Scalar         |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.rsub.Scalar               |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.select.int                |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.slice.Tensor              |                 45 |           0 |         0 |          0 | ✘           |       0 |
| 26 | aten.split.Tensor              |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 27 | aten.stack.default             |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 28 | aten.sub.Tensor                |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 29 | aten.sum.default               |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 30 | aten.sym_size.int              |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 31 | aten.t.default                 |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 32 | aten.tanh.default              |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 33 | aten.transpose.int             |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 34 | aten.unsqueeze.default         |                 10 |           0 |         0 |          0 | ✘           |       0 |
| 35 | aten.view.default              |                 44 |           0 |         0 |          0 | ✘           |       0 |
| 36 | aten.where.self                |                  3 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                                | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 16, 1, 6]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9996742205481157 | -1     |
|  1 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 16, 5, 5]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9996043922487964 | -1     |
### aten._to_copy.default
|    | ATen Input Variations                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 5]> self = ?,<br>Optional[int] dtype = torch.bfloat16         | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, 6]> self = ?,<br>Optional[int] dtype = torch.bfloat16         | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16   | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 51200]> self = ?,<br>Optional[int] dtype = torch.float32         | Unknown  | Fallback   | 1.0   | -1     |
|  4 | Tensor<[1, 16, 1, 6]> self = ?,<br>Optional[int] dtype = torch.bfloat16        | Unknown  | Fallback   | 1.0   | -1     |
|  5 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16  | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 16, 5, 5]> self = ?,<br>Optional[int] dtype = torch.bfloat16        | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 16, 5, 64]> self = ?,<br>Optional[int] dtype = torch.bfloat16       | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 16, 6, 64]> self = ?,<br>Optional[int] dtype = torch.bfloat16       | Unknown  | Fallback   | 1.0   | -1     |
|  9 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 5, 51200]> self = ?,<br>Optional[int] dtype = torch.float32         | Unknown  | Unknown    | N/A   | N/A    |
### aten._unsafe_view.default
|    | ATen Input Variations                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 4, 4, 64]> self = ?,<br>List[int] size = [1, 1, 16, 64] | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 5, 4, 4, 64]> self = ?,<br>List[int] size = [1, 5, 16, 64] | Unknown  | Done       |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?              | Unknown  | Done       | 0.999997708526932  | -1     |
|  1 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 16, 32]> other = ?          | Unknown  | Done       | 0.9999975131988779 | -1     |
|  2 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.9999942810115126 | -1     |
|  3 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?              | Unknown  | Done       | 0.999997859191166  | -1     |
|  4 | Tensor<[1, 16, 1, 6]> self = ?,<br>Tensor<[1, 1, 1, 6]> other = ?             | Unknown  | Done       | 0.9999971567390962 | -1     |
|  5 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[1, 1, 1, 5]> other = ?             | Unknown  | Done       | 0.9999976072045348 | -1     |
|  7 | Tensor<[1, 5, 1024]> self = ?,<br>Tensor<[1, 5, 1024]> other = ?              | Unknown  | Done       | 0.9999977947563233 | -1     |
|  8 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 16, 32]> other = ?          | Unknown  | Done       | 0.9999978494634207 | -1     |
|  9 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.9999948051872644 | -1     |
| 10 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?              | Unknown  | Done       | 0.9999979829417085 | -1     |
### aten.addmm.default
|    | ATen Input Variations                                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1024]> self = ?,<br>Tensor<[1, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ?   | Unknown  | Done       | 0.999933 |     -1 |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[5, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ?   | Unknown  | Done       | 0.999934 |     -1 |
|  2 | Tensor<[4096]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ?   | Unknown  | Done       | 0.999964 |     -1 |
|  3 | Tensor<[4096]> self = ?,<br>Tensor<[5, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ?   | Unknown  | Done       | 0.999964 |     -1 |
|  4 | Tensor<[51200]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 51200]> mat2 = ? | Unknown  | Done       | 0.999964 |     -1 |
|  5 | Tensor<[51200]> self = ?,<br>Tensor<[5, 1024]> mat1 = ?,<br>Tensor<[1024, 51200]> mat2 = ? | Unknown  | Done       | 0.999964 |     -1 |
### aten.bmm.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 6]> mat2 = ?            | Unknown  | Done       | 0.9999873246382998 | -1     |
|  1 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, s10 + 1]> mat2 = ?      | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[16, 1, 6]> self = ?,<br>Tensor<[16, 6, 64]> mat2 = ?             | Unknown  | Done       | 0.9999931354183943 | -1     |
|  3 | Tensor<[16, 1, s10 + 1]> self = ?,<br>Tensor<[16, s10 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[16, 5, 5]> self = ?,<br>Tensor<[16, 5, 64]> mat2 = ?             | Unknown  | Done       | 0.9999918956838406 | -1     |
|  5 | Tensor<[16, 5, 64]> self = ?,<br>Tensor<[16, 64, 5]> mat2 = ?            | Unknown  | Done       | 0.9999874184402366 | -1     |
### aten.cat.default
|    | ATen Input Variations                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 1, 16, 32]>, <[1, 1, 16, 32]>],<br>int dim = -1   | Unknown  | Done       | 1.0   | -1     |
|  1 | List[Tensor] tensors = [<[1, 16, 5, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2   | Unknown  | Done       | 1.0   | -1     |
|  2 | List[Tensor] tensors = [<[1, 16, s10, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | List[Tensor] tensors = [<[1, 5, 16, 32]>, <[1, 5, 16, 32]>],<br>int dim = -1   | Unknown  | Done       | 1.0   | -1     |
|  4 | List[Tensor] tensors = [<[1, 5]>, <[1, 1]>],<br>int dim = -1                   | Unknown  | Failed     | N/A   | N/A    |
|  5 | List[Tensor] tensors = [<[1, s40]>, <[1, 1]>],<br>int dim = -1                 | Unknown  | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 16, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1, 1024]> self = ?                                                               | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 1, 4, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 16, 1, 6]> self = ?                                                              | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 16, 1, s10 + 1]> self = ?                                                        | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 16, 5, 5]> self = ?                                                              | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 5, 1, 16, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 5, 1024]> self = ?                                                               | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 5, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 5, 4, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       | 1.0   | -1     |
### aten.cumsum.default
|    | ATen Input Variations                     | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 5]> self = ?,<br>int dim = -1  | Unknown  | Done       | 0.9999975343802608 | -1     |
|  1 | Tensor<[1, s0]> self = ?,<br>int dim = -1 | Unknown  | Unknown    | N/A                | N/A    |
### aten.div.Tensor
|    | ATen Input Variations                                         | Status   | Isolated   | PCC                | Host   |
|---:|:--------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 16, 1, 6]> self = ?,<br>Tensor<[]> other = ?       | Unknown  | Done       | 0.9999962069066549 | -1     |
|  1 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[]> other = ?       | Unknown  | Done       | 0.9999965866281796 | -1     |
### aten.embedding.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[51200, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ? | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[51200, 1024]> weight = ?,<br>Tensor<[1, 5]> indices = ? | Unknown  | Done       |     1 |     -1 |
### aten.eq.Scalar
|    | ATen Input Variations                         | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 5]> self = ?,<br>number other = 0  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, s0]> self = ?,<br>number other = 0 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1]> self = ?,<br>number other = 50256 | Unknown  | Done       | 1.0   | -1     |
### aten.expand.default
|    | ATen Input Variations                                                             | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 16, 1]> self = ?,<br>List[int] size = [1, 1, 1, 16, 2]           | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [1, 16, 1, 64]               | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 16, 1, 6]> self = ?,<br>List[int] size = [1, 16, 1, 6]                 | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 16, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 16, 5, 5]> self = ?,<br>List[int] size = [1, 16, 5, 5]                 | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 16, 5, 64]> self = ?,<br>List[int] size = [1, 16, 5, 64]               | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 16, 6, 64]> self = ?,<br>List[int] size = [1, 16, 6, 64]               | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 16, 64, 5]> self = ?,<br>List[int] size = [1, 16, 64, 5]               | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 16, 64, 6]> self = ?,<br>List[int] size = [1, 16, 64, 6]               | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 16, 64, s10 + 1]> self = ?,<br>List[int] size = [1, 16, 64, <s10 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>List[int] size = [1, 16, <s10 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 5, 1, 16, 1]> self = ?,<br>List[int] size = [1, 5, 1, 16, 2]           | Unknown  | Done       | 1.0   | -1     |
### aten.gt.Scalar
|    | ATen Input Variations                    | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[]> self = ?,<br>number other = 0 | Unknown  | Fallback   |     1 |     -1 |
### aten.index.Tensor
|    | ATen Input Variations                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2048, 32]> self = ?,<br>List[Optional[Tensor]] indices = [<[1, 1]>] | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[2048, 32]> self = ?,<br>List[Optional[Tensor]] indices = [<[1, 5]>] | Unknown  | Done       |     1 |     -1 |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 5]> self = ?,<br>Tensor<[1, 5]> mask = ?,<br>number value = 1   | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, s0]> self = ?,<br>Tensor<[1, s0]> mask = ?,<br>number value = 1 | Unknown  | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Unknown  | Done       | 0.999962 |     -1 |
|  1 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 3072]> mat2 = ? | Unknown  | Done       | 0.999965 |     -1 |
|  2 | Tensor<[5, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Unknown  | Done       | 0.999967 |     -1 |
|  3 | Tensor<[5, 1024]> self = ?,<br>Tensor<[1024, 3072]> mat2 = ? | Unknown  | Done       | 0.999966 |     -1 |
### aten.mul.Tensor
|    | ATen Input Variations                                                          | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1, 5]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 0.9999908006597918 | -1     |
|  1 | Tensor<[1, 1, 1, 6]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 0.9999950086683703 | -1     |
|  2 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 1, 32]> other = ?            | Unknown  | Done       | 0.9999957368876484 | -1     |
|  4 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999952655493477 | -1     |
|  5 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                | -1     |
|  6 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999971557849855 | -1     |
|  7 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?               | Unknown  | Done       | 0.9999958585306314 | -1     |
|  8 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 1, 32]> other = ?            | Unknown  | Done       | 0.9999956830528524 | -1     |
|  9 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999953276138621 | -1     |
| 10 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                | -1     |
| 11 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999972260011082 | -1     |
| 12 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?               | Unknown  | Done       | 0.9999961417995408 | -1     |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                      | Status   | Isolated   | PCC   |   Host |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 1, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05 | Unknown  | Done       | N/A   |      0 |
|  1 | Tensor<[1, 5, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05 | Unknown  | Done       | N/A   |      0 |
### aten.neg.default
|    | ATen Input Variations           | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 16, 16]> self = ? | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 5, 16, 16]> self = ? | Unknown  | Done       |     1 |     -1 |
### aten.new_ones.default
|    | ATen Input Variations                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 5]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False   | Unknown  | Fallback   | 1.0   | -1     |
|  1 | Tensor<[1, s40]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.permute.default
|    | ATen Input Variations                                             | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 16, 5, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 5, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  | Done       |     1 |     -1 |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                   | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 4096]> self = ?,<br>number exponent = 3.0 | Unknown  | Done       | 0.999996 |     -1 |
|  1 | Tensor<[1, 5, 4096]> self = ?,<br>number exponent = 3.0 | Unknown  | Done       | 0.999996 |     -1 |
### aten.rsub.Scalar
|    | ATen Input Variations                                      | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1, 5]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 0.9999995124009606 | -1     |
|  1 | Tensor<[1, 1, 1, 6]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 0.9999825264946388 | -1     |
|  2 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A                | N/A    |
### aten.select.int
|    | ATen Input Variations                                      | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 5]> self = ?,<br>int dim = 1,<br>int index = -1 | Unknown  | Done       |     1 |     -1 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 16]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 6                                   | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int]<s10 + 1> end = ?                          | Unknown  | Failed     | N/A   | N/A    |
|  3 | Tensor<[1, 1, 1, 5]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 1, 1, 6]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807              | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | Unknown  | Fallback   | 1.0   | -1     |
| 10 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | Unknown  | Fallback   | 1.0   | -1     |
| 11 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 12 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 13 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 14 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                                   | Unknown  | Done       | 1.0   | -1     |
| 15 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 32,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Done       | 1.0   | -1     |
| 16 | Tensor<[1, 1, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Done       | 1.0   | -1     |
| 17 | Tensor<[1, 1, 16]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Done       | 1.0   | -1     |
| 18 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807              | Unknown  | Done       | 1.0   | -1     |
| 19 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807              | Unknown  | Done       | 1.0   | -1     |
| 20 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 5                                | Unknown  | Done       | 1.0   | -1     |
| 21 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 5,<br>Optional[int] end = 6                                | Unknown  | Done       | 1.0   | -1     |
| 22 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int]<s10> start = ?,<br>Optional[int]<s10 + 1> end = ?                  | Unknown  | Failed     | N/A   | N/A    |
| 23 | Tensor<[1, 1, 5, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 5                                   | Unknown  | Done       | 1.0   | -1     |
| 24 | Tensor<[1, 5, 1, 16]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Done       | 1.0   | -1     |
| 25 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 26 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 27 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 28 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | Unknown  | Fallback   | 1.0   | -1     |
| 29 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | Unknown  | Fallback   | 1.0   | -1     |
| 30 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 31 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 32 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 33 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                                   | Unknown  | Done       | 1.0   | -1     |
| 34 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 32,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Done       | 1.0   | -1     |
| 35 | Tensor<[1, 5, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Done       | 1.0   | -1     |
| 36 | Tensor<[1, 5, 16]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Done       | 1.0   | -1     |
| 37 | Tensor<[1, 5]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Done       | 1.0   | -1     |
| 38 | Tensor<[1, 6]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Done       | 1.0   | -1     |
| 39 | Tensor<[1, 6]> self = ?,<br>int dim = 1,<br>Optional[int] start = 5,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Done       | 1.0   | -1     |
| 40 | Tensor<[1, s0]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                         | Unknown  | Unknown    | N/A   | N/A    |
| 41 | Tensor<[1, s0]> self = ?,<br>int dim = 1,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                        | Unknown  | Unknown    | N/A   | N/A    |
| 42 | Tensor<[1, s1 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Unknown    | N/A   | N/A    |
| 43 | Tensor<[1, s1 + 1]> self = ?,<br>int dim = 1,<br>Optional[int]<s1> start = ?,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Unknown    | N/A   | N/A    |
| 44 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Unknown    | N/A   | N/A    |
### aten.split.Tensor
|    | ATen Input Variations                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>int split_size = 16,<br>int dim = -1      | Unknown  | Done       |     1 |     -2 |
|  1 | Tensor<[1, 1, 4, 768]> self = ?,<br>int split_size = 256,<br>int dim = -1 | Unknown  | Done       |     1 |     -3 |
|  2 | Tensor<[1, 5, 32]> self = ?,<br>int split_size = 16,<br>int dim = -1      | Unknown  | Done       |     1 |     -2 |
|  3 | Tensor<[1, 5, 4, 768]> self = ?,<br>int split_size = 256,<br>int dim = -1 | Unknown  | Done       |     1 |     -3 |
### aten.stack.default
|    | ATen Input Variations                                                        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 1, 16, 16]>, <[1, 1, 16, 16]>],<br>int dim = -1 | Unknown  | Done       |     1 |     -1 |
|  1 | List[Tensor] tensors = [<[1, 5, 16, 16]>, <[1, 5, 16, 16]>],<br>int dim = -1 | Unknown  | Done       |     1 |     -1 |
### aten.sub.Tensor
|    | ATen Input Variations                         | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 5]> self = ?,<br>Tensor other = 1  | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, s0]> self = ?,<br>Tensor other = 1 | Unknown  | Unknown    | N/A   | N/A    |
### aten.sum.default
|    | ATen Input Variations   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1]> self = ?    | Unknown  | Done       |     1 |     -1 |
### aten.sym_size.int
|    | ATen Input Variations                                 | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>int dim = 3   | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations          | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1024, 1024]> self = ?  | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[1024, 4096]> self = ?  | Unknown  | Done       |     1 |     -1 |
|  2 | Tensor<[3072, 1024]> self = ?  | Unknown  | Done       |     1 |     -1 |
|  3 | Tensor<[4096, 1024]> self = ?  | Unknown  | Done       |     1 |     -1 |
|  4 | Tensor<[51200, 1024]> self = ? | Unknown  | Done       |     1 |     -1 |
### aten.tanh.default
|    | ATen Input Variations         | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 4096]> self = ? | Unknown  | Done       | 0.999945 |     -1 |
|  1 | Tensor<[1, 5, 4096]> self = ? | Unknown  | Done       | 0.999942 |     -1 |
### aten.transpose.int
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16, 5, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 16, 6, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 16]> self = ?,<br>int dim = 4   | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1, 16]> self = ?,<br>int dim = 2      | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 1, 5]> self = ?,<br>int dim = 2       | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 1, 6]> self = ?,<br>int dim = 2       | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 1, s10 + 1]> self = ?,<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 5, 1, 16]> self = ?,<br>int dim = 4   | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 5, 16]> self = ?,<br>int dim = 2      | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 5]> self = ?,<br>int dim = 1          | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 6]> self = ?,<br>int dim = 1          | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1    | Unknown  | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 16, 2]> self = ?,<br>List[int] size = [1, 1, 1, 32]           | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1, 1024]                | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1024]                   | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 1, 16, 16, 2]> self = ?,<br>List[int] size = [1, 1, 16, 32]         | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 1, 16, 64]> self = ?,<br>List[int] size = [1, 1, 1024]              | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 1, 4, -1]               | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 1, 4, 256]> self = ?,<br>List[int] size = [1, 1, 4, 4, 64]          | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 1, 4096]> self = ?,<br>List[int] size = [1, 4096]                   | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1, 1, 1024]                   | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [16, 1, 64]               | Unknown  | Done       | 1.0   | -1     |
| 10 | Tensor<[1, 16, 1, 6]> self = ?,<br>List[int] size = [16, 1, 6]                 | Unknown  | Done       | 1.0   | -1     |
| 11 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>List[int] size = [16, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 16, 5, 5]> self = ?,<br>List[int] size = [16, 5, 5]                 | Unknown  | Done       | 1.0   | -1     |
| 13 | Tensor<[1, 16, 5, 64]> self = ?,<br>List[int] size = [16, 5, 64]               | Unknown  | Done       | 1.0   | -1     |
| 14 | Tensor<[1, 16, 6, 64]> self = ?,<br>List[int] size = [16, 6, 64]               | Unknown  | Done       | 1.0   | -1     |
| 15 | Tensor<[1, 16, 64, 5]> self = ?,<br>List[int] size = [16, 64, 5]               | Unknown  | Done       | 1.0   | -1     |
| 16 | Tensor<[1, 16, 64, 6]> self = ?,<br>List[int] size = [16, 64, 6]               | Unknown  | Done       | 1.0   | -1     |
| 17 | Tensor<[1, 16, 64, s10 + 1]> self = ?,<br>List[int] size = [16, 64, <s10 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>List[int] size = [16, <s10 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                           | Unknown  | Done       | 1.0   | -1     |
| 20 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [1, 1, 3072]                   | Unknown  | Done       | 1.0   | -1     |
| 21 | Tensor<[1, 4096]> self = ?,<br>List[int] size = [1, 1, 4096]                   | Unknown  | Done       | 1.0   | -1     |
| 22 | Tensor<[1, 5, 1, 16, 2]> self = ?,<br>List[int] size = [1, 5, 1, 32]           | Unknown  | Done       | 1.0   | -1     |
| 23 | Tensor<[1, 5, 1024]> self = ?,<br>List[int] size = [1, 5, 1024]                | Unknown  | Done       | 1.0   | -1     |
| 24 | Tensor<[1, 5, 1024]> self = ?,<br>List[int] size = [5, 1024]                   | Unknown  | Done       | 1.0   | -1     |
| 25 | Tensor<[1, 5, 16, 16, 2]> self = ?,<br>List[int] size = [1, 5, 16, 32]         | Unknown  | Done       | 1.0   | -1     |
| 26 | Tensor<[1, 5, 16, 64]> self = ?,<br>List[int] size = [1, 5, 1024]              | Unknown  | Done       | 1.0   | -1     |
| 27 | Tensor<[1, 5, 3072]> self = ?,<br>List[int] size = [1, 5, 4, -1]               | Unknown  | Done       | 1.0   | -1     |
| 28 | Tensor<[1, 5, 4, 256]> self = ?,<br>List[int] size = [1, 5, 4, 4, 64]          | Unknown  | Done       | 1.0   | -1     |
| 29 | Tensor<[1, 5, 4096]> self = ?,<br>List[int] size = [5, 4096]                   | Unknown  | Done       | 1.0   | -1     |
| 30 | Tensor<[1, 51200]> self = ?,<br>List[int] size = [1, 1, 51200]                 | Unknown  | Done       | 1.0   | -1     |
| 31 | Tensor<[1, 5]> self = ?,<br>List[int] size = [-1, 5]                           | Unknown  | Done       | 1.0   | -1     |
| 32 | Tensor<[1, 5]> self = ?,<br>List[int] size = [1, -1]                           | Unknown  | Done       | 1.0   | -1     |
| 33 | Tensor<[1, 6]> self = ?,<br>List[int] size = [1, -1]                           | Unknown  | Done       | 1.0   | -1     |
| 34 | Tensor<[1, s10 + 1]> self = ?,<br>List[int] size = [1, -1]                     | Unknown  | Unknown    | N/A   | N/A    |
| 35 | Tensor<[16, 1, 64]> self = ?,<br>List[int] size = [1, 16, 1, 64]               | Unknown  | Done       | 1.0   | -1     |
| 36 | Tensor<[16, 1, 6]> self = ?,<br>List[int] size = [1, 16, 1, 6]                 | Unknown  | Done       | 1.0   | -1     |
| 37 | Tensor<[16, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 16, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
| 38 | Tensor<[16, 5, 5]> self = ?,<br>List[int] size = [1, 16, 5, 5]                 | Unknown  | Done       | 1.0   | -1     |
| 39 | Tensor<[16, 5, 64]> self = ?,<br>List[int] size = [1, 16, 5, 64]               | Unknown  | Done       | 1.0   | -1     |
| 40 | Tensor<[5, 1024]> self = ?,<br>List[int] size = [1, 5, 1024]                   | Unknown  | Done       | 1.0   | -1     |
| 41 | Tensor<[5, 3072]> self = ?,<br>List[int] size = [1, 5, 3072]                   | Unknown  | Done       | 1.0   | -1     |
| 42 | Tensor<[5, 4096]> self = ?,<br>List[int] size = [1, 5, 4096]                   | Unknown  | Done       | 1.0   | -1     |
| 43 | Tensor<[5, 51200]> self = ?,<br>List[int] size = [1, 5, 51200]                 | Unknown  | Done       | 1.0   | -1     |
### aten.where.self
|    | ATen Input Variations                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 6]> condition = ?,<br>Tensor<[1, 16, 1, 6]> self = ?,<br>Tensor other = ?             | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, s10 + 1]> condition = ?,<br>Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 5, 5]> condition = ?,<br>Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor other = ?             | Unknown  | Unknown    | N/A   | N/A    |

