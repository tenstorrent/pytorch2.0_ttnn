# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |
|---:|:-------------------------------|-------------------:|------------:|
|  0 | aten._softmax.default          |                  4 |           4 |
|  1 | aten._unsafe_view.default      |                 19 |           0 |
|  2 | aten.add.Tensor                |                 11 |          11 |
|  3 | aten.addmm.default             |                 17 |          17 |
|  4 | aten.as_strided.default        |                  1 |           0 |
|  5 | aten.bmm.default               |                  8 |           8 |
|  6 | aten.cat.default               |                  3 |           0 |
|  7 | aten.clone.default             |                 39 |          31 |
|  8 | aten.constant_pad_nd.default   |                  4 |           4 |
|  9 | aten.convolution.default       |                  1 |           0 |
| 10 | aten.eq.Scalar                 |                  3 |           0 |
| 11 | aten.expand.default            |                 12 |           0 |
| 12 | aten.gelu.default              |                  4 |           4 |
| 13 | aten.index.Tensor              |                  4 |           0 |
| 14 | aten.masked_fill.Scalar        |                  6 |           0 |
| 15 | aten.mean.dim                  |                  1 |           1 |
| 16 | aten.mm.default                |                  3 |           3 |
| 17 | aten.mul.Tensor                |                  4 |           4 |
| 18 | aten.native_layer_norm.default |                  7 |           7 |
| 19 | aten.ne.Scalar                 |                  3 |           0 |
| 20 | aten.new_zeros.default         |                  3 |           0 |
| 21 | aten.permute.default           |                 21 |          21 |
| 22 | aten.roll.default              |                  6 |           0 |
| 23 | aten.select.int                |                 12 |           0 |
| 24 | aten.slice.Tensor              |                 23 |           0 |
| 25 | aten.sub.Tensor                |                  3 |           3 |
| 26 | aten.t.default                 |                 20 |          20 |
| 27 | aten.transpose.int             |                  8 |           8 |
| 28 | aten.unsqueeze.default         |                 16 |          13 |
| 29 | aten.view.default              |                 73 |           5 |
***
### aten._softmax.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 49, 49]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Done     |
|  1 | Tensor<[16, 6, 49, 49]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Done     |
|  2 | Tensor<[4, 12, 49, 49]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Done     |
|  3 | Tensor<[64, 3, 49, 49]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Done     |
### aten._unsafe_view.default
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2, 2, 7, 7, 384]> self = ?,<br>List[int]<> size = [4, 49, 384]     | Unknown  |
|  1 | Tensor<[1, 2, 7, 2, 7, 384]> self = ?,<br>List[int]<> size = [1, 14, 14, 384] | Unknown  |
|  2 | Tensor<[1, 4, 4, 7, 7, 192]> self = ?,<br>List[int]<> size = [16, 49, 192]    | Unknown  |
|  3 | Tensor<[1, 4, 7, 4, 7, 192]> self = ?,<br>List[int]<> size = [1, 28, 28, 192] | Unknown  |
|  4 | Tensor<[1, 49, 24, 32]> self = ?,<br>List[int]<> size = [1, 49, 768]          | Unknown  |
|  5 | Tensor<[1, 8, 7, 8, 7, 96]> self = ?,<br>List[int]<> size = [1, 56, 56, 96]   | Unknown  |
|  6 | Tensor<[1, 8, 8, 7, 7, 96]> self = ?,<br>List[int]<> size = [64, 49, 96]      | Unknown  |
|  7 | Tensor<[16, 49, 6, 32]> self = ?,<br>List[int]<> size = [16, 49, 192]         | Unknown  |
|  8 | Tensor<[16, 6, 32, 49]> self = ?,<br>List[int]<> size = [96, 32, 49]          | Unknown  |
|  9 | Tensor<[16, 6, 49, 32]> self = ?,<br>List[int]<> size = [96, 49, 32]          | Unknown  |
| 10 | Tensor<[2, 2, 7, 7]> self = ?,<br>List[int]<> size = [4, 49]                  | Unknown  |
| 11 | Tensor<[4, 12, 32, 49]> self = ?,<br>List[int]<> size = [48, 32, 49]          | Unknown  |
| 12 | Tensor<[4, 12, 49, 32]> self = ?,<br>List[int]<> size = [48, 49, 32]          | Unknown  |
| 13 | Tensor<[4, 4, 7, 7]> self = ?,<br>List[int]<> size = [16, 49]                 | Unknown  |
| 14 | Tensor<[4, 49, 12, 32]> self = ?,<br>List[int]<> size = [4, 49, 384]          | Unknown  |
| 15 | Tensor<[64, 3, 32, 49]> self = ?,<br>List[int]<> size = [192, 32, 49]         | Unknown  |
| 16 | Tensor<[64, 3, 49, 32]> self = ?,<br>List[int]<> size = [192, 49, 32]         | Unknown  |
| 17 | Tensor<[64, 49, 3, 32]> self = ?,<br>List[int]<> size = [64, 49, 96]          | Unknown  |
| 18 | Tensor<[8, 8, 7, 7]> self = ?,<br>List[int]<> size = [64, 49]                 | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   |
|---:|:-----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 14, 384]> self = ?,<br>Tensor<[1, 14, 14, 384]> other = ?     | Done     |
|  1 | Tensor<[1, 16, 6, 49, 49]> self = ?,<br>Tensor<[1, 16, 1, 49, 49]> other = ? | Done     |
|  2 | Tensor<[1, 24, 49, 49]> self = ?,<br>Tensor<[1, 24, 49, 49]> other = ?       | Done     |
|  3 | Tensor<[1, 28, 28, 192]> self = ?,<br>Tensor<[1, 28, 28, 192]> other = ?     | Done     |
|  4 | Tensor<[1, 4, 12, 49, 49]> self = ?,<br>Tensor<[1, 4, 1, 49, 49]> other = ?  | Done     |
|  5 | Tensor<[1, 56, 56, 96]> self = ?,<br>Tensor<[1, 56, 56, 96]> other = ?       | Done     |
|  6 | Tensor<[1, 64, 3, 49, 49]> self = ?,<br>Tensor<[1, 64, 1, 49, 49]> other = ? | Done     |
|  7 | Tensor<[1, 7, 7, 768]> self = ?,<br>Tensor<[1, 7, 7, 768]> other = ?         | Done     |
|  8 | Tensor<[16, 6, 49, 49]> self = ?,<br>Tensor<[1, 6, 49, 49]> other = ?        | Done     |
|  9 | Tensor<[4, 12, 49, 49]> self = ?,<br>Tensor<[1, 12, 49, 49]> other = ?       | Done     |
| 10 | Tensor<[64, 3, 49, 49]> self = ?,<br>Tensor<[1, 3, 49, 49]> other = ?        | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 1000]> mat2 = ?   | Done     |
|  1 | Tensor<[1152]> self = ?,<br>Tensor<[196, 384]> mat1 = ?,<br>Tensor<[384, 1152]> mat2 = ? | Done     |
|  2 | Tensor<[1536]> self = ?,<br>Tensor<[196, 384]> mat1 = ?,<br>Tensor<[384, 1536]> mat2 = ? | Done     |
|  3 | Tensor<[192]> self = ?,<br>Tensor<[784, 192]> mat1 = ?,<br>Tensor<[192, 192]> mat2 = ?   | Done     |
|  4 | Tensor<[192]> self = ?,<br>Tensor<[784, 768]> mat1 = ?,<br>Tensor<[768, 192]> mat2 = ?   | Done     |
|  5 | Tensor<[2304]> self = ?,<br>Tensor<[49, 768]> mat1 = ?,<br>Tensor<[768, 2304]> mat2 = ?  | Done     |
|  6 | Tensor<[288]> self = ?,<br>Tensor<[3136, 96]> mat1 = ?,<br>Tensor<[96, 288]> mat2 = ?    | Done     |
|  7 | Tensor<[3072]> self = ?,<br>Tensor<[49, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?  | Done     |
|  8 | Tensor<[384]> self = ?,<br>Tensor<[196, 1536]> mat1 = ?,<br>Tensor<[1536, 384]> mat2 = ? | Done     |
|  9 | Tensor<[384]> self = ?,<br>Tensor<[196, 384]> mat1 = ?,<br>Tensor<[384, 384]> mat2 = ?   | Done     |
| 10 | Tensor<[384]> self = ?,<br>Tensor<[3136, 96]> mat1 = ?,<br>Tensor<[96, 384]> mat2 = ?    | Done     |
| 11 | Tensor<[576]> self = ?,<br>Tensor<[784, 192]> mat1 = ?,<br>Tensor<[192, 576]> mat2 = ?   | Done     |
| 12 | Tensor<[768]> self = ?,<br>Tensor<[49, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?  | Done     |
| 13 | Tensor<[768]> self = ?,<br>Tensor<[49, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?    | Done     |
| 14 | Tensor<[768]> self = ?,<br>Tensor<[784, 192]> mat1 = ?,<br>Tensor<[192, 768]> mat2 = ?   | Done     |
| 15 | Tensor<[96]> self = ?,<br>Tensor<[3136, 384]> mat1 = ?,<br>Tensor<[384, 96]> mat2 = ?    | Done     |
| 16 | Tensor<[96]> self = ?,<br>Tensor<[3136, 96]> mat1 = ?,<br>Tensor<[96, 96]> mat2 = ?      | Done     |
### aten.as_strided.default
|    | ATen Input Variations                                                                                             | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int]<> size = [1, 768, 1, 1],<br>List[int]<> stride = [768, 1, 768, 768] | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[192, 49, 32]> self = ?,<br>Tensor<[192, 32, 49]> mat2 = ? | Done     |
|  1 | Tensor<[192, 49, 49]> self = ?,<br>Tensor<[192, 49, 32]> mat2 = ? | Done     |
|  2 | Tensor<[24, 49, 32]> self = ?,<br>Tensor<[24, 32, 49]> mat2 = ?   | Done     |
|  3 | Tensor<[24, 49, 49]> self = ?,<br>Tensor<[24, 49, 32]> mat2 = ?   | Done     |
|  4 | Tensor<[48, 49, 32]> self = ?,<br>Tensor<[48, 32, 49]> mat2 = ?   | Done     |
|  5 | Tensor<[48, 49, 49]> self = ?,<br>Tensor<[48, 49, 32]> mat2 = ?   | Done     |
|  6 | Tensor<[96, 49, 32]> self = ?,<br>Tensor<[96, 32, 49]> mat2 = ?   | Done     |
|  7 | Tensor<[96, 49, 49]> self = ?,<br>Tensor<[96, 49, 32]> mat2 = ?   | Done     |
### aten.cat.default
|    | ATen Input Variations                                                                                                                                                        | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([1, 14, 14, 192])', 'torch.Size([1, 14, 14, 192])', 'torch.Size([1, 14, 14, 192])', 'torch.Size([1, 14, 14, 192])'],<br>int<> dim = -1 | Unknown  |
|  1 | List[Tensor]<> tensors = ['torch.Size([1, 28, 28, 96])', 'torch.Size([1, 28, 28, 96])', 'torch.Size([1, 28, 28, 96])', 'torch.Size([1, 28, 28, 96])'],<br>int<> dim = -1     | Unknown  |
|  2 | List[Tensor]<> tensors = ['torch.Size([1, 7, 7, 384])', 'torch.Size([1, 7, 7, 384])', 'torch.Size([1, 7, 7, 384])', 'torch.Size([1, 7, 7, 384])'],<br>int<> dim = -1         | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 14, 1536]> self = ?                                                                | Done     |
|  1 | Tensor<[1, 14, 14, 384]> self = ?                                                                 | Unknown  |
|  2 | Tensor<[1, 2, 2, 7, 7, 384]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  3 | Tensor<[1, 2, 7, 2, 7, 384]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  4 | Tensor<[1, 24, 49, 49]> self = ?                                                                  | Done     |
|  5 | Tensor<[1, 28, 28, 192]> self = ?                                                                 | Unknown  |
|  6 | Tensor<[1, 28, 28, 768]> self = ?                                                                 | Done     |
|  7 | Tensor<[1, 4, 4, 7, 7, 192]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  8 | Tensor<[1, 4, 7, 4, 7, 192]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  9 | Tensor<[1, 49, 24, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 10 | Tensor<[1, 49, 768]> self = ?                                                                     | Done     |
| 11 | Tensor<[1, 56, 56, 384]> self = ?                                                                 | Done     |
| 12 | Tensor<[1, 56, 56, 96]> self = ?                                                                  | Unknown  |
| 13 | Tensor<[1, 7, 7, 3072]> self = ?                                                                  | Done     |
| 14 | Tensor<[1, 7, 7, 768]> self = ?                                                                   | Unknown  |
| 15 | Tensor<[1, 8, 7, 8, 7, 96]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format  | Done     |
| 16 | Tensor<[1, 8, 8, 7, 7, 96]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format  | Done     |
| 17 | Tensor<[12, 49, 49]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Unknown  |
| 18 | Tensor<[16, 49, 192]> self = ?                                                                    | Done     |
| 19 | Tensor<[16, 49, 6, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 20 | Tensor<[16, 6, 32, 49]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 21 | Tensor<[16, 6, 49, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 22 | Tensor<[16, 6, 49, 49]> self = ?                                                                  | Done     |
| 23 | Tensor<[2, 2, 7, 7]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Done     |
| 24 | Tensor<[24, 49, 49]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Unknown  |
| 25 | Tensor<[3, 49, 49]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format          | Unknown  |
| 26 | Tensor<[4, 12, 32, 49]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 27 | Tensor<[4, 12, 49, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 28 | Tensor<[4, 12, 49, 49]> self = ?                                                                  | Done     |
| 29 | Tensor<[4, 4, 7, 7]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Done     |
| 30 | Tensor<[4, 49, 12, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 31 | Tensor<[4, 49, 384]> self = ?                                                                     | Done     |
| 32 | Tensor<[6, 49, 49]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format          | Unknown  |
| 33 | Tensor<[64, 3, 32, 49]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 34 | Tensor<[64, 3, 49, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 35 | Tensor<[64, 3, 49, 49]> self = ?                                                                  | Done     |
| 36 | Tensor<[64, 49, 3, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 37 | Tensor<[64, 49, 96]> self = ?                                                                     | Done     |
| 38 | Tensor<[8, 8, 7, 7]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Done     |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 14, 384]> self = ?,<br>List[int]<> pad = [0, 0, 0, 0, 0, 0],<br>number<> value = 0.0 | Done     |
|  1 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int]<> pad = [0, 0, 0, 0, 0, 0],<br>number<> value = 0.0 | Done     |
|  2 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int]<> pad = [0, 0, 0, 0, 0, 0],<br>number<> value = 0.0  | Done     |
|  3 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int]<> pad = [0, 0, 0, 0, 0, 0],<br>number<> value = 0.0   | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                     | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[96, 3, 4, 4]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>List[int]<> stride = [4, 4],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Unknown  |
### aten.eq.Scalar
|    | ATen Input Variations                                | Status   |
|---:|:-----------------------------------------------------|:---------|
|  0 | Tensor<[16, 49, 49]> self = ?,<br>number<> other = 0 | Unknown  |
|  1 | Tensor<[4, 49, 49]> self = ?,<br>number<> other = 0  | Unknown  |
|  2 | Tensor<[64, 49, 49]> self = ?,<br>number<> other = 0 | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 32, 49]> self = ?,<br>List[int]<> size = [1, 24, 32, 49] | Unknown  |
|  1 | Tensor<[1, 24, 49, 32]> self = ?,<br>List[int]<> size = [1, 24, 49, 32] | Unknown  |
|  2 | Tensor<[1, 24, 49, 49]> self = ?,<br>List[int]<> size = [1, 24, 49, 49] | Unknown  |
|  3 | Tensor<[16, 6, 32, 49]> self = ?,<br>List[int]<> size = [16, 6, 32, 49] | Unknown  |
|  4 | Tensor<[16, 6, 49, 32]> self = ?,<br>List[int]<> size = [16, 6, 49, 32] | Unknown  |
|  5 | Tensor<[16, 6, 49, 49]> self = ?,<br>List[int]<> size = [16, 6, 49, 49] | Unknown  |
|  6 | Tensor<[4, 12, 32, 49]> self = ?,<br>List[int]<> size = [4, 12, 32, 49] | Unknown  |
|  7 | Tensor<[4, 12, 49, 32]> self = ?,<br>List[int]<> size = [4, 12, 49, 32] | Unknown  |
|  8 | Tensor<[4, 12, 49, 49]> self = ?,<br>List[int]<> size = [4, 12, 49, 49] | Unknown  |
|  9 | Tensor<[64, 3, 32, 49]> self = ?,<br>List[int]<> size = [64, 3, 32, 49] | Unknown  |
| 10 | Tensor<[64, 3, 49, 32]> self = ?,<br>List[int]<> size = [64, 3, 49, 32] | Unknown  |
| 11 | Tensor<[64, 3, 49, 49]> self = ?,<br>List[int]<> size = [64, 3, 49, 49] | Unknown  |
### aten.gelu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 14, 14, 1536]> self = ? | Done     |
|  1 | Tensor<[1, 28, 28, 768]> self = ?  | Done     |
|  2 | Tensor<[1, 56, 56, 384]> self = ?  | Done     |
|  3 | Tensor<[1, 7, 7, 3072]> self = ?   | Done     |
### aten.index.Tensor
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[169, 12]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([2401])'] | Unknown  |
|  1 | Tensor<[169, 24]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([2401])'] | Unknown  |
|  2 | Tensor<[169, 3]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([2401])']  | Unknown  |
|  3 | Tensor<[169, 6]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([2401])']  | Unknown  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 49, 49]> self = ?,<br>Tensor<[16, 49, 49]> mask = ?,<br>number<> value = -100.0 | Unknown  |
|  1 | Tensor<[16, 49, 49]> self = ?,<br>Tensor<[16, 49, 49]> mask = ?,<br>number<> value = 0.0    | Unknown  |
|  2 | Tensor<[4, 49, 49]> self = ?,<br>Tensor<[4, 49, 49]> mask = ?,<br>number<> value = -100.0   | Unknown  |
|  3 | Tensor<[4, 49, 49]> self = ?,<br>Tensor<[4, 49, 49]> mask = ?,<br>number<> value = 0.0      | Unknown  |
|  4 | Tensor<[64, 49, 49]> self = ?,<br>Tensor<[64, 49, 49]> mask = ?,<br>number<> value = -100.0 | Unknown  |
|  5 | Tensor<[64, 49, 49]> self = ?,<br>Tensor<[64, 49, 49]> mask = ?,<br>number<> value = 0.0    | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768, 7, 7]> self = ?,<br>Optional[List[int]]<> dim = [-1, -2],<br>bool<> keepdim = True | Done     |
### aten.mm.default
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[196, 768]> self = ?,<br>Tensor<[768, 384]> mat2 = ?  | Done     |
|  1 | Tensor<[49, 1536]> self = ?,<br>Tensor<[1536, 768]> mat2 = ? | Done     |
|  2 | Tensor<[784, 384]> self = ?,<br>Tensor<[384, 192]> mat2 = ?  | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 49, 32]> self = ?,<br>Tensor<> other = 0.1767766952966369 | Done     |
|  1 | Tensor<[16, 6, 49, 32]> self = ?,<br>Tensor<> other = 0.1767766952966369 | Done     |
|  2 | Tensor<[4, 12, 49, 32]> self = ?,<br>Tensor<> other = 0.1767766952966369 | Done     |
|  3 | Tensor<[64, 3, 49, 32]> self = ?,<br>Tensor<> other = 0.1767766952966369 | Done     |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                             | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 14, 384]> input = ?,<br>List[int]<> normalized_shape = [384],<br>Optional[Tensor]<[384]> weight = ?,<br>Optional[Tensor]<[384]> bias = ?,<br>float<> eps = 1e-05   | Done     |
|  1 | Tensor<[1, 14, 14, 768]> input = ?,<br>List[int]<> normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float<> eps = 1e-05   | Done     |
|  2 | Tensor<[1, 28, 28, 192]> input = ?,<br>List[int]<> normalized_shape = [192],<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>float<> eps = 1e-05   | Done     |
|  3 | Tensor<[1, 28, 28, 384]> input = ?,<br>List[int]<> normalized_shape = [384],<br>Optional[Tensor]<[384]> weight = ?,<br>Optional[Tensor]<[384]> bias = ?,<br>float<> eps = 1e-05   | Done     |
|  4 | Tensor<[1, 56, 56, 96]> input = ?,<br>List[int]<> normalized_shape = [96],<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>float<> eps = 1e-05       | Done     |
|  5 | Tensor<[1, 7, 7, 1536]> input = ?,<br>List[int]<> normalized_shape = [1536],<br>Optional[Tensor]<[1536]> weight = ?,<br>Optional[Tensor]<[1536]> bias = ?,<br>float<> eps = 1e-05 | Done     |
|  6 | Tensor<[1, 7, 7, 768]> input = ?,<br>List[int]<> normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float<> eps = 1e-05     | Done     |
### aten.ne.Scalar
|    | ATen Input Variations                                | Status   |
|---:|:-----------------------------------------------------|:---------|
|  0 | Tensor<[16, 49, 49]> self = ?,<br>number<> other = 0 | Unknown  |
|  1 | Tensor<[4, 49, 49]> self = ?,<br>number<> other = 0  | Unknown  |
|  2 | Tensor<[64, 49, 49]> self = ?,<br>number<> other = 0 | Unknown  |
### aten.new_zeros.default
|    | ATen Input Variations                                                                                  | Status   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 49, 192]> self = ?,<br>List[int]<> size = [28, 28],<br>Optional[bool]<> pin_memory = False | Unknown  |
|  1 | Tensor<[4, 49, 384]> self = ?,<br>List[int]<> size = [14, 14],<br>Optional[bool]<> pin_memory = False  | Unknown  |
|  2 | Tensor<[64, 49, 96]> self = ?,<br>List[int]<> size = [56, 56],<br>Optional[bool]<> pin_memory = False  | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                                           | Status   |
|---:|:--------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 7, 7, 768]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5] | Done     |
|  1 | Tensor<[1, 1, 7, 1, 7, 768]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5] | Done     |
|  2 | Tensor<[1, 2, 2, 7, 7, 384]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5] | Done     |
|  3 | Tensor<[1, 2, 7, 2, 7, 384]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5] | Done     |
|  4 | Tensor<[1, 4, 4, 7, 7, 192]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5] | Done     |
|  5 | Tensor<[1, 4, 7, 4, 7, 192]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5] | Done     |
|  6 | Tensor<[1, 49, 3, 24, 32]> self = ?,<br>List[int]<> dims = [2, 0, 3, 1, 4]      | Done     |
|  7 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int]<> dims = [0, 3, 1, 2]             | Done     |
|  8 | Tensor<[1, 8, 7, 8, 7, 96]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5]  | Done     |
|  9 | Tensor<[1, 8, 8, 7, 7, 96]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5]  | Done     |
| 10 | Tensor<[1, 96, 56, 56]> self = ?,<br>List[int]<> dims = [0, 2, 3, 1]            | Done     |
| 11 | Tensor<[16, 49, 3, 6, 32]> self = ?,<br>List[int]<> dims = [2, 0, 3, 1, 4]      | Done     |
| 12 | Tensor<[2, 7, 2, 7]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]               | Done     |
| 13 | Tensor<[4, 49, 3, 12, 32]> self = ?,<br>List[int]<> dims = [2, 0, 3, 1, 4]      | Done     |
| 14 | Tensor<[4, 7, 4, 7]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]               | Done     |
| 15 | Tensor<[49, 49, 12]> self = ?,<br>List[int]<> dims = [2, 0, 1]                  | Done     |
| 16 | Tensor<[49, 49, 24]> self = ?,<br>List[int]<> dims = [2, 0, 1]                  | Done     |
| 17 | Tensor<[49, 49, 3]> self = ?,<br>List[int]<> dims = [2, 0, 1]                   | Done     |
| 18 | Tensor<[49, 49, 6]> self = ?,<br>List[int]<> dims = [2, 0, 1]                   | Done     |
| 19 | Tensor<[64, 49, 3, 3, 32]> self = ?,<br>List[int]<> dims = [2, 0, 3, 1, 4]      | Done     |
| 20 | Tensor<[8, 7, 8, 7]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]               | Done     |
### aten.roll.default
|    | ATen Input Variations                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 14, 384]> self = ?,<br>List[int]<> shifts = [-3, -3],<br>List[int]<> dims = [1, 2] | Unknown  |
|  1 | Tensor<[1, 14, 14, 384]> self = ?,<br>List[int]<> shifts = [3, 3],<br>List[int]<> dims = [1, 2]   | Unknown  |
|  2 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int]<> shifts = [-3, -3],<br>List[int]<> dims = [1, 2] | Unknown  |
|  3 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int]<> shifts = [3, 3],<br>List[int]<> dims = [1, 2]   | Unknown  |
|  4 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int]<> shifts = [-3, -3],<br>List[int]<> dims = [1, 2]  | Unknown  |
|  5 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int]<> shifts = [3, 3],<br>List[int]<> dims = [1, 2]    | Unknown  |
### aten.select.int
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 1, 24, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | Unknown  |
|  1 | Tensor<[3, 1, 24, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 1 | Unknown  |
|  2 | Tensor<[3, 1, 24, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 2 | Unknown  |
|  3 | Tensor<[3, 16, 6, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | Unknown  |
|  4 | Tensor<[3, 16, 6, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 1 | Unknown  |
|  5 | Tensor<[3, 16, 6, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 2 | Unknown  |
|  6 | Tensor<[3, 4, 12, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | Unknown  |
|  7 | Tensor<[3, 4, 12, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 1 | Unknown  |
|  8 | Tensor<[3, 4, 12, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 2 | Unknown  |
|  9 | Tensor<[3, 64, 3, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | Unknown  |
| 10 | Tensor<[3, 64, 3, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 1 | Unknown  |
| 11 | Tensor<[3, 64, 3, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 2 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                             | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 14, 192]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
|  1 | Tensor<[1, 14, 14, 384]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
|  2 | Tensor<[1, 14, 14, 384]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
|  3 | Tensor<[1, 14, 14, 384]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
|  4 | Tensor<[1, 14, 14, 384]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
|  5 | Tensor<[1, 14, 28, 192]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
|  6 | Tensor<[1, 14, 28, 192]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
|  7 | Tensor<[1, 28, 28, 192]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
|  8 | Tensor<[1, 28, 28, 192]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
|  9 | Tensor<[1, 28, 28, 192]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
| 10 | Tensor<[1, 28, 28, 192]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
| 11 | Tensor<[1, 28, 28, 96]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                     | Unknown  |
| 12 | Tensor<[1, 28, 56, 96]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2  | Unknown  |
| 13 | Tensor<[1, 28, 56, 96]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2  | Unknown  |
| 14 | Tensor<[1, 56, 56, 96]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                     | Unknown  |
| 15 | Tensor<[1, 56, 56, 96]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2  | Unknown  |
| 16 | Tensor<[1, 56, 56, 96]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2  | Unknown  |
| 17 | Tensor<[1, 56, 56, 96]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                     | Unknown  |
| 18 | Tensor<[1, 7, 14, 384]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2  | Unknown  |
| 19 | Tensor<[1, 7, 14, 384]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2  | Unknown  |
| 20 | Tensor<[1, 7, 7, 384]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                      | Unknown  |
| 21 | Tensor<[1, 7, 7, 768]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                      | Unknown  |
| 22 | Tensor<[1, 7, 7, 768]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                      | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 1, 49]> self = ?,<br>Tensor<[16, 49, 1]> other = ? | Done     |
|  1 | Tensor<[4, 1, 49]> self = ?,<br>Tensor<[4, 49, 1]> other = ?   | Done     |
|  2 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ? | Done     |
### aten.t.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | Tensor<[1000, 768]> self = ? | Done     |
|  1 | Tensor<[1152, 384]> self = ? | Done     |
|  2 | Tensor<[1536, 384]> self = ? | Done     |
|  3 | Tensor<[192, 192]> self = ?  | Done     |
|  4 | Tensor<[192, 384]> self = ?  | Done     |
|  5 | Tensor<[192, 768]> self = ?  | Done     |
|  6 | Tensor<[2304, 768]> self = ? | Done     |
|  7 | Tensor<[288, 96]> self = ?   | Done     |
|  8 | Tensor<[3072, 768]> self = ? | Done     |
|  9 | Tensor<[384, 1536]> self = ? | Done     |
| 10 | Tensor<[384, 384]> self = ?  | Done     |
| 11 | Tensor<[384, 768]> self = ?  | Done     |
| 12 | Tensor<[384, 96]> self = ?   | Done     |
| 13 | Tensor<[576, 192]> self = ?  | Done     |
| 14 | Tensor<[768, 1536]> self = ? | Done     |
| 15 | Tensor<[768, 192]> self = ?  | Done     |
| 16 | Tensor<[768, 3072]> self = ? | Done     |
| 17 | Tensor<[768, 768]> self = ?  | Done     |
| 18 | Tensor<[96, 384]> self = ?   | Done     |
| 19 | Tensor<[96, 96]> self = ?    | Done     |
### aten.transpose.int
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 49, 32]> self = ?,<br>int<> dim0 = -2,<br>int<> dim1 = -1 | Done     |
|  1 | Tensor<[1, 24, 49, 32]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
|  2 | Tensor<[16, 6, 49, 32]> self = ?,<br>int<> dim0 = -2,<br>int<> dim1 = -1 | Done     |
|  3 | Tensor<[16, 6, 49, 32]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
|  4 | Tensor<[4, 12, 49, 32]> self = ?,<br>int<> dim0 = -2,<br>int<> dim1 = -1 | Done     |
|  5 | Tensor<[4, 12, 49, 32]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
|  6 | Tensor<[64, 3, 49, 32]> self = ?,<br>int<> dim0 = -2,<br>int<> dim1 = -1 | Done     |
|  7 | Tensor<[64, 3, 49, 32]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[12, 49, 49]> self = ?,<br>int<> dim = 0    | Done     |
|  1 | Tensor<[16, 1, 49, 49]> self = ?,<br>int<> dim = 0 | Done     |
|  2 | Tensor<[16, 49, 49]> self = ?,<br>int<> dim = 1    | Done     |
|  3 | Tensor<[16, 49]> self = ?,<br>int<> dim = 1        | Done     |
|  4 | Tensor<[16, 49]> self = ?,<br>int<> dim = 2        | Unknown  |
|  5 | Tensor<[24, 49, 49]> self = ?,<br>int<> dim = 0    | Done     |
|  6 | Tensor<[3, 49, 49]> self = ?,<br>int<> dim = 0     | Done     |
|  7 | Tensor<[4, 1, 49, 49]> self = ?,<br>int<> dim = 0  | Done     |
|  8 | Tensor<[4, 49, 49]> self = ?,<br>int<> dim = 1     | Done     |
|  9 | Tensor<[4, 49]> self = ?,<br>int<> dim = 1         | Done     |
| 10 | Tensor<[4, 49]> self = ?,<br>int<> dim = 2         | Unknown  |
| 11 | Tensor<[6, 49, 49]> self = ?,<br>int<> dim = 0     | Done     |
| 12 | Tensor<[64, 1, 49, 49]> self = ?,<br>int<> dim = 0 | Done     |
| 13 | Tensor<[64, 49, 49]> self = ?,<br>int<> dim = 1    | Done     |
| 14 | Tensor<[64, 49]> self = ?,<br>int<> dim = 1        | Done     |
| 15 | Tensor<[64, 49]> self = ?,<br>int<> dim = 2        | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 7, 7, 768]> self = ?,<br>List[int]<> size = [1, 49, 768]     | Unknown  |
|  1 | Tensor<[1, 1, 7, 1, 7, 768]> self = ?,<br>List[int]<> size = [1, 7, 7, 768]   | Unknown  |
|  2 | Tensor<[1, 14, 14, 1536]> self = ?,<br>List[int]<> size = [196, 1536]         | Unknown  |
|  3 | Tensor<[1, 14, 14, 384]> self = ?,<br>List[int]<> size = [1, 2, 7, 2, 7, 384] | Unknown  |
|  4 | Tensor<[1, 14, 14, 384]> self = ?,<br>List[int]<> size = [196, 384]           | Unknown  |
|  5 | Tensor<[1, 14, 14, 768]> self = ?,<br>List[int]<> size = [196, 768]           | Unknown  |
|  6 | Tensor<[1, 16, 6, 49, 49]> self = ?,<br>List[int]<> size = [-1, 6, 49, 49]    | Unknown  |
|  7 | Tensor<[1, 24, 32, 49]> self = ?,<br>List[int]<> size = [24, 32, 49]          | Unknown  |
|  8 | Tensor<[1, 24, 49, 32]> self = ?,<br>List[int]<> size = [24, 49, 32]          | Done     |
|  9 | Tensor<[1, 24, 49, 49]> self = ?,<br>List[int]<> size = [24, 49, 49]          | Unknown  |
| 10 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int]<> size = [1, 4, 7, 4, 7, 192] | Unknown  |
| 11 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int]<> size = [784, 192]           | Unknown  |
| 12 | Tensor<[1, 28, 28, 384]> self = ?,<br>List[int]<> size = [784, 384]           | Unknown  |
| 13 | Tensor<[1, 28, 28, 768]> self = ?,<br>List[int]<> size = [784, 768]           | Unknown  |
| 14 | Tensor<[1, 4, 12, 49, 49]> self = ?,<br>List[int]<> size = [-1, 12, 49, 49]   | Unknown  |
| 15 | Tensor<[1, 49, 2304]> self = ?,<br>List[int]<> size = [1, 49, 3, 24, 32]      | Unknown  |
| 16 | Tensor<[1, 49, 768]> self = ?,<br>List[int]<> size = [1, 1, 1, 7, 7, 768]     | Unknown  |
| 17 | Tensor<[1, 49, 768]> self = ?,<br>List[int]<> size = [49, 768]                | Done     |
| 18 | Tensor<[1, 56, 56, 384]> self = ?,<br>List[int]<> size = [3136, 384]          | Unknown  |
| 19 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int]<> size = [1, 8, 7, 8, 7, 96]   | Unknown  |
| 20 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int]<> size = [3136, 96]            | Unknown  |
| 21 | Tensor<[1, 64, 3, 49, 49]> self = ?,<br>List[int]<> size = [-1, 3, 49, 49]    | Unknown  |
| 22 | Tensor<[1, 7, 7, 1536]> self = ?,<br>List[int]<> size = [49, 1536]            | Unknown  |
| 23 | Tensor<[1, 7, 7, 3072]> self = ?,<br>List[int]<> size = [49, 3072]            | Unknown  |
| 24 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int]<> size = [1, 1, 7, 1, 7, 768]   | Unknown  |
| 25 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int]<> size = [49, 768]              | Unknown  |
| 26 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int]<> size = [1, 768]               | Unknown  |
| 27 | Tensor<[14, 14]> self = ?,<br>List[int]<> size = [2, 7, 2, 7]                 | Unknown  |
| 28 | Tensor<[16, 49, 192]> self = ?,<br>List[int]<> size = [1, 4, 4, 7, 7, 192]    | Unknown  |
| 29 | Tensor<[16, 49, 192]> self = ?,<br>List[int]<> size = [784, 192]              | Unknown  |
| 30 | Tensor<[16, 49, 576]> self = ?,<br>List[int]<> size = [16, 49, 3, 6, 32]      | Unknown  |
| 31 | Tensor<[16, 6, 49, 49]> self = ?,<br>List[int]<> size = [1, 16, 6, 49, 49]    | Unknown  |
| 32 | Tensor<[16, 6, 49, 49]> self = ?,<br>List[int]<> size = [96, 49, 49]          | Unknown  |
| 33 | Tensor<[192, 49, 32]> self = ?,<br>List[int]<> size = [64, 3, 49, 32]         | Unknown  |
| 34 | Tensor<[192, 49, 49]> self = ?,<br>List[int]<> size = [64, 3, 49, 49]         | Unknown  |
| 35 | Tensor<[196, 1152]> self = ?,<br>List[int]<> size = [4, 49, 1152]             | Unknown  |
| 36 | Tensor<[196, 1536]> self = ?,<br>List[int]<> size = [1, 14, 14, 1536]         | Unknown  |
| 37 | Tensor<[196, 384]> self = ?,<br>List[int]<> size = [1, 14, 14, 384]           | Unknown  |
| 38 | Tensor<[196, 384]> self = ?,<br>List[int]<> size = [4, 49, 384]               | Unknown  |
| 39 | Tensor<[24, 49, 32]> self = ?,<br>List[int]<> size = [1, 24, 49, 32]          | Done     |
| 40 | Tensor<[24, 49, 49]> self = ?,<br>List[int]<> size = [1, 24, 49, 49]          | Unknown  |
| 41 | Tensor<[2401, 12]> self = ?,<br>List[int]<> size = [49, 49, -1]               | Unknown  |
| 42 | Tensor<[2401, 24]> self = ?,<br>List[int]<> size = [49, 49, -1]               | Unknown  |
| 43 | Tensor<[2401, 3]> self = ?,<br>List[int]<> size = [49, 49, -1]                | Unknown  |
| 44 | Tensor<[2401, 6]> self = ?,<br>List[int]<> size = [49, 49, -1]                | Unknown  |
| 45 | Tensor<[28, 28]> self = ?,<br>List[int]<> size = [4, 7, 4, 7]                 | Unknown  |
| 46 | Tensor<[3136, 288]> self = ?,<br>List[int]<> size = [64, 49, 288]             | Unknown  |
| 47 | Tensor<[3136, 384]> self = ?,<br>List[int]<> size = [1, 56, 56, 384]          | Unknown  |
| 48 | Tensor<[3136, 96]> self = ?,<br>List[int]<> size = [1, 56, 56, 96]            | Unknown  |
| 49 | Tensor<[3136, 96]> self = ?,<br>List[int]<> size = [64, 49, 96]               | Unknown  |
| 50 | Tensor<[4, 12, 49, 49]> self = ?,<br>List[int]<> size = [1, 4, 12, 49, 49]    | Unknown  |
| 51 | Tensor<[4, 12, 49, 49]> self = ?,<br>List[int]<> size = [48, 49, 49]          | Unknown  |
| 52 | Tensor<[4, 49, 1152]> self = ?,<br>List[int]<> size = [4, 49, 3, 12, 32]      | Unknown  |
| 53 | Tensor<[4, 49, 384]> self = ?,<br>List[int]<> size = [1, 2, 2, 7, 7, 384]     | Unknown  |
| 54 | Tensor<[4, 49, 384]> self = ?,<br>List[int]<> size = [196, 384]               | Unknown  |
| 55 | Tensor<[48, 49, 32]> self = ?,<br>List[int]<> size = [4, 12, 49, 32]          | Unknown  |
| 56 | Tensor<[48, 49, 49]> self = ?,<br>List[int]<> size = [4, 12, 49, 49]          | Unknown  |
| 57 | Tensor<[49, 2304]> self = ?,<br>List[int]<> size = [1, 49, 2304]              | Done     |
| 58 | Tensor<[49, 3072]> self = ?,<br>List[int]<> size = [1, 7, 7, 3072]            | Unknown  |
| 59 | Tensor<[49, 768]> self = ?,<br>List[int]<> size = [1, 49, 768]                | Done     |
| 60 | Tensor<[49, 768]> self = ?,<br>List[int]<> size = [1, 7, 7, 768]              | Unknown  |
| 61 | Tensor<[56, 56]> self = ?,<br>List[int]<> size = [8, 7, 8, 7]                 | Unknown  |
| 62 | Tensor<[64, 3, 49, 49]> self = ?,<br>List[int]<> size = [1, 64, 3, 49, 49]    | Unknown  |
| 63 | Tensor<[64, 3, 49, 49]> self = ?,<br>List[int]<> size = [192, 49, 49]         | Unknown  |
| 64 | Tensor<[64, 49, 288]> self = ?,<br>List[int]<> size = [64, 49, 3, 3, 32]      | Unknown  |
| 65 | Tensor<[64, 49, 96]> self = ?,<br>List[int]<> size = [1, 8, 8, 7, 7, 96]      | Unknown  |
| 66 | Tensor<[64, 49, 96]> self = ?,<br>List[int]<> size = [3136, 96]               | Unknown  |
| 67 | Tensor<[784, 192]> self = ?,<br>List[int]<> size = [1, 28, 28, 192]           | Unknown  |
| 68 | Tensor<[784, 192]> self = ?,<br>List[int]<> size = [16, 49, 192]              | Unknown  |
| 69 | Tensor<[784, 576]> self = ?,<br>List[int]<> size = [16, 49, 576]              | Unknown  |
| 70 | Tensor<[784, 768]> self = ?,<br>List[int]<> size = [1, 28, 28, 768]           | Unknown  |
| 71 | Tensor<[96, 49, 32]> self = ?,<br>List[int]<> size = [16, 6, 49, 32]          | Unknown  |
| 72 | Tensor<[96, 49, 49]> self = ?,<br>List[int]<> size = [16, 6, 49, 49]          | Unknown  |

