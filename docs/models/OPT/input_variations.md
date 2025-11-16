# High Level Operations Status
|    | Operations                                               |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:---------------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._scaled_dot_product_flash_attention_for_cpu.default |                 72 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._unsafe_view.default                                |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten.add.Tensor                                          |                 10 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.addmm.default                                       |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.any.default                                         |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.arange.default                                      |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.bitwise_or.Tensor                                   |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.cat.default                                         |                 28 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.clone.default                                       |                 11 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.copy.default                                        |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.cumsum.default                                      |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.embedding.default                                   |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.eq.Scalar                                           |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.expand.default                                      |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.full.default                                        |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.gt.Tensor                                           |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.index.Tensor                                        |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.isin.Tensor_Tensor                                  |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.lt.Scalar                                           |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.masked_fill.Scalar                                  |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.mm.default                                          |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.mul.Tensor                                          |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.native_layer_norm.default                           |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.new_ones.default                                    |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.relu.default                                        |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.select.int                                          |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 26 | aten.slice.Tensor                                        |                 23 |           0 |         0 |          0 | ✘           |       0 |
| 27 | aten.slice_scatter.default                               |                  9 |           0 |         0 |          0 | ✘           |       0 |
| 28 | aten.sub.Tensor                                          |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 29 | aten.t.default                                           |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 30 | aten.transpose.int                                       |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 31 | aten.triu.default                                        |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 32 | aten.unsqueeze.default                                   |                 12 |           0 |         0 |          0 | ✘           |       0 |
| 33 | aten.view.default                                        |                 16 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._scaled_dot_product_flash_attention_for_cpu.default
|    | ATen Input Variations                                                                                                                                                                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_104,<br>Optional[float] scale = 1.0              | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_110,<br>Optional[float] scale = 1.0              | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_116,<br>Optional[float] scale = 1.0              | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_122,<br>Optional[float] scale = 1.0              | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_128,<br>Optional[float] scale = 1.0              | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_134,<br>Optional[float] scale = 1.0              | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_140,<br>Optional[float] scale = 1.0              | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_146,<br>Optional[float] scale = 1.0              | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_152,<br>Optional[float] scale = 1.0              | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_158,<br>Optional[float] scale = 1.0              | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_164,<br>Optional[float] scale = 1.0              | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_26,<br>Optional[float] scale = 1.0               | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_32,<br>Optional[float] scale = 1.0               | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_38,<br>Optional[float] scale = 1.0               | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_44,<br>Optional[float] scale = 1.0               | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_50,<br>Optional[float] scale = 1.0               | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_56,<br>Optional[float] scale = 1.0               | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_62,<br>Optional[float] scale = 1.0               | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_68,<br>Optional[float] scale = 1.0               | Unknown  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_74,<br>Optional[float] scale = 1.0               | Unknown  | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_80,<br>Optional[float] scale = 1.0               | Unknown  | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_86,<br>Optional[float] scale = 1.0               | Unknown  | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_92,<br>Optional[float] scale = 1.0               | Unknown  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, 60, 64]> key = ?,<br>Tensor<[1, 16, 60, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, 60]> attn_mask = slice_98,<br>Optional[float] scale = 1.0               | Unknown  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s11 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_50,<br>Optional[float] scale = 1.0  | Unknown  | Unknown    | N/A   | N/A    |
| 25 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s13 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_56,<br>Optional[float] scale = 1.0  | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s15 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_62,<br>Optional[float] scale = 1.0  | Unknown  | Unknown    | N/A   | N/A    |
| 27 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s17 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_68,<br>Optional[float] scale = 1.0  | Unknown  | Unknown    | N/A   | N/A    |
| 28 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s19 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_74,<br>Optional[float] scale = 1.0  | Unknown  | Unknown    | N/A   | N/A    |
| 29 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s21 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_80,<br>Optional[float] scale = 1.0  | Unknown  | Unknown    | N/A   | N/A    |
| 30 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s23 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_86,<br>Optional[float] scale = 1.0  | Unknown  | Unknown    | N/A   | N/A    |
| 31 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s25 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_92,<br>Optional[float] scale = 1.0  | Unknown  | Unknown    | N/A   | N/A    |
| 32 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s27 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_98,<br>Optional[float] scale = 1.0  | Unknown  | Unknown    | N/A   | N/A    |
| 33 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s29 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_104,<br>Optional[float] scale = 1.0 | Unknown  | Unknown    | N/A   | N/A    |
| 34 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s3 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_26,<br>Optional[float] scale = 1.0   | Unknown  | Unknown    | N/A   | N/A    |
| 35 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s31 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_110,<br>Optional[float] scale = 1.0 | Unknown  | Unknown    | N/A   | N/A    |
| 36 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s33 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_116,<br>Optional[float] scale = 1.0 | Unknown  | Unknown    | N/A   | N/A    |
| 37 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s35 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_122,<br>Optional[float] scale = 1.0 | Unknown  | Unknown    | N/A   | N/A    |
| 38 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s37 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_128,<br>Optional[float] scale = 1.0 | Unknown  | Unknown    | N/A   | N/A    |
| 39 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s39 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_134,<br>Optional[float] scale = 1.0 | Unknown  | Unknown    | N/A   | N/A    |
| 40 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s41 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_140,<br>Optional[float] scale = 1.0 | Unknown  | Unknown    | N/A   | N/A    |
| 41 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s43 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_146,<br>Optional[float] scale = 1.0 | Unknown  | Unknown    | N/A   | N/A    |
| 42 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s45 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_152,<br>Optional[float] scale = 1.0 | Unknown  | Unknown    | N/A   | N/A    |
| 43 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s47 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_158,<br>Optional[float] scale = 1.0 | Unknown  | Unknown    | N/A   | N/A    |
| 44 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s49 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_164,<br>Optional[float] scale = 1.0 | Unknown  | Unknown    | N/A   | N/A    |
| 45 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s5 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_32,<br>Optional[float] scale = 1.0   | Unknown  | Unknown    | N/A   | N/A    |
| 46 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s7 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_38,<br>Optional[float] scale = 1.0   | Unknown  | Unknown    | N/A   | N/A    |
| 47 | Tensor<[1, 16, 1, 64]> query = ?,<br>Tensor<[1, 16, s0 + 1, 64]> key = ?,<br>Tensor<[1, 16, s9 + 1, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 1, s0 + 1]> attn_mask = slice_44,<br>Optional[float] scale = 1.0   | Unknown  | Unknown    | N/A   | N/A    |
| 48 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_104,<br>Optional[float] scale = 1.0            | Unknown  | Unknown    | N/A   | N/A    |
| 49 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_110,<br>Optional[float] scale = 1.0            | Unknown  | Unknown    | N/A   | N/A    |
| 50 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_116,<br>Optional[float] scale = 1.0            | Unknown  | Unknown    | N/A   | N/A    |
| 51 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_122,<br>Optional[float] scale = 1.0            | Unknown  | Unknown    | N/A   | N/A    |
| 52 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_128,<br>Optional[float] scale = 1.0            | Unknown  | Unknown    | N/A   | N/A    |
| 53 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_134,<br>Optional[float] scale = 1.0            | Unknown  | Unknown    | N/A   | N/A    |
| 54 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_140,<br>Optional[float] scale = 1.0            | Unknown  | Unknown    | N/A   | N/A    |
| 55 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_146,<br>Optional[float] scale = 1.0            | Unknown  | Unknown    | N/A   | N/A    |
| 56 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_152,<br>Optional[float] scale = 1.0            | Unknown  | Unknown    | N/A   | N/A    |
| 57 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_158,<br>Optional[float] scale = 1.0            | Unknown  | Unknown    | N/A   | N/A    |
| 58 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_164,<br>Optional[float] scale = 1.0            | Unknown  | Unknown    | N/A   | N/A    |
| 59 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_26,<br>Optional[float] scale = 1.0             | Unknown  | Unknown    | N/A   | N/A    |
| 60 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_32,<br>Optional[float] scale = 1.0             | Unknown  | Unknown    | N/A   | N/A    |
| 61 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_38,<br>Optional[float] scale = 1.0             | Unknown  | Unknown    | N/A   | N/A    |
| 62 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_44,<br>Optional[float] scale = 1.0             | Unknown  | Unknown    | N/A   | N/A    |
| 63 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_50,<br>Optional[float] scale = 1.0             | Unknown  | Unknown    | N/A   | N/A    |
| 64 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_56,<br>Optional[float] scale = 1.0             | Unknown  | Unknown    | N/A   | N/A    |
| 65 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_62,<br>Optional[float] scale = 1.0             | Unknown  | Unknown    | N/A   | N/A    |
| 66 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_68,<br>Optional[float] scale = 1.0             | Unknown  | Unknown    | N/A   | N/A    |
| 67 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_74,<br>Optional[float] scale = 1.0             | Unknown  | Unknown    | N/A   | N/A    |
| 68 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_80,<br>Optional[float] scale = 1.0             | Unknown  | Unknown    | N/A   | N/A    |
| 69 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_86,<br>Optional[float] scale = 1.0             | Unknown  | Unknown    | N/A   | N/A    |
| 70 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_92,<br>Optional[float] scale = 1.0             | Unknown  | Unknown    | N/A   | N/A    |
| 71 | Tensor<[1, 16, 59, 64]> query = ?,<br>Tensor<[1, 16, 59, 64]> key = ?,<br>Tensor<[1, 16, 59, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 59, 59]> attn_mask = slice_98,<br>Optional[float] scale = 1.0             | Unknown  | Unknown    | N/A   | N/A    |
### aten._unsafe_view.default
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1, 1, 1024]     | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 50272]> self = ?,<br>List[int] size = [1, 1, 50272]   | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 512]> self = ?,<br>List[int] size = [1, 1, 512]       | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[59, 1024]> self = ?,<br>List[int] size = [1, 59, 1024]   | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[59, 50272]> self = ?,<br>List[int] size = [1, 59, 50272] | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[59, 512]> self = ?,<br>List[int] size = [1, 59, 512]     | Unknown  | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> other = ?         | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?           | Unknown  | Done       | 0.9999982773405695 | 0      |
|  3 | Tensor<[1, 1, 59, 59]> self = ?,<br>Tensor<[1, 1, 1, 59]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1, 1024]> other = ?                 | Unknown  | Done       | 0.9999981143488617 | 0      |
|  5 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2                               | Unknown  | Done       | 1.0                | 0      |
|  6 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor<[1, 59, 1024]> other = ?         | Unknown  | Done       | 0.9999979904816403 | 0      |
|  7 | Tensor<[1, 59]> self = ?,<br>Tensor other = 2                              | Unknown  | Done       | 0.999987366877724  | 0      |
|  8 | Tensor<[1]> self = ?,<br>Tensor other = 1                                  | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[59, 1024]> self = ?,<br>Tensor<[59, 1024]> other = ?               | Unknown  | Done       | 0.9999980640608037 | 0      |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1024]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ?  | Unknown  | Done       | 0.999966 |      0 |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[1, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ?  | Unknown  | Done       | 0.999934 |      0 |
|  2 | Tensor<[1024]> self = ?,<br>Tensor<[59, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Unknown  | Done       | 0.999964 |      0 |
|  3 | Tensor<[1024]> self = ?,<br>Tensor<[59, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Unknown  | Done       | 0.999932 |      0 |
|  4 | Tensor<[4096]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ?  | Unknown  | Done       | 0.999965 |      0 |
|  5 | Tensor<[4096]> self = ?,<br>Tensor<[59, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Unknown  | Done       | 0.999964 |      0 |
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
### aten.cat.default
|    | ATen Input Variations                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 16, 59, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | List[Tensor] tensors = [<[1, 16, s0, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2  | Unknown  | Unknown    | N/A   | N/A    |
|  2 | List[Tensor] tensors = [<[1, 16, s11, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | List[Tensor] tensors = [<[1, 16, s13, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | List[Tensor] tensors = [<[1, 16, s15, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
|  5 | List[Tensor] tensors = [<[1, 16, s17, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
|  6 | List[Tensor] tensors = [<[1, 16, s19, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
|  7 | List[Tensor] tensors = [<[1, 16, s21, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
|  8 | List[Tensor] tensors = [<[1, 16, s23, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
|  9 | List[Tensor] tensors = [<[1, 16, s25, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
| 10 | List[Tensor] tensors = [<[1, 16, s27, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
| 11 | List[Tensor] tensors = [<[1, 16, s29, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
| 12 | List[Tensor] tensors = [<[1, 16, s3, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2  | Unknown  | Unknown    | N/A   | N/A    |
| 13 | List[Tensor] tensors = [<[1, 16, s31, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
| 14 | List[Tensor] tensors = [<[1, 16, s33, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
| 15 | List[Tensor] tensors = [<[1, 16, s35, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
| 16 | List[Tensor] tensors = [<[1, 16, s37, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
| 17 | List[Tensor] tensors = [<[1, 16, s39, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
| 18 | List[Tensor] tensors = [<[1, 16, s41, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
| 19 | List[Tensor] tensors = [<[1, 16, s43, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
| 20 | List[Tensor] tensors = [<[1, 16, s45, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
| 21 | List[Tensor] tensors = [<[1, 16, s47, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
| 22 | List[Tensor] tensors = [<[1, 16, s49, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
| 23 | List[Tensor] tensors = [<[1, 16, s5, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2  | Unknown  | Unknown    | N/A   | N/A    |
| 24 | List[Tensor] tensors = [<[1, 16, s7, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2  | Unknown  | Unknown    | N/A   | N/A    |
| 25 | List[Tensor] tensors = [<[1, 16, s9, 64]>, <[1, 16, 1, 64]>],<br>int dim = -2  | Unknown  | Unknown    | N/A   | N/A    |
| 26 | List[Tensor] tensors = [<[1, 59]>, <[1, 1]>],<br>int dim = -1                  | Unknown  | Done       | 1.0   | 0      |
| 27 | List[Tensor] tensors = [<[1, s0]>, <[1, 1]>],<br>int dim = -1                  | Unknown  | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 60]> self = ?                                                             | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, s0 + 1]> self = ?                                                         | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 1024]> self = ?                                                              | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 1, 59, 59]> self = ?                                                            | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1024]> self = ?                                                                 | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 16, 59, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 1]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 59, 1024]> self = ?                                                             | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 59, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 59]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[59, 1024]> self = ?                                                                | Unknown  | Done       | 1.0   | 0      |
### aten.copy.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> src = ?         | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> src = ? | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 59, 59]> self = ?,<br>Tensor<[1, 1, 59, 59]> src = ?       | Unknown  | Unknown    | N/A   | N/A    |
### aten.cumsum.default
|    | ATen Input Variations                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 59]> self = ?,<br>int dim = -1 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, s1]> self = ?,<br>int dim = -1 | Unknown  | Unknown    | N/A   | N/A    |
### aten.embedding.default
|    | ATen Input Variations                                                                   | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                          | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 59]> indices = ?                         | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 1  | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 59]> indices = ?,<br>int padding_idx = 1 | Unknown  | Done       |     1 |      0 |
### aten.eq.Scalar
|    | ATen Input Variations                                   | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 60]> self = ?,<br>number other = 0     | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>number other = 0 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 59, 59]> self = ?,<br>number other = 0    | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 59]> self = ?,<br>number other = 0           | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, s1]> self = ?,<br>number other = 0           | Unknown  | Unknown    | N/A   | N/A    |
### aten.expand.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 60]> self = ?,<br>List[int] size = [1, 1, -1, -1]     | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 1, -1, -1] | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 59, 59]> self = ?,<br>List[int] size = [1, 1, -1, -1]    | Unknown  | Unknown    | N/A   | N/A    |
### aten.full.default
|    | ATen Input Variations                                                                                                                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [1, 60],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False       | Unknown  | Unknown    | N/A   | N/A    |
|  1 | List[int] size = [1, <s0 + 1>],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
|  2 | List[int] size = [1],<br>number fill_value = False,<br>Optional[int] dtype = torch.bool,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | List[int] size = [1],<br>number<s0 >= 89> fill_value = ?,<br>Optional[int] dtype = torch.bool,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                           | Unknown  | Unknown    | N/A   | N/A    |
|  4 | List[int] size = [59, 59],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False      | Unknown  | Unknown    | N/A   | N/A    |
### aten.gt.Tensor
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[1, 1]> other = ?           | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor self = ?,<br>Tensor<[59, 1]> other = ?          | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[s0 + 1]> self = ?,<br>Tensor<[1, 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.index.Tensor
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 59]> self = ?,<br>List[Optional[Tensor]] indices = [None, <[59]>] | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, s0]> self = ?,<br>List[Optional[Tensor]] indices = [None, <[1]>]  | Unknown  | Unknown    | N/A   | N/A    |
### aten.isin.Tensor_Tensor
|    | ATen Input Variations                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor elements = ?,<br>Tensor test_elements = ?           | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1]> elements = ?,<br>Tensor<[1]> test_elements = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.lt.Scalar
|    | ATen Input Variations                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1]> self = ?,<br>number other = 0 | Unknown  | Unknown    | N/A   | N/A    |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> mask = ?,<br>number value = -3.3895313892515355e+38         | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> mask = ?,<br>number value = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 59, 59]> self = ?,<br>Tensor<[1, 1, 59, 59]> mask = ?,<br>number value = -3.3895313892515355e+38       | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 59]> self = ?,<br>Tensor<[1, 59]> mask = ?,<br>number value = 1                                           | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, s1]> self = ?,<br>Tensor<[1, s1]> mask = ?,<br>number value = 1                                           | Unknown  | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?  | Unknown  | Done       | 0.999968 |      0 |
|  1 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?   | Unknown  | Done       | 0.999972 |      0 |
|  2 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 50272]> mat2 = ?  | Unknown  | Done       | 0.999972 |      0 |
|  3 | Tensor<[59, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ? | Unknown  | Done       | 0.999955 |      0 |
|  4 | Tensor<[59, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?  | Unknown  | Done       | 0.999971 |      0 |
|  5 | Tensor<[59, 512]> self = ?,<br>Tensor<[512, 50272]> mat2 = ? | Unknown  | Done       | 0.999971 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.125         | Unknown  | Done       | 1.0                | 0      |
|  1 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor other = 0.125        | Unknown  | Done       | 1.0                | 0      |
|  2 | Tensor<[1, 60]> self = ?,<br>Tensor<[1, 60]> other = ?         | Unknown  | Done       | 0.9999976357827657 | 0      |
|  3 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[59, 59]> self = ?,<br>Tensor<[59, 59]> other = ?       | Unknown  | Unknown    | N/A                | N/A    |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                       | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05  | Unknown  | Done       | 0.999998 |      3 |
|  1 | Tensor<[1, 59, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05 | Unknown  | Done       | 0.996189 |      3 |
### aten.new_ones.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 59]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False | Unknown  | Fallback   | 1.0   | -1     |
|  1 | Tensor<[1, s0]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.relu.default
|    | ATen Input Variations       | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 4096]> self = ?  | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[59, 4096]> self = ? | Unknown  | Done       |     1 |      0 |
### aten.select.int
|    | ATen Input Variations                                       | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 60]> self = ?,<br>int dim = 1,<br>int index = -1 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, s0]> self = ?,<br>int dim = 1,<br>int index = -1 | Unknown  | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, 59]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 1, 1, 60]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 1, 60]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 1, 60]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1, 1, 60]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 1, 59, 59]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 1, 59, 59]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 1, 59, 59]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Unknown  | Done       | 1.0   | -1     |
| 13 | Tensor<[1, 1, 59, 59]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Unknown  | Done       | 1.0   | -1     |
| 14 | Tensor<[1, 59]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Done       | 1.0   | -1     |
| 15 | Tensor<[1, 59]> self = ?,<br>int dim = 1,<br>Optional[int] start = -59,<br>Optional[int] end = 9223372036854775807         | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 60]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Done       | 1.0   | -1     |
| 17 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, s0]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, s1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, s1]> self = ?,<br>int dim = 1,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807          | Unknown  | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1]> self = ?,<br>int dim = 0,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807              | Unknown  | Unknown    | N/A   | N/A    |
| 22 | Tensor<[59]> self = ?,<br>int dim = 0,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807             | Unknown  | Unknown    | N/A   | N/A    |
### aten.slice_scatter.default
|    | ATen Input Variations                                                                                                                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807         | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> src = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807         | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807         | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> src = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 1, 59, 59]> self = ?,<br>Tensor<[1, 1, 59, 59]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 1, 59, 59]> self = ?,<br>Tensor<[1, 1, 59, 59]> src = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 1, 59, 59]> self = ?,<br>Tensor<[1, 1, 59, 59]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
### aten.sub.Tensor
|    | ATen Input Variations                         | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 59]> self = ?,<br>Tensor other = 1 | Unknown  | Done       | 0.9999977546825711 | 0      |
|  1 | Tensor<[1, s1]> self = ?,<br>Tensor other = 1 | Unknown  | Unknown    | N/A                | N/A    |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1024, 1024]> self = ? | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1024, 4096]> self = ? | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1024, 512]> self = ?  | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[4096, 1024]> self = ? | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[50272, 512]> self = ? | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[512, 1024]> self = ?  | Unknown  | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 16, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 16, 59, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 59, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | Done       |     1 |      0 |
### aten.triu.default
|    | ATen Input Variations                          | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[59, 59]> self = ?,<br>int diagonal = 1 | Unknown  | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                           | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 59]> self = ?,<br>int dim = 2     | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 60]> self = ?,<br>int dim = 1     | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 60]> self = ?,<br>int dim = 2     | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 1 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 59, 59]> self = ?,<br>int dim = 1    | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 59]> self = ?,<br>int dim = 1        | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 60]> self = ?,<br>int dim = 0        | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 60]> self = ?,<br>int dim = 1        | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 0    | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 1    | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[59, 59]> self = ?,<br>int dim = 0       | Unknown  | Done       | 1.0   | 0      |
### aten.view.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [-1, 1024]       | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64]  | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1024]        | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 1, 16, 64]> self = ?,<br>List[int] size = [1, 1, -1]     | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [1, 512]          | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1, 1, 1024]        | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [-1, 1024]      | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64] | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [59, 1024]      | Unknown  | Done       | 1.0   | 0      |
| 10 | Tensor<[1, 59, 16, 64]> self = ?,<br>List[int] size = [1, 59, -1]   | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 59, 512]> self = ?,<br>List[int] size = [59, 512]        | Unknown  | Done       | 1.0   | 0      |
| 12 | Tensor<[1, 59]> self = ?,<br>List[int] size = [-1, 59]              | Unknown  | Done       | 1.0   | 0      |
| 13 | Tensor<[1]> self = ?,<br>List[int] size = [-1, 1]                   | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[59, 1024]> self = ?,<br>List[int] size = [1, 59, 1024]      | Unknown  | Done       | 1.0   | 0      |
| 15 | Tensor<[59]> self = ?,<br>List[int] size = [-1, 1]                  | Unknown  | Unknown    | N/A   | N/A    |

