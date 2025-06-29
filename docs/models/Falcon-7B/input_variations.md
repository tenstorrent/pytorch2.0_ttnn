# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._unsafe_view.default      |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten.add.Tensor                |                  4 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.all.default               |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.bmm.default               |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.cat.default               |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.clone.default             |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.embedding.default         |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.eq.Scalar                 |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.expand.default            |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.gelu.default              |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.index.Tensor              |                 65 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.logical_not.default       |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.masked_fill.Scalar        |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.mm.default                |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.mul.Scalar                |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.mul.Tensor                |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.native_layer_norm.default |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.neg.default               |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.permute.default           |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.slice.Tensor              |                  8 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.t.default                 |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.transpose.int             |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.tril.default              |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.unsqueeze.default         |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.view.default              |                 14 |           0 |         0 |          0 | ✘           |       0 |
| 26 | aten.zeros_like.default        |                  1 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 71, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A   | N/A    |
### aten._unsafe_view.default
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 7, 71, 64]> self = ?,<br>List[int] size = [1, 7, 4544] | Unknown  | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?   | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 7, 4544]> self = ?,<br>Tensor<[1, 7, 4544]> other = ?     | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 71, 7, 64]> self = ?,<br>Tensor<[1, 71, 7, 64]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 71, 7, 7]> self = ?,<br>Tensor<[7, 7]> other = ?          | Unknown  | Unknown    | N/A   | N/A    |
### aten.all.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 7]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.bmm.default
|    | ATen Input Variations                                         | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[71, 7, 64]> self = ?,<br>Tensor<[71, 64, 7]> mat2 = ? | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[71, 7, 7]> self = ?,<br>Tensor<[71, 7, 64]> mat2 = ?  | Unknown  | Unknown    | N/A   | N/A    |
### aten.cat.default
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 1, 7, 32]>, <[1, 1, 7, 32]>],<br>int dim = -1   | Unknown  | Unknown    | N/A   | N/A    |
|  1 | List[Tensor] tensors = [<[1, 71, 7, 32]>, <[1, 71, 7, 32]>],<br>int dim = -1 | Unknown  | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 7, 4544]> self = ?                                                             | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 7, 71, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Unknown    | N/A   | N/A    |
### aten.embedding.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[65024, 4544]> weight = ?,<br>Tensor<[1, 7]> indices = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.eq.Scalar
|    | ATen Input Variations                        | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 7]> self = ?,<br>number other = 1 | Unknown  | Unknown    | N/A   | N/A    |
### aten.expand.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 64, 7]> self = ?,<br>List[int] size = [1, 71, 64, 7]  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64]  | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64] | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 71, 7, 7]> self = ?,<br>List[int] size = [1, 71, 7, 7]   | Unknown  | Unknown    | N/A   | N/A    |
### aten.gelu.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 7, 18176]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.index.Tensor
|    | ATen Input Variations                                                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy]    | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_10] | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_11] | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_12] | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_13] | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_14] | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_15] | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_16] | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_17] | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_18] | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_19] | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_1]  | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_20] | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_21] | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_22] | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_23] | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_24] | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_25] | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_26] | Unknown  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_27] | Unknown  | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_28] | Unknown  | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_29] | Unknown  | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_2]  | Unknown  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_30] | Unknown  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_31] | Unknown  | Unknown    | N/A   | N/A    |
| 25 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_32] | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_33] | Unknown  | Unknown    | N/A   | N/A    |
| 27 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_34] | Unknown  | Unknown    | N/A   | N/A    |
| 28 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_35] | Unknown  | Unknown    | N/A   | N/A    |
| 29 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_36] | Unknown  | Unknown    | N/A   | N/A    |
| 30 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_37] | Unknown  | Unknown    | N/A   | N/A    |
| 31 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_38] | Unknown  | Unknown    | N/A   | N/A    |
| 32 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_39] | Unknown  | Unknown    | N/A   | N/A    |
| 33 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_3]  | Unknown  | Unknown    | N/A   | N/A    |
| 34 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_40] | Unknown  | Unknown    | N/A   | N/A    |
| 35 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_41] | Unknown  | Unknown    | N/A   | N/A    |
| 36 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_42] | Unknown  | Unknown    | N/A   | N/A    |
| 37 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_43] | Unknown  | Unknown    | N/A   | N/A    |
| 38 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_44] | Unknown  | Unknown    | N/A   | N/A    |
| 39 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_45] | Unknown  | Unknown    | N/A   | N/A    |
| 40 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_46] | Unknown  | Unknown    | N/A   | N/A    |
| 41 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_47] | Unknown  | Unknown    | N/A   | N/A    |
| 42 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_48] | Unknown  | Unknown    | N/A   | N/A    |
| 43 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_49] | Unknown  | Unknown    | N/A   | N/A    |
| 44 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_4]  | Unknown  | Unknown    | N/A   | N/A    |
| 45 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_50] | Unknown  | Unknown    | N/A   | N/A    |
| 46 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_51] | Unknown  | Unknown    | N/A   | N/A    |
| 47 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_52] | Unknown  | Unknown    | N/A   | N/A    |
| 48 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_53] | Unknown  | Unknown    | N/A   | N/A    |
| 49 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_54] | Unknown  | Unknown    | N/A   | N/A    |
| 50 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_55] | Unknown  | Unknown    | N/A   | N/A    |
| 51 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_56] | Unknown  | Unknown    | N/A   | N/A    |
| 52 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_57] | Unknown  | Unknown    | N/A   | N/A    |
| 53 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_58] | Unknown  | Unknown    | N/A   | N/A    |
| 54 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_59] | Unknown  | Unknown    | N/A   | N/A    |
| 55 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_5]  | Unknown  | Unknown    | N/A   | N/A    |
| 56 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_60] | Unknown  | Unknown    | N/A   | N/A    |
| 57 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_61] | Unknown  | Unknown    | N/A   | N/A    |
| 58 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_62] | Unknown  | Unknown    | N/A   | N/A    |
| 59 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_63] | Unknown  | Unknown    | N/A   | N/A    |
| 60 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_6]  | Unknown  | Unknown    | N/A   | N/A    |
| 61 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_7]  | Unknown  | Unknown    | N/A   | N/A    |
| 62 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_8]  | Unknown  | Unknown    | N/A   | N/A    |
| 63 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_lift_fresh_copy_9]  | Unknown  | Unknown    | N/A   | N/A    |
| 64 | Tensor<[7, 64]> self = ?,<br>List[Optional[Tensor]] indices = [<[1, 7]>]                                      | Unknown  | Unknown    | N/A   | N/A    |
### aten.logical_not.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[7, 7]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[7, 7]> self = ?,<br>Tensor<[7, 7]> mask = ?,<br>number value = -inf | Unknown  | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[7, 18176]> self = ?,<br>Tensor<[18176, 4544]> mat2 = ? | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[7, 4544]> self = ?,<br>Tensor<[4544, 18176]> mat2 = ?  | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[7, 4544]> self = ?,<br>Tensor<[4544, 4544]> mat2 = ?   | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[7, 4544]> self = ?,<br>Tensor<[4544, 4672]> mat2 = ?   | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[7, 4544]> self = ?,<br>Tensor<[4544, 65024]> mat2 = ?  | Unknown  | Unknown    | N/A   | N/A    |
### aten.mul.Scalar
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 64, 7]> self = ?,<br>number other = 0.3535533905932738  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 71, 7, 64]> self = ?,<br>number other = 0.3535533905932738 | Unknown  | Unknown    | N/A   | N/A    |
### aten.mul.Tensor
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 71, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 7, 4544]> input = ?,<br>List[int] normalized_shape = [4544],<br>Optional[Tensor]<[4544]> weight = ?,<br>Optional[Tensor]<[4544]> bias = ?,<br>float eps = 1e-05 | Unknown  | Unknown    | N/A   | N/A    |
### aten.neg.default
|    | ATen Input Variations           | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 7, 32]> self = ?  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 71, 7, 32]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.permute.default
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[18176, 4544]> self = ?,<br>List[int] dims = [1, 0]        | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[4544, 18176]> self = ?,<br>List[int] dims = [1, 0]        | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[4544, 4544]> self = ?,<br>List[int] dims = [1, 0]         | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[4672, 4544]> self = ?,<br>List[int] dims = [1, 0]         | Unknown  | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                    | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 32,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 7, 71, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 7, 73, 64]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -2                   | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 7, 73, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 71, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                   | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 71, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 32,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[2048, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 7                        | Unknown  | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[65024, 4544]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.transpose.int
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 7, 64]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 7, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 7, 71, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | Unknown    | N/A   | N/A    |
### aten.tril.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?         | Unknown  | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 7, 64]> self = ?,<br>int dim = 1 | Unknown  | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 7, 64]> self = ?,<br>List[int] size = [1, 1, 7, 64]   | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 7, 18176]> self = ?,<br>List[int] size = [7, 18176]      | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 7, 4544]> self = ?,<br>List[int] size = [7, 4544]        | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 7, 4672]> self = ?,<br>List[int] size = [1, 7, 73, 64]   | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 71, 64, 7]> self = ?,<br>List[int] size = [71, 64, 7]    | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64] | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] size = [71, 7, 64]    | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 71, 7, 7]> self = ?,<br>List[int] size = [71, 7, 7]      | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[7, 18176]> self = ?,<br>List[int] size = [1, 7, 18176]      | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[7, 4544]> self = ?,<br>List[int] size = [1, 7, 4544]        | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[7, 4672]> self = ?,<br>List[int] size = [1, 7, 4672]        | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[7, 65024]> self = ?,<br>List[int] size = [1, 7, 65024]      | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[71, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64]    | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[71, 7, 7]> self = ?,<br>List[int] size = [1, 71, 7, 7]      | Unknown  | Unknown    | N/A   | N/A    |
### aten.zeros_like.default
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  | Unknown    | N/A   | N/A    |

