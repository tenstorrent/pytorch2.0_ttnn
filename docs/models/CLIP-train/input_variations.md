# High Level Operations Status
|    | Operations                                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:------------------------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._scaled_dot_product_flash_attention_for_cpu.default          |                 13 |           0 |        12 |          0 | 🚧          |    0.92 |
|  1 | aten._scaled_dot_product_flash_attention_for_cpu_backward.default |                 13 |           0 |        12 |          0 | 🚧          |    0.92 |
|  2 | aten._to_copy.default                                             |                  4 |           3 |         1 |          0 | ✅          |    1    |
|  3 | aten.add.Tensor                                                   |                  9 |           9 |         0 |          0 | ✅          |    1    |
|  4 | aten.addmm.default                                                |                  6 |           6 |         0 |          0 | ✅          |    1    |
|  5 | aten.argmax.default                                               |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  6 | aten.cat.default                                                  |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  7 | aten.clone.default                                                |                  4 |           0 |         4 |          0 | ✅          |    1    |
|  8 | aten.convolution.default                                          |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  9 | aten.convolution_backward.default                                 |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.detach.default                                               |                  5 |           0 |         5 |          0 | ✅          |    1    |
| 11 | aten.div.Tensor                                                   |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 12 | aten.embedding.default                                            |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 13 | aten.embedding_dense_backward.default                             |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.exp.default                                                  |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 15 | aten.expand.default                                               |                  5 |           5 |         0 |          0 | ✅          |    1    |
| 16 | aten.full.default                                                 |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 17 | aten.index.Tensor                                                 |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 18 | aten.index_put.default                                            |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 19 | aten.lt.Tensor                                                    |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 20 | aten.masked_fill.Scalar                                           |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 21 | aten.mm.default                                                   |                 20 |          20 |         0 |          0 | ✅          |    1    |
| 22 | aten.mul.Scalar                                                   |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 23 | aten.mul.Tensor                                                   |                 10 |          10 |         0 |          0 | ✅          |    1    |
| 24 | aten.native_layer_norm.default                                    |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 25 | aten.native_layer_norm_backward.default                           |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 26 | aten.neg.default                                                  |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 27 | aten.new_zeros.default                                            |                  1 |           0 |         1 |          0 | ✅          |    1    |
| 28 | aten.pow.Tensor_Scalar                                            |                  8 |           8 |         0 |          0 | ✅          |    1    |
| 29 | aten.select.int                                                   |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 30 | aten.select_backward.default                                      |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 31 | aten.sigmoid.default                                              |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 32 | aten.sigmoid_backward.default                                     |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 33 | aten.slice.Tensor                                                 |                 13 |           3 |        10 |          0 | ✅          |    1    |
| 34 | aten.slice_backward.default                                       |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 35 | aten.sub.Tensor                                                   |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 36 | aten.sum.default                                                  |                  1 |           0 |         0 |          1 | ✘           |    0    |
| 37 | aten.sum.dim_IntList                                              |                 10 |           0 |         0 |          0 | ✘           |    0    |
| 38 | aten.t.default                                                    |                 16 |          16 |         0 |          0 | ✅          |    1    |
| 39 | aten.transpose.int                                                |                  6 |           6 |         0 |          0 | ✅          |    1    |
| 40 | aten.unsqueeze.default                                            |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 41 | aten.view.default                                                 |                 22 |          22 |         0 |          0 | ✅          |    1    |
| 42 | aten.zeros.default                                                |                  1 |           1 |         0 |          0 | ✅          |    1    |
***
### aten._scaled_dot_product_flash_attention_for_cpu.default
|    | ATen Input Variations                                                                                                                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 50, 64]> query = ?,<br>Tensor<[1, 12, 50, 64]> key = ?,<br>Tensor<[1, 12, 50, 64]> value = ?,<br>Optional[float] scale = 0.125                                                   | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_11,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_14,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_17,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_20,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_23,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_26,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_29,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_32,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_35,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_38,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_41,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_44,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
### aten._scaled_dot_product_flash_attention_for_cpu_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 50, 64]> grad_out = ?,<br>Tensor<[1, 12, 50, 64]> query = ?,<br>Tensor<[1, 12, 50, 64]> key = ?,<br>Tensor<[1, 12, 50, 64]> value = ?,<br>Tensor<[1, 12, 50, 64]> out = ?,<br>Tensor<[1, 12, 50]> logsumexp = ?,<br>float dropout_p = 0.0,<br>bool is_causal = False,<br>Optional[float] scale = 0.125                                             | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[2, 8, 7, 64]> grad_out = ?,<br>Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Tensor<[2, 8, 7, 64]> out = ?,<br>Tensor<[2, 8, 7]> logsumexp = ?,<br>float dropout_p = 0.0,<br>bool is_causal = False,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_11,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[2, 8, 7, 64]> grad_out = ?,<br>Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Tensor<[2, 8, 7, 64]> out = ?,<br>Tensor<[2, 8, 7]> logsumexp = ?,<br>float dropout_p = 0.0,<br>bool is_causal = False,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_14,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[2, 8, 7, 64]> grad_out = ?,<br>Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Tensor<[2, 8, 7, 64]> out = ?,<br>Tensor<[2, 8, 7]> logsumexp = ?,<br>float dropout_p = 0.0,<br>bool is_causal = False,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_17,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[2, 8, 7, 64]> grad_out = ?,<br>Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Tensor<[2, 8, 7, 64]> out = ?,<br>Tensor<[2, 8, 7]> logsumexp = ?,<br>float dropout_p = 0.0,<br>bool is_causal = False,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_20,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[2, 8, 7, 64]> grad_out = ?,<br>Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Tensor<[2, 8, 7, 64]> out = ?,<br>Tensor<[2, 8, 7]> logsumexp = ?,<br>float dropout_p = 0.0,<br>bool is_causal = False,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_23,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[2, 8, 7, 64]> grad_out = ?,<br>Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Tensor<[2, 8, 7, 64]> out = ?,<br>Tensor<[2, 8, 7]> logsumexp = ?,<br>float dropout_p = 0.0,<br>bool is_causal = False,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_26,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[2, 8, 7, 64]> grad_out = ?,<br>Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Tensor<[2, 8, 7, 64]> out = ?,<br>Tensor<[2, 8, 7]> logsumexp = ?,<br>float dropout_p = 0.0,<br>bool is_causal = False,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_29,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[2, 8, 7, 64]> grad_out = ?,<br>Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Tensor<[2, 8, 7, 64]> out = ?,<br>Tensor<[2, 8, 7]> logsumexp = ?,<br>float dropout_p = 0.0,<br>bool is_causal = False,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_32,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[2, 8, 7, 64]> grad_out = ?,<br>Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Tensor<[2, 8, 7, 64]> out = ?,<br>Tensor<[2, 8, 7]> logsumexp = ?,<br>float dropout_p = 0.0,<br>bool is_causal = False,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_35,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[2, 8, 7, 64]> grad_out = ?,<br>Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Tensor<[2, 8, 7, 64]> out = ?,<br>Tensor<[2, 8, 7]> logsumexp = ?,<br>float dropout_p = 0.0,<br>bool is_causal = False,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_38,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[2, 8, 7, 64]> grad_out = ?,<br>Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Tensor<[2, 8, 7, 64]> out = ?,<br>Tensor<[2, 8, 7]> logsumexp = ?,<br>float dropout_p = 0.0,<br>bool is_causal = False,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_41,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[2, 8, 7, 64]> grad_out = ?,<br>Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Tensor<[2, 8, 7, 64]> out = ?,<br>Tensor<[2, 8, 7]> logsumexp = ?,<br>float dropout_p = 0.0,<br>bool is_causal = False,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_44,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
### aten._to_copy.default
|    | ATen Input Variations                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 1, 7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16                          | Done     | Fallback   |     1 |     -1 |
|  1 | Tensor<[2, 1, 7, 7]> self = ?,<br>Optional[int] dtype = torch.bool                              | Done     | Fallback   |     1 |     -1 |
|  2 | Tensor<[2, 7]> self = ?,<br>Optional[int] dtype = torch.int32,<br>Optional[Device] device = cpu | Removed  | Fallback   |     1 |     -1 |
|  3 | Tensor<[7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                | Done     | Fallback   |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ? | Done     | Done       | 0.99999798390132   | 0      |
|  1 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<[1, 50, 768]> other = ?   | Done     | Done       | 0.9999979335318387 | 0      |
|  2 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?           | Done     | Done       | 0.9999983917019766 | 0      |
|  3 | Tensor<[1, 768]> self = ?,<br>Tensor<[1, 768]> other = ?           | Done     | Done       | 0.9999981011010042 | 0      |
|  4 | Tensor<[2, 1, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> other = ?   | Done     | Unknown    | N/A                | N/A    |
|  5 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?           | Done     | Done       | 0.9999980735903939 | 0      |
|  6 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?   | Done     | Done       | 0.9999980860029762 | 0      |
|  7 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[1, 7, 512]> other = ?     | Done     | Done       | 0.9999981093373539 | 0      |
|  8 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[2, 7, 512]> other = ?     | Done     | Done       | 0.9999981094332147 | 0      |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[2048]> self = ?,<br>Tensor<[14, 512]> mat1 = ?,<br>Tensor<[512, 2048]> mat2 = ? | Done     | Done       | 0.99997  |      0 |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     | Done       | 0.999967 |      0 |
|  2 | Tensor<[512]> self = ?,<br>Tensor<[14, 2048]> mat1 = ?,<br>Tensor<[2048, 512]> mat2 = ? | Done     | Done       | 0.999954 |      0 |
|  3 | Tensor<[512]> self = ?,<br>Tensor<[14, 512]> mat1 = ?,<br>Tensor<[512, 512]> mat2 = ?   | Done     | Done       | 0.99997  |      0 |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[50, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | Done       | 0.999943 |      0 |
|  5 | Tensor<[768]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | Done       | 0.999967 |      0 |
### aten.argmax.default
|    | ATen Input Variations                              | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 7]> self = ?,<br>Optional[int] dim = -1 | None     | Fallback   |     1 |     -1 |
### aten.cat.default
|    | ATen Input Variations                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 1, 768]>, <[1, 49, 768]>],<br>int dim = 1 | Done     | Done       |     1 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 50, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[1, 50, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |      0 |
|  2 | Tensor<[2, 7, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       |     1 |      0 |
|  3 | Tensor<[2, 8, 7, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                        | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 32, 32]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   |     1 |     -1 |
### aten.convolution_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                                               | Status   | Isolated   | PCC   |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 768, 7, 7]> grad_output = ?,<br>Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 32, 32]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False] | None     | Fallback   | N/A   |      0 |
### aten.detach.default
|    | ATen Input Variations            | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 50, 64]> self = ? | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 50, 3072]> self = ?   | Removed  | Done       | 1.0   | -1     |
|  2 | Tensor<[2, 7, 2048]> self = ?    | Removed  | Done       | 1.0   | -1     |
|  3 | Tensor<[2, 8, 7, 64]> self = ?   | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[]> self = ?              | Removed  | Done       | 1.0   | -1     |
### aten.div.Tensor
|    | ATen Input Variations                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 1]> other = ? | Done     | Done       | 0.999997 |      0 |
|  1 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 1]> other = ? | Done     | Done       | 0.999997 |      0 |
### aten.embedding.default
|    | ATen Input Variations                                          | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[49408, 512]> weight = ?,<br>Tensor<[2, 7]> indices = ? | Done     | Done       |     1 |      0 |
|  1 | Tensor<[50, 768]> weight = ?,<br>Tensor<[1, 50]> indices = ?   | Done     | Done       |     1 |      0 |
|  2 | Tensor<[77, 512]> weight = ?,<br>Tensor<[1, 7]> indices = ?    | Done     | Done       |     1 |      0 |
### aten.embedding_dense_backward.default
|    | ATen Input Variations                                                                                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 768]> grad_output = ?,<br>Tensor<[1, 50]> indices = ?,<br>int num_weights = 50,<br>int padding_idx = -1,<br>bool scale_grad_by_freq = False  | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 7, 512]> grad_output = ?,<br>Tensor<[1, 7]> indices = ?,<br>int num_weights = 77,<br>int padding_idx = -1,<br>bool scale_grad_by_freq = False    | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[2, 7, 512]> grad_output = ?,<br>Tensor<[2, 7]> indices = ?,<br>int num_weights = 49408,<br>int padding_idx = -1,<br>bool scale_grad_by_freq = False | None     | Fallback   |     1 |     -1 |
### aten.exp.default
|    | ATen Input Variations   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[]> self = ?     | Done     | Done       |     1 |      0 |
### aten.expand.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>List[int] size = [2, 1, 7, 7] | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1]> self = ?,<br>List[int] size = [1, 512]           | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[2, 1, 1, 7]> self = ?,<br>List[int] size = [2, 1, 7, 7] | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[2, 1]> self = ?,<br>List[int] size = [2, 512]           | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[768]> self = ?,<br>List[int] size = [1, 1, -1]          | Done     | Done       | 1.0   | 0      |
### aten.full.default
|    | ATen Input Variations                                                                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[int] size = [7, 7],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Done     | Done       |     1 |      0 |
### aten.index.Tensor
|    | ATen Input Variations                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[2, 7, 512]> self = ?,<br>List[Optional[Tensor]] indices = [_folded_arange_1, <[2]>] | None     | Unknown    | N/A   | N/A    |
### aten.index_put.default
|    | ATen Input Variations                                                                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 7, 512]> self = ?,<br>List[Optional[Tensor]] indices = [<[2]>, <[2]>],<br>Tensor<[2, 512]> values = ?,<br>bool accumulate = True | None     | Fallback   |     1 |     -1 |
### aten.lt.Tensor
|    | ATen Input Variations                | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor other = ? | None     | Unknown    | N/A   | N/A    |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[2, 1, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> mask = ?,<br>number value = -3.3895313892515355e+38 | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[7, 7]> self = ?,<br>Tensor<[7, 7]> mask = ?,<br>number value = 0                                   | None     | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 512]> mat2 = ?        | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 768]> mat2 = ?    | Done     | Done       | 0.999973 |      0 |
|  2 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 512]> mat2 = ?    | Done     | Done       | 0.999966 |      0 |
|  3 | Tensor<[14, 2048]> self = ?,<br>Tensor<[2048, 512]> mat2 = ? | Done     | Done       | 0.999956 |      0 |
|  4 | Tensor<[14, 512]> self = ?,<br>Tensor<[512, 2048]> mat2 = ?  | Done     | Done       | 0.999971 |      0 |
|  5 | Tensor<[14, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ?   | Done     | Done       | 0.999971 |      0 |
|  6 | Tensor<[2, 1]> self = ?,<br>Tensor<[1, 512]> mat2 = ?        | Done     | Done       | 0.999996 |      0 |
|  7 | Tensor<[2, 512]> self = ?,<br>Tensor<[512, 1]> mat2 = ?      | Done     | Done       | 1        |      0 |
|  8 | Tensor<[2, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ?    | Done     | Done       | 0.999973 |      0 |
|  9 | Tensor<[2048, 14]> self = ?,<br>Tensor<[14, 512]> mat2 = ?   | Done     | Done       | 0.999992 |      0 |
| 10 | Tensor<[3072, 50]> self = ?,<br>Tensor<[50, 768]> mat2 = ?   | Done     | Done       | 0.999986 |      0 |
| 11 | Tensor<[50, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | Done       | 0.999945 |      0 |
| 12 | Tensor<[50, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?  | Done     | Done       | 0.999968 |      0 |
| 13 | Tensor<[50, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | Done       | 0.999969 |      0 |
| 14 | Tensor<[512, 14]> self = ?,<br>Tensor<[14, 2048]> mat2 = ?   | Done     | Done       | 0.999992 |      0 |
| 15 | Tensor<[512, 14]> self = ?,<br>Tensor<[14, 512]> mat2 = ?    | Done     | Done       | 0.999992 |      0 |
| 16 | Tensor<[512, 1]> self = ?,<br>Tensor<[1, 768]> mat2 = ?      | Done     | Done       | 0.999992 |      0 |
| 17 | Tensor<[512, 2]> self = ?,<br>Tensor<[2, 512]> mat2 = ?      | Done     | Done       | 0.999992 |      0 |
| 18 | Tensor<[768, 50]> self = ?,<br>Tensor<[50, 3072]> mat2 = ?   | Done     | Done       | 0.999986 |      0 |
| 19 | Tensor<[768, 50]> self = ?,<br>Tensor<[50, 768]> mat2 = ?    | Done     | Done       | 0.999986 |      0 |
### aten.mul.Scalar
|    | ATen Input Variations                            | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>number other = 0.5   | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 512]> self = ?,<br>number other = 2.0 | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[2, 1]> self = ?,<br>number other = 0.5   | None     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[2, 512]> self = ?,<br>number other = 2.0 | None     | Unknown    | N/A   | N/A    |
### aten.mul.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?               | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor other = 1.702            | Done     | Done       | 0.999996009249444  | 0      |
|  2 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ? | Done     | Done       | 0.9999958985977929 | 0      |
|  3 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?           | Done     | Done       | 0.9999960530220504 | 0      |
|  4 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 1]> other = ?               | Done     | Done       | 1.0                | 0      |
|  5 | Tensor<[2, 1]> self = ?,<br>Tensor<[]> other = ?                   | Done     | Done       | 1.0                | 0      |
|  6 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?           | Done     | Done       | 0.9999963991411411 | 0      |
|  7 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor other = 1.702             | Done     | Done       | 0.9999960679849902 | 0      |
|  8 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?   | Done     | Done       | 0.9999960682578177 | 0      |
|  9 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                       | Done     | Done       | 1.0                | 0      |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 50, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | 0.997938 |      3 |
|  1 | Tensor<[1, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05     | Done     | Done       | 0.999998 |      3 |
|  2 | Tensor<[2, 7, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05  | Done     | Done       | 0.998742 |      3 |
### aten.native_layer_norm_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                   | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 768]> grad_out = ?,<br>Tensor<[1, 50, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Tensor<[1, 50, 1]> mean = ?,<br>Tensor<[1, 50, 1]> rstd = ?,<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[bool] output_mask = [True, True, True] | None     | Fallback   |     1 |      0 |
|  1 | Tensor<[1, 768]> grad_out = ?,<br>Tensor<[1, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Tensor<[1, 1]> mean = ?,<br>Tensor<[1, 1]> rstd = ?,<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[bool] output_mask = [True, True, True]                 | None     | Fallback   |     1 |      0 |
|  2 | Tensor<[2, 7, 512]> grad_out = ?,<br>Tensor<[2, 7, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Tensor<[2, 7, 1]> mean = ?,<br>Tensor<[2, 7, 1]> rstd = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[bool] output_mask = [True, True, True]     | None     | Fallback   |     1 |      0 |
### aten.neg.default
|    | ATen Input Variations     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 512]> self = ? | Done     | Done       |     1 |      0 |
|  1 | Tensor<[2, 512]> self = ? | Done     | Done       |     1 |      0 |
### aten.new_zeros.default
|    | ATen Input Variations                                                                                                                                                          | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 512]> self = ?,<br>List[int] size = [2, 7, 512],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Removed  | Done       |     1 |      0 |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                               | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>number exponent = -0.5  | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1]> self = ?,<br>number exponent = 0.5   | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 512]> self = ?,<br>number exponent = 1.0 | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 512]> self = ?,<br>number exponent = 2   | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[2, 1]> self = ?,<br>number exponent = -0.5  | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[2, 1]> self = ?,<br>number exponent = 0.5   | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[2, 512]> self = ?,<br>number exponent = 1.0 | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[2, 512]> self = ?,<br>number exponent = 2   | Done     | Unknown    | N/A   | N/A    |
### aten.select.int
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>int index = 0 | Done     | Done       |     1 |      0 |
### aten.select_backward.default
|    | ATen Input Variations                                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 768]> grad_output = ?,<br>List[int] input_sizes = [1, 50, 768],<br>int dim = 1,<br>int index = 0 | None     | Fallback   |     1 |     -1 |
### aten.sigmoid.default
|    | ATen Input Variations          | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 50, 3072]> self = ? | Done     | Done       | 0.999755 |      0 |
|  1 | Tensor<[2, 7, 2048]> self = ?  | Done     | Done       | 0.999757 |      0 |
### aten.sigmoid_backward.default
|    | ATen Input Variations                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 3072]> grad_output = ?,<br>Tensor<[1, 50, 3072]> output = ? | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[2, 7, 2048]> grad_output = ?,<br>Tensor<[2, 7, 2048]> output = ?   | None     | Fallback   |     1 |     -1 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 1                   | Done     | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 50                  | Done     | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 77]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Removed  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 77]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 7                        | Done     | Done       | 1.0   | 0      |
|  8 | Tensor<[2, 1, 1, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       | 1.0   | -1     |
|  9 | Tensor<[2, 1, 7, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[2, 1, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[2, 1, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[2, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Done       | 1.0   | -1     |
### aten.slice_backward.default
|    | ATen Input Variations                                                                                                                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 768]> grad_output = ?,<br>List[int] input_sizes = [1, 50, 768],<br>int dim = 0,<br>int start = 0,<br>int end = 9223372036854775807,<br>int step = 1 | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 768]> grad_output = ?,<br>List[int] input_sizes = [1, 768],<br>int dim = 1,<br>int start = 0,<br>int end = 9223372036854775807,<br>int step = 1         | None     | Fallback   |     1 |     -1 |
### aten.sub.Tensor
|    | ATen Input Variations                              | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[2, 1, 7, 7]> other = ? | Done     | Unknown    | N/A   | N/A    |
### aten.sum.default
|    | ATen Input Variations   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 1]> self = ? | Fallback | Fallback   |     1 |      0 |
### aten.sum.dim_IntList
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>Optional[List[int]] dim = [0, 1],<br>bool keepdim = True | None     | Fallback   | 1.0   | -1     |
|  1 | Tensor<[1, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True      | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 512]> self = ?,<br>Optional[List[int]] dim = [1],<br>bool keepdim = True       | None     | Fallback   | 1.0   | -1     |
|  3 | Tensor<[14, 2048]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True     | None     | Fallback   | 1.0   | -1     |
|  4 | Tensor<[14, 512]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True      | None     | Fallback   | 1.0   | -1     |
|  5 | Tensor<[2, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True      | None     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[2, 512]> self = ?,<br>Optional[List[int]] dim = [1],<br>bool keepdim = True       | None     | Fallback   | 1.0   | -1     |
|  7 | Tensor<[2, 7, 512]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True    | None     | Fallback   | 1.0   | -1     |
|  8 | Tensor<[50, 3072]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True     | None     | Fallback   | 1.0   | -1     |
|  9 | Tensor<[50, 768]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True      | None     | Fallback   | 1.0   | -1     |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 512]> self = ?    | Done     | Done       |     1 |      0 |
|  1 | Tensor<[14, 2048]> self = ?  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[14, 512]> self = ?   | Done     | Done       |     1 |      0 |
|  3 | Tensor<[2, 1]> self = ?      | Done     | Done       |     1 |      0 |
|  4 | Tensor<[2, 512]> self = ?    | Done     | Done       |     1 |      0 |
|  5 | Tensor<[2048, 512]> self = ? | Done     | Done       |     1 |      0 |
|  6 | Tensor<[3072, 768]> self = ? | Done     | Done       |     1 |      0 |
|  7 | Tensor<[50, 3072]> self = ?  | Done     | Done       |     1 |      0 |
|  8 | Tensor<[50, 768]> self = ?   | Done     | Done       |     1 |      0 |
|  9 | Tensor<[512, 1]> self = ?    | Done     | Done       |     1 |      0 |
| 10 | Tensor<[512, 2048]> self = ? | Done     | Done       |     1 |      0 |
| 11 | Tensor<[512, 512]> self = ?  | Done     | Done       |     1 |      0 |
| 12 | Tensor<[512, 768]> self = ?  | Done     | Done       |     1 |      0 |
| 13 | Tensor<[768, 3072]> self = ? | Done     | Done       |     1 |      0 |
| 14 | Tensor<[768, 512]> self = ?  | Done     | Done       |     1 |      0 |
| 15 | Tensor<[768, 768]> self = ?  | Done     | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 50, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 49, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 50, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 768, 49]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
|  4 | Tensor<[2, 7, 8, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |      0 |
|  5 | Tensor<[2, 8, 7, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                      | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 7, 7]> self = ?,<br>int dim = 1 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[2, 1, 7]> self = ?,<br>int dim = 2 | Done     | Done       |     1 |      0 |
|  2 | Tensor<[2, 7]> self = ?,<br>int dim = 1    | Done     | Done       |     1 |      0 |
|  3 | Tensor<[7, 7]> self = ?,<br>int dim = 0    | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [768]            | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 2048]> self = ?,<br>List[int] size = [2048]             | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [3072]             | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 50, 12, 64]> self = ?,<br>List[int] size = [1, 50, 768] | Done     | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 50, 3072]> self = ?,<br>List[int] size = [50, 3072]     | Done     | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [1, 50, -1, 64] | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [1, 50, 12, 64] | Done     | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [50, 768]       | Done     | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 512]> self = ?,<br>List[int] size = [512]               | Done     | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 768, 49]> self = ?,<br>List[int] size = [1, 768, 7, 7]  | Done     | Done       | 1.0   | 0      |
| 10 | Tensor<[1, 768, 7, 7]> self = ?,<br>List[int] size = [1, 768, 49]  | Done     | Done       | 1.0   | 0      |
| 11 | Tensor<[1, 768]> self = ?,<br>List[int] size = [768]               | Done     | Done       | 1.0   | 0      |
| 12 | Tensor<[14, 2048]> self = ?,<br>List[int] size = [2, 7, 2048]      | Done     | Done       | 1.0   | 0      |
| 13 | Tensor<[14, 512]> self = ?,<br>List[int] size = [2, 7, 512]        | Done     | Done       | 1.0   | 0      |
| 14 | Tensor<[2, 7, 2048]> self = ?,<br>List[int] size = [14, 2048]      | Done     | Done       | 1.0   | 0      |
| 15 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [14, 512]        | Done     | Done       | 1.0   | 0      |
| 16 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [2, 7, -1, 64]   | Done     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [2, 7, 8, 64]    | Done     | Done       | 1.0   | 0      |
| 18 | Tensor<[2, 7, 8, 64]> self = ?,<br>List[int] size = [2, 7, 512]    | Done     | Done       | 1.0   | 0      |
| 19 | Tensor<[2, 7]> self = ?,<br>List[int] size = [-1, 7]               | Done     | Done       | 1.0   | 0      |
| 20 | Tensor<[50, 3072]> self = ?,<br>List[int] size = [1, 50, 3072]     | Done     | Done       | 1.0   | 0      |
| 21 | Tensor<[50, 768]> self = ?,<br>List[int] size = [1, 50, 768]       | Done     | Done       | 1.0   | 0      |
### aten.zeros.default
|    | ATen Input Variations                                                                                                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [2, 7, 512],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Done     | Unknown    | N/A   | N/A    |

