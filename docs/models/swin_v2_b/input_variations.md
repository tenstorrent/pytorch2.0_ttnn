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
|  0 | Tensor<[1, 32, 64, 64]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Unknown  |
|  1 | Tensor<[16, 8, 64, 64]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Unknown  |
|  2 | Tensor<[4, 16, 64, 64]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Unknown  |
|  3 | Tensor<[64, 4, 64, 64]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2, 2, 8, 8, 512]> self = ?,<br>List[int]<> size = [4, 64, 512]     | Unknown  |
|  1 | Tensor<[1, 2, 8, 2, 8, 512]> self = ?,<br>List[int]<> size = [1, 16, 16, 512] | Unknown  |
|  2 | Tensor<[1, 4, 4, 8, 8, 256]> self = ?,<br>List[int]<> size = [16, 64, 256]    | Unknown  |
|  3 | Tensor<[1, 4, 8, 4, 8, 256]> self = ?,<br>List[int]<> size = [1, 32, 32, 256] | Unknown  |
|  4 | Tensor<[1, 64, 32, 32]> self = ?,<br>List[int]<> size = [1, 64, 1024]         | Unknown  |
|  5 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>List[int]<> size = [1, 64, 64, 128] | Unknown  |
|  6 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>List[int]<> size = [64, 64, 128]    | Unknown  |
|  7 | Tensor<[16, 64, 8, 32]> self = ?,<br>List[int]<> size = [16, 64, 256]         | Unknown  |
|  8 | Tensor<[16, 8, 32, 64]> self = ?,<br>List[int]<> size = [128, 32, 64]         | Unknown  |
|  9 | Tensor<[16, 8, 64, 32]> self = ?,<br>List[int]<> size = [128, 64, 32]         | Unknown  |
| 10 | Tensor<[2, 2, 8, 8]> self = ?,<br>List[int]<> size = [4, 64]                  | Unknown  |
| 11 | Tensor<[4, 16, 32, 64]> self = ?,<br>List[int]<> size = [64, 32, 64]          | Unknown  |
| 12 | Tensor<[4, 16, 64, 32]> self = ?,<br>List[int]<> size = [64, 64, 32]          | Unknown  |
| 13 | Tensor<[4, 4, 8, 8]> self = ?,<br>List[int]<> size = [16, 64]                 | Unknown  |
| 14 | Tensor<[4, 64, 16, 32]> self = ?,<br>List[int]<> size = [4, 64, 512]          | Unknown  |
| 15 | Tensor<[64, 4, 32, 64]> self = ?,<br>List[int]<> size = [256, 32, 64]         | Unknown  |
| 16 | Tensor<[64, 4, 64, 32]> self = ?,<br>List[int]<> size = [256, 64, 32]         | Unknown  |
| 17 | Tensor<[64, 64, 4, 32]> self = ?,<br>List[int]<> size = [64, 64, 128]         | Unknown  |
| 18 | Tensor<[8, 8, 8, 8]> self = ?,<br>List[int]<> size = [64, 64]                 | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   |
|---:|:-----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 512]> self = ?,<br>Tensor<[1, 16, 16, 512]> other = ?     | Unknown  |
|  1 | Tensor<[1, 16, 8, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ? | Unknown  |
|  2 | Tensor<[1, 32, 32, 256]> self = ?,<br>Tensor<[1, 32, 32, 256]> other = ?     | Unknown  |
|  3 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[1, 32, 64, 64]> other = ?       | Unknown  |
|  4 | Tensor<[1, 4, 16, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?  | Unknown  |
|  5 | Tensor<[1, 64, 4, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ? | Unknown  |
|  6 | Tensor<[1, 64, 64, 128]> self = ?,<br>Tensor<[1, 64, 64, 128]> other = ?     | Unknown  |
|  7 | Tensor<[1, 8, 8, 1024]> self = ?,<br>Tensor<[1, 8, 8, 1024]> other = ?       | Unknown  |
|  8 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[1, 8, 64, 64]> other = ?        | Unknown  |
|  9 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[1, 16, 64, 64]> other = ?       | Unknown  |
| 10 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[1, 4, 64, 64]> other = ?        | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1000]> mat2 = ?  | Unknown  |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[1024, 256]> mat1 = ?,<br>Tensor<[256, 1024]> mat2 = ? | Unknown  |
|  2 | Tensor<[1024]> self = ?,<br>Tensor<[64, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Unknown  |
|  3 | Tensor<[1024]> self = ?,<br>Tensor<[64, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Unknown  |
|  4 | Tensor<[128]> self = ?,<br>Tensor<[4096, 128]> mat1 = ?,<br>Tensor<[128, 128]> mat2 = ?   | Unknown  |
|  5 | Tensor<[128]> self = ?,<br>Tensor<[4096, 512]> mat1 = ?,<br>Tensor<[512, 128]> mat2 = ?   | Unknown  |
|  6 | Tensor<[1536]> self = ?,<br>Tensor<[256, 512]> mat1 = ?,<br>Tensor<[512, 1536]> mat2 = ?  | Unknown  |
|  7 | Tensor<[2048]> self = ?,<br>Tensor<[256, 512]> mat1 = ?,<br>Tensor<[512, 2048]> mat2 = ?  | Unknown  |
|  8 | Tensor<[256]> self = ?,<br>Tensor<[1024, 1024]> mat1 = ?,<br>Tensor<[1024, 256]> mat2 = ? | Unknown  |
|  9 | Tensor<[256]> self = ?,<br>Tensor<[1024, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?   | Unknown  |
| 10 | Tensor<[3072]> self = ?,<br>Tensor<[64, 1024]> mat1 = ?,<br>Tensor<[1024, 3072]> mat2 = ? | Unknown  |
| 11 | Tensor<[384]> self = ?,<br>Tensor<[4096, 128]> mat1 = ?,<br>Tensor<[128, 384]> mat2 = ?   | Unknown  |
| 12 | Tensor<[4096]> self = ?,<br>Tensor<[64, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Unknown  |
| 13 | Tensor<[512]> self = ?,<br>Tensor<[225, 2]> mat1 = ?,<br>Tensor<[2, 512]> mat2 = ?        | Unknown  |
| 14 | Tensor<[512]> self = ?,<br>Tensor<[256, 2048]> mat1 = ?,<br>Tensor<[2048, 512]> mat2 = ?  | Unknown  |
| 15 | Tensor<[512]> self = ?,<br>Tensor<[256, 512]> mat1 = ?,<br>Tensor<[512, 512]> mat2 = ?    | Unknown  |
| 16 | Tensor<[512]> self = ?,<br>Tensor<[4096, 128]> mat1 = ?,<br>Tensor<[128, 512]> mat2 = ?   | Unknown  |
| 17 | Tensor<[768]> self = ?,<br>Tensor<[1024, 256]> mat1 = ?,<br>Tensor<[256, 768]> mat2 = ?   | Unknown  |
### aten.as_strided.default
|    | ATen Input Variations                                                                                                  | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int]<> size = [1, 1024, 1, 1],<br>List[int]<> stride = [1024, 1, 1024, 1024] | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[128, 64, 32]> self = ?,<br>Tensor<[128, 32, 64]> mat2 = ? | Unknown  |
|  1 | Tensor<[128, 64, 64]> self = ?,<br>Tensor<[128, 64, 32]> mat2 = ? | Unknown  |
|  2 | Tensor<[256, 64, 32]> self = ?,<br>Tensor<[256, 32, 64]> mat2 = ? | Unknown  |
|  3 | Tensor<[256, 64, 64]> self = ?,<br>Tensor<[256, 64, 32]> mat2 = ? | Unknown  |
|  4 | Tensor<[32, 64, 32]> self = ?,<br>Tensor<[32, 32, 64]> mat2 = ?   | Unknown  |
|  5 | Tensor<[32, 64, 64]> self = ?,<br>Tensor<[32, 64, 32]> mat2 = ?   | Unknown  |
|  6 | Tensor<[64, 64, 32]> self = ?,<br>Tensor<[64, 32, 64]> mat2 = ?   | Unknown  |
|  7 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 32]> mat2 = ?   | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                                                                                                                                        | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([1, 16, 16, 256])', 'torch.Size([1, 16, 16, 256])', 'torch.Size([1, 16, 16, 256])', 'torch.Size([1, 16, 16, 256])'],<br>int<> dim = -1 | Unknown  |
|  1 | List[Tensor]<> tensors = ['torch.Size([1, 32, 32, 128])', 'torch.Size([1, 32, 32, 128])', 'torch.Size([1, 32, 32, 128])', 'torch.Size([1, 32, 32, 128])'],<br>int<> dim = -1 | Unknown  |
|  2 | List[Tensor]<> tensors = ['torch.Size([1, 8, 8, 512])', 'torch.Size([1, 8, 8, 512])', 'torch.Size([1, 8, 8, 512])', 'torch.Size([1, 8, 8, 512])'],<br>int<> dim = -1         | Unknown  |
### aten.clamp.default
|    | ATen Input Variations                                                                                     | Status   |
|---:|:----------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 1, 1]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 4.605170185988092 | Unknown  |
|  1 | Tensor<[32, 1, 1]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 4.605170185988092 | Unknown  |
|  2 | Tensor<[4, 1, 1]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 4.605170185988092  | Unknown  |
|  3 | Tensor<[8, 1, 1]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 4.605170185988092  | Unknown  |
### aten.clamp_min.default
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 64, 1]> self = ?,<br>number<> min = 1e-12 | Unknown  |
|  1 | Tensor<[16, 8, 64, 1]> self = ?,<br>number<> min = 1e-12 | Unknown  |
|  2 | Tensor<[4, 16, 64, 1]> self = ?,<br>number<> min = 1e-12 | Unknown  |
|  3 | Tensor<[64, 4, 64, 1]> self = ?,<br>number<> min = 1e-12 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 2048]> self = ?                                                                | Unknown  |
|  1 | Tensor<[1, 16, 16, 512]> self = ?                                                                 | Unknown  |
|  2 | Tensor<[1, 2, 2, 8, 8, 512]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Unknown  |
|  3 | Tensor<[1, 2, 8, 2, 8, 512]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Unknown  |
|  4 | Tensor<[1, 32, 32, 1024]> self = ?                                                                | Unknown  |
|  5 | Tensor<[1, 32, 32, 256]> self = ?                                                                 | Unknown  |
|  6 | Tensor<[1, 32, 64, 64]> self = ?                                                                  | Unknown  |
|  7 | Tensor<[1, 4, 4, 8, 8, 256]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Unknown  |
|  8 | Tensor<[1, 4, 8, 4, 8, 256]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Unknown  |
|  9 | Tensor<[1, 64, 1024]> self = ?                                                                    | Unknown  |
| 10 | Tensor<[1, 64, 32, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Unknown  |
| 11 | Tensor<[1, 64, 64, 128]> self = ?                                                                 | Unknown  |
| 12 | Tensor<[1, 64, 64, 512]> self = ?                                                                 | Unknown  |
| 13 | Tensor<[1, 8, 8, 1024]> self = ?                                                                  | Unknown  |
| 14 | Tensor<[1, 8, 8, 4096]> self = ?                                                                  | Unknown  |
| 15 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Unknown  |
| 16 | Tensor<[16, 64, 256]> self = ?                                                                    | Unknown  |
| 17 | Tensor<[16, 64, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Unknown  |
| 18 | Tensor<[16, 64, 8, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Unknown  |
| 19 | Tensor<[16, 8, 32, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Unknown  |
| 20 | Tensor<[16, 8, 64, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Unknown  |
| 21 | Tensor<[16, 8, 64, 64]> self = ?                                                                  | Unknown  |
| 22 | Tensor<[2, 2, 8, 8]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Unknown  |
| 23 | Tensor<[32, 64, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Unknown  |
| 24 | Tensor<[4, 16, 32, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Unknown  |
| 25 | Tensor<[4, 16, 64, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Unknown  |
| 26 | Tensor<[4, 16, 64, 64]> self = ?                                                                  | Unknown  |
| 27 | Tensor<[4, 4, 8, 8]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Unknown  |
| 28 | Tensor<[4, 64, 16, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Unknown  |
| 29 | Tensor<[4, 64, 512]> self = ?                                                                     | Unknown  |
| 30 | Tensor<[4, 64, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format          | Unknown  |
| 31 | Tensor<[64, 4, 32, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Unknown  |
| 32 | Tensor<[64, 4, 64, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Unknown  |
| 33 | Tensor<[64, 4, 64, 64]> self = ?                                                                  | Unknown  |
| 34 | Tensor<[64, 64, 128]> self = ?                                                                    | Unknown  |
| 35 | Tensor<[64, 64, 4, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Unknown  |
| 36 | Tensor<[8, 64, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format          | Unknown  |
| 37 | Tensor<[8, 8, 8, 8]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Unknown  |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int]<> pad = [0, 0, 0, 0, 0, 0],<br>number<> value = 0.0 | Unknown  |
|  1 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int]<> pad = [0, 0, 0, 0, 0, 0],<br>number<> value = 0.0 | Unknown  |
|  2 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int]<> pad = [0, 0, 0, 0, 0, 0],<br>number<> value = 0.0 | Unknown  |
|  3 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int]<> pad = [0, 0, 0, 0, 0, 0],<br>number<> value = 0.0  | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                       | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 256, 256]> input = ?,<br>Tensor<[128, 3, 4, 4]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int]<> stride = [4, 4],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 64, 32]> self = ?,<br>Tensor<[1, 32, 64, 32]> other = ? | Unknown  |
|  1 | Tensor<[16, 8, 64, 32]> self = ?,<br>Tensor<[16, 8, 64, 32]> other = ? | Unknown  |
|  2 | Tensor<[4, 16, 64, 32]> self = ?,<br>Tensor<[4, 16, 64, 32]> other = ? | Unknown  |
|  3 | Tensor<[64, 4, 64, 32]> self = ?,<br>Tensor<[64, 4, 64, 32]> other = ? | Unknown  |
### aten.eq.Scalar
|    | ATen Input Variations                                | Status   |
|---:|:-----------------------------------------------------|:---------|
|  0 | Tensor<[16, 64, 64]> self = ?,<br>number<> other = 0 | Unknown  |
|  1 | Tensor<[4, 64, 64]> self = ?,<br>number<> other = 0  | Unknown  |
|  2 | Tensor<[64, 64, 64]> self = ?,<br>number<> other = 0 | Unknown  |
### aten.exp.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[16, 1, 1]> self = ? | Unknown  |
|  1 | Tensor<[32, 1, 1]> self = ? | Unknown  |
|  2 | Tensor<[4, 1, 1]> self = ?  | Unknown  |
|  3 | Tensor<[8, 1, 1]> self = ?  | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 32, 64]> self = ?,<br>List[int]<> size = [1, 32, 32, 64] | Unknown  |
|  1 | Tensor<[1, 32, 64, 1]> self = ?,<br>List[int]<> size = [1, 32, 64, 32]  | Unknown  |
|  2 | Tensor<[1, 32, 64, 32]> self = ?,<br>List[int]<> size = [1, 32, 64, 32] | Unknown  |
|  3 | Tensor<[1, 32, 64, 64]> self = ?,<br>List[int]<> size = [1, 32, 64, 64] | Unknown  |
|  4 | Tensor<[16, 8, 32, 64]> self = ?,<br>List[int]<> size = [16, 8, 32, 64] | Unknown  |
|  5 | Tensor<[16, 8, 64, 1]> self = ?,<br>List[int]<> size = [16, 8, 64, 32]  | Unknown  |
|  6 | Tensor<[16, 8, 64, 32]> self = ?,<br>List[int]<> size = [16, 8, 64, 32] | Unknown  |
|  7 | Tensor<[16, 8, 64, 64]> self = ?,<br>List[int]<> size = [16, 8, 64, 64] | Unknown  |
|  8 | Tensor<[4, 16, 32, 64]> self = ?,<br>List[int]<> size = [4, 16, 32, 64] | Unknown  |
|  9 | Tensor<[4, 16, 64, 1]> self = ?,<br>List[int]<> size = [4, 16, 64, 32]  | Unknown  |
| 10 | Tensor<[4, 16, 64, 32]> self = ?,<br>List[int]<> size = [4, 16, 64, 32] | Unknown  |
| 11 | Tensor<[4, 16, 64, 64]> self = ?,<br>List[int]<> size = [4, 16, 64, 64] | Unknown  |
| 12 | Tensor<[64, 4, 32, 64]> self = ?,<br>List[int]<> size = [64, 4, 32, 64] | Unknown  |
| 13 | Tensor<[64, 4, 64, 1]> self = ?,<br>List[int]<> size = [64, 4, 64, 32]  | Unknown  |
| 14 | Tensor<[64, 4, 64, 32]> self = ?,<br>List[int]<> size = [64, 4, 64, 32] | Unknown  |
| 15 | Tensor<[64, 4, 64, 64]> self = ?,<br>List[int]<> size = [64, 4, 64, 64] | Unknown  |
### aten.gelu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 2048]> self = ? | Unknown  |
|  1 | Tensor<[1, 32, 32, 1024]> self = ? | Unknown  |
|  2 | Tensor<[1, 64, 64, 512]> self = ?  | Unknown  |
|  3 | Tensor<[1, 8, 8, 4096]> self = ?   | Unknown  |
### aten.index.Tensor
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[225, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([4096])'] | Unknown  |
|  1 | Tensor<[225, 32]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([4096])'] | Unknown  |
|  2 | Tensor<[225, 4]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([4096])']  | Unknown  |
|  3 | Tensor<[225, 8]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([4096])']  | Unknown  |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                                  | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 64, 32]> self = ?,<br>number<> ord = 2.0,<br>Optional[List[int]]<> dim = [-1],<br>bool<> keepdim = True | Unknown  |
|  1 | Tensor<[16, 8, 64, 32]> self = ?,<br>number<> ord = 2.0,<br>Optional[List[int]]<> dim = [-1],<br>bool<> keepdim = True | Unknown  |
|  2 | Tensor<[4, 16, 64, 32]> self = ?,<br>number<> ord = 2.0,<br>Optional[List[int]]<> dim = [-1],<br>bool<> keepdim = True | Unknown  |
|  3 | Tensor<[64, 4, 64, 32]> self = ?,<br>number<> ord = 2.0,<br>Optional[List[int]]<> dim = [-1],<br>bool<> keepdim = True | Unknown  |
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
|    | ATen Input Variations                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 8, 8]> self = ?,<br>Optional[List[int]]<> dim = [-1, -2],<br>bool<> keepdim = True | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                         | Status   |
|---:|:--------------------------------------------------------------|:---------|
|  0 | Tensor<[1024, 512]> self = ?,<br>Tensor<[512, 256]> mat2 = ?  | Unknown  |
|  1 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 16]> mat2 = ?    | Unknown  |
|  2 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 32]> mat2 = ?    | Unknown  |
|  3 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 4]> mat2 = ?     | Unknown  |
|  4 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 8]> mat2 = ?     | Unknown  |
|  5 | Tensor<[256, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ? | Unknown  |
|  6 | Tensor<[64, 2048]> self = ?,<br>Tensor<[2048, 1024]> mat2 = ? | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 64, 64]> self = ?,<br>Tensor<> other = 16          | Unknown  |
|  1 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<> other = 16          | Unknown  |
|  2 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[32, 1, 1]> other = ? | Unknown  |
|  3 | Tensor<[1, 4, 64, 64]> self = ?,<br>Tensor<> other = 16           | Unknown  |
|  4 | Tensor<[1, 8, 64, 64]> self = ?,<br>Tensor<> other = 16           | Unknown  |
|  5 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[8, 1, 1]> other = ?  | Unknown  |
|  6 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[16, 1, 1]> other = ? | Unknown  |
|  7 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[4, 1, 1]> other = ?  | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                             | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 512]> input = ?,<br>List[int]<> normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float<> eps = 1e-05   | Unknown  |
|  1 | Tensor<[1, 32, 32, 256]> input = ?,<br>List[int]<> normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float<> eps = 1e-05   | Unknown  |
|  2 | Tensor<[1, 64, 64, 128]> input = ?,<br>List[int]<> normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float<> eps = 1e-05   | Unknown  |
|  3 | Tensor<[1, 8, 8, 1024]> input = ?,<br>List[int]<> normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float<> eps = 1e-05 | Unknown  |
### aten.ne.Scalar
|    | ATen Input Variations                                | Status   |
|---:|:-----------------------------------------------------|:---------|
|  0 | Tensor<[16, 64, 64]> self = ?,<br>number<> other = 0 | Unknown  |
|  1 | Tensor<[4, 64, 64]> self = ?,<br>number<> other = 0  | Unknown  |
|  2 | Tensor<[64, 64, 64]> self = ?,<br>number<> other = 0 | Unknown  |
### aten.new_zeros.default
|    | ATen Input Variations                                                                                  | Status   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 64, 256]> self = ?,<br>List[int]<> size = [32, 32],<br>Optional[bool]<> pin_memory = False | Unknown  |
|  1 | Tensor<[4, 64, 512]> self = ?,<br>List[int]<> size = [16, 16],<br>Optional[bool]<> pin_memory = False  | Unknown  |
|  2 | Tensor<[64, 64, 128]> self = ?,<br>List[int]<> size = [64, 64],<br>Optional[bool]<> pin_memory = False | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                                            | Status   |
|---:|:---------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 8, 8, 1024]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5] | Unknown  |
|  1 | Tensor<[1, 1, 8, 1, 8, 1024]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5] | Unknown  |
|  2 | Tensor<[1, 128, 64, 64]> self = ?,<br>List[int]<> dims = [0, 2, 3, 1]            | Unknown  |
|  3 | Tensor<[1, 2, 2, 8, 8, 512]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5]  | Unknown  |
|  4 | Tensor<[1, 2, 8, 2, 8, 512]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5]  | Unknown  |
|  5 | Tensor<[1, 4, 4, 8, 8, 256]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5]  | Unknown  |
|  6 | Tensor<[1, 4, 8, 4, 8, 256]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5]  | Unknown  |
|  7 | Tensor<[1, 64, 3, 32, 32]> self = ?,<br>List[int]<> dims = [2, 0, 3, 1, 4]       | Unknown  |
|  8 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int]<> dims = [0, 3, 1, 2]             | Unknown  |
|  9 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5]  | Unknown  |
| 10 | Tensor<[16, 64, 3, 8, 32]> self = ?,<br>List[int]<> dims = [2, 0, 3, 1, 4]       | Unknown  |
| 11 | Tensor<[2, 8, 2, 8]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]                | Unknown  |
| 12 | Tensor<[4, 64, 3, 16, 32]> self = ?,<br>List[int]<> dims = [2, 0, 3, 1, 4]       | Unknown  |
| 13 | Tensor<[4, 8, 4, 8]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]                | Unknown  |
| 14 | Tensor<[64, 64, 16]> self = ?,<br>List[int]<> dims = [2, 0, 1]                   | Unknown  |
| 15 | Tensor<[64, 64, 3, 4, 32]> self = ?,<br>List[int]<> dims = [2, 0, 3, 1, 4]       | Unknown  |
| 16 | Tensor<[64, 64, 32]> self = ?,<br>List[int]<> dims = [2, 0, 1]                   | Unknown  |
| 17 | Tensor<[64, 64, 4]> self = ?,<br>List[int]<> dims = [2, 0, 1]                    | Unknown  |
| 18 | Tensor<[64, 64, 8]> self = ?,<br>List[int]<> dims = [2, 0, 1]                    | Unknown  |
| 19 | Tensor<[8, 8, 8, 8]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]                | Unknown  |
### aten.relu.default
|    | ATen Input Variations             | Status   |
|---:|:----------------------------------|:---------|
|  0 | Tensor<[1, 15, 15, 512]> self = ? | Unknown  |
### aten.roll.default
|    | ATen Input Variations                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int]<> shifts = [-4, -4],<br>List[int]<> dims = [1, 2] | Unknown  |
|  1 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int]<> shifts = [4, 4],<br>List[int]<> dims = [1, 2]   | Unknown  |
|  2 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int]<> shifts = [-4, -4],<br>List[int]<> dims = [1, 2] | Unknown  |
|  3 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int]<> shifts = [4, 4],<br>List[int]<> dims = [1, 2]   | Unknown  |
|  4 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int]<> shifts = [-4, -4],<br>List[int]<> dims = [1, 2] | Unknown  |
|  5 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int]<> shifts = [4, 4],<br>List[int]<> dims = [1, 2]   | Unknown  |
### aten.select.int
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 1, 32, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | Unknown  |
|  1 | Tensor<[3, 1, 32, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 1 | Unknown  |
|  2 | Tensor<[3, 1, 32, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 2 | Unknown  |
|  3 | Tensor<[3, 16, 8, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | Unknown  |
|  4 | Tensor<[3, 16, 8, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 1 | Unknown  |
|  5 | Tensor<[3, 16, 8, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 2 | Unknown  |
|  6 | Tensor<[3, 4, 16, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | Unknown  |
|  7 | Tensor<[3, 4, 16, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 1 | Unknown  |
|  8 | Tensor<[3, 4, 16, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 2 | Unknown  |
|  9 | Tensor<[3, 64, 4, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | Unknown  |
| 10 | Tensor<[3, 64, 4, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 1 | Unknown  |
| 11 | Tensor<[3, 64, 4, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 2 | Unknown  |
### aten.sigmoid.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 16, 64, 64]> self = ? | Unknown  |
|  1 | Tensor<[1, 32, 64, 64]> self = ? | Unknown  |
|  2 | Tensor<[1, 4, 64, 64]> self = ?  | Unknown  |
|  3 | Tensor<[1, 8, 64, 64]> self = ?  | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                             | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 256]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
|  1 | Tensor<[1, 16, 16, 512]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
|  2 | Tensor<[1, 16, 16, 512]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
|  3 | Tensor<[1, 16, 16, 512]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
|  4 | Tensor<[1, 16, 16, 512]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
|  5 | Tensor<[1, 16, 32, 256]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
|  6 | Tensor<[1, 16, 32, 256]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
|  7 | Tensor<[1, 32, 32, 128]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
|  8 | Tensor<[1, 32, 32, 256]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
|  9 | Tensor<[1, 32, 32, 256]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
| 10 | Tensor<[1, 32, 32, 256]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
| 11 | Tensor<[1, 32, 32, 256]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
| 12 | Tensor<[1, 32, 64, 128]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
| 13 | Tensor<[1, 32, 64, 128]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
| 14 | Tensor<[1, 64, 64, 128]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
| 15 | Tensor<[1, 64, 64, 128]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
| 16 | Tensor<[1, 64, 64, 128]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
| 17 | Tensor<[1, 64, 64, 128]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
| 18 | Tensor<[1, 8, 16, 512]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2  | Unknown  |
| 19 | Tensor<[1, 8, 16, 512]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2  | Unknown  |
| 20 | Tensor<[1, 8, 8, 1024]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                     | Unknown  |
| 21 | Tensor<[1, 8, 8, 1024]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                     | Unknown  |
| 22 | Tensor<[1, 8, 8, 512]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                      | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ? | Unknown  |
|  1 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?   | Unknown  |
|  2 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ? | Unknown  |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1000, 1024]> self = ? | Unknown  |
|  1 | Tensor<[1024, 1024]> self = ? | Unknown  |
|  2 | Tensor<[1024, 2048]> self = ? | Unknown  |
|  3 | Tensor<[1024, 256]> self = ?  | Unknown  |
|  4 | Tensor<[1024, 4096]> self = ? | Unknown  |
|  5 | Tensor<[128, 128]> self = ?   | Unknown  |
|  6 | Tensor<[128, 512]> self = ?   | Unknown  |
|  7 | Tensor<[1536, 512]> self = ?  | Unknown  |
|  8 | Tensor<[16, 512]> self = ?    | Unknown  |
|  9 | Tensor<[2048, 512]> self = ?  | Unknown  |
| 10 | Tensor<[256, 1024]> self = ?  | Unknown  |
| 11 | Tensor<[256, 256]> self = ?   | Unknown  |
| 12 | Tensor<[256, 512]> self = ?   | Unknown  |
| 13 | Tensor<[3072, 1024]> self = ? | Unknown  |
| 14 | Tensor<[32, 512]> self = ?    | Unknown  |
| 15 | Tensor<[384, 128]> self = ?   | Unknown  |
| 16 | Tensor<[4, 512]> self = ?     | Unknown  |
| 17 | Tensor<[4096, 1024]> self = ? | Unknown  |
| 18 | Tensor<[512, 1024]> self = ?  | Unknown  |
| 19 | Tensor<[512, 128]> self = ?   | Unknown  |
| 20 | Tensor<[512, 2048]> self = ?  | Unknown  |
| 21 | Tensor<[512, 2]> self = ?     | Unknown  |
| 22 | Tensor<[512, 512]> self = ?   | Unknown  |
| 23 | Tensor<[768, 256]> self = ?   | Unknown  |
| 24 | Tensor<[8, 512]> self = ?     | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 64, 32]> self = ?,<br>int<> dim0 = -2,<br>int<> dim1 = -1 | Unknown  |
|  1 | Tensor<[1, 32, 64, 32]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Unknown  |
|  2 | Tensor<[16, 8, 64, 32]> self = ?,<br>int<> dim0 = -2,<br>int<> dim1 = -1 | Unknown  |
|  3 | Tensor<[16, 8, 64, 32]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Unknown  |
|  4 | Tensor<[4, 16, 64, 32]> self = ?,<br>int<> dim0 = -2,<br>int<> dim1 = -1 | Unknown  |
|  5 | Tensor<[4, 16, 64, 32]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Unknown  |
|  6 | Tensor<[64, 4, 64, 32]> self = ?,<br>int<> dim0 = -2,<br>int<> dim1 = -1 | Unknown  |
|  7 | Tensor<[64, 4, 64, 32]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[16, 1, 64, 64]> self = ?,<br>int<> dim = 0 | Unknown  |
|  1 | Tensor<[16, 64, 64]> self = ?,<br>int<> dim = 0    | Unknown  |
|  2 | Tensor<[16, 64, 64]> self = ?,<br>int<> dim = 1    | Unknown  |
|  3 | Tensor<[16, 64]> self = ?,<br>int<> dim = 1        | Unknown  |
|  4 | Tensor<[16, 64]> self = ?,<br>int<> dim = 2        | Unknown  |
|  5 | Tensor<[32, 64, 64]> self = ?,<br>int<> dim = 0    | Unknown  |
|  6 | Tensor<[4, 1, 64, 64]> self = ?,<br>int<> dim = 0  | Unknown  |
|  7 | Tensor<[4, 64, 64]> self = ?,<br>int<> dim = 0     | Unknown  |
|  8 | Tensor<[4, 64, 64]> self = ?,<br>int<> dim = 1     | Unknown  |
|  9 | Tensor<[4, 64]> self = ?,<br>int<> dim = 1         | Unknown  |
| 10 | Tensor<[4, 64]> self = ?,<br>int<> dim = 2         | Unknown  |
| 11 | Tensor<[64, 1, 64, 64]> self = ?,<br>int<> dim = 0 | Unknown  |
| 12 | Tensor<[64, 64, 64]> self = ?,<br>int<> dim = 1    | Unknown  |
| 13 | Tensor<[64, 64]> self = ?,<br>int<> dim = 1        | Unknown  |
| 14 | Tensor<[64, 64]> self = ?,<br>int<> dim = 2        | Unknown  |
| 15 | Tensor<[8, 64, 64]> self = ?,<br>int<> dim = 0     | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 8, 8, 1024]> self = ?,<br>List[int]<> size = [1, 64, 1024]   | Unknown  |
|  1 | Tensor<[1, 1, 8, 1, 8, 1024]> self = ?,<br>List[int]<> size = [1, 8, 8, 1024] | Unknown  |
|  2 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int]<> size = [1, 1024]             | Unknown  |
|  3 | Tensor<[1, 15, 15, 16]> self = ?,<br>List[int]<> size = [-1, 16]              | Unknown  |
|  4 | Tensor<[1, 15, 15, 2]> self = ?,<br>List[int]<> size = [225, 2]               | Unknown  |
|  5 | Tensor<[1, 15, 15, 32]> self = ?,<br>List[int]<> size = [-1, 32]              | Unknown  |
|  6 | Tensor<[1, 15, 15, 4]> self = ?,<br>List[int]<> size = [-1, 4]                | Unknown  |
|  7 | Tensor<[1, 15, 15, 512]> self = ?,<br>List[int]<> size = [225, 512]           | Unknown  |
|  8 | Tensor<[1, 15, 15, 8]> self = ?,<br>List[int]<> size = [-1, 8]                | Unknown  |
|  9 | Tensor<[1, 16, 16, 1024]> self = ?,<br>List[int]<> size = [256, 1024]         | Unknown  |
| 10 | Tensor<[1, 16, 16, 2048]> self = ?,<br>List[int]<> size = [256, 2048]         | Unknown  |
| 11 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int]<> size = [1, 2, 8, 2, 8, 512] | Unknown  |
| 12 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int]<> size = [256, 512]           | Unknown  |
| 13 | Tensor<[1, 16, 8, 64, 64]> self = ?,<br>List[int]<> size = [-1, 8, 64, 64]    | Unknown  |
| 14 | Tensor<[1, 32, 32, 1024]> self = ?,<br>List[int]<> size = [1024, 1024]        | Unknown  |
| 15 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int]<> size = [1, 4, 8, 4, 8, 256] | Unknown  |
| 16 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int]<> size = [1024, 256]          | Unknown  |
| 17 | Tensor<[1, 32, 32, 512]> self = ?,<br>List[int]<> size = [1024, 512]          | Unknown  |
| 18 | Tensor<[1, 32, 32, 64]> self = ?,<br>List[int]<> size = [32, 32, 64]          | Unknown  |
| 19 | Tensor<[1, 32, 64, 32]> self = ?,<br>List[int]<> size = [32, 64, 32]          | Unknown  |
| 20 | Tensor<[1, 32, 64, 64]> self = ?,<br>List[int]<> size = [32, 64, 64]          | Unknown  |
| 21 | Tensor<[1, 4, 16, 64, 64]> self = ?,<br>List[int]<> size = [-1, 16, 64, 64]   | Unknown  |
| 22 | Tensor<[1, 64, 1024]> self = ?,<br>List[int]<> size = [1, 1, 1, 8, 8, 1024]   | Unknown  |
| 23 | Tensor<[1, 64, 1024]> self = ?,<br>List[int]<> size = [64, 1024]              | Unknown  |
| 24 | Tensor<[1, 64, 3072]> self = ?,<br>List[int]<> size = [1, 64, 3, 32, 32]      | Unknown  |
| 25 | Tensor<[1, 64, 4, 64, 64]> self = ?,<br>List[int]<> size = [-1, 4, 64, 64]    | Unknown  |
| 26 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int]<> size = [1, 8, 8, 8, 8, 128] | Unknown  |
| 27 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int]<> size = [4096, 128]          | Unknown  |
| 28 | Tensor<[1, 64, 64, 512]> self = ?,<br>List[int]<> size = [4096, 512]          | Unknown  |
| 29 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int]<> size = [1, 1, 8, 1, 8, 1024] | Unknown  |
| 30 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int]<> size = [64, 1024]            | Unknown  |
| 31 | Tensor<[1, 8, 8, 2048]> self = ?,<br>List[int]<> size = [64, 2048]            | Unknown  |
| 32 | Tensor<[1, 8, 8, 4096]> self = ?,<br>List[int]<> size = [64, 4096]            | Unknown  |
| 33 | Tensor<[1024, 1024]> self = ?,<br>List[int]<> size = [1, 32, 32, 1024]        | Unknown  |
| 34 | Tensor<[1024, 256]> self = ?,<br>List[int]<> size = [1, 32, 32, 256]          | Unknown  |
| 35 | Tensor<[1024, 256]> self = ?,<br>List[int]<> size = [16, 64, 256]             | Unknown  |
| 36 | Tensor<[1024, 768]> self = ?,<br>List[int]<> size = [16, 64, 768]             | Unknown  |
| 37 | Tensor<[128, 64, 32]> self = ?,<br>List[int]<> size = [16, 8, 64, 32]         | Unknown  |
| 38 | Tensor<[128, 64, 64]> self = ?,<br>List[int]<> size = [16, 8, 64, 64]         | Unknown  |
| 39 | Tensor<[16, 16]> self = ?,<br>List[int]<> size = [2, 8, 2, 8]                 | Unknown  |
| 40 | Tensor<[16, 64, 256]> self = ?,<br>List[int]<> size = [1, 4, 4, 8, 8, 256]    | Unknown  |
| 41 | Tensor<[16, 64, 256]> self = ?,<br>List[int]<> size = [1024, 256]             | Unknown  |
| 42 | Tensor<[16, 64, 768]> self = ?,<br>List[int]<> size = [16, 64, 3, 8, 32]      | Unknown  |
| 43 | Tensor<[16, 8, 64, 64]> self = ?,<br>List[int]<> size = [1, 16, 8, 64, 64]    | Unknown  |
| 44 | Tensor<[16, 8, 64, 64]> self = ?,<br>List[int]<> size = [128, 64, 64]         | Unknown  |
| 45 | Tensor<[225, 16]> self = ?,<br>List[int]<> size = [1, 15, 15, 16]             | Unknown  |
| 46 | Tensor<[225, 32]> self = ?,<br>List[int]<> size = [1, 15, 15, 32]             | Unknown  |
| 47 | Tensor<[225, 4]> self = ?,<br>List[int]<> size = [1, 15, 15, 4]               | Unknown  |
| 48 | Tensor<[225, 512]> self = ?,<br>List[int]<> size = [1, 15, 15, 512]           | Unknown  |
| 49 | Tensor<[225, 8]> self = ?,<br>List[int]<> size = [1, 15, 15, 8]               | Unknown  |
| 50 | Tensor<[256, 1536]> self = ?,<br>List[int]<> size = [4, 64, 1536]             | Unknown  |
| 51 | Tensor<[256, 2048]> self = ?,<br>List[int]<> size = [1, 16, 16, 2048]         | Unknown  |
| 52 | Tensor<[256, 512]> self = ?,<br>List[int]<> size = [1, 16, 16, 512]           | Unknown  |
| 53 | Tensor<[256, 512]> self = ?,<br>List[int]<> size = [4, 64, 512]               | Unknown  |
| 54 | Tensor<[256, 64, 32]> self = ?,<br>List[int]<> size = [64, 4, 64, 32]         | Unknown  |
| 55 | Tensor<[256, 64, 64]> self = ?,<br>List[int]<> size = [64, 4, 64, 64]         | Unknown  |
| 56 | Tensor<[32, 32]> self = ?,<br>List[int]<> size = [4, 8, 4, 8]                 | Unknown  |
| 57 | Tensor<[32, 64, 32]> self = ?,<br>List[int]<> size = [1, 32, 64, 32]          | Unknown  |
| 58 | Tensor<[32, 64, 64]> self = ?,<br>List[int]<> size = [1, 32, 64, 64]          | Unknown  |
| 59 | Tensor<[4, 16, 64, 64]> self = ?,<br>List[int]<> size = [1, 4, 16, 64, 64]    | Unknown  |
| 60 | Tensor<[4, 16, 64, 64]> self = ?,<br>List[int]<> size = [64, 64, 64]          | Unknown  |
| 61 | Tensor<[4, 64, 1536]> self = ?,<br>List[int]<> size = [4, 64, 3, 16, 32]      | Unknown  |
| 62 | Tensor<[4, 64, 512]> self = ?,<br>List[int]<> size = [1, 2, 2, 8, 8, 512]     | Unknown  |
| 63 | Tensor<[4, 64, 512]> self = ?,<br>List[int]<> size = [256, 512]               | Unknown  |
| 64 | Tensor<[4096, 128]> self = ?,<br>List[int]<> size = [1, 64, 64, 128]          | Unknown  |
| 65 | Tensor<[4096, 128]> self = ?,<br>List[int]<> size = [64, 64, 128]             | Unknown  |
| 66 | Tensor<[4096, 16]> self = ?,<br>List[int]<> size = [64, 64, -1]               | Unknown  |
| 67 | Tensor<[4096, 32]> self = ?,<br>List[int]<> size = [64, 64, -1]               | Unknown  |
| 68 | Tensor<[4096, 384]> self = ?,<br>List[int]<> size = [64, 64, 384]             | Unknown  |
| 69 | Tensor<[4096, 4]> self = ?,<br>List[int]<> size = [64, 64, -1]                | Unknown  |
| 70 | Tensor<[4096, 512]> self = ?,<br>List[int]<> size = [1, 64, 64, 512]          | Unknown  |
| 71 | Tensor<[4096, 8]> self = ?,<br>List[int]<> size = [64, 64, -1]                | Unknown  |
| 72 | Tensor<[64, 1024]> self = ?,<br>List[int]<> size = [1, 64, 1024]              | Unknown  |
| 73 | Tensor<[64, 1024]> self = ?,<br>List[int]<> size = [1, 8, 8, 1024]            | Unknown  |
| 74 | Tensor<[64, 3072]> self = ?,<br>List[int]<> size = [1, 64, 3072]              | Unknown  |
| 75 | Tensor<[64, 4, 64, 64]> self = ?,<br>List[int]<> size = [1, 64, 4, 64, 64]    | Unknown  |
| 76 | Tensor<[64, 4, 64, 64]> self = ?,<br>List[int]<> size = [256, 64, 64]         | Unknown  |
| 77 | Tensor<[64, 4096]> self = ?,<br>List[int]<> size = [1, 8, 8, 4096]            | Unknown  |
| 78 | Tensor<[64, 64, 128]> self = ?,<br>List[int]<> size = [1, 8, 8, 8, 8, 128]    | Unknown  |
| 79 | Tensor<[64, 64, 128]> self = ?,<br>List[int]<> size = [4096, 128]             | Unknown  |
| 80 | Tensor<[64, 64, 32]> self = ?,<br>List[int]<> size = [4, 16, 64, 32]          | Unknown  |
| 81 | Tensor<[64, 64, 384]> self = ?,<br>List[int]<> size = [64, 64, 3, 4, 32]      | Unknown  |
| 82 | Tensor<[64, 64, 64]> self = ?,<br>List[int]<> size = [4, 16, 64, 64]          | Unknown  |
| 83 | Tensor<[64, 64]> self = ?,<br>List[int]<> size = [8, 8, 8, 8]                 | Unknown  |

