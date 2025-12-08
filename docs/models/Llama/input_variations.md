# High Level Operations Status
|    | Operations                                               |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:---------------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._scaled_dot_product_flash_attention_for_cpu.default |                 32 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._to_copy.default                                    |                  5 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten._unsafe_view.default                                |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.add.Tensor                                          |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.bitwise_and.Tensor                                  |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.bmm.default                                         |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.cat.default                                         |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.clone.default                                       |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.cos.default                                         |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.embedding.default                                   |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.expand.default                                      |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.index.Tensor                                        |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.le.Tensor                                           |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.mean.dim                                            |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.mm.default                                          |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.mul.Tensor                                          |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.neg.default                                         |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.new_ones.default                                    |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.pow.Tensor_Scalar                                   |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.rsqrt.default                                       |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.scalar_tensor.default                               |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.silu.default                                        |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.sin.default                                         |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.slice.Tensor                                        |                 11 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.t.default                                           |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.transpose.int                                       |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 26 | aten.unsqueeze.default                                   |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 27 | aten.view.default                                        |                 10 |           0 |         0 |          0 | ✘           |       0 |
| 28 | aten.where.self                                          |                  1 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._scaled_dot_product_flash_attention_for_cpu.default
|    | ATen Input Variations                                                                                                                                                                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where,<br>Optional[float] scale = 0.08838834764831845    | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_1,<br>Optional[float] scale = 0.08838834764831845  | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_10,<br>Optional[float] scale = 0.08838834764831845 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_11,<br>Optional[float] scale = 0.08838834764831845 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_12,<br>Optional[float] scale = 0.08838834764831845 | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_13,<br>Optional[float] scale = 0.08838834764831845 | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_14,<br>Optional[float] scale = 0.08838834764831845 | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_15,<br>Optional[float] scale = 0.08838834764831845 | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_16,<br>Optional[float] scale = 0.08838834764831845 | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_17,<br>Optional[float] scale = 0.08838834764831845 | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_18,<br>Optional[float] scale = 0.08838834764831845 | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_19,<br>Optional[float] scale = 0.08838834764831845 | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_2,<br>Optional[float] scale = 0.08838834764831845  | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_20,<br>Optional[float] scale = 0.08838834764831845 | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_21,<br>Optional[float] scale = 0.08838834764831845 | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_22,<br>Optional[float] scale = 0.08838834764831845 | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_23,<br>Optional[float] scale = 0.08838834764831845 | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_24,<br>Optional[float] scale = 0.08838834764831845 | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_25,<br>Optional[float] scale = 0.08838834764831845 | Unknown  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_26,<br>Optional[float] scale = 0.08838834764831845 | Unknown  | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_27,<br>Optional[float] scale = 0.08838834764831845 | Unknown  | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_28,<br>Optional[float] scale = 0.08838834764831845 | Unknown  | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_29,<br>Optional[float] scale = 0.08838834764831845 | Unknown  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_3,<br>Optional[float] scale = 0.08838834764831845  | Unknown  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_30,<br>Optional[float] scale = 0.08838834764831845 | Unknown  | Unknown    | N/A   | N/A    |
| 25 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_31,<br>Optional[float] scale = 0.08838834764831845 | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_4,<br>Optional[float] scale = 0.08838834764831845  | Unknown  | Unknown    | N/A   | N/A    |
| 27 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_5,<br>Optional[float] scale = 0.08838834764831845  | Unknown  | Unknown    | N/A   | N/A    |
| 28 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_6,<br>Optional[float] scale = 0.08838834764831845  | Unknown  | Unknown    | N/A   | N/A    |
| 29 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_7,<br>Optional[float] scale = 0.08838834764831845  | Unknown  | Unknown    | N/A   | N/A    |
| 30 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_8,<br>Optional[float] scale = 0.08838834764831845  | Unknown  | Unknown    | N/A   | N/A    |
| 31 | Tensor<[1, 32, 32, 128]> query = ?,<br>Tensor<[1, 32, 32, 128]> key = ?,<br>Tensor<[1, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[1, 1, 32, 32]> attn_mask = where_9,<br>Optional[float] scale = 0.08838834764831845  | Unknown  | Unknown    | N/A   | N/A    |
### aten._to_copy.default
|    | ATen Input Variations                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>Optional[int] dtype = torch.float32                             | Unknown  | Fallback   | 1.0   | -1     |
|  1 | Tensor<[1, 32, 128]> self = ?,<br>Optional[int] dtype = torch.bfloat16                          | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 32, 4096]> self = ?,<br>Optional[int] dtype = torch.bfloat16                         | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 32, 4096]> self = ?,<br>Optional[int] dtype = torch.float32                          | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 32]> self = ?,<br>Optional[int] dtype = torch.bool,<br>Optional[Device] device = cpu | Unknown  | Unknown    | N/A   | N/A    |
### aten._unsafe_view.default
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 11008]> self = ?,<br>List[int] size = [1, 32, 11008] | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32, 32000]> self = ?,<br>List[int] size = [1, 32, 32000] | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[32, 4096]> self = ?,<br>List[int] size = [1, 32, 4096]   | Unknown  | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 1]> self = ?,<br>Tensor other = 1e-06                     | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 32, 32, 128]> self = ?,<br>Tensor<[1, 32, 32, 128]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 32, 4096]> self = ?,<br>Tensor<[1, 32, 4096]> other = ?       | Unknown  | Unknown    | N/A   | N/A    |
### aten.bitwise_and.Tensor
|    | ATen Input Variations                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 1]> self = ?,<br>Tensor<[32, 32]> other = ?    | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32, 32]> self = ?,<br>Tensor<[1, 1, 32]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.bmm.default
|    | ATen Input Variations                                       | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 64, 1]> self = ?,<br>Tensor<[1, 1, 32]> mat2 = ? | Unknown  | Done       | 0.999993 |      0 |
### aten.cat.default
|    | ATen Input Variations                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 32, 32, 64]>, <[1, 32, 32, 64]>],<br>int dim = -1 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | List[Tensor] tensors = [<[1, 32, 64]>, <[1, 32, 64]>],<br>int dim = -1         | Unknown  | Done       | 1.0   | 0      |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 32, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Unknown    | N/A   | N/A    |
### aten.cos.default
|    | ATen Input Variations         | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 32, 128]> self = ? | Unknown  | Done       | 0.999993 |      0 |
### aten.embedding.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[32000, 4096]> weight = ?,<br>Tensor<[1, 32]> indices = ?,<br>int padding_idx = 0 | Unknown  | Done       |     1 |      0 |
### aten.expand.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 32, 32]> self = ?,<br>List[int] size = [1, 1, 32, 32] | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32]         | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, -1, 1]         | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, 64, 1]         | Unknown  | Done       | 1.0   | -1     |
### aten.index.Tensor
|    | ATen Input Variations                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32]> self = ?,<br>List[Optional[Tensor]] indices = [_folded_view_2, _folded_add] | Unknown  | Unknown    | N/A   | N/A    |
### aten.le.Tensor
|    | ATen Input Variations                | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.mean.dim
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 4096]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | Unknown  | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 11008]> self = ?,<br>Tensor<[11008, 4096]> mat2 = ? | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32, 4096]> self = ?,<br>Tensor<[4096, 11008]> mat2 = ?  | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[32, 4096]> self = ?,<br>Tensor<[4096, 32000]> mat2 = ?  | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[32, 4096]> self = ?,<br>Tensor<[4096, 4096]> mat2 = ?   | Unknown  | Unknown    | N/A   | N/A    |
### aten.mul.Tensor
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 11008]> self = ?,<br>Tensor<[1, 32, 11008]> other = ?    | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 32, 128]> self = ?,<br>Tensor other = 1.0                    | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 32, 32, 128]> self = ?,<br>Tensor<[1, 1, 32, 128]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 32, 4096]> self = ?,<br>Tensor<[1, 32, 1]> other = ?         | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[4096]> self = ?,<br>Tensor<[1, 32, 4096]> other = ?             | Unknown  | Unknown    | N/A   | N/A    |
### aten.neg.default
|    | ATen Input Variations            | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 32, 64]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.new_ones.default
|    | ATen Input Variations                                                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>List[int] size = [32],<br>Optional[int] dtype = torch.bool,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 4096]> self = ?,<br>number exponent = 2 | Unknown  | Unknown    | N/A   | N/A    |
### aten.rsqrt.default
|    | ATen Input Variations       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 1]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.scalar_tensor.default
|    | ATen Input Variations                                                                                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | number s = -inf,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu                                         | Unknown  | Unknown    | N/A   | N/A    |
|  1 | number s = 0.0,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  | Unknown    | N/A   | N/A    |
### aten.silu.default
|    | ATen Input Variations           | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 11008]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.sin.default
|    | ATen Input Variations         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 128]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 32, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 32, 32]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 32, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807        | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 32, 32, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 64                   | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 32, 32, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 64,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 32, 4096]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 32, 4096]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 32, 4096]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[11008, 4096]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32000, 4096]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[4096, 11008]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[4096, 4096]> self = ?  | Unknown  | Unknown    | N/A   | N/A    |
### aten.transpose.int
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 32, 128]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
### aten.unsqueeze.default
|    | ATen Input Variations                         | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 128]> self = ?,<br>int dim = 1 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 32]> self = ?,<br>int dim = 1      | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 64]> self = ?,<br>int dim = 2      | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[64]> self = ?,<br>int dim = 0         | Unknown  | Done       | 1.0   | 0      |
### aten.view.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32]          | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 32, 11008]> self = ?,<br>List[int] size = [32, 11008]     | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 32, 32, 128]> self = ?,<br>List[int] size = [1, 32, -1]   | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 32, 32]> self = ?,<br>List[int] size = [1, 1, 32, 32]     | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 32, 4096]> self = ?,<br>List[int] size = [1, 32, -1, 128] | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 32, 4096]> self = ?,<br>List[int] size = [32, 4096]       | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 32]> self = ?,<br>List[int] size = [1, 1, 32]             | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, 64, 1]          | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 64, 32]> self = ?,<br>List[int] size = [1, 64, 32]        | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[32]> self = ?,<br>List[int] size = [32, 1]                   | Unknown  | Unknown    | N/A   | N/A    |
### aten.where.self
|    | ATen Input Variations                                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 32, 32]> condition = ?,<br>Tensor<[]> self = ?,<br>Tensor<[]> other = ? | Unknown  | Unknown    | N/A   | N/A    |

