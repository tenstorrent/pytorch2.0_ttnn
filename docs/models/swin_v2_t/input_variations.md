# High Level Operations Status
|    | Operations                      |   Input Variations |   Converted |
|---:|:--------------------------------|-------------------:|------------:|
|  0 | aten._softmax.default           |                  4 |           0 |
|  1 | aten._unsafe_view.default       |                 19 |           0 |
|  2 | aten.add.Tensor                 |                 11 |           0 |
|  3 | aten.addmm.default              |                 18 |           0 |
|  4 | aten.as_strided.default         |                  1 |           0 |
|  5 | aten.bmm.default                |                  8 |           0 |
|  6 | aten.cat.default                |                  3 |           0 |
|  7 | aten.clamp.default              |                  4 |           0 |
|  8 | aten.clamp_min.default          |                  4 |           0 |
|  9 | aten.clone.default              |                 38 |           0 |
| 10 | aten.constant_pad_nd.default    |                  4 |           0 |
| 11 | aten.convolution.default        |                  1 |           0 |
| 12 | aten.div.Tensor                 |                  4 |           0 |
| 13 | aten.eq.Scalar                  |                  3 |           0 |
| 14 | aten.exp.default                |                  4 |           0 |
| 15 | aten.expand.default             |                 16 |           0 |
| 16 | aten.gelu.default               |                  4 |           0 |
| 17 | aten.index.Tensor               |                  4 |           0 |
| 18 | aten.linalg_vector_norm.default |                  4 |           0 |
| 19 | aten.masked_fill.Scalar         |                  6 |           0 |
| 20 | aten.mean.dim                   |                  1 |           0 |
| 21 | aten.mm.default                 |                  7 |           0 |
| 22 | aten.mul.Tensor                 |                  8 |           0 |
| 23 | aten.native_layer_norm.default  |                  4 |           0 |
| 24 | aten.ne.Scalar                  |                  3 |           0 |
| 25 | aten.new_zeros.default          |                  3 |           0 |
| 26 | aten.permute.default            |                 20 |           0 |
| 27 | aten.relu.default               |                  1 |           0 |
| 28 | aten.roll.default               |                  6 |           0 |
| 29 | aten.select.int                 |                 12 |           0 |
| 30 | aten.sigmoid.default            |                  4 |           0 |
| 31 | aten.slice.Tensor               |                 23 |           0 |
| 32 | aten.sub.Tensor                 |                  3 |           0 |
| 33 | aten.t.default                  |                 25 |           0 |
| 34 | aten.transpose.int              |                  8 |           0 |
| 35 | aten.unsqueeze.default          |                 16 |           0 |
| 36 | aten.view.default               |                 84 |           0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 64, 64]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Unknown  |
|  1 | Tensor<[16, 6, 64, 64]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Unknown  |
|  2 | Tensor<[4, 12, 64, 64]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Unknown  |
|  3 | Tensor<[64, 3, 64, 64]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>List[int]<> size = [4, 64, 384]     | Unknown  |
|  1 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>List[int]<> size = [1, 16, 16, 384] | Unknown  |
|  2 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>List[int]<> size = [16, 64, 192]    | Unknown  |
|  3 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>List[int]<> size = [1, 32, 32, 192] | Unknown  |
|  4 | Tensor<[1, 64, 24, 32]> self = ?,<br>List[int]<> size = [1, 64, 768]          | Unknown  |
|  5 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>List[int]<> size = [1, 64, 64, 96]   | Unknown  |
|  6 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>List[int]<> size = [64, 64, 96]      | Unknown  |
|  7 | Tensor<[16, 6, 32, 64]> self = ?,<br>List[int]<> size = [96, 32, 64]          | Unknown  |
|  8 | Tensor<[16, 6, 64, 32]> self = ?,<br>List[int]<> size = [96, 64, 32]          | Unknown  |
|  9 | Tensor<[16, 64, 6, 32]> self = ?,<br>List[int]<> size = [16, 64, 192]         | Unknown  |
| 10 | Tensor<[2, 2, 8, 8]> self = ?,<br>List[int]<> size = [4, 64]                  | Unknown  |
| 11 | Tensor<[4, 12, 32, 64]> self = ?,<br>List[int]<> size = [48, 32, 64]          | Unknown  |
| 12 | Tensor<[4, 12, 64, 32]> self = ?,<br>List[int]<> size = [48, 64, 32]          | Unknown  |
| 13 | Tensor<[4, 4, 8, 8]> self = ?,<br>List[int]<> size = [16, 64]                 | Unknown  |
| 14 | Tensor<[4, 64, 12, 32]> self = ?,<br>List[int]<> size = [4, 64, 384]          | Unknown  |
| 15 | Tensor<[64, 3, 32, 64]> self = ?,<br>List[int]<> size = [192, 32, 64]         | Unknown  |
| 16 | Tensor<[64, 3, 64, 32]> self = ?,<br>List[int]<> size = [192, 64, 32]         | Unknown  |
| 17 | Tensor<[64, 64, 3, 32]> self = ?,<br>List[int]<> size = [64, 64, 96]          | Unknown  |
| 18 | Tensor<[8, 8, 8, 8]> self = ?,<br>List[int]<> size = [64, 64]                 | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   |
|---:|:-----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 384]> self = ?,<br>Tensor<[1, 16, 16, 384]> other = ?     | Unknown  |
|  1 | Tensor<[1, 16, 6, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ? | Unknown  |
|  2 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[1, 24, 64, 64]> other = ?       | Unknown  |
|  3 | Tensor<[1, 32, 32, 192]> self = ?,<br>Tensor<[1, 32, 32, 192]> other = ?     | Unknown  |
|  4 | Tensor<[1, 4, 12, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?  | Unknown  |
|  5 | Tensor<[1, 64, 3, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ? | Unknown  |
|  6 | Tensor<[1, 64, 64, 96]> self = ?,<br>Tensor<[1, 64, 64, 96]> other = ?       | Unknown  |
|  7 | Tensor<[1, 8, 8, 768]> self = ?,<br>Tensor<[1, 8, 8, 768]> other = ?         | Unknown  |
|  8 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[1, 6, 64, 64]> other = ?        | Unknown  |
|  9 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[1, 12, 64, 64]> other = ?       | Unknown  |
| 10 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[1, 3, 64, 64]> other = ?        | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 1000]> mat2 = ?   | Unknown  |
|  1 | Tensor<[1152]> self = ?,<br>Tensor<[256, 384]> mat1 = ?,<br>Tensor<[384, 1152]> mat2 = ? | Unknown  |
|  2 | Tensor<[1536]> self = ?,<br>Tensor<[256, 384]> mat1 = ?,<br>Tensor<[384, 1536]> mat2 = ? | Unknown  |
|  3 | Tensor<[192]> self = ?,<br>Tensor<[1024, 192]> mat1 = ?,<br>Tensor<[192, 192]> mat2 = ?  | Unknown  |
|  4 | Tensor<[192]> self = ?,<br>Tensor<[1024, 768]> mat1 = ?,<br>Tensor<[768, 192]> mat2 = ?  | Unknown  |
|  5 | Tensor<[2304]> self = ?,<br>Tensor<[64, 768]> mat1 = ?,<br>Tensor<[768, 2304]> mat2 = ?  | Unknown  |
|  6 | Tensor<[288]> self = ?,<br>Tensor<[4096, 96]> mat1 = ?,<br>Tensor<[96, 288]> mat2 = ?    | Unknown  |
|  7 | Tensor<[3072]> self = ?,<br>Tensor<[64, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?  | Unknown  |
|  8 | Tensor<[384]> self = ?,<br>Tensor<[256, 1536]> mat1 = ?,<br>Tensor<[1536, 384]> mat2 = ? | Unknown  |
|  9 | Tensor<[384]> self = ?,<br>Tensor<[256, 384]> mat1 = ?,<br>Tensor<[384, 384]> mat2 = ?   | Unknown  |
| 10 | Tensor<[384]> self = ?,<br>Tensor<[4096, 96]> mat1 = ?,<br>Tensor<[96, 384]> mat2 = ?    | Unknown  |
| 11 | Tensor<[512]> self = ?,<br>Tensor<[225, 2]> mat1 = ?,<br>Tensor<[2, 512]> mat2 = ?       | Unknown  |
| 12 | Tensor<[576]> self = ?,<br>Tensor<[1024, 192]> mat1 = ?,<br>Tensor<[192, 576]> mat2 = ?  | Unknown  |
| 13 | Tensor<[768]> self = ?,<br>Tensor<[1024, 192]> mat1 = ?,<br>Tensor<[192, 768]> mat2 = ?  | Unknown  |
| 14 | Tensor<[768]> self = ?,<br>Tensor<[64, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?  | Unknown  |
| 15 | Tensor<[768]> self = ?,<br>Tensor<[64, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?    | Unknown  |
| 16 | Tensor<[96]> self = ?,<br>Tensor<[4096, 384]> mat1 = ?,<br>Tensor<[384, 96]> mat2 = ?    | Unknown  |
| 17 | Tensor<[96]> self = ?,<br>Tensor<[4096, 96]> mat1 = ?,<br>Tensor<[96, 96]> mat2 = ?      | Unknown  |
### aten.as_strided.default
|    | ATen Input Variations                                                                                             | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int]<> size = [1, 768, 1, 1],<br>List[int]<> stride = [768, 1, 768, 768] | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[192, 64, 32]> self = ?,<br>Tensor<[192, 32, 64]> mat2 = ? | Unknown  |
|  1 | Tensor<[192, 64, 64]> self = ?,<br>Tensor<[192, 64, 32]> mat2 = ? | Unknown  |
|  2 | Tensor<[24, 64, 32]> self = ?,<br>Tensor<[24, 32, 64]> mat2 = ?   | Unknown  |
|  3 | Tensor<[24, 64, 64]> self = ?,<br>Tensor<[24, 64, 32]> mat2 = ?   | Unknown  |
|  4 | Tensor<[48, 64, 32]> self = ?,<br>Tensor<[48, 32, 64]> mat2 = ?   | Unknown  |
|  5 | Tensor<[48, 64, 64]> self = ?,<br>Tensor<[48, 64, 32]> mat2 = ?   | Unknown  |
|  6 | Tensor<[96, 64, 32]> self = ?,<br>Tensor<[96, 32, 64]> mat2 = ?   | Unknown  |
|  7 | Tensor<[96, 64, 64]> self = ?,<br>Tensor<[96, 64, 32]> mat2 = ?   | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                                                                                                                                        | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([1, 16, 16, 192])', 'torch.Size([1, 16, 16, 192])', 'torch.Size([1, 16, 16, 192])', 'torch.Size([1, 16, 16, 192])'],<br>int<> dim = -1 | Unknown  |
|  1 | List[Tensor]<> tensors = ['torch.Size([1, 32, 32, 96])', 'torch.Size([1, 32, 32, 96])', 'torch.Size([1, 32, 32, 96])', 'torch.Size([1, 32, 32, 96])'],<br>int<> dim = -1     | Unknown  |
|  2 | List[Tensor]<> tensors = ['torch.Size([1, 8, 8, 384])', 'torch.Size([1, 8, 8, 384])', 'torch.Size([1, 8, 8, 384])', 'torch.Size([1, 8, 8, 384])'],<br>int<> dim = -1         | Unknown  |
### aten.clamp.default
|    | ATen Input Variations                                                                                     | Status   |
|---:|:----------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 1, 1]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 4.605170185988092 | Unknown  |
|  1 | Tensor<[24, 1, 1]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 4.605170185988092 | Unknown  |
|  2 | Tensor<[3, 1, 1]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 4.605170185988092  | Unknown  |
|  3 | Tensor<[6, 1, 1]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 4.605170185988092  | Unknown  |
### aten.clamp_min.default
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 64, 1]> self = ?,<br>number<> min = 1e-12 | Unknown  |
|  1 | Tensor<[16, 6, 64, 1]> self = ?,<br>number<> min = 1e-12 | Unknown  |
|  2 | Tensor<[4, 12, 64, 1]> self = ?,<br>number<> min = 1e-12 | Unknown  |
|  3 | Tensor<[64, 3, 64, 1]> self = ?,<br>number<> min = 1e-12 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 1536]> self = ?                                                                | Unknown  |
|  1 | Tensor<[1, 16, 16, 384]> self = ?                                                                 | Unknown  |
|  2 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Unknown  |
|  3 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Unknown  |
|  4 | Tensor<[1, 24, 64, 64]> self = ?                                                                  | Unknown  |
|  5 | Tensor<[1, 32, 32, 192]> self = ?                                                                 | Unknown  |
|  6 | Tensor<[1, 32, 32, 768]> self = ?                                                                 | Unknown  |
|  7 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Unknown  |
|  8 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Unknown  |
|  9 | Tensor<[1, 64, 24, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Unknown  |
| 10 | Tensor<[1, 64, 64, 384]> self = ?                                                                 | Unknown  |
| 11 | Tensor<[1, 64, 64, 96]> self = ?                                                                  | Unknown  |
| 12 | Tensor<[1, 64, 768]> self = ?                                                                     | Unknown  |
| 13 | Tensor<[1, 8, 8, 3072]> self = ?                                                                  | Unknown  |
| 14 | Tensor<[1, 8, 8, 768]> self = ?                                                                   | Unknown  |
| 15 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format  | Unknown  |
| 16 | Tensor<[12, 64, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Unknown  |
| 17 | Tensor<[16, 6, 32, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Unknown  |
| 18 | Tensor<[16, 6, 64, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Unknown  |
| 19 | Tensor<[16, 6, 64, 64]> self = ?                                                                  | Unknown  |
| 20 | Tensor<[16, 64, 192]> self = ?                                                                    | Unknown  |
| 21 | Tensor<[16, 64, 6, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Unknown  |
| 22 | Tensor<[2, 2, 8, 8]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Unknown  |
| 23 | Tensor<[24, 64, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Unknown  |
| 24 | Tensor<[3, 64, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format          | Unknown  |
| 25 | Tensor<[4, 12, 32, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Unknown  |
| 26 | Tensor<[4, 12, 64, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Unknown  |
| 27 | Tensor<[4, 12, 64, 64]> self = ?                                                                  | Unknown  |
| 28 | Tensor<[4, 4, 8, 8]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Unknown  |
| 29 | Tensor<[4, 64, 12, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Unknown  |
| 30 | Tensor<[4, 64, 384]> self = ?                                                                     | Unknown  |
| 31 | Tensor<[6, 64, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format          | Unknown  |
| 32 | Tensor<[64, 3, 32, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Unknown  |
| 33 | Tensor<[64, 3, 64, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Unknown  |
| 34 | Tensor<[64, 3, 64, 64]> self = ?                                                                  | Unknown  |
| 35 | Tensor<[64, 64, 3, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Unknown  |
| 36 | Tensor<[64, 64, 96]> self = ?                                                                     | Unknown  |
| 37 | Tensor<[8, 8, 8, 8]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Unknown  |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int]<> pad = [0, 0, 0, 0, 0, 0],<br>number<> value = 0.0 | Unknown  |
|  1 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int]<> pad = [0, 0, 0, 0, 0, 0],<br>number<> value = 0.0 | Unknown  |
|  2 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int]<> pad = [0, 0, 0, 0, 0, 0],<br>number<> value = 0.0  | Unknown  |
|  3 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int]<> pad = [0, 0, 0, 0, 0, 0],<br>number<> value = 0.0   | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                     | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 256, 256]> input = ?,<br>Tensor<[96, 3, 4, 4]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>List[int]<> stride = [4, 4],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 64, 32]> self = ?,<br>Tensor<[1, 24, 64, 32]> other = ? | Unknown  |
|  1 | Tensor<[16, 6, 64, 32]> self = ?,<br>Tensor<[16, 6, 64, 32]> other = ? | Unknown  |
|  2 | Tensor<[4, 12, 64, 32]> self = ?,<br>Tensor<[4, 12, 64, 32]> other = ? | Unknown  |
|  3 | Tensor<[64, 3, 64, 32]> self = ?,<br>Tensor<[64, 3, 64, 32]> other = ? | Unknown  |
### aten.eq.Scalar
|    | ATen Input Variations                                | Status   |
|---:|:-----------------------------------------------------|:---------|
|  0 | Tensor<[16, 64, 64]> self = ?,<br>number<> other = 0 | Unknown  |
|  1 | Tensor<[4, 64, 64]> self = ?,<br>number<> other = 0  | Unknown  |
|  2 | Tensor<[64, 64, 64]> self = ?,<br>number<> other = 0 | Unknown  |
### aten.exp.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[12, 1, 1]> self = ? | Unknown  |
|  1 | Tensor<[24, 1, 1]> self = ? | Unknown  |
|  2 | Tensor<[3, 1, 1]> self = ?  | Unknown  |
|  3 | Tensor<[6, 1, 1]> self = ?  | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 32, 64]> self = ?,<br>List[int]<> size = [1, 24, 32, 64] | Unknown  |
|  1 | Tensor<[1, 24, 64, 1]> self = ?,<br>List[int]<> size = [1, 24, 64, 32]  | Unknown  |
|  2 | Tensor<[1, 24, 64, 32]> self = ?,<br>List[int]<> size = [1, 24, 64, 32] | Unknown  |
|  3 | Tensor<[1, 24, 64, 64]> self = ?,<br>List[int]<> size = [1, 24, 64, 64] | Unknown  |
|  4 | Tensor<[16, 6, 32, 64]> self = ?,<br>List[int]<> size = [16, 6, 32, 64] | Unknown  |
|  5 | Tensor<[16, 6, 64, 1]> self = ?,<br>List[int]<> size = [16, 6, 64, 32]  | Unknown  |
|  6 | Tensor<[16, 6, 64, 32]> self = ?,<br>List[int]<> size = [16, 6, 64, 32] | Unknown  |
|  7 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int]<> size = [16, 6, 64, 64] | Unknown  |
|  8 | Tensor<[4, 12, 32, 64]> self = ?,<br>List[int]<> size = [4, 12, 32, 64] | Unknown  |
|  9 | Tensor<[4, 12, 64, 1]> self = ?,<br>List[int]<> size = [4, 12, 64, 32]  | Unknown  |
| 10 | Tensor<[4, 12, 64, 32]> self = ?,<br>List[int]<> size = [4, 12, 64, 32] | Unknown  |
| 11 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int]<> size = [4, 12, 64, 64] | Unknown  |
| 12 | Tensor<[64, 3, 32, 64]> self = ?,<br>List[int]<> size = [64, 3, 32, 64] | Unknown  |
| 13 | Tensor<[64, 3, 64, 1]> self = ?,<br>List[int]<> size = [64, 3, 64, 32]  | Unknown  |
| 14 | Tensor<[64, 3, 64, 32]> self = ?,<br>List[int]<> size = [64, 3, 64, 32] | Unknown  |
| 15 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int]<> size = [64, 3, 64, 64] | Unknown  |
### aten.gelu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 1536]> self = ? | Unknown  |
|  1 | Tensor<[1, 32, 32, 768]> self = ?  | Unknown  |
|  2 | Tensor<[1, 64, 64, 384]> self = ?  | Unknown  |
|  3 | Tensor<[1, 8, 8, 3072]> self = ?   | Unknown  |
### aten.index.Tensor
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[225, 12]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([4096])'] | Unknown  |
|  1 | Tensor<[225, 24]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([4096])'] | Unknown  |
|  2 | Tensor<[225, 3]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([4096])']  | Unknown  |
|  3 | Tensor<[225, 6]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([4096])']  | Unknown  |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                                  | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 64, 32]> self = ?,<br>number<> ord = 2.0,<br>Optional[List[int]]<> dim = [-1],<br>bool<> keepdim = True | Unknown  |
|  1 | Tensor<[16, 6, 64, 32]> self = ?,<br>number<> ord = 2.0,<br>Optional[List[int]]<> dim = [-1],<br>bool<> keepdim = True | Unknown  |
|  2 | Tensor<[4, 12, 64, 32]> self = ?,<br>number<> ord = 2.0,<br>Optional[List[int]]<> dim = [-1],<br>bool<> keepdim = True | Unknown  |
|  3 | Tensor<[64, 3, 64, 32]> self = ?,<br>number<> ord = 2.0,<br>Optional[List[int]]<> dim = [-1],<br>bool<> keepdim = True | Unknown  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 64, 64]> self = ?,<br>Tensor<[16, 64, 64]> mask = ?,<br>number<> value = -100.0 | Unknown  |
|  1 | Tensor<[16, 64, 64]> self = ?,<br>Tensor<[16, 64, 64]> mask = ?,<br>number<> value = 0.0    | Unknown  |
|  2 | Tensor<[4, 64, 64]> self = ?,<br>Tensor<[4, 64, 64]> mask = ?,<br>number<> value = -100.0   | Unknown  |
|  3 | Tensor<[4, 64, 64]> self = ?,<br>Tensor<[4, 64, 64]> mask = ?,<br>number<> value = 0.0      | Unknown  |
|  4 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 64]> mask = ?,<br>number<> value = -100.0 | Unknown  |
|  5 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 64]> mask = ?,<br>number<> value = 0.0    | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768, 8, 8]> self = ?,<br>Optional[List[int]]<> dim = [-1, -2],<br>bool<> keepdim = True | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[1024, 384]> self = ?,<br>Tensor<[384, 192]> mat2 = ? | Unknown  |
|  1 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 12]> mat2 = ?   | Unknown  |
|  2 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 24]> mat2 = ?   | Unknown  |
|  3 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 3]> mat2 = ?    | Unknown  |
|  4 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 6]> mat2 = ?    | Unknown  |
|  5 | Tensor<[256, 768]> self = ?,<br>Tensor<[768, 384]> mat2 = ?  | Unknown  |
|  6 | Tensor<[64, 1536]> self = ?,<br>Tensor<[1536, 768]> mat2 = ? | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 64, 64]> self = ?,<br>Tensor<> other = 16          | Unknown  |
|  1 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<> other = 16          | Unknown  |
|  2 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[24, 1, 1]> other = ? | Unknown  |
|  3 | Tensor<[1, 3, 64, 64]> self = ?,<br>Tensor<> other = 16           | Unknown  |
|  4 | Tensor<[1, 6, 64, 64]> self = ?,<br>Tensor<> other = 16           | Unknown  |
|  5 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[6, 1, 1]> other = ?  | Unknown  |
|  6 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[12, 1, 1]> other = ? | Unknown  |
|  7 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[3, 1, 1]> other = ?  | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                           | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 384]> input = ?,<br>List[int]<> normalized_shape = [384],<br>Optional[Tensor]<[384]> weight = ?,<br>Optional[Tensor]<[384]> bias = ?,<br>float<> eps = 1e-05 | Unknown  |
|  1 | Tensor<[1, 32, 32, 192]> input = ?,<br>List[int]<> normalized_shape = [192],<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>float<> eps = 1e-05 | Unknown  |
|  2 | Tensor<[1, 64, 64, 96]> input = ?,<br>List[int]<> normalized_shape = [96],<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>float<> eps = 1e-05     | Unknown  |
|  3 | Tensor<[1, 8, 8, 768]> input = ?,<br>List[int]<> normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float<> eps = 1e-05   | Unknown  |
### aten.ne.Scalar
|    | ATen Input Variations                                | Status   |
|---:|:-----------------------------------------------------|:---------|
|  0 | Tensor<[16, 64, 64]> self = ?,<br>number<> other = 0 | Unknown  |
|  1 | Tensor<[4, 64, 64]> self = ?,<br>number<> other = 0  | Unknown  |
|  2 | Tensor<[64, 64, 64]> self = ?,<br>number<> other = 0 | Unknown  |
### aten.new_zeros.default
|    | ATen Input Variations                                                                                  | Status   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 64, 192]> self = ?,<br>List[int]<> size = [32, 32],<br>Optional[bool]<> pin_memory = False | Unknown  |
|  1 | Tensor<[4, 64, 384]> self = ?,<br>List[int]<> size = [16, 16],<br>Optional[bool]<> pin_memory = False  | Unknown  |
|  2 | Tensor<[64, 64, 96]> self = ?,<br>List[int]<> size = [64, 64],<br>Optional[bool]<> pin_memory = False  | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                                           | Status   |
|---:|:--------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 8, 8, 768]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5] | Unknown  |
|  1 | Tensor<[1, 1, 8, 1, 8, 768]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5] | Unknown  |
|  2 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5] | Unknown  |
|  3 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5] | Unknown  |
|  4 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5] | Unknown  |
|  5 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5] | Unknown  |
|  6 | Tensor<[1, 64, 3, 24, 32]> self = ?,<br>List[int]<> dims = [2, 0, 3, 1, 4]      | Unknown  |
|  7 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int]<> dims = [0, 3, 1, 2]             | Unknown  |
|  8 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5]  | Unknown  |
|  9 | Tensor<[1, 96, 64, 64]> self = ?,<br>List[int]<> dims = [0, 2, 3, 1]            | Unknown  |
| 10 | Tensor<[16, 64, 3, 6, 32]> self = ?,<br>List[int]<> dims = [2, 0, 3, 1, 4]      | Unknown  |
| 11 | Tensor<[2, 8, 2, 8]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]               | Unknown  |
| 12 | Tensor<[4, 64, 3, 12, 32]> self = ?,<br>List[int]<> dims = [2, 0, 3, 1, 4]      | Unknown  |
| 13 | Tensor<[4, 8, 4, 8]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]               | Unknown  |
| 14 | Tensor<[64, 64, 12]> self = ?,<br>List[int]<> dims = [2, 0, 1]                  | Unknown  |
| 15 | Tensor<[64, 64, 24]> self = ?,<br>List[int]<> dims = [2, 0, 1]                  | Unknown  |
| 16 | Tensor<[64, 64, 3, 3, 32]> self = ?,<br>List[int]<> dims = [2, 0, 3, 1, 4]      | Unknown  |
| 17 | Tensor<[64, 64, 3]> self = ?,<br>List[int]<> dims = [2, 0, 1]                   | Unknown  |
| 18 | Tensor<[64, 64, 6]> self = ?,<br>List[int]<> dims = [2, 0, 1]                   | Unknown  |
| 19 | Tensor<[8, 8, 8, 8]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]               | Unknown  |
### aten.relu.default
|    | ATen Input Variations             | Status   |
|---:|:----------------------------------|:---------|
|  0 | Tensor<[1, 15, 15, 512]> self = ? | Unknown  |
### aten.roll.default
|    | ATen Input Variations                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int]<> shifts = [-4, -4],<br>List[int]<> dims = [1, 2] | Unknown  |
|  1 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int]<> shifts = [4, 4],<br>List[int]<> dims = [1, 2]   | Unknown  |
|  2 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int]<> shifts = [-4, -4],<br>List[int]<> dims = [1, 2] | Unknown  |
|  3 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int]<> shifts = [4, 4],<br>List[int]<> dims = [1, 2]   | Unknown  |
|  4 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int]<> shifts = [-4, -4],<br>List[int]<> dims = [1, 2]  | Unknown  |
|  5 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int]<> shifts = [4, 4],<br>List[int]<> dims = [1, 2]    | Unknown  |
### aten.select.int
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | Unknown  |
|  1 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 1 | Unknown  |
|  2 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 2 | Unknown  |
|  3 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | Unknown  |
|  4 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 1 | Unknown  |
|  5 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 2 | Unknown  |
|  6 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | Unknown  |
|  7 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 1 | Unknown  |
|  8 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 2 | Unknown  |
|  9 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | Unknown  |
| 10 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 1 | Unknown  |
| 11 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 2 | Unknown  |
### aten.sigmoid.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 12, 64, 64]> self = ? | Unknown  |
|  1 | Tensor<[1, 24, 64, 64]> self = ? | Unknown  |
|  2 | Tensor<[1, 3, 64, 64]> self = ?  | Unknown  |
|  3 | Tensor<[1, 6, 64, 64]> self = ?  | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                             | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 192]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
|  1 | Tensor<[1, 16, 16, 384]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
|  2 | Tensor<[1, 16, 16, 384]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
|  3 | Tensor<[1, 16, 16, 384]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
|  4 | Tensor<[1, 16, 16, 384]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
|  5 | Tensor<[1, 16, 32, 192]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
|  6 | Tensor<[1, 16, 32, 192]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
|  7 | Tensor<[1, 32, 32, 192]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
|  8 | Tensor<[1, 32, 32, 192]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
|  9 | Tensor<[1, 32, 32, 192]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
| 10 | Tensor<[1, 32, 32, 192]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
| 11 | Tensor<[1, 32, 32, 96]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                     | Unknown  |
| 12 | Tensor<[1, 32, 64, 96]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2  | Unknown  |
| 13 | Tensor<[1, 32, 64, 96]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2  | Unknown  |
| 14 | Tensor<[1, 64, 64, 96]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                     | Unknown  |
| 15 | Tensor<[1, 64, 64, 96]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2  | Unknown  |
| 16 | Tensor<[1, 64, 64, 96]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2  | Unknown  |
| 17 | Tensor<[1, 64, 64, 96]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                     | Unknown  |
| 18 | Tensor<[1, 8, 16, 384]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2  | Unknown  |
| 19 | Tensor<[1, 8, 16, 384]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2  | Unknown  |
| 20 | Tensor<[1, 8, 8, 384]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                      | Unknown  |
| 21 | Tensor<[1, 8, 8, 768]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                      | Unknown  |
| 22 | Tensor<[1, 8, 8, 768]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                      | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ? | Unknown  |
|  1 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?   | Unknown  |
|  2 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ? | Unknown  |
### aten.t.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | Tensor<[1000, 768]> self = ? | Unknown  |
|  1 | Tensor<[1152, 384]> self = ? | Unknown  |
|  2 | Tensor<[12, 512]> self = ?   | Unknown  |
|  3 | Tensor<[1536, 384]> self = ? | Unknown  |
|  4 | Tensor<[192, 192]> self = ?  | Unknown  |
|  5 | Tensor<[192, 384]> self = ?  | Unknown  |
|  6 | Tensor<[192, 768]> self = ?  | Unknown  |
|  7 | Tensor<[2304, 768]> self = ? | Unknown  |
|  8 | Tensor<[24, 512]> self = ?   | Unknown  |
|  9 | Tensor<[288, 96]> self = ?   | Unknown  |
| 10 | Tensor<[3, 512]> self = ?    | Unknown  |
| 11 | Tensor<[3072, 768]> self = ? | Unknown  |
| 12 | Tensor<[384, 1536]> self = ? | Unknown  |
| 13 | Tensor<[384, 384]> self = ?  | Unknown  |
| 14 | Tensor<[384, 768]> self = ?  | Unknown  |
| 15 | Tensor<[384, 96]> self = ?   | Unknown  |
| 16 | Tensor<[512, 2]> self = ?    | Unknown  |
| 17 | Tensor<[576, 192]> self = ?  | Unknown  |
| 18 | Tensor<[6, 512]> self = ?    | Unknown  |
| 19 | Tensor<[768, 1536]> self = ? | Unknown  |
| 20 | Tensor<[768, 192]> self = ?  | Unknown  |
| 21 | Tensor<[768, 3072]> self = ? | Unknown  |
| 22 | Tensor<[768, 768]> self = ?  | Unknown  |
| 23 | Tensor<[96, 384]> self = ?   | Unknown  |
| 24 | Tensor<[96, 96]> self = ?    | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 64, 32]> self = ?,<br>int<> dim0 = -2,<br>int<> dim1 = -1 | Unknown  |
|  1 | Tensor<[1, 24, 64, 32]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Unknown  |
|  2 | Tensor<[16, 6, 64, 32]> self = ?,<br>int<> dim0 = -2,<br>int<> dim1 = -1 | Unknown  |
|  3 | Tensor<[16, 6, 64, 32]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Unknown  |
|  4 | Tensor<[4, 12, 64, 32]> self = ?,<br>int<> dim0 = -2,<br>int<> dim1 = -1 | Unknown  |
|  5 | Tensor<[4, 12, 64, 32]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Unknown  |
|  6 | Tensor<[64, 3, 64, 32]> self = ?,<br>int<> dim0 = -2,<br>int<> dim1 = -1 | Unknown  |
|  7 | Tensor<[64, 3, 64, 32]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[12, 64, 64]> self = ?,<br>int<> dim = 0    | Unknown  |
|  1 | Tensor<[16, 1, 64, 64]> self = ?,<br>int<> dim = 0 | Unknown  |
|  2 | Tensor<[16, 64, 64]> self = ?,<br>int<> dim = 1    | Unknown  |
|  3 | Tensor<[16, 64]> self = ?,<br>int<> dim = 1        | Unknown  |
|  4 | Tensor<[16, 64]> self = ?,<br>int<> dim = 2        | Unknown  |
|  5 | Tensor<[24, 64, 64]> self = ?,<br>int<> dim = 0    | Unknown  |
|  6 | Tensor<[3, 64, 64]> self = ?,<br>int<> dim = 0     | Unknown  |
|  7 | Tensor<[4, 1, 64, 64]> self = ?,<br>int<> dim = 0  | Unknown  |
|  8 | Tensor<[4, 64, 64]> self = ?,<br>int<> dim = 1     | Unknown  |
|  9 | Tensor<[4, 64]> self = ?,<br>int<> dim = 1         | Unknown  |
| 10 | Tensor<[4, 64]> self = ?,<br>int<> dim = 2         | Unknown  |
| 11 | Tensor<[6, 64, 64]> self = ?,<br>int<> dim = 0     | Unknown  |
| 12 | Tensor<[64, 1, 64, 64]> self = ?,<br>int<> dim = 0 | Unknown  |
| 13 | Tensor<[64, 64, 64]> self = ?,<br>int<> dim = 1    | Unknown  |
| 14 | Tensor<[64, 64]> self = ?,<br>int<> dim = 1        | Unknown  |
| 15 | Tensor<[64, 64]> self = ?,<br>int<> dim = 2        | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 8, 8, 768]> self = ?,<br>List[int]<> size = [1, 64, 768]     | Unknown  |
|  1 | Tensor<[1, 1, 8, 1, 8, 768]> self = ?,<br>List[int]<> size = [1, 8, 8, 768]   | Unknown  |
|  2 | Tensor<[1, 15, 15, 12]> self = ?,<br>List[int]<> size = [-1, 12]              | Unknown  |
|  3 | Tensor<[1, 15, 15, 24]> self = ?,<br>List[int]<> size = [-1, 24]              | Unknown  |
|  4 | Tensor<[1, 15, 15, 2]> self = ?,<br>List[int]<> size = [225, 2]               | Unknown  |
|  5 | Tensor<[1, 15, 15, 3]> self = ?,<br>List[int]<> size = [-1, 3]                | Unknown  |
|  6 | Tensor<[1, 15, 15, 512]> self = ?,<br>List[int]<> size = [225, 512]           | Unknown  |
|  7 | Tensor<[1, 15, 15, 6]> self = ?,<br>List[int]<> size = [-1, 6]                | Unknown  |
|  8 | Tensor<[1, 16, 16, 1536]> self = ?,<br>List[int]<> size = [256, 1536]         | Unknown  |
|  9 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int]<> size = [1, 2, 8, 2, 8, 384] | Unknown  |
| 10 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int]<> size = [256, 384]           | Unknown  |
| 11 | Tensor<[1, 16, 16, 768]> self = ?,<br>List[int]<> size = [256, 768]           | Unknown  |
| 12 | Tensor<[1, 16, 6, 64, 64]> self = ?,<br>List[int]<> size = [-1, 6, 64, 64]    | Unknown  |
| 13 | Tensor<[1, 24, 32, 64]> self = ?,<br>List[int]<> size = [24, 32, 64]          | Unknown  |
| 14 | Tensor<[1, 24, 64, 32]> self = ?,<br>List[int]<> size = [24, 64, 32]          | Unknown  |
| 15 | Tensor<[1, 24, 64, 64]> self = ?,<br>List[int]<> size = [24, 64, 64]          | Unknown  |
| 16 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int]<> size = [1, 4, 8, 4, 8, 192] | Unknown  |
| 17 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int]<> size = [1024, 192]          | Unknown  |
| 18 | Tensor<[1, 32, 32, 384]> self = ?,<br>List[int]<> size = [1024, 384]          | Unknown  |
| 19 | Tensor<[1, 32, 32, 768]> self = ?,<br>List[int]<> size = [1024, 768]          | Unknown  |
| 20 | Tensor<[1, 4, 12, 64, 64]> self = ?,<br>List[int]<> size = [-1, 12, 64, 64]   | Unknown  |
| 21 | Tensor<[1, 64, 2304]> self = ?,<br>List[int]<> size = [1, 64, 3, 24, 32]      | Unknown  |
| 22 | Tensor<[1, 64, 3, 64, 64]> self = ?,<br>List[int]<> size = [-1, 3, 64, 64]    | Unknown  |
| 23 | Tensor<[1, 64, 64, 384]> self = ?,<br>List[int]<> size = [4096, 384]          | Unknown  |
| 24 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int]<> size = [1, 8, 8, 8, 8, 96]   | Unknown  |
| 25 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int]<> size = [4096, 96]            | Unknown  |
| 26 | Tensor<[1, 64, 768]> self = ?,<br>List[int]<> size = [1, 1, 1, 8, 8, 768]     | Unknown  |
| 27 | Tensor<[1, 64, 768]> self = ?,<br>List[int]<> size = [64, 768]                | Unknown  |
| 28 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int]<> size = [1, 768]               | Unknown  |
| 29 | Tensor<[1, 8, 8, 1536]> self = ?,<br>List[int]<> size = [64, 1536]            | Unknown  |
| 30 | Tensor<[1, 8, 8, 3072]> self = ?,<br>List[int]<> size = [64, 3072]            | Unknown  |
| 31 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int]<> size = [1, 1, 8, 1, 8, 768]   | Unknown  |
| 32 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int]<> size = [64, 768]              | Unknown  |
| 33 | Tensor<[1024, 192]> self = ?,<br>List[int]<> size = [1, 32, 32, 192]          | Unknown  |
| 34 | Tensor<[1024, 192]> self = ?,<br>List[int]<> size = [16, 64, 192]             | Unknown  |
| 35 | Tensor<[1024, 576]> self = ?,<br>List[int]<> size = [16, 64, 576]             | Unknown  |
| 36 | Tensor<[1024, 768]> self = ?,<br>List[int]<> size = [1, 32, 32, 768]          | Unknown  |
| 37 | Tensor<[16, 16]> self = ?,<br>List[int]<> size = [2, 8, 2, 8]                 | Unknown  |
| 38 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int]<> size = [1, 16, 6, 64, 64]    | Unknown  |
| 39 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int]<> size = [96, 64, 64]          | Unknown  |
| 40 | Tensor<[16, 64, 192]> self = ?,<br>List[int]<> size = [1, 4, 4, 8, 8, 192]    | Unknown  |
| 41 | Tensor<[16, 64, 192]> self = ?,<br>List[int]<> size = [1024, 192]             | Unknown  |
| 42 | Tensor<[16, 64, 576]> self = ?,<br>List[int]<> size = [16, 64, 3, 6, 32]      | Unknown  |
| 43 | Tensor<[192, 64, 32]> self = ?,<br>List[int]<> size = [64, 3, 64, 32]         | Unknown  |
| 44 | Tensor<[192, 64, 64]> self = ?,<br>List[int]<> size = [64, 3, 64, 64]         | Unknown  |
| 45 | Tensor<[225, 12]> self = ?,<br>List[int]<> size = [1, 15, 15, 12]             | Unknown  |
| 46 | Tensor<[225, 24]> self = ?,<br>List[int]<> size = [1, 15, 15, 24]             | Unknown  |
| 47 | Tensor<[225, 3]> self = ?,<br>List[int]<> size = [1, 15, 15, 3]               | Unknown  |
| 48 | Tensor<[225, 512]> self = ?,<br>List[int]<> size = [1, 15, 15, 512]           | Unknown  |
| 49 | Tensor<[225, 6]> self = ?,<br>List[int]<> size = [1, 15, 15, 6]               | Unknown  |
| 50 | Tensor<[24, 64, 32]> self = ?,<br>List[int]<> size = [1, 24, 64, 32]          | Unknown  |
| 51 | Tensor<[24, 64, 64]> self = ?,<br>List[int]<> size = [1, 24, 64, 64]          | Unknown  |
| 52 | Tensor<[256, 1152]> self = ?,<br>List[int]<> size = [4, 64, 1152]             | Unknown  |
| 53 | Tensor<[256, 1536]> self = ?,<br>List[int]<> size = [1, 16, 16, 1536]         | Unknown  |
| 54 | Tensor<[256, 384]> self = ?,<br>List[int]<> size = [1, 16, 16, 384]           | Unknown  |
| 55 | Tensor<[256, 384]> self = ?,<br>List[int]<> size = [4, 64, 384]               | Unknown  |
| 56 | Tensor<[32, 32]> self = ?,<br>List[int]<> size = [4, 8, 4, 8]                 | Unknown  |
| 57 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int]<> size = [1, 4, 12, 64, 64]    | Unknown  |
| 58 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int]<> size = [48, 64, 64]          | Unknown  |
| 59 | Tensor<[4, 64, 1152]> self = ?,<br>List[int]<> size = [4, 64, 3, 12, 32]      | Unknown  |
| 60 | Tensor<[4, 64, 384]> self = ?,<br>List[int]<> size = [1, 2, 2, 8, 8, 384]     | Unknown  |
| 61 | Tensor<[4, 64, 384]> self = ?,<br>List[int]<> size = [256, 384]               | Unknown  |
| 62 | Tensor<[4096, 12]> self = ?,<br>List[int]<> size = [64, 64, -1]               | Unknown  |
| 63 | Tensor<[4096, 24]> self = ?,<br>List[int]<> size = [64, 64, -1]               | Unknown  |
| 64 | Tensor<[4096, 288]> self = ?,<br>List[int]<> size = [64, 64, 288]             | Unknown  |
| 65 | Tensor<[4096, 384]> self = ?,<br>List[int]<> size = [1, 64, 64, 384]          | Unknown  |
| 66 | Tensor<[4096, 3]> self = ?,<br>List[int]<> size = [64, 64, -1]                | Unknown  |
| 67 | Tensor<[4096, 6]> self = ?,<br>List[int]<> size = [64, 64, -1]                | Unknown  |
| 68 | Tensor<[4096, 96]> self = ?,<br>List[int]<> size = [1, 64, 64, 96]            | Unknown  |
| 69 | Tensor<[4096, 96]> self = ?,<br>List[int]<> size = [64, 64, 96]               | Unknown  |
| 70 | Tensor<[48, 64, 32]> self = ?,<br>List[int]<> size = [4, 12, 64, 32]          | Unknown  |
| 71 | Tensor<[48, 64, 64]> self = ?,<br>List[int]<> size = [4, 12, 64, 64]          | Unknown  |
| 72 | Tensor<[64, 2304]> self = ?,<br>List[int]<> size = [1, 64, 2304]              | Unknown  |
| 73 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int]<> size = [1, 64, 3, 64, 64]    | Unknown  |
| 74 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int]<> size = [192, 64, 64]         | Unknown  |
| 75 | Tensor<[64, 3072]> self = ?,<br>List[int]<> size = [1, 8, 8, 3072]            | Unknown  |
| 76 | Tensor<[64, 64, 288]> self = ?,<br>List[int]<> size = [64, 64, 3, 3, 32]      | Unknown  |
| 77 | Tensor<[64, 64, 96]> self = ?,<br>List[int]<> size = [1, 8, 8, 8, 8, 96]      | Unknown  |
| 78 | Tensor<[64, 64, 96]> self = ?,<br>List[int]<> size = [4096, 96]               | Unknown  |
| 79 | Tensor<[64, 64]> self = ?,<br>List[int]<> size = [8, 8, 8, 8]                 | Unknown  |
| 80 | Tensor<[64, 768]> self = ?,<br>List[int]<> size = [1, 64, 768]                | Unknown  |
| 81 | Tensor<[64, 768]> self = ?,<br>List[int]<> size = [1, 8, 8, 768]              | Unknown  |
| 82 | Tensor<[96, 64, 32]> self = ?,<br>List[int]<> size = [16, 6, 64, 32]          | Unknown  |
| 83 | Tensor<[96, 64, 64]> self = ?,<br>List[int]<> size = [16, 6, 64, 64]          | Unknown  |

