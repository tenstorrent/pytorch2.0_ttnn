# High Level Operations Status
|    | Operations                 |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:---------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default      |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._to_copy.default      |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten.add.Tensor            |                  4 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.all.dim               |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.any.default           |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.bitwise_not.default   |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.bmm.default           |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.cat.default           |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.clone.default         |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.copy.default          |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.cos.default           |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.embedding.default     |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.eq.Scalar             |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.eq.Tensor             |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.expand.default        |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.index.Tensor          |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.masked_fill.Scalar    |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.mean.dim              |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.min.default           |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.mm.default            |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.mul.Scalar            |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.mul.Tensor            |                  7 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.ne.Scalar             |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.neg.default           |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.pow.Tensor_Scalar     |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.repeat.default        |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 26 | aten.rsqrt.default         |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 27 | aten.silu.default          |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 28 | aten.sin.default           |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 29 | aten.slice.Tensor          |                 11 |           0 |         0 |          0 | ✘           |       0 |
| 30 | aten.slice_scatter.default |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 31 | aten.t.default             |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 32 | aten.transpose.int         |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 33 | aten.unsqueeze.default     |                  8 |           0 |         0 |          0 | ✘           |       0 |
| 34 | aten.view.default          |                 15 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                            | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 32, 32]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A   | N/A    |
### aten._to_copy.default
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 32]> self = ?,<br>Optional[int] dtype = torch.float32          | Unknown  | Fallback   | 1.0   | -1     |
|  2 | Tensor<[1, 32, 128]> self = ?,<br>Optional[int] dtype = torch.bfloat16       | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 32, 32000]> self = ?,<br>Optional[int] dtype = torch.float32      | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 32, 4096]> self = ?,<br>Optional[int] dtype = torch.bfloat16      | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 32, 4096]> self = ?,<br>Optional[int] dtype = torch.float32       | Unknown  | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 1]> self = ?,<br>Tensor other = 1e-06                     | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 32, 32, 128]> self = ?,<br>Tensor<[1, 32, 32, 128]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 32, 32, 32]> self = ?,<br>Tensor<[1, 1, 32, 32]> other = ?    | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 32, 4096]> self = ?,<br>Tensor<[1, 32, 4096]> other = ?       | Unknown  | Unknown    | N/A   | N/A    |
### aten.all.dim
|    | ATen Input Variations                                | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = -1 | Unknown  | Unknown    | N/A   | N/A    |
### aten.any.default
|    | ATen Input Variations    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.bitwise_not.default
|    | ATen Input Variations            | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 2048, 1]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 64, 1]> self = ?,<br>Tensor<[1, 1, 32]> mat2 = ?       | Unknown  | Done       | 0.9999924340495363 | 0      |
|  1 | Tensor<[32, 32, 128]> self = ?,<br>Tensor<[32, 128, 32]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[32, 32, 32]> self = ?,<br>Tensor<[32, 32, 128]> mat2 = ?  | Unknown  | Unknown    | N/A                | N/A    |
### aten.cat.default
|    | ATen Input Variations                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 32, 32, 64]>, <[1, 32, 32, 64]>],<br>int dim = -1 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | List[Tensor] tensors = [<[1, 32, 64]>, <[1, 32, 64]>],<br>int dim = -1         | Unknown  | Done       | 1.0   | 0      |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 32, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Unknown    | N/A   | N/A    |
### aten.copy.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 2048, 32]> self = ?,<br>Tensor<[1, 1, 2048, 32]> src = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.cos.default
|    | ATen Input Variations         | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 32, 128]> self = ? | Unknown  | Done       | 0.999993 |      0 |
### aten.embedding.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[32000, 4096]> weight = ?,<br>Tensor<[1, 32]> indices = ?,<br>int padding_idx = 0 | Unknown  | Done       |     1 |      0 |
### aten.eq.Scalar
|    | ATen Input Variations                                    | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 32]> self = ?,<br>number other = 0.0    | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 2048, 32]> self = ?,<br>number other = 0.0 | Unknown  | Unknown    | N/A   | N/A    |
### aten.eq.Tensor
|    | ATen Input Variations                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Tensor<[]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.expand.default
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32]             | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 32, 128, 32]> self = ?,<br>List[int] size = [1, 32, 128, 32] | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 32, 32, 128]> self = ?,<br>List[int] size = [1, 32, 32, 128] | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 32, 32, 32]> self = ?,<br>List[int] size = [1, 32, 32, 32]   | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, -1, 1]             | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, 64, 1]             | Unknown  | Done       | 1.0   | -1     |
### aten.index.Tensor
|    | ATen Input Variations                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 2048, 32]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[32]>] | Unknown  | Unknown    | N/A   | N/A    |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 2048, 32]> self = ?,<br>Tensor<[1, 1, 2048, 32]> mask = ?,<br>number value = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A   | N/A    |
### aten.mean.dim
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 4096]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | Unknown  | Unknown    | N/A   | N/A    |
### aten.min.default
|    | ATen Input Variations               | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 11008]> self = ?,<br>Tensor<[11008, 4096]> mat2 = ? | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32, 4096]> self = ?,<br>Tensor<[4096, 11008]> mat2 = ?  | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[32, 4096]> self = ?,<br>Tensor<[4096, 32000]> mat2 = ?  | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[32, 4096]> self = ?,<br>Tensor<[4096, 4096]> mat2 = ?   | Unknown  | Unknown    | N/A   | N/A    |
### aten.mul.Scalar
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 128, 32]> self = ?,<br>number other = 0.29730177875068026 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 32, 32, 128]> self = ?,<br>number other = 0.29730177875068026 | Unknown  | Unknown    | N/A   | N/A    |
### aten.mul.Tensor
|    | ATen Input Variations                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Tensor<[1, 1, 2048, 1]> other = ?      | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 2048, 32]> self = ?,<br>Tensor<[1, 1, 1, 32]> other = ?          | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 32, 11008]> self = ?,<br>Tensor<[1, 32, 11008]> other = ?           | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 32, 32, 128]> self = ?,<br>Tensor<[1, 1, 32, 128]> other = ?        | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 32, 4096]> self = ?,<br>Tensor<[1, 32, 1]> other = ?                | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[4096]> self = ?,<br>Tensor<[1, 32, 4096]> other = ?                    | Unknown  | Unknown    | N/A   | N/A    |
### aten.ne.Scalar
|    | ATen Input Variations                         | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32]> self = ?,<br>number other = 1 | Unknown  | Unknown    | N/A   | N/A    |
### aten.neg.default
|    | ATen Input Variations            | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 32, 64]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 4096]> self = ?,<br>number exponent = 2 | Unknown  | Unknown    | N/A   | N/A    |
### aten.repeat.default
|    | ATen Input Variations                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>List[int] repeats = [1, 1, 1, 1] | Unknown  | Done       |     1 |     -1 |
### aten.rsqrt.default
|    | ATen Input Variations       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 1]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.silu.default
|    | ATen Input Variations           | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 11008]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.sin.default
|    | ATen Input Variations         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 128]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                  | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 1, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807         | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 32, 32, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 64                    | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 32, 32, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 64,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Done       | 1.0   | -1     |
### aten.slice_scatter.default
|    | ATen Input Variations                                                                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Tensor<[1, 1, 2048, 32]> src = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32 | Unknown  | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[11008, 4096]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32000, 4096]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[4096, 11008]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[4096, 4096]> self = ?  | Unknown  | Unknown    | N/A   | N/A    |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 32, 128]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 32, 32, 128]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Unknown  | Done       | 1.0   | 0      |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 2048]> self = ?,<br>int dim = 3    | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 32]> self = ?,<br>int dim = 2      | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 2048, 2048]> self = ?,<br>int dim = 1 | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 32, 128]> self = ?,<br>int dim = 1    | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 32]> self = ?,<br>int dim = 1         | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 64]> self = ?,<br>int dim = 2         | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[2048, 2048]> self = ?,<br>int dim = 0    | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[64]> self = ?,<br>int dim = 0            | Unknown  | Done       | 1.0   | 0      |
### aten.view.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32]          | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 32, 11008]> self = ?,<br>List[int] size = [32, 11008]     | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 32, 128, 32]> self = ?,<br>List[int] size = [32, 128, 32] | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 32, 32, 128]> self = ?,<br>List[int] size = [1, 32, 4096] | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 32, 32, 128]> self = ?,<br>List[int] size = [32, 32, 128] | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 32, 32, 32]> self = ?,<br>List[int] size = [32, 32, 32]   | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 32, 4096]> self = ?,<br>List[int] size = [1, 32, 32, 128] | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 32, 4096]> self = ?,<br>List[int] size = [32, 4096]       | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, 64, 1]          | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 64, 32]> self = ?,<br>List[int] size = [1, 64, 32]        | Unknown  | Done       | 1.0   | 0      |
| 10 | Tensor<[32, 11008]> self = ?,<br>List[int] size = [1, 32, 11008]     | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[32, 32, 128]> self = ?,<br>List[int] size = [1, 32, 32, 128] | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[32, 32, 32]> self = ?,<br>List[int] size = [1, 32, 32, 32]   | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[32, 32000]> self = ?,<br>List[int] size = [1, 32, 32000]     | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[32, 4096]> self = ?,<br>List[int] size = [1, 32, 4096]       | Unknown  | Unknown    | N/A   | N/A    |

