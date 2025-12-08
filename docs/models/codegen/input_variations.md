# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._to_copy.default          |                 10 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten._unsafe_view.default      |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.add.Tensor                |                 15 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.addmm.default             |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.any.default               |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.arange.default            |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.bitwise_or.Tensor         |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.bmm.default               |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.cat.default               |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.clone.default             |                 15 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.copy.default              |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.cumsum.default            |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.div.Tensor                |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.embedding.default         |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.eq.Scalar                 |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.expand.default            |                 15 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.full.default              |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.gt.Tensor                 |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.index.Tensor              |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.isin.Tensor_Tensor        |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.lt.Scalar                 |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.masked_fill.Scalar        |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.mm.default                |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.mul.Tensor                |                 13 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.native_layer_norm.default |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 26 | aten.neg.default               |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 27 | aten.new_ones.default          |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 28 | aten.permute.default           |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 29 | aten.pow.Tensor_Scalar         |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 30 | aten.select.int                |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 31 | aten.slice.Tensor              |                 49 |           0 |         0 |          0 | ✘           |       0 |
| 32 | aten.slice_scatter.default     |                  9 |           0 |         0 |          0 | ✘           |       0 |
| 33 | aten.split.Tensor              |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 34 | aten.stack.default             |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 35 | aten.sub.Tensor                |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 36 | aten.t.default                 |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 37 | aten.tanh.default              |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 38 | aten.transpose.int             |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 39 | aten.triu.default              |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 40 | aten.unsqueeze.default         |                 16 |           0 |         0 |          0 | ✘           |       0 |
| 41 | aten.view.default              |                 39 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                               | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 16, 1, 6]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9996064211210685 | 0      |
|  1 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 16, 5, 5]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9996049366152029 | 0      |
### aten._to_copy.default
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 51200]> self = ?,<br>Optional[int] dtype = torch.float32       | Unknown  | Fallback   | 1.0   | -1     |
|  1 | Tensor<[1, 16, 1, 64]> self = ?,<br>Optional[int] dtype = torch.bfloat16     | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 16, 1, 6]> self = ?,<br>Optional[int] dtype = torch.bfloat16      | Unknown  | Fallback   | 1.0   | -1     |
|  3 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 16, 5, 5]> self = ?,<br>Optional[int] dtype = torch.bfloat16      | Unknown  | Fallback   | 1.0   | -1     |
|  5 | Tensor<[1, 16, 5, 64]> self = ?,<br>Optional[int] dtype = torch.bfloat16     | Unknown  | Fallback   | 1.0   | -1     |
|  6 | Tensor<[1, 16, 5, 64]> self = ?,<br>Optional[int] dtype = torch.float32      | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 16, 6, 64]> self = ?,<br>Optional[int] dtype = torch.float32      | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>Optional[int] dtype = torch.float32 | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 5, 51200]> self = ?,<br>Optional[int] dtype = torch.float32       | Unknown  | Fallback   | 1.0   | -1     |
### aten._unsafe_view.default
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 4, 4, 64]> self = ?,<br>List[int] size = [1, 1, 16, 64] | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1, 1, 1024]          | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [1, 1, 3072]          | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 5, 4, 4, 64]> self = ?,<br>List[int] size = [1, 5, 16, 64] | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[5, 1024]> self = ?,<br>List[int] size = [1, 5, 1024]          | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[5, 3072]> self = ?,<br>List[int] size = [1, 5, 3072]          | Unknown  | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1, 6]> self = ?,<br>Tensor<[1, 1, 1, 6]> other = ?            | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?  | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?            | Unknown  | Done       | 0.9999977354837987 | 0      |
|  3 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 16, 32]> other = ?        | Unknown  | Done       | 0.9999980606648985 | 0      |
|  4 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 1.0                        | Unknown  | Done       | 0.9999944170212539 | 0      |
|  5 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?            | Unknown  | Done       | 0.9999980492911931 | 0      |
|  6 | Tensor<[1, 1, 5, 5]> self = ?,<br>Tensor<[1, 1, 1, 5]> other = ?            | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 16, 1, 6]> self = ?,<br>Tensor<[1, 1, 1, 6]> other = ?           | Unknown  | Done       | 0.9999990576792989 | 0      |
|  8 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[1, 1, 5, 5]> other = ?           | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[1, 5, 1024]> self = ?,<br>Tensor<[1, 5, 1024]> other = ?            | Unknown  | Done       | 0.9999981303465112 | 0      |
| 11 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 16, 32]> other = ?        | Unknown  | Done       | 0.9999980180895619 | 0      |
| 12 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 1.0                        | Unknown  | Done       | 0.9999949042737246 | 0      |
| 13 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?            | Unknown  | Done       | 0.9999980832180688 | 0      |
| 14 | Tensor<[1]> self = ?,<br>Tensor other = 1                                   | Unknown  | Unknown    | N/A                | N/A    |
### aten.addmm.default
|    | ATen Input Variations                                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1024]> self = ?,<br>Tensor<[1, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ?   | Unknown  | Done       | 0.999938 |      0 |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[5, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ?   | Unknown  | Done       | 0.999934 |      0 |
|  2 | Tensor<[4096]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ?   | Unknown  | Done       | 0.999963 |      0 |
|  3 | Tensor<[4096]> self = ?,<br>Tensor<[5, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ?   | Unknown  | Done       | 0.999965 |      0 |
|  4 | Tensor<[51200]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 51200]> mat2 = ? | Unknown  | Done       | 0.999964 |      0 |
|  5 | Tensor<[51200]> self = ?,<br>Tensor<[5, 1024]> mat1 = ?,<br>Tensor<[1024, 51200]> mat2 = ? | Unknown  | Done       | 0.999964 |      0 |
### aten.any.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1]> self = ?    | Unknown  | Unknown    | N/A   | N/A    |
### aten.arange.default
|    | ATen Input Variations                                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | number<s0 + 1> end = ?,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.bitwise_or.Tensor
|    | ATen Input Variations                          | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1]> self = ?,<br>Tensor<[1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.bmm.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 6]> mat2 = ?          | Unknown  | Done       | 0.9999879829156241 | 0      |
|  1 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, s0 + 1]> mat2 = ?     | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[16, 1, 6]> self = ?,<br>Tensor<[16, 6, 64]> mat2 = ?           | Unknown  | Done       | 0.999992892109958  | 0      |
|  3 | Tensor<[16, 1, s0 + 1]> self = ?,<br>Tensor<[16, s0 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[16, 5, 5]> self = ?,<br>Tensor<[16, 5, 64]> mat2 = ?           | Unknown  | Done       | 0.9999921927929883 | 0      |
|  5 | Tensor<[16, 5, 64]> self = ?,<br>Tensor<[16, 64, 5]> mat2 = ?          | Unknown  | Done       | 0.9999879290004471 | 0      |
### aten.cat.default
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 1, 16, 32]>, <[1, 1, 16, 32]>],<br>int dim = -1  | Unknown  | Done       | 1.0   | 0      |
|  1 | List[Tensor] tensors = [<[1, 16, 5, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2  | Unknown  | Done       | 1.0   | 0      |
|  2 | List[Tensor] tensors = [<[1, 16, s0, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | List[Tensor] tensors = [<[1, 5, 16, 32]>, <[1, 5, 16, 32]>],<br>int dim = -1  | Unknown  | Done       | 1.0   | 0      |
|  4 | List[Tensor] tensors = [<[1, 5]>, <[1, 1]>],<br>int dim = -1                  | Unknown  | Done       | 1.0   | 0      |
|  5 | List[Tensor] tensors = [<[1, s0]>, <[1, 1]>],<br>int dim = -1                 | Unknown  | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 16, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 1, 6]> self = ?                                                               | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 1, s0 + 1]> self = ?                                                          | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 1024]> self = ?                                                               | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 1, 4, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 1, 5, 5]> self = ?                                                               | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 16, 1, 6]> self = ?                                                              | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 16, 1, s0 + 1]> self = ?                                                         | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 16, 5, 5]> self = ?                                                              | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 1]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 5, 1, 16, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       | 1.0   | 0      |
| 11 | Tensor<[1, 5, 1024]> self = ?                                                               | Unknown  | Done       | 1.0   | 0      |
| 12 | Tensor<[1, 5, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  | Done       | 1.0   | 0      |
| 13 | Tensor<[1, 5, 4, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       | 1.0   | 0      |
| 14 | Tensor<[1, 5]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Unknown  | Unknown    | N/A   | N/A    |
### aten.copy.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 6]> self = ?,<br>Tensor<[1, 1, 1, 6]> src = ?           | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> src = ? | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 5, 5]> self = ?,<br>Tensor<[1, 1, 5, 5]> src = ?           | Unknown  | Unknown    | N/A   | N/A    |
### aten.cumsum.default
|    | ATen Input Variations                     | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 5]> self = ?,<br>int dim = -1  | Unknown  | Done       | 0.9999580850845687 | 0      |
|  1 | Tensor<[1, s1]> self = ?,<br>int dim = -1 | Unknown  | Unknown    | N/A                | N/A    |
### aten.div.Tensor
|    | ATen Input Variations                                        | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 16, 1, 6]> self = ?,<br>Tensor<[]> other = ?      | Unknown  | Done       | 0.9999969044842453 | 0      |
|  1 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Tensor<[]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[]> other = ?      | Unknown  | Done       | 0.9999957750458977 | 0      |
### aten.embedding.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[51200, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ? | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[51200, 1024]> weight = ?,<br>Tensor<[1, 5]> indices = ? | Unknown  | Done       |     1 |      0 |
### aten.eq.Scalar
|    | ATen Input Variations                                   | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 6]> self = ?,<br>number other = 0      | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>number other = 0 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 5, 5]> self = ?,<br>number other = 0      | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 5]> self = ?,<br>number other = 0            | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, s1]> self = ?,<br>number other = 0           | Unknown  | Unknown    | N/A   | N/A    |
### aten.expand.default
|    | ATen Input Variations                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 16, 1]> self = ?,<br>List[int] size = [1, 1, 1, 16, 2]         | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 1, 6]> self = ?,<br>List[int] size = [1, 1, -1, -1]               | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 1, -1, -1]          | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 5, 5]> self = ?,<br>List[int] size = [1, 1, -1, -1]               | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [1, 16, 1, 64]             | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 16, 1, 6]> self = ?,<br>List[int] size = [1, 16, 1, 6]               | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 16, 1, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 16, 5, 5]> self = ?,<br>List[int] size = [1, 16, 5, 5]               | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 16, 5, 64]> self = ?,<br>List[int] size = [1, 16, 5, 64]             | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 16, 6, 64]> self = ?,<br>List[int] size = [1, 16, 6, 64]             | Unknown  | Done       | 1.0   | -1     |
| 10 | Tensor<[1, 16, 64, 5]> self = ?,<br>List[int] size = [1, 16, 64, 5]             | Unknown  | Done       | 1.0   | -1     |
| 11 | Tensor<[1, 16, 64, 6]> self = ?,<br>List[int] size = [1, 16, 64, 6]             | Unknown  | Done       | 1.0   | -1     |
| 12 | Tensor<[1, 16, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 16, 64, <s0 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 16, <s0 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 5, 1, 16, 1]> self = ?,<br>List[int] size = [1, 5, 1, 16, 2]         | Unknown  | Done       | 1.0   | 0      |
### aten.full.default
|    | ATen Input Variations                                                                                                                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [1, 6],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Unknown    | N/A   | N/A    |
|  1 | List[int] size = [1, <s0 + 1>],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
|  2 | List[int] size = [1],<br>number fill_value = False,<br>Optional[int] dtype = torch.bool,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | List[int] size = [1],<br>number<s0 >= 25> fill_value = ?,<br>Optional[int] dtype = torch.bool,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                           | Unknown  | Unknown    | N/A   | N/A    |
|  4 | List[int] size = [5, 5],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Unknown    | N/A   | N/A    |
### aten.gt.Tensor
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[1, 1]> other = ?           | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor self = ?,<br>Tensor<[5, 1]> other = ?           | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[s0 + 1]> self = ?,<br>Tensor<[1, 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.index.Tensor
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 5]> self = ?,<br>List[Optional[Tensor]] indices = [None, <[5]>]  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, s0]> self = ?,<br>List[Optional[Tensor]] indices = [None, <[1]>] | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[2048, 32]> self = ?,<br>List[Optional[Tensor]] indices = [<[1, 1]>] | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[2048, 32]> self = ?,<br>List[Optional[Tensor]] indices = [<[1, 5]>] | Unknown  | Done       | 1.0   | 0      |
### aten.isin.Tensor_Tensor
|    | ATen Input Variations                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1]> elements = ?,<br>Tensor<[1]> test_elements = ? | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1]> elements = ?,<br>Tensor<[]> test_elements = ?  | Unknown  | Unknown    | N/A   | N/A    |
### aten.lt.Scalar
|    | ATen Input Variations                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1]> self = ?,<br>number other = 0 | Unknown  | Unknown    | N/A   | N/A    |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 6]> self = ?,<br>Tensor<[1, 1, 1, 6]> mask = ?,<br>number value = -3.3895313892515355e+38           | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> mask = ?,<br>number value = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 5, 5]> self = ?,<br>Tensor<[1, 1, 5, 5]> mask = ?,<br>number value = -3.3895313892515355e+38           | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 5]> self = ?,<br>Tensor<[1, 5]> mask = ?,<br>number value = 1                                             | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, s1]> self = ?,<br>Tensor<[1, s1]> mask = ?,<br>number value = 1                                           | Unknown  | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Unknown  | Done       | 0.999964 |      0 |
|  1 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 3072]> mat2 = ? | Unknown  | Done       | 0.999965 |      0 |
|  2 | Tensor<[5, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Unknown  | Done       | 0.999965 |      0 |
|  3 | Tensor<[5, 1024]> self = ?,<br>Tensor<[1024, 3072]> mat2 = ? | Unknown  | Done       | 0.999966 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                               | Status   | Isolated   | PCC                | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 1, 32]> other = ? | Unknown  | Done       | 0.9999956487312514 | 0      |
|  1 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.044715           | Unknown  | Done       | 0.9999952124271347 | 0      |
|  2 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.5                | Unknown  | Done       | 1.0                | 0      |
|  3 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.7978845608028654 | Unknown  | Done       | 0.9999968453602969 | 0      |
|  4 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?    | Unknown  | Done       | 0.9999959247960075 | 0      |
|  5 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 1, 32]> other = ? | Unknown  | Done       | 0.999996444730068  | 0      |
|  6 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.044715           | Unknown  | Done       | 0.9999955865594777 | 0      |
|  7 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.5                | Unknown  | Done       | 1.0                | 0      |
|  8 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.7978845608028654 | Unknown  | Done       | 0.9999971305075652 | 0      |
|  9 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?    | Unknown  | Done       | 0.9999960476081742 | 0      |
| 10 | Tensor<[1, 6]> self = ?,<br>Tensor<[1, 6]> other = ?                | Unknown  | Unknown    | N/A                | N/A    |
| 11 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[1, s0 + 1]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 12 | Tensor<[5, 5]> self = ?,<br>Tensor<[5, 5]> other = ?                | Unknown  | Unknown    | N/A                | N/A    |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05 | Unknown  | Done       | 0.999999 |      3 |
|  1 | Tensor<[1, 5, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05 | Unknown  | Done       | 0.996522 |      3 |
### aten.neg.default
|    | ATen Input Variations           | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 16, 16]> self = ? | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 5, 16, 16]> self = ? | Unknown  | Done       |     1 |      0 |
### aten.new_ones.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 5]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False  | Unknown  | Fallback   | 1.0   | -1     |
|  1 | Tensor<[1, s0]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.permute.default
|    | ATen Input Variations                                             | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 16, 5, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 5, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  | Done       |     1 |      0 |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                   | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 4096]> self = ?,<br>number exponent = 3.0 | Unknown  | Done       | 0.999997 |      0 |
|  1 | Tensor<[1, 5, 4096]> self = ?,<br>number exponent = 3.0 | Unknown  | Done       | 0.999996 |      0 |
### aten.select.int
|    | ATen Input Variations                                       | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 6]> self = ?,<br>int dim = 1,<br>int index = -1  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, s0]> self = ?,<br>int dim = 1,<br>int index = -1 | Unknown  | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                                  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, 16]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 1, 1, 5]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 1, 1, 6]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 1, 6]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1, 1, 6]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 1, 1, 6]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807               | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807               | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807               | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807               | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 12 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 13 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 14 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | Unknown  | Done       | 1.0   | 0      |
| 15 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | Unknown  | Done       | 1.0   | 0      |
| 16 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 17 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 18 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 19 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                                   | Unknown  | Done       | 1.0   | 0      |
| 20 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 32,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Done       | 1.0   | 0      |
| 21 | Tensor<[1, 1, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Done       | 1.0   | -1     |
| 22 | Tensor<[1, 1, 16]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Done       | 1.0   | -1     |
| 23 | Tensor<[1, 1, 5, 5]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 1, 5, 5]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Unknown    | N/A   | N/A    |
| 25 | Tensor<[1, 1, 5, 5]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[1, 1, 5, 5]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Unknown    | N/A   | N/A    |
| 27 | Tensor<[1, 5, 1, 16]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Done       | 1.0   | -1     |
| 28 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 29 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 30 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 31 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | Unknown  | Done       | 1.0   | 0      |
| 32 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | Unknown  | Done       | 1.0   | 0      |
| 33 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 34 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 35 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 36 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                                   | Unknown  | Done       | 1.0   | 0      |
| 37 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 32,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Done       | 1.0   | 0      |
| 38 | Tensor<[1, 5, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Done       | 1.0   | -1     |
| 39 | Tensor<[1, 5, 16]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Done       | 1.0   | -1     |
| 40 | Tensor<[1, 5]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Done       | 1.0   | -1     |
| 41 | Tensor<[1, 5]> self = ?,<br>int dim = 1,<br>Optional[int] start = -5,<br>Optional[int] end = 9223372036854775807                         | Unknown  | Unknown    | N/A   | N/A    |
| 42 | Tensor<[1, 6]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Done       | 1.0   | -1     |
| 43 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Unknown    | N/A   | N/A    |
| 44 | Tensor<[1, s0]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                         | Unknown  | Unknown    | N/A   | N/A    |
| 45 | Tensor<[1, s1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                         | Unknown  | Unknown    | N/A   | N/A    |
| 46 | Tensor<[1, s1]> self = ?,<br>int dim = 1,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                        | Unknown  | Unknown    | N/A   | N/A    |
| 47 | Tensor<[1]> self = ?,<br>int dim = 0,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Unknown    | N/A   | N/A    |
| 48 | Tensor<[5]> self = ?,<br>int dim = 0,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Unknown    | N/A   | N/A    |
### aten.slice_scatter.default
|    | ATen Input Variations                                                                                                                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 6]> self = ?,<br>Tensor<[1, 1, 1, 6]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, 6]> self = ?,<br>Tensor<[1, 1, 1, 6]> src = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 1, 6]> self = ?,<br>Tensor<[1, 1, 1, 6]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> src = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 1, 5, 5]> self = ?,<br>Tensor<[1, 1, 5, 5]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 1, 5, 5]> self = ?,<br>Tensor<[1, 1, 5, 5]> src = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 1, 5, 5]> self = ?,<br>Tensor<[1, 1, 5, 5]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   | N/A    |
### aten.split.Tensor
|    | ATen Input Variations                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>int split_size = 16,<br>int dim = -1      | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 1, 4, 768]> self = ?,<br>int split_size = 256,<br>int dim = -1 | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 5, 32]> self = ?,<br>int split_size = 16,<br>int dim = -1      | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 5, 4, 768]> self = ?,<br>int split_size = 256,<br>int dim = -1 | Unknown  | Done       |     1 |      0 |
### aten.stack.default
|    | ATen Input Variations                                                        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 1, 16, 16]>, <[1, 1, 16, 16]>],<br>int dim = -1 | Unknown  | Done       |     1 |      0 |
|  1 | List[Tensor] tensors = [<[1, 5, 16, 16]>, <[1, 5, 16, 16]>],<br>int dim = -1 | Unknown  | Done       |     1 |      0 |
### aten.sub.Tensor
|    | ATen Input Variations                         | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 5]> self = ?,<br>Tensor other = 1  | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, s1]> self = ?,<br>Tensor other = 1 | Unknown  | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations          | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1024, 1024]> self = ?  | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1024, 4096]> self = ?  | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[3072, 1024]> self = ?  | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[4096, 1024]> self = ?  | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[51200, 1024]> self = ? | Unknown  | Done       |     1 |      0 |
### aten.tanh.default
|    | ATen Input Variations         | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 4096]> self = ? | Unknown  | Done       | 0.999993 |      0 |
|  1 | Tensor<[1, 5, 4096]> self = ? | Unknown  | Done       | 0.999993 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16, 5, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 16, 6, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  | Unknown    | N/A   | N/A    |
### aten.triu.default
|    | ATen Input Variations                        | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[5, 5]> self = ?,<br>int diagonal = 1 | Unknown  | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                           | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 16]> self = ?,<br>int dim = 4  | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 16]> self = ?,<br>int dim = 2     | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1, 5]> self = ?,<br>int dim = 2      | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 1, 6]> self = ?,<br>int dim = 1      | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 6]> self = ?,<br>int dim = 2      | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 1 | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 5, 1, 16]> self = ?,<br>int dim = 4  | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 5, 16]> self = ?,<br>int dim = 2     | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 5, 5]> self = ?,<br>int dim = 1      | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 5]> self = ?,<br>int dim = 1         | Unknown  | Done       | 1.0   | 0      |
| 11 | Tensor<[1, 6]> self = ?,<br>int dim = 0         | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 6]> self = ?,<br>int dim = 1         | Unknown  | Done       | 1.0   | 0      |
| 13 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 0    | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 1    | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[5, 5]> self = ?,<br>int dim = 0         | Unknown  | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 16, 2]> self = ?,<br>List[int] size = [1, 1, 1, 32]         | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [-1, 1, 1024]             | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1024]                 | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 1, 16, 16, 2]> self = ?,<br>List[int] size = [1, 1, 16, 32]       | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 1, 16, 64]> self = ?,<br>List[int] size = [1, 1, 1024]            | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 1, 4, -1]             | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 1, 4, 256]> self = ?,<br>List[int] size = [1, 1, 4, 4, 64]        | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 1, 4096]> self = ?,<br>List[int] size = [1, 4096]                 | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1, 1, 1024]                 | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [16, 1, 64]             | Unknown  | Done       | 1.0   | 0      |
| 10 | Tensor<[1, 16, 1, 6]> self = ?,<br>List[int] size = [16, 1, 6]               | Unknown  | Done       | 1.0   | 0      |
| 11 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>List[int] size = [16, 1, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 16, 5, 5]> self = ?,<br>List[int] size = [16, 5, 5]               | Unknown  | Done       | 1.0   | 0      |
| 13 | Tensor<[1, 16, 5, 64]> self = ?,<br>List[int] size = [16, 5, 64]             | Unknown  | Done       | 1.0   | 0      |
| 14 | Tensor<[1, 16, 6, 64]> self = ?,<br>List[int] size = [16, 6, 64]             | Unknown  | Done       | 1.0   | 0      |
| 15 | Tensor<[1, 16, 64, 5]> self = ?,<br>List[int] size = [16, 64, 5]             | Unknown  | Done       | 1.0   | 0      |
| 16 | Tensor<[1, 16, 64, 6]> self = ?,<br>List[int] size = [16, 64, 6]             | Unknown  | Done       | 1.0   | 0      |
| 17 | Tensor<[1, 16, 64, s0 + 1]> self = ?,<br>List[int] size = [16, 64, <s0 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>List[int] size = [16, <s0 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 4096]> self = ?,<br>List[int] size = [1, 1, 4096]                 | Unknown  | Done       | 1.0   | 0      |
| 20 | Tensor<[1, 5, 1, 16, 2]> self = ?,<br>List[int] size = [1, 5, 1, 32]         | Unknown  | Done       | 1.0   | 0      |
| 21 | Tensor<[1, 5, 1024]> self = ?,<br>List[int] size = [-1, 5, 1024]             | Unknown  | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, 5, 1024]> self = ?,<br>List[int] size = [5, 1024]                 | Unknown  | Done       | 1.0   | 0      |
| 23 | Tensor<[1, 5, 16, 16, 2]> self = ?,<br>List[int] size = [1, 5, 16, 32]       | Unknown  | Done       | 1.0   | 0      |
| 24 | Tensor<[1, 5, 16, 64]> self = ?,<br>List[int] size = [1, 5, 1024]            | Unknown  | Done       | 1.0   | 0      |
| 25 | Tensor<[1, 5, 3072]> self = ?,<br>List[int] size = [1, 5, 4, -1]             | Unknown  | Done       | 1.0   | 0      |
| 26 | Tensor<[1, 5, 4, 256]> self = ?,<br>List[int] size = [1, 5, 4, 4, 64]        | Unknown  | Done       | 1.0   | 0      |
| 27 | Tensor<[1, 5, 4096]> self = ?,<br>List[int] size = [5, 4096]                 | Unknown  | Done       | 1.0   | 0      |
| 28 | Tensor<[1, 51200]> self = ?,<br>List[int] size = [1, 1, 51200]               | Unknown  | Done       | 1.0   | 0      |
| 29 | Tensor<[16, 1, 64]> self = ?,<br>List[int] size = [1, 16, 1, 64]             | Unknown  | Done       | 1.0   | 0      |
| 30 | Tensor<[16, 1, 6]> self = ?,<br>List[int] size = [1, 16, 1, 6]               | Unknown  | Done       | 1.0   | 0      |
| 31 | Tensor<[16, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 16, 1, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
| 32 | Tensor<[16, 5, 5]> self = ?,<br>List[int] size = [1, 16, 5, 5]               | Unknown  | Done       | 1.0   | 0      |
| 33 | Tensor<[16, 5, 64]> self = ?,<br>List[int] size = [1, 16, 5, 64]             | Unknown  | Done       | 1.0   | 0      |
| 34 | Tensor<[1]> self = ?,<br>List[int] size = [-1, 1]                            | Unknown  | Unknown    | N/A   | N/A    |
| 35 | Tensor<[5, 1024]> self = ?,<br>List[int] size = [1, 5, 1024]                 | Unknown  | Done       | 1.0   | 0      |
| 36 | Tensor<[5, 4096]> self = ?,<br>List[int] size = [1, 5, 4096]                 | Unknown  | Done       | 1.0   | 0      |
| 37 | Tensor<[5, 51200]> self = ?,<br>List[int] size = [1, 5, 51200]               | Unknown  | Done       | 1.0   | 0      |
| 38 | Tensor<[5]> self = ?,<br>List[int] size = [-1, 1]                            | Unknown  | Unknown    | N/A   | N/A    |

