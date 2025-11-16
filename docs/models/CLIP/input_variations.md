# High Level Operations Status
|    | Operations                                               |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:---------------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._scaled_dot_product_flash_attention_for_cpu.default |                 25 |          13 |        12 |          0 | ✅          |     1   |
|  1 | aten._to_copy.default                                    |                  4 |           3 |         1 |          0 | ✅          |     1   |
|  2 | aten.add.Tensor                                          |                  4 |           4 |         0 |          0 | ✅          |     1   |
|  3 | aten.addmm.default                                       |                  6 |           3 |         3 |          0 | ✅          |     1   |
|  4 | aten.argmax.default                                      |                  1 |           0 |         0 |          0 | ✘           |     0   |
|  5 | aten.cat.default                                         |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  6 | aten.clone.default                                       |                  4 |           0 |         4 |          0 | ✅          |     1   |
|  7 | aten.convolution.default                                 |                  1 |           0 |         0 |          0 | ✘           |     0   |
|  8 | aten.div.Tensor                                          |                  2 |           2 |         0 |          0 | ✅          |     1   |
|  9 | aten.embedding.default                                   |                  3 |           1 |         2 |          0 | ✅          |     1   |
| 10 | aten.exp.default                                         |                  1 |           0 |         1 |          0 | ✅          |     1   |
| 11 | aten.expand.default                                      |                  3 |           2 |         1 |          0 | ✅          |     1   |
| 12 | aten.full.default                                        |                  1 |           0 |         1 |          0 | ✅          |     1   |
| 13 | aten.index.Tensor                                        |                  1 |           0 |         0 |          0 | ✘           |     0   |
| 14 | aten.lt.Tensor                                           |                  1 |           0 |         0 |          0 | ✘           |     0   |
| 15 | aten.masked_fill.Scalar                                  |                  2 |           1 |         0 |          0 | 🚧          |     0.5 |
| 16 | aten.mm.default                                          |                  3 |           3 |         0 |          0 | ✅          |     1   |
| 17 | aten.mul.Tensor                                          |                  5 |           5 |         0 |          0 | ✅          |     1   |
| 18 | aten.native_layer_norm.default                           |                  3 |           3 |         0 |          0 | ✅          |     1   |
| 19 | aten.pow.Tensor_Scalar                                   |                  4 |           4 |         0 |          0 | ✅          |     1   |
| 20 | aten.select.int                                          |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 21 | aten.sigmoid.default                                     |                  2 |           2 |         0 |          0 | ✅          |     1   |
| 22 | aten.slice.Tensor                                        |                 11 |           0 |        11 |          0 | ✅          |     1   |
| 23 | aten.sub.Tensor                                          |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 24 | aten.sum.dim_IntList                                     |                  2 |           0 |         0 |          0 | ✘           |     0   |
| 25 | aten.t.default                                           |                  9 |           2 |         7 |          0 | ✅          |     1   |
| 26 | aten.transpose.int                                       |                  5 |           5 |         0 |          0 | ✅          |     1   |
| 27 | aten.unsqueeze.default                                   |                  4 |           4 |         0 |          0 | ✅          |     1   |
| 28 | aten.view.default                                        |                 14 |          14 |         0 |          0 | ✅          |     1   |
***
### aten._scaled_dot_product_flash_attention_for_cpu.default
|    | ATen Input Variations                                                                                                                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 50, 64]> query = ?,<br>Tensor<[1, 12, 50, 64]> key = ?,<br>Tensor<[1, 12, 50, 64]> value = ?,<br>Optional[float] scale = 0.125                                                   | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_10),<br>Optional[float] scale = 0.125 | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_13),<br>Optional[float] scale = 0.125 | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_16),<br>Optional[float] scale = 0.125 | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_19),<br>Optional[float] scale = 0.125 | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_22),<br>Optional[float] scale = 0.125 | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_25),<br>Optional[float] scale = 0.125 | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_28),<br>Optional[float] scale = 0.125 | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_31),<br>Optional[float] scale = 0.125 | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_34),<br>Optional[float] scale = 0.125 | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_37),<br>Optional[float] scale = 0.125 | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_40),<br>Optional[float] scale = 0.125 | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_43),<br>Optional[float] scale = 0.125 | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_11,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_14,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_17,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_20,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_23,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_26,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_29,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
| 20 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_32,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
| 21 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_35,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
| 22 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_38,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_41,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[2, 8, 7, 64]> query = ?,<br>Tensor<[2, 8, 7, 64]> key = ?,<br>Tensor<[2, 8, 7, 64]> value = ?,<br>Optional[Tensor]<[2, 1, 7, 7]> attn_mask = slice_44,<br>Optional[float] scale = 0.125 | Removed  | Unknown    | N/A   | N/A    |
### aten._to_copy.default
|    | ATen Input Variations                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 1, 7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16                          | Done     | Fallback   |     1 |     -1 |
|  1 | Tensor<[2, 1, 7, 7]> self = ?,<br>Optional[int] dtype = torch.bool                              | Done     | Fallback   |     1 |     -1 |
|  2 | Tensor<[2, 7]> self = ?,<br>Optional[int] dtype = torch.int32,<br>Optional[Device] device = cpu | Removed  | Fallback   |     1 |     -1 |
|  3 | Tensor<[7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                | Done     | Fallback   |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                            | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<[1, 50, 768]> other = ? | Done     | Done       | 0.9999979544533946 | 0      |
|  1 | Tensor<[2, 1, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> other = ? | Done     | Unknown    | N/A                | N/A    |
|  2 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[1, 7, 512]> other = ?   | Done     | Done       | 0.9999978646673556 | 0      |
|  3 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[2, 7, 512]> other = ?   | Done     | Done       | 0.9999981452836538 | 0      |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[2048]> self = ?,<br>Tensor<[14, 512]> mat1 = ?,<br>Tensor<[512, 2048]> mat2 = ? | Done     | Done       | 0.999971 |      0 |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Removed  | Done       | 0.999967 |      0 |
|  2 | Tensor<[512]> self = ?,<br>Tensor<[14, 2048]> mat1 = ?,<br>Tensor<[2048, 512]> mat2 = ? | Done     | Done       | 0.999951 |      0 |
|  3 | Tensor<[512]> self = ?,<br>Tensor<[14, 512]> mat1 = ?,<br>Tensor<[512, 512]> mat2 = ?   | Done     | Done       | 0.999969 |      0 |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[50, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Removed  | Done       | 0.999944 |      0 |
|  5 | Tensor<[768]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Removed  | Done       | 0.999968 |      0 |
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
### aten.div.Tensor
|    | ATen Input Variations                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 1]> other = ? | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 1]> other = ? | Done     | Done       | 0.999995 |      0 |
### aten.embedding.default
|    | ATen Input Variations                                          | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[49408, 512]> weight = ?,<br>Tensor<[2, 7]> indices = ? | Done     | Done       |     1 |      0 |
|  1 | Tensor<[50, 768]> weight = ?,<br>Tensor<[1, 50]> indices = ?   | Removed  | Done       |     1 |      0 |
|  2 | Tensor<[77, 512]> weight = ?,<br>Tensor<[1, 7]> indices = ?    | Removed  | Done       |     1 |      0 |
### aten.exp.default
|    | ATen Input Variations   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[]> self = ?     | Removed  | Done       |     1 |      0 |
### aten.expand.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>List[int] size = [2, 1, 7, 7] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[2, 1, 1, 7]> self = ?,<br>List[int] size = [2, 1, 7, 7] | Done     | Done       |     1 |      0 |
|  2 | Tensor<[768]> self = ?,<br>List[int] size = [1, 1, -1]          | Removed  | Done       |     1 |      0 |
### aten.full.default
|    | ATen Input Variations                                                                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[int] size = [7, 7],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Removed  | Done       |     1 |      0 |
### aten.index.Tensor
|    | ATen Input Variations                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[2, 7, 512]> self = ?,<br>List[Optional[Tensor]] indices = [_folded_arange_1, <[2]>] | None     | Unknown    | N/A   | N/A    |
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
|    | ATen Input Variations                                     | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 512]> mat2 = ? | Done     | Done       | 0.999971 |      0 |
|  1 | Tensor<[2, 512]> self = ?,<br>Tensor<[512, 1]> mat2 = ?   | Done     | Done       | 1        |      0 |
|  2 | Tensor<[2, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ? | Done     | Done       | 0.999969 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor other = 1.702            | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ? | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[2, 1]> self = ?,<br>Tensor<[]> other = ?                   | Done     | Done       | 1        |      0 |
|  3 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor other = 1.702             | Done     | Done       | 0.999996 |      0 |
|  4 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?   | Done     | Done       | 0.999996 |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 50, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | 0.997264 |      3 |
|  1 | Tensor<[1, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05     | Done     | Done       | 0.999998 |      3 |
|  2 | Tensor<[2, 7, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05  | Done     | Done       | 0.99858  |      3 |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                             | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>number exponent = 0.5 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 512]> self = ?,<br>number exponent = 2 | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[2, 1]> self = ?,<br>number exponent = 0.5 | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[2, 512]> self = ?,<br>number exponent = 2 | Done     | Unknown    | N/A   | N/A    |
### aten.select.int
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>int index = 0 | Done     | Done       |     1 |      0 |
### aten.sigmoid.default
|    | ATen Input Variations          | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 50, 3072]> self = ? | Done     | Done       | 0.999754 |      0 |
|  1 | Tensor<[2, 7, 2048]> self = ?  | Done     | Done       | 0.999757 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 77]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Removed  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 77]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 7                        | Removed  | Done       | 1.0   | 0      |
|  6 | Tensor<[2, 1, 1, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       | 1.0   | -1     |
|  7 | Tensor<[2, 1, 7, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[2, 1, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[2, 1, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[2, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Done       | 1.0   | -1     |
### aten.sub.Tensor
|    | ATen Input Variations                              | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[2, 1, 7, 7]> other = ? | Done     | Unknown    | N/A   | N/A    |
### aten.sum.dim_IntList
|    | ATen Input Variations                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[2, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 512]> self = ?    | Done     | Done       |     1 |      0 |
|  1 | Tensor<[2, 1]> self = ?      | Done     | Done       |     1 |      0 |
|  2 | Tensor<[2048, 512]> self = ? | Removed  | Done       |     1 |      0 |
|  3 | Tensor<[3072, 768]> self = ? | Removed  | Done       |     1 |      0 |
|  4 | Tensor<[512, 2048]> self = ? | Removed  | Done       |     1 |      0 |
|  5 | Tensor<[512, 512]> self = ?  | Removed  | Done       |     1 |      0 |
|  6 | Tensor<[512, 768]> self = ?  | Removed  | Done       |     1 |      0 |
|  7 | Tensor<[768, 3072]> self = ? | Removed  | Done       |     1 |      0 |
|  8 | Tensor<[768, 768]> self = ?  | Removed  | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 50, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 50, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 768, 49]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
|  3 | Tensor<[2, 7, 8, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |      0 |
|  4 | Tensor<[2, 8, 7, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |      0 |
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
|  0 | Tensor<[1, 50, 12, 64]> self = ?,<br>List[int] size = [1, 50, 768] | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 50, 3072]> self = ?,<br>List[int] size = [50, 3072]     | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [1, 50, -1, 64] | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [50, 768]       | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 768, 7, 7]> self = ?,<br>List[int] size = [1, 768, 49]  | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[14, 2048]> self = ?,<br>List[int] size = [2, 7, 2048]      | Done     | Done       | 1.0   | 0      |
|  6 | Tensor<[14, 512]> self = ?,<br>List[int] size = [2, 7, 512]        | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[2, 7, 2048]> self = ?,<br>List[int] size = [14, 2048]      | Done     | Done       | 1.0   | 0      |
|  8 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [14, 512]        | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [2, 7, -1, 64]   | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[2, 7, 8, 64]> self = ?,<br>List[int] size = [2, 7, 512]    | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[2, 7]> self = ?,<br>List[int] size = [-1, 7]               | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[50, 3072]> self = ?,<br>List[int] size = [1, 50, 3072]     | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[50, 768]> self = ?,<br>List[int] size = [1, 50, 768]       | Done     | Unknown    | N/A   | N/A    |

