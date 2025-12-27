# High Level Operations Status
|    | Operations                                               |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:---------------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._scaled_dot_product_flash_attention_for_cpu.default |                 64 |          32 |        32 |          0 | ✅          |     1   |
|  1 | aten._to_copy.default                                    |                  5 |           4 |         0 |          0 | 🚧          |     0.8 |
|  2 | aten._unsafe_view.default                                |                  5 |           5 |         0 |          0 | ✅          |     1   |
|  3 | aten.add.Tensor                                          |                  5 |           5 |         0 |          0 | ✅          |     1   |
|  4 | aten.bmm.default                                         |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  5 | aten.cat.default                                         |                  3 |           3 |         0 |          0 | ✅          |     1   |
|  6 | aten.clone.default                                       |                  2 |           0 |         2 |          0 | ✅          |     1   |
|  7 | aten.copy.default                                        |                  1 |           0 |         1 |          0 | ✅          |     1   |
|  8 | aten.cos.default                                         |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  9 | aten.embedding.default                                   |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 10 | aten.eq.Scalar                                           |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 11 | aten.expand.default                                      |                  5 |           2 |         3 |          0 | ✅          |     1   |
| 12 | aten.full.default                                        |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 13 | aten.gt.Tensor                                           |                  1 |           0 |         0 |          0 | ✘           |     0   |
| 14 | aten.masked_fill.Scalar                                  |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 15 | aten.mean.dim                                            |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 16 | aten.mm.default                                          |                  5 |           5 |         0 |          0 | ✅          |     1   |
| 17 | aten.mul.Tensor                                          |                  6 |           6 |         0 |          0 | ✅          |     1   |
| 18 | aten.neg.default                                         |                  2 |           2 |         0 |          0 | ✅          |     1   |
| 19 | aten.pow.Tensor_Scalar                                   |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 20 | aten.rsqrt.default                                       |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 21 | aten.silu.default                                        |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 22 | aten.sin.default                                         |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 23 | aten.slice.Tensor                                        |                 18 |           4 |        14 |          0 | ✅          |     1   |
| 24 | aten.slice_scatter.default                               |                  3 |           0 |         3 |          0 | ✅          |     1   |
| 25 | aten.t.default                                           |                  5 |           5 |         0 |          0 | ✅          |     1   |
| 26 | aten.transpose.int                                       |                  3 |           3 |         0 |          0 | ✅          |     1   |
| 27 | aten.unsqueeze.default                                   |                  9 |           9 |         0 |          0 | ✅          |     1   |
| 28 | aten.view.default                                        |                  8 |           8 |         0 |          0 | ✅          |     1   |
***
### aten._scaled_dot_product_flash_attention_for_cpu.default
|    | ATen Input Variations                                                                                                                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_104)    | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_122)    | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_140)    | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_158)    | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_176)    | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_194)    | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_212)    | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_230)    | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_248)    | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_266)    | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_284)    | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_302)    | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_32)     | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_320)    | Done     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_338)    | Done     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_356)    | Done     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_374)    | Done     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_392)    | Done     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_410)    | Done     | Unknown    | N/A   | N/A    |
| 19 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_428)    | Done     | Unknown    | N/A   | N/A    |
| 20 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_446)    | Done     | Unknown    | N/A   | N/A    |
| 21 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_464)    | Done     | Unknown    | N/A   | N/A    |
| 22 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_482)    | Done     | Unknown    | N/A   | N/A    |
| 23 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_50)     | Done     | Unknown    | N/A   | N/A    |
| 24 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_500)    | Done     | Unknown    | N/A   | N/A    |
| 25 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_518)    | Done     | Unknown    | N/A   | N/A    |
| 26 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_536)    | Done     | Unknown    | N/A   | N/A    |
| 27 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_554)    | Done     | Unknown    | N/A   | N/A    |
| 28 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_572)    | Done     | Unknown    | N/A   | N/A    |
| 29 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_590)    | Done     | Unknown    | N/A   | N/A    |
| 30 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_68)     | Done     | Unknown    | N/A   | N/A    |
| 31 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_86)     | Done     | Unknown    | N/A   | N/A    |
| 32 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_104 | Removed  | Unknown    | N/A   | N/A    |
| 33 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_125 | Removed  | Unknown    | N/A   | N/A    |
| 34 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_146 | Removed  | Unknown    | N/A   | N/A    |
| 35 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_167 | Removed  | Unknown    | N/A   | N/A    |
| 36 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_188 | Removed  | Unknown    | N/A   | N/A    |
| 37 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_209 | Removed  | Unknown    | N/A   | N/A    |
| 38 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_230 | Removed  | Unknown    | N/A   | N/A    |
| 39 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_251 | Removed  | Unknown    | N/A   | N/A    |
| 40 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_272 | Removed  | Unknown    | N/A   | N/A    |
| 41 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_293 | Removed  | Unknown    | N/A   | N/A    |
| 42 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_314 | Removed  | Unknown    | N/A   | N/A    |
| 43 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_335 | Removed  | Unknown    | N/A   | N/A    |
| 44 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_356 | Removed  | Unknown    | N/A   | N/A    |
| 45 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_377 | Removed  | Unknown    | N/A   | N/A    |
| 46 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_398 | Removed  | Unknown    | N/A   | N/A    |
| 47 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_41  | Removed  | Unknown    | N/A   | N/A    |
| 48 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_419 | Removed  | Unknown    | N/A   | N/A    |
| 49 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_440 | Removed  | Unknown    | N/A   | N/A    |
| 50 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_461 | Removed  | Unknown    | N/A   | N/A    |
| 51 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_482 | Removed  | Unknown    | N/A   | N/A    |
| 52 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_503 | Removed  | Unknown    | N/A   | N/A    |
| 53 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_524 | Removed  | Unknown    | N/A   | N/A    |
| 54 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_545 | Removed  | Unknown    | N/A   | N/A    |
| 55 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_566 | Removed  | Unknown    | N/A   | N/A    |
| 56 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_587 | Removed  | Unknown    | N/A   | N/A    |
| 57 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_608 | Removed  | Unknown    | N/A   | N/A    |
| 58 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_62  | Removed  | Unknown    | N/A   | N/A    |
| 59 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_629 | Removed  | Unknown    | N/A   | N/A    |
| 60 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_650 | Removed  | Unknown    | N/A   | N/A    |
| 61 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_671 | Removed  | Unknown    | N/A   | N/A    |
| 62 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_692 | Removed  | Unknown    | N/A   | N/A    |
| 63 | Tensor<[32, 32, 32, 128]> query = ?,<br>Tensor<[32, 32, 32, 128]> key = ?,<br>Tensor<[32, 32, 32, 128]> value = ?,<br>Optional[Tensor]<[32, 1, 32, 32]> attn_mask = slice_83  | Removed  | Unknown    | N/A   | N/A    |
### aten._to_copy.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>Optional[int] dtype = torch.float32      | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 32, 128]> self = ?,<br>Optional[int] dtype = torch.bfloat16   | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[32, 32, 32768]> self = ?,<br>Optional[int] dtype = torch.float32 | None     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[32, 32, 4096]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[32, 32, 4096]> self = ?,<br>Optional[int] dtype = torch.float32  | Done     | Unknown    | N/A   | N/A    |
### aten._unsafe_view.default
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1024, 1024]> self = ?,<br>List[int] size = [32, 32, 1024]           | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1024, 14336]> self = ?,<br>List[int] size = [32, 32, 14336]         | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1024, 32768]> self = ?,<br>List[int] size = [32, 32, 32768]         | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1024, 4096]> self = ?,<br>List[int] size = [32, 32, 4096]           | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[32, 8, 4, 32, 128]> self = ?,<br>List[int] size = [32, 32, 32, 128] | Done     | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 1, 32, 32]> self = ?,<br>Tensor<[32, 1, 1, 32]> other = ?      | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32, 32, 1]> self = ?,<br>Tensor other = 1e-05                      | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[32, 32, 32, 128]> self = ?,<br>Tensor<[32, 32, 32, 128]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[32, 32, 4096]> self = ?,<br>Tensor<[32, 32, 4096]> other = ?       | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[32, 8, 32, 128]> self = ?,<br>Tensor<[32, 8, 32, 128]> other = ?   | Done     | Unknown    | N/A   | N/A    |
### aten.bmm.default
|    | ATen Input Variations                                       | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 64, 1]> self = ?,<br>Tensor<[1, 1, 32]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
### aten.cat.default
|    | ATen Input Variations                                                            | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 32, 64]>, <[1, 32, 64]>],<br>int dim = -1           | Done     | Unknown    | N/A   | N/A    |
|  1 | List[Tensor] tensors = [<[32, 32, 32, 64]>, <[32, 32, 32, 64]>],<br>int dim = -1 | Done     | Unknown    | N/A   | N/A    |
|  2 | List[Tensor] tensors = [<[32, 8, 32, 64]>, <[32, 8, 32, 64]>],<br>int dim = -1   | Done     | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 1, 32, 32]> self = ?                                                               | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32, 8, 4, 32, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Unknown    | N/A   | N/A    |
### aten.copy.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 1, 32, 32]> self = ?,<br>Tensor<[32, 1, 32, 32]> src = ? | Removed  | Unknown    | N/A   | N/A    |
### aten.cos.default
|    | ATen Input Variations         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 128]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.embedding.default
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32768, 4096]> weight = ?,<br>Tensor<[32, 32]> indices = ? | Done     | Unknown    | N/A   | N/A    |
### aten.eq.Scalar
|    | ATen Input Variations                                 | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 1, 32, 32]> self = ?,<br>number other = 0 | Done     | Unknown    | N/A   | N/A    |
### aten.expand.default
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 32, 32]> self = ?,<br>List[int] size = [32, 1, -1, -1]          | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32]                   | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, -1, 1]                   | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, 64, 1]                   | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[32, 8, 1, 32, 128]> self = ?,<br>List[int] size = [32, 8, 4, 32, 128] | Done     | Unknown    | N/A   | N/A    |
### aten.full.default
|    | ATen Input Variations                                                                                                                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [32, 32],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Done     | Unknown    | N/A   | N/A    |
### aten.gt.Tensor
|    | ATen Input Variations                | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor other = ? | None     | Unknown    | N/A   | N/A    |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 1, 32, 32]> self = ?,<br>Tensor<[32, 1, 32, 32]> mask = ?,<br>number value = -3.3895313892515355e+38 | Done     | Unknown    | N/A   | N/A    |
### aten.mean.dim
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 32, 4096]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | Done     | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1024, 14336]> self = ?,<br>Tensor<[14336, 4096]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1024, 4096]> self = ?,<br>Tensor<[4096, 1024]> mat2 = ?   | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1024, 4096]> self = ?,<br>Tensor<[4096, 14336]> mat2 = ?  | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1024, 4096]> self = ?,<br>Tensor<[4096, 32768]> mat2 = ?  | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1024, 4096]> self = ?,<br>Tensor<[4096, 4096]> mat2 = ?   | Done     | Unknown    | N/A   | N/A    |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 32, 14336]> self = ?,<br>Tensor<[32, 32, 14336]> other = ?   | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32, 32, 32, 128]> self = ?,<br>Tensor<[1, 1, 32, 128]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[32, 32, 4096]> self = ?,<br>Tensor<[32, 32, 1]> other = ?        | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[32, 32]> self = ?,<br>Tensor<[32, 32]> other = ?                 | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[32, 8, 32, 128]> self = ?,<br>Tensor<[1, 1, 32, 128]> other = ?  | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[4096]> self = ?,<br>Tensor<[32, 32, 4096]> other = ?             | Done     | Unknown    | N/A   | N/A    |
### aten.neg.default
|    | ATen Input Variations             | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 32, 32, 64]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32, 8, 32, 64]> self = ?  | Done     | Unknown    | N/A   | N/A    |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                   | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 32, 4096]> self = ?,<br>number exponent = 2 | Done     | Unknown    | N/A   | N/A    |
### aten.rsqrt.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 32, 1]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.silu.default
|    | ATen Input Variations            | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 32, 14336]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.sin.default
|    | ATen Input Variations         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 128]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 32, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 32, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807             | Removed  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[32, 1, 1, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Removed  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[32, 1, 32, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[32, 1, 32, 32]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[32, 1, 32, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[32, 32, 32, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 64                    | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[32, 32, 32, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 64,<br>Optional[int] end = 9223372036854775807  | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[32, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Removed  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[32, 8, 1, 32, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[32, 8, 1, 32, 128]> self = ?,<br>int dim = 4,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[32, 8, 32, 128]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[32, 8, 32, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[32, 8, 32, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 64                     | Done     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[32, 8, 32, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 64,<br>Optional[int] end = 9223372036854775807   | Done     | Unknown    | N/A   | N/A    |
### aten.slice_scatter.default
|    | ATen Input Variations                                                                                                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 1, 32, 32]> self = ?,<br>Tensor<[32, 1, 32, 32]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32, 1, 32, 32]> self = ?,<br>Tensor<[32, 1, 32, 32]> src = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[32, 1, 32, 32]> self = ?,<br>Tensor<[32, 1, 32, 32]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1024, 4096]> self = ?  | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[14336, 4096]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[32768, 4096]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[4096, 14336]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[4096, 4096]> self = ?  | Done     | Unknown    | N/A   | N/A    |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32, 32, 32, 128]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[32, 32, 8, 128]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Done     | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                             | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 128]> self = ?,<br>int dim = 1     | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 32, 32]> self = ?,<br>int dim = 1      | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 32]> self = ?,<br>int dim = 1          | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 64]> self = ?,<br>int dim = 2          | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[32, 1, 32]> self = ?,<br>int dim = 2      | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[32, 32]> self = ?,<br>int dim = 0         | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[32, 32]> self = ?,<br>int dim = 1         | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[32, 8, 32, 128]> self = ?,<br>int dim = 2 | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[64]> self = ?,<br>int dim = 0             | Done     | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32]            | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, 64, 1]            | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 64, 32]> self = ?,<br>List[int] size = [1, 64, 32]          | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[32, 32, 1024]> self = ?,<br>List[int] size = [32, 32, 8, 128]  | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[32, 32, 14336]> self = ?,<br>List[int] size = [1024, 14336]    | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[32, 32, 32, 128]> self = ?,<br>List[int] size = [32, 32, -1]   | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[32, 32, 4096]> self = ?,<br>List[int] size = [1024, 4096]      | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[32, 32, 4096]> self = ?,<br>List[int] size = [32, 32, 32, 128] | Done     | Unknown    | N/A   | N/A    |

