# High Level Operations Status
|    | Operations                                               |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:---------------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._scaled_dot_product_flash_attention_for_cpu.default |                 51 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._unsafe_view.default                                |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten.add.Tensor                                          |                  7 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.addmm.default                                       |                  9 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.any.default                                         |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.arange.default                                      |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.argmax.default                                      |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.bitwise_and.Tensor                                  |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.bitwise_or.Tensor                                   |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.cat.default                                         |                 15 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.clone.default                                       |                 12 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.constant_pad_nd.default                             |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.convolution.default                                 |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.div.Tensor                                          |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.embedding.default                                   |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.expand.default                                      |                  8 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.full.default                                        |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.ge.Scalar                                           |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.gelu.default                                        |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.index.Tensor                                        |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.index_put.default                                   |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.isin.Tensor_Tensor                                  |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.le.Tensor                                           |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.lt.Scalar                                           |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.lt.Tensor                                           |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.mm.default                                          |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 26 | aten.mul.Tensor                                          |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 27 | aten.native_layer_norm.default                           |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 28 | aten.ones_like.default                                   |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 29 | aten.permute.default                                     |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 30 | aten.repeat.default                                      |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 31 | aten.scalar_tensor.default                               |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 32 | aten.select.int                                          |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 33 | aten.select_scatter.default                              |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 34 | aten.slice.Tensor                                        |                 27 |           0 |         0 |          0 | ✘           |       0 |
| 35 | aten.slice_scatter.default                               |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 36 | aten.stack.default                                       |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 37 | aten.t.default                                           |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 38 | aten.transpose.int                                       |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 39 | aten.unsqueeze.default                                   |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 40 | aten.view.default                                        |                 26 |           0 |         0 |          0 | ✘           |       0 |
| 41 | aten.where.self                                          |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 42 | aten.zeros.default                                       |                  1 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._scaled_dot_product_flash_attention_for_cpu.default
|    | ATen Input Variations                                                                                                                                                                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 1, 64]> key = ?,<br>Tensor<[1, 12, 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 1]> attn_mask = where,<br>Optional[float] scale = 1.0                    | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 1, 64]> key = ?,<br>Tensor<[1, 12, 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 1]> attn_mask = where_1,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 1, 64]> key = ?,<br>Tensor<[1, 12, 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 1]> attn_mask = where_10,<br>Optional[float] scale = 1.0                 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 1, 64]> key = ?,<br>Tensor<[1, 12, 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 1]> attn_mask = where_11,<br>Optional[float] scale = 1.0                 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 1, 64]> key = ?,<br>Tensor<[1, 12, 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 1]> attn_mask = where_2,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 1, 64]> key = ?,<br>Tensor<[1, 12, 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 1]> attn_mask = where_3,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 1, 64]> key = ?,<br>Tensor<[1, 12, 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 1]> attn_mask = where_4,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 1, 64]> key = ?,<br>Tensor<[1, 12, 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 1]> attn_mask = where_5,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 1, 64]> key = ?,<br>Tensor<[1, 12, 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 1]> attn_mask = where_6,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 1, 64]> key = ?,<br>Tensor<[1, 12, 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 1]> attn_mask = where_7,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 1, 64]> key = ?,<br>Tensor<[1, 12, 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 1]> attn_mask = where_8,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 1, 64]> key = ?,<br>Tensor<[1, 12, 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 1]> attn_mask = where_9,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 1500, 64]> key = ?,<br>Tensor<[1, 12, 1500, 64]> value = ?,<br>Optional[float] scale = 1.0                                                                   | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 5, 64]> key = ?,<br>Tensor<[1, 12, 5, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 5]> attn_mask = where,<br>Optional[float] scale = 1.0                    | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 5, 64]> key = ?,<br>Tensor<[1, 12, 5, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 5]> attn_mask = where_1,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 5, 64]> key = ?,<br>Tensor<[1, 12, 5, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 5]> attn_mask = where_10,<br>Optional[float] scale = 1.0                 | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 5, 64]> key = ?,<br>Tensor<[1, 12, 5, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 5]> attn_mask = where_11,<br>Optional[float] scale = 1.0                 | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 5, 64]> key = ?,<br>Tensor<[1, 12, 5, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 5]> attn_mask = where_2,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 5, 64]> key = ?,<br>Tensor<[1, 12, 5, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 5]> attn_mask = where_3,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 5, 64]> key = ?,<br>Tensor<[1, 12, 5, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 5]> attn_mask = where_4,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 5, 64]> key = ?,<br>Tensor<[1, 12, 5, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 5]> attn_mask = where_5,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 5, 64]> key = ?,<br>Tensor<[1, 12, 5, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 5]> attn_mask = where_6,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 5, 64]> key = ?,<br>Tensor<[1, 12, 5, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 5]> attn_mask = where_7,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 5, 64]> key = ?,<br>Tensor<[1, 12, 5, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 5]> attn_mask = where_8,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 5, 64]> key = ?,<br>Tensor<[1, 12, 5, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 5]> attn_mask = where_9,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
| 25 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s0 + 1, 64]> key = ?,<br>Tensor<[1, 12, s10 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = where_4,<br>Optional[float] scale = 1.0  | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s0 + 1, 64]> key = ?,<br>Tensor<[1, 12, s12 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = where_5,<br>Optional[float] scale = 1.0  | Unknown  | Unknown    | N/A   | N/A    |
| 27 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s0 + 1, 64]> key = ?,<br>Tensor<[1, 12, s14 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = where_6,<br>Optional[float] scale = 1.0  | Unknown  | Unknown    | N/A   | N/A    |
| 28 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s0 + 1, 64]> key = ?,<br>Tensor<[1, 12, s16 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = where_7,<br>Optional[float] scale = 1.0  | Unknown  | Unknown    | N/A   | N/A    |
| 29 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s0 + 1, 64]> key = ?,<br>Tensor<[1, 12, s18 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = where_8,<br>Optional[float] scale = 1.0  | Unknown  | Unknown    | N/A   | N/A    |
| 30 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s0 + 1, 64]> key = ?,<br>Tensor<[1, 12, s2 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = where,<br>Optional[float] scale = 1.0     | Unknown  | Unknown    | N/A   | N/A    |
| 31 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s0 + 1, 64]> key = ?,<br>Tensor<[1, 12, s20 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = where_9,<br>Optional[float] scale = 1.0  | Unknown  | Unknown    | N/A   | N/A    |
| 32 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s0 + 1, 64]> key = ?,<br>Tensor<[1, 12, s22 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = where_10,<br>Optional[float] scale = 1.0 | Unknown  | Unknown    | N/A   | N/A    |
| 33 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s0 + 1, 64]> key = ?,<br>Tensor<[1, 12, s24 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = where_11,<br>Optional[float] scale = 1.0 | Unknown  | Unknown    | N/A   | N/A    |
| 34 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s0 + 1, 64]> key = ?,<br>Tensor<[1, 12, s4 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = where_1,<br>Optional[float] scale = 1.0   | Unknown  | Unknown    | N/A   | N/A    |
| 35 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s0 + 1, 64]> key = ?,<br>Tensor<[1, 12, s6 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = where_2,<br>Optional[float] scale = 1.0   | Unknown  | Unknown    | N/A   | N/A    |
| 36 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s0 + 1, 64]> key = ?,<br>Tensor<[1, 12, s8 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = where_3,<br>Optional[float] scale = 1.0   | Unknown  | Unknown    | N/A   | N/A    |
| 37 | Tensor<[1, 12, 1500, 64]> query = ?,<br>Tensor<[1, 12, 1500, 64]> key = ?,<br>Tensor<[1, 12, 1500, 64]> value = ?,<br>Optional[float] scale = 1.0                                                                | Unknown  | Unknown    | N/A   | N/A    |
| 38 | Tensor<[1, 12, 4, 64]> query = ?,<br>Tensor<[1, 12, 1500, 64]> key = ?,<br>Tensor<[1, 12, 1500, 64]> value = ?,<br>Optional[float] scale = 1.0                                                                   | Unknown  | Unknown    | N/A   | N/A    |
| 39 | Tensor<[1, 12, 4, 64]> query = ?,<br>Tensor<[1, 12, 4, 64]> key = ?,<br>Tensor<[1, 12, 4, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 4, 4]> attn_mask = where,<br>Optional[float] scale = 1.0                    | Unknown  | Unknown    | N/A   | N/A    |
| 40 | Tensor<[1, 12, 4, 64]> query = ?,<br>Tensor<[1, 12, 4, 64]> key = ?,<br>Tensor<[1, 12, 4, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 4, 4]> attn_mask = where_1,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
| 41 | Tensor<[1, 12, 4, 64]> query = ?,<br>Tensor<[1, 12, 4, 64]> key = ?,<br>Tensor<[1, 12, 4, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 4, 4]> attn_mask = where_10,<br>Optional[float] scale = 1.0                 | Unknown  | Unknown    | N/A   | N/A    |
| 42 | Tensor<[1, 12, 4, 64]> query = ?,<br>Tensor<[1, 12, 4, 64]> key = ?,<br>Tensor<[1, 12, 4, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 4, 4]> attn_mask = where_11,<br>Optional[float] scale = 1.0                 | Unknown  | Unknown    | N/A   | N/A    |
| 43 | Tensor<[1, 12, 4, 64]> query = ?,<br>Tensor<[1, 12, 4, 64]> key = ?,<br>Tensor<[1, 12, 4, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 4, 4]> attn_mask = where_2,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
| 44 | Tensor<[1, 12, 4, 64]> query = ?,<br>Tensor<[1, 12, 4, 64]> key = ?,<br>Tensor<[1, 12, 4, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 4, 4]> attn_mask = where_3,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
| 45 | Tensor<[1, 12, 4, 64]> query = ?,<br>Tensor<[1, 12, 4, 64]> key = ?,<br>Tensor<[1, 12, 4, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 4, 4]> attn_mask = where_4,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
| 46 | Tensor<[1, 12, 4, 64]> query = ?,<br>Tensor<[1, 12, 4, 64]> key = ?,<br>Tensor<[1, 12, 4, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 4, 4]> attn_mask = where_5,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
| 47 | Tensor<[1, 12, 4, 64]> query = ?,<br>Tensor<[1, 12, 4, 64]> key = ?,<br>Tensor<[1, 12, 4, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 4, 4]> attn_mask = where_6,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
| 48 | Tensor<[1, 12, 4, 64]> query = ?,<br>Tensor<[1, 12, 4, 64]> key = ?,<br>Tensor<[1, 12, 4, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 4, 4]> attn_mask = where_7,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
| 49 | Tensor<[1, 12, 4, 64]> query = ?,<br>Tensor<[1, 12, 4, 64]> key = ?,<br>Tensor<[1, 12, 4, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 4, 4]> attn_mask = where_8,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
| 50 | Tensor<[1, 12, 4, 64]> query = ?,<br>Tensor<[1, 12, 4, 64]> key = ?,<br>Tensor<[1, 12, 4, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 4, 4]> attn_mask = where_9,<br>Optional[float] scale = 1.0                  | Unknown  | Unknown    | N/A   | N/A    |
### aten._unsafe_view.default
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 51865]> self = ?,<br>List[int] size = [1, 51865]   | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 51865]> self = ?,<br>List[int] size = [1, 1, 51865]   | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 768]> self = ?,<br>List[int] size = [1, 1, 768]       | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1500, 768]> self = ?,<br>List[int] size = [1, 1500, 768] | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[4, 51865]> self = ?,<br>List[int] size = [1, 4, 51865]   | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[4, 768]> self = ?,<br>List[int] size = [1, 4, 768]       | Unknown  | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?       | Unknown  | Done       | 0.9999981451304495 | 0      |
|  1 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1, 1500, 768]> other = ? | Unknown  | Done       | 0.999997978818409  | 0      |
|  2 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1500, 768]> other = ?    | Unknown  | Done       | 0.9999979915743177 | 0      |
|  3 | Tensor<[1, 4, 768]> self = ?,<br>Tensor<[1, 4, 768]> other = ?       | Unknown  | Done       | 0.9999978536711165 | 0      |
|  4 | Tensor<[1]> self = ?,<br>Tensor other = 1                            | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[]> self = ?,<br>Tensor other = 30.0                          | Unknown  | Unknown    | N/A                | N/A    |
|  6 | Tensor<[s0 + 1]> self = ?,<br>Tensor other = 0                       | Unknown  | Unknown    | N/A                | N/A    |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[3072]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?    | Unknown  | Done       | 0.999968 |      0 |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[1500, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Unknown  | Done       | 0.999962 |      0 |
|  2 | Tensor<[3072]> self = ?,<br>Tensor<[4, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?    | Unknown  | Done       | 0.999968 |      0 |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[1, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?    | Unknown  | Done       | 0.999943 |      0 |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?      | Unknown  | Done       | 0.999968 |      0 |
|  5 | Tensor<[768]> self = ?,<br>Tensor<[1500, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Unknown  | Done       | 0.999883 |      0 |
|  6 | Tensor<[768]> self = ?,<br>Tensor<[1500, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Unknown  | Done       | 0.999962 |      0 |
|  7 | Tensor<[768]> self = ?,<br>Tensor<[4, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?    | Unknown  | Done       | 0.999945 |      0 |
|  8 | Tensor<[768]> self = ?,<br>Tensor<[4, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?      | Unknown  | Done       | 0.999965 |      0 |
### aten.any.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1]> self = ?    | Unknown  | Unknown    | N/A   | N/A    |
### aten.arange.default
|    | ATen Input Variations                                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | number<s0 + 1> end = ?,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.argmax.default
|    | ATen Input Variations                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 51865]> self = ?,<br>Optional[int] dim = -1 | Unknown  | Fallback   |     1 |     -1 |
### aten.bitwise_and.Tensor
|    | ATen Input Variations                            | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[21]> self = ?,<br>Tensor<[21]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.bitwise_or.Tensor
|    | ATen Input Variations                          | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1]> self = ?,<br>Tensor<[1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.cat.default
|    | ATen Input Variations                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 12, 4, 64]>, <[1, 12, 1, 64]>],<br>int dim = -2   | Unknown  | Unknown    | N/A   | N/A    |
|  1 | List[Tensor] tensors = [<[1, 12, s0, 64]>, <[1, 12, 1, 64]>],<br>int dim = -2  | Unknown  | Unknown    | N/A   | N/A    |
|  2 | List[Tensor] tensors = [<[1, 12, s10, 64]>, <[1, 12, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | List[Tensor] tensors = [<[1, 12, s12, 64]>, <[1, 12, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | List[Tensor] tensors = [<[1, 12, s14, 64]>, <[1, 12, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
|  5 | List[Tensor] tensors = [<[1, 12, s16, 64]>, <[1, 12, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
|  6 | List[Tensor] tensors = [<[1, 12, s18, 64]>, <[1, 12, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
|  7 | List[Tensor] tensors = [<[1, 12, s2, 64]>, <[1, 12, 1, 64]>],<br>int dim = -2  | Unknown  | Unknown    | N/A   | N/A    |
|  8 | List[Tensor] tensors = [<[1, 12, s20, 64]>, <[1, 12, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
|  9 | List[Tensor] tensors = [<[1, 12, s22, 64]>, <[1, 12, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
| 10 | List[Tensor] tensors = [<[1, 12, s24, 64]>, <[1, 12, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
| 11 | List[Tensor] tensors = [<[1, 12, s4, 64]>, <[1, 12, 1, 64]>],<br>int dim = -2  | Unknown  | Unknown    | N/A   | N/A    |
| 12 | List[Tensor] tensors = [<[1, 12, s6, 64]>, <[1, 12, 1, 64]>],<br>int dim = -2  | Unknown  | Unknown    | N/A   | N/A    |
| 13 | List[Tensor] tensors = [<[1, 12, s8, 64]>, <[1, 12, 1, 64]>],<br>int dim = -2  | Unknown  | Unknown    | N/A   | N/A    |
| 14 | List[Tensor] tensors = [<[22]>],<br>int dim = -1                               | Unknown  | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 3072]> self = ?                                                                | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 768]> self = ?                                                                 | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 12, 1500, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 12, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 1500, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1500, 3072]> self = ?                                                             | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 1500, 768]> self = ?                                                              | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 1]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 4, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 4, 3072]> self = ?                                                                | Unknown  | Done       | 1.0   | 0      |
| 10 | Tensor<[1, 4, 768]> self = ?                                                                 | Unknown  | Done       | 1.0   | 0      |
| 11 | Tensor<[1, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Unknown  | Unknown    | N/A   | N/A    |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[22]> self = ?,<br>List[int] pad = [0, 0],<br>number value = 50257.0 | Unknown  | Unknown    | N/A   | N/A    |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 768, 3000]> input = ?,<br>Tensor<[768, 768, 3]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [2],<br>List[int] padding = [1],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1 | Unknown  | Fallback   | 1        |     -1 |
|  1 | Tensor<[1, 80, 3000]> input = ?,<br>Tensor<[768, 80, 3]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [1],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1   | Unknown  | Done       | 0.999966 |      1 |
### aten.div.Tensor
|    | ATen Input Variations                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[]> self = ?,<br>Tensor other = 0.02 | Unknown  | Unknown    | N/A   | N/A    |
### aten.embedding.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1500, 768]> weight = ?,<br>Tensor indices = ?                                      | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[51865, 768]> weight = ?,<br>Tensor indices = ?,<br>int padding_idx = 50257         | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 50257 | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 4]> indices = ?,<br>int padding_idx = 50257 | Unknown  | Done       | 1.0   | 0      |
### aten.expand.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>List[int] size = [1, 1, 1, 1]             | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 5]> self = ?,<br>List[int] size = [1, 1, 1, 5]             | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 1, 1, <s0 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1]> self = ?,<br>List[int] size = [1, 1, 1]                   | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 4, 4]> self = ?,<br>List[int] size = [1, 1, 4, 4]             | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 5]> self = ?,<br>List[int] size = [1, 1, 5]                   | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, s0 + 1]> self = ?,<br>List[int] size = [1, 1, <s0 + 1>]       | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[4, 4]> self = ?,<br>List[int] size = [1, 4, 4]                   | Unknown  | Unknown    | N/A   | N/A    |
### aten.full.default
|    | ATen Input Variations                                                                                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [1],<br>number fill_value = False,<br>Optional[int] dtype = torch.bool,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Unknown    | N/A   | N/A    |
|  1 | List[int] size = [1],<br>number<s0 >= 448> fill_value = ?,<br>Optional[int] dtype = torch.bool,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.ge.Scalar
|    | ATen Input Variations                          | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[22]> self = ?,<br>number other = 50364 | Unknown  | Unknown    | N/A   | N/A    |
### aten.gelu.default
|    | ATen Input Variations            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 3072]> self = ?    | Unknown  | Done       | 0.999991 |      0 |
|  1 | Tensor<[1, 1500, 3072]> self = ? | Unknown  | Done       | 0.999991 |      0 |
|  2 | Tensor<[1, 4, 3072]> self = ?    | Unknown  | Done       | 0.999991 |      0 |
|  3 | Tensor<[1, 768, 1500]> self = ?  | Unknown  | Done       | 0.999991 |      0 |
|  4 | Tensor<[1, 768, 3000]> self = ?  | Unknown  | Done       | 0.999991 |      0 |
### aten.index.Tensor
|    | ATen Input Variations                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 4]> self = ?,<br>List[Optional[Tensor]] indices = [None, <[4]>]             | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 4]> self = ?,<br>List[Optional[Tensor]] indices = [_folded_lift_fresh_copy] | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, s0]> self = ?,<br>List[Optional[Tensor]] indices = [None, <[1]>]            | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[22]> self = ?,<br>List[Optional[Tensor]] indices = [<[0]>]                     | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[448, 768]> self = ?,<br>List[Optional[Tensor]] indices = [<[1, 1]>]            | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[448, 768]> self = ?,<br>List[Optional[Tensor]] indices = [<[1, 4]>]            | Unknown  | Unknown    | N/A   | N/A    |
### aten.index_put.default
|    | ATen Input Variations                                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 51865]> self = ?,<br>List[Optional[Tensor]] indices = [None, <[51865]>],<br>Tensor values = ?        | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[51865]> self = ?,<br>List[Optional[Tensor]] indices = [_folded_lift_fresh_copy_1],<br>Tensor values = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.isin.Tensor_Tensor
|    | ATen Input Variations                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor elements = ?,<br>Tensor test_elements = ?           | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor elements = ?,<br>Tensor<[2]> test_elements = ?      | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor elements = ?,<br>Tensor<[88]> test_elements = ?     | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1]> elements = ?,<br>Tensor<[1]> test_elements = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.le.Tensor
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor other = ?                   | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor self = ?,<br>Tensor<[1, 1]> other = ?           | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor self = ?,<br>Tensor<[4, 1]> other = ?           | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[s0 + 1]> self = ?,<br>Tensor<[1, 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.lt.Scalar
|    | ATen Input Variations                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1]> self = ?,<br>number other = 0 | Unknown  | Unknown    | N/A   | N/A    |
### aten.lt.Tensor
|    | ATen Input Variations                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1]> self = ?,<br>Tensor other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 51865]> mat2 = ?  | Unknown  | Done       | 0.999968 |      0 |
|  1 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?    | Unknown  | Done       | 0.99997  |      0 |
|  2 | Tensor<[1500, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ? | Unknown  | Done       | 0.999963 |      0 |
|  3 | Tensor<[4, 768]> self = ?,<br>Tensor<[768, 51865]> mat2 = ?  | Unknown  | Done       | 0.999968 |      0 |
|  4 | Tensor<[4, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?    | Unknown  | Done       | 0.999969 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                    | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.125    | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor other = 0.125 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 4, 768]> self = ?,<br>Tensor other = 0.125    | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[]> self = ?,<br>Tensor other = 0.01              | Unknown  | Unknown    | N/A   | N/A    |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                     | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05    | Unknown  | Done       | 0.999998 |      3 |
|  1 | Tensor<[1, 1500, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Unknown  | Done       | 0.998366 |      3 |
|  2 | Tensor<[1, 4, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05    | Unknown  | Done       | 0.999779 |      3 |
### aten.ones_like.default
|    | ATen Input Variations                                                                               | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[51865]> self = ?,<br>Optional[int] dtype = torch.bool,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.permute.default
|    | ATen Input Variations                                          | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 768, 1500]> self = ?,<br>List[int] dims = [0, 2, 1] | Unknown  | Done       |     1 |      0 |
### aten.repeat.default
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>List[int] repeats = [1, 1]         | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1]> self = ?,<br>List[int] repeats = [1, 1] | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 4]> self = ?,<br>List[int] repeats = [1, 1] | Unknown  | Unknown    | N/A   | N/A    |
### aten.scalar_tensor.default
|    | ATen Input Variations                                                                                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | number s = -inf,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu                                         | Unknown  | Unknown    | N/A   | N/A    |
|  1 | number s = -inf,<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  | Unknown    | N/A   | N/A    |
|  2 | number s = 0.0,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  | Unknown    | N/A   | N/A    |
### aten.select.int
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 51865]> self = ?,<br>int dim = 1,<br>int index = -1 | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 51865]> self = ?,<br>int dim = 0,<br>int index = 0     | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 5]> self = ?,<br>int dim = 1,<br>int index = -1        | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, s0]> self = ?,<br>int dim = 1,<br>int index = -1       | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1]> self = ?,<br>int dim = 0,<br>int index = 0            | Unknown  | Done       | 1.0   | 0      |
### aten.select_scatter.default
|    | ATen Input Variations                                                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 51865]> self = ?,<br>Tensor<[1, 51865]> src = ?,<br>int dim = 1,<br>int index = -1 | Unknown  | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 1, 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 1, 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 1, 5]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1, 1, 5]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 1, 1, 5]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 1, 4, 4]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 1, 4, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 1, 4, 4]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 1, 51865]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | Done       | 1.0   | -1     |
| 14 | Tensor<[1, 27]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 27]> self = ?,<br>int dim = 1,<br>Optional[int] start = 4,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 4]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 51865]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807        | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 5]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 80, 3000]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | Done       | 1.0   | -1     |
| 20 | Tensor<[1, 80, 3000]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | Done       | 1.0   | -1     |
| 21 | Tensor<[1, s0]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1]> self = ?,<br>int dim = 0,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807              | Unknown  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[22]> self = ?,<br>int dim = 0,<br>Optional[int] start = -2,<br>Optional[int] end = 9223372036854775807             | Unknown  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[22]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                               | Unknown  | Unknown    | N/A   | N/A    |
| 25 | Tensor<[22]> self = ?,<br>int dim = 0,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807              | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[4]> self = ?,<br>int dim = 0,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807              | Unknown  | Unknown    | N/A   | N/A    |
### aten.slice_scatter.default
|    | ATen Input Variations                                                                                                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 51865]> self = ?,<br>Tensor<[1, 1, 51865]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 51865]> self = ?,<br>Tensor<[1, 51865]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
### aten.stack.default
|    | ATen Input Variations           | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[22]>] | Unknown  | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[3072, 768]> self = ?  | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[51865, 768]> self = ? | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[768, 3072]> self = ?  | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[768, 768]> self = ?   | Unknown  | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 12, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 12, 1500, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 12, 4, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[1, 1500, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[1, 4, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1]> self = ?,<br>int dim = 0 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[4]> self = ?,<br>int dim = 0 | Unknown  | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[0, 1]> self = ?,<br>List[int] size = [0]                       | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int] size = [1, 1, -1]        | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 3072]           | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]      | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 1, -1, 64]       | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 768]             | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 1500, 12, 64]> self = ?,<br>List[int] size = [1, 1500, -1]  | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 1500, 3072]> self = ?,<br>List[int] size = [1500, 3072]     | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 1500, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]   | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 1500, 768]> self = ?,<br>List[int] size = [1, 1500, -1, 64] | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 1500, 768]> self = ?,<br>List[int] size = [1500, 768]       | Unknown  | Done       | 1.0   | 0      |
| 11 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                   | Unknown  | Done       | 1.0   | 0      |
| 12 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [1, 1, 3072]           | Unknown  | Done       | 1.0   | 0      |
| 13 | Tensor<[1, 4, 12, 64]> self = ?,<br>List[int] size = [1, 4, -1]        | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 4, 3072]> self = ?,<br>List[int] size = [4, 3072]           | Unknown  | Done       | 1.0   | 0      |
| 15 | Tensor<[1, 4, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]      | Unknown  | Done       | 1.0   | 0      |
| 16 | Tensor<[1, 4, 768]> self = ?,<br>List[int] size = [1, 4, -1, 64]       | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 4, 768]> self = ?,<br>List[int] size = [4, 768]             | Unknown  | Done       | 1.0   | 0      |
| 18 | Tensor<[1, 4]> self = ?,<br>List[int] size = [-1, 4]                   | Unknown  | Done       | 1.0   | 0      |
| 19 | Tensor<[1, 768]> self = ?,<br>List[int] size = [1, 1, 768]             | Unknown  | Done       | 1.0   | 0      |
| 20 | Tensor<[1500, 3072]> self = ?,<br>List[int] size = [1, 1500, 3072]     | Unknown  | Done       | 1.0   | 0      |
| 21 | Tensor<[1500, 768]> self = ?,<br>List[int] size = [1, 1500, 768]       | Unknown  | Done       | 1.0   | 0      |
| 22 | Tensor<[1]> self = ?,<br>List[int] size = [1, 1]                       | Unknown  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[4, 3072]> self = ?,<br>List[int] size = [1, 4, 3072]           | Unknown  | Done       | 1.0   | 0      |
| 24 | Tensor<[4, 768]> self = ?,<br>List[int] size = [1, 4, 768]             | Unknown  | Done       | 1.0   | 0      |
| 25 | Tensor<[4]> self = ?,<br>List[int] size = [4, 1]                       | Unknown  | Unknown    | N/A   | N/A    |
### aten.where.self
|    | ATen Input Variations                                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 1]> condition = ?,<br>Tensor<[]> self = ?,<br>Tensor<[]> other = ?      | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, 5]> condition = ?,<br>Tensor<[]> self = ?,<br>Tensor<[]> other = ?      | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 1, s0 + 1]> condition = ?,<br>Tensor<[]> self = ?,<br>Tensor<[]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 4, 4]> condition = ?,<br>Tensor<[]> self = ?,<br>Tensor<[]> other = ?      | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[51865]> condition = ?,<br>Tensor<[]> self = ?,<br>Tensor<[1, 51865]> other = ?   | Unknown  | Unknown    | N/A   | N/A    |
### aten.zeros.default
|    | ATen Input Variations                                                                                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [1],<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |

