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
| 29 | aten.view.default              |                 73 |           0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 49, 49]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Done     |
|  1 | Tensor<[16, 8, 49, 49]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Done     |
|  2 | Tensor<[4, 16, 49, 49]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Done     |
|  3 | Tensor<[64, 4, 49, 49]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Done     |
### aten._unsafe_view.default
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2, 2, 7, 7, 512]> self = ?,<br>List[int]<> size = [4, 49, 512]     | Unknown  |
|  1 | Tensor<[1, 2, 7, 2, 7, 512]> self = ?,<br>List[int]<> size = [1, 14, 14, 512] | Unknown  |
|  2 | Tensor<[1, 4, 4, 7, 7, 256]> self = ?,<br>List[int]<> size = [16, 49, 256]    | Unknown  |
|  3 | Tensor<[1, 4, 7, 4, 7, 256]> self = ?,<br>List[int]<> size = [1, 28, 28, 256] | Unknown  |
|  4 | Tensor<[1, 49, 32, 32]> self = ?,<br>List[int]<> size = [1, 49, 1024]         | Unknown  |
|  5 | Tensor<[1, 8, 7, 8, 7, 128]> self = ?,<br>List[int]<> size = [1, 56, 56, 128] | Unknown  |
|  6 | Tensor<[1, 8, 8, 7, 7, 128]> self = ?,<br>List[int]<> size = [64, 49, 128]    | Unknown  |
|  7 | Tensor<[16, 49, 8, 32]> self = ?,<br>List[int]<> size = [16, 49, 256]         | Unknown  |
|  8 | Tensor<[16, 8, 32, 49]> self = ?,<br>List[int]<> size = [128, 32, 49]         | Unknown  |
|  9 | Tensor<[16, 8, 49, 32]> self = ?,<br>List[int]<> size = [128, 49, 32]         | Unknown  |
| 10 | Tensor<[2, 2, 7, 7]> self = ?,<br>List[int]<> size = [4, 49]                  | Unknown  |
| 11 | Tensor<[4, 16, 32, 49]> self = ?,<br>List[int]<> size = [64, 32, 49]          | Unknown  |
| 12 | Tensor<[4, 16, 49, 32]> self = ?,<br>List[int]<> size = [64, 49, 32]          | Unknown  |
| 13 | Tensor<[4, 4, 7, 7]> self = ?,<br>List[int]<> size = [16, 49]                 | Unknown  |
| 14 | Tensor<[4, 49, 16, 32]> self = ?,<br>List[int]<> size = [4, 49, 512]          | Unknown  |
| 15 | Tensor<[64, 4, 32, 49]> self = ?,<br>List[int]<> size = [256, 32, 49]         | Unknown  |
| 16 | Tensor<[64, 4, 49, 32]> self = ?,<br>List[int]<> size = [256, 49, 32]         | Unknown  |
| 17 | Tensor<[64, 49, 4, 32]> self = ?,<br>List[int]<> size = [64, 49, 128]         | Unknown  |
| 18 | Tensor<[8, 8, 7, 7]> self = ?,<br>List[int]<> size = [64, 49]                 | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   |
|---:|:-----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 14, 512]> self = ?,<br>Tensor<[1, 14, 14, 512]> other = ?     | Done     |
|  1 | Tensor<[1, 16, 8, 49, 49]> self = ?,<br>Tensor<[1, 16, 1, 49, 49]> other = ? | Done     |
|  2 | Tensor<[1, 28, 28, 256]> self = ?,<br>Tensor<[1, 28, 28, 256]> other = ?     | Done     |
|  3 | Tensor<[1, 32, 49, 49]> self = ?,<br>Tensor<[1, 32, 49, 49]> other = ?       | Done     |
|  4 | Tensor<[1, 4, 16, 49, 49]> self = ?,<br>Tensor<[1, 4, 1, 49, 49]> other = ?  | Done     |
|  5 | Tensor<[1, 56, 56, 128]> self = ?,<br>Tensor<[1, 56, 56, 128]> other = ?     | Done     |
|  6 | Tensor<[1, 64, 4, 49, 49]> self = ?,<br>Tensor<[1, 64, 1, 49, 49]> other = ? | Done     |
|  7 | Tensor<[1, 7, 7, 1024]> self = ?,<br>Tensor<[1, 7, 7, 1024]> other = ?       | Done     |
|  8 | Tensor<[16, 8, 49, 49]> self = ?,<br>Tensor<[1, 8, 49, 49]> other = ?        | Done     |
|  9 | Tensor<[4, 16, 49, 49]> self = ?,<br>Tensor<[1, 16, 49, 49]> other = ?       | Done     |
| 10 | Tensor<[64, 4, 49, 49]> self = ?,<br>Tensor<[1, 4, 49, 49]> other = ?        | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1000]> mat2 = ?  | Done     |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[49, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Done     |
|  2 | Tensor<[1024]> self = ?,<br>Tensor<[49, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Done     |
|  3 | Tensor<[1024]> self = ?,<br>Tensor<[784, 256]> mat1 = ?,<br>Tensor<[256, 1024]> mat2 = ?  | Done     |
|  4 | Tensor<[128]> self = ?,<br>Tensor<[3136, 128]> mat1 = ?,<br>Tensor<[128, 128]> mat2 = ?   | Done     |
|  5 | Tensor<[128]> self = ?,<br>Tensor<[3136, 512]> mat1 = ?,<br>Tensor<[512, 128]> mat2 = ?   | Done     |
|  6 | Tensor<[1536]> self = ?,<br>Tensor<[196, 512]> mat1 = ?,<br>Tensor<[512, 1536]> mat2 = ?  | Done     |
|  7 | Tensor<[2048]> self = ?,<br>Tensor<[196, 512]> mat1 = ?,<br>Tensor<[512, 2048]> mat2 = ?  | Done     |
|  8 | Tensor<[256]> self = ?,<br>Tensor<[784, 1024]> mat1 = ?,<br>Tensor<[1024, 256]> mat2 = ?  | Done     |
|  9 | Tensor<[256]> self = ?,<br>Tensor<[784, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?    | Done     |
| 10 | Tensor<[3072]> self = ?,<br>Tensor<[49, 1024]> mat1 = ?,<br>Tensor<[1024, 3072]> mat2 = ? | Done     |
| 11 | Tensor<[384]> self = ?,<br>Tensor<[3136, 128]> mat1 = ?,<br>Tensor<[128, 384]> mat2 = ?   | Done     |
| 12 | Tensor<[4096]> self = ?,<br>Tensor<[49, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Done     |
| 13 | Tensor<[512]> self = ?,<br>Tensor<[196, 2048]> mat1 = ?,<br>Tensor<[2048, 512]> mat2 = ?  | Done     |
| 14 | Tensor<[512]> self = ?,<br>Tensor<[196, 512]> mat1 = ?,<br>Tensor<[512, 512]> mat2 = ?    | Done     |
| 15 | Tensor<[512]> self = ?,<br>Tensor<[3136, 128]> mat1 = ?,<br>Tensor<[128, 512]> mat2 = ?   | Done     |
| 16 | Tensor<[768]> self = ?,<br>Tensor<[784, 256]> mat1 = ?,<br>Tensor<[256, 768]> mat2 = ?    | Done     |
### aten.as_strided.default
|    | ATen Input Variations                                                                                                  | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int]<> size = [1, 1024, 1, 1],<br>List[int]<> stride = [1024, 1, 1024, 1024] | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[128, 49, 32]> self = ?,<br>Tensor<[128, 32, 49]> mat2 = ? | Done     |
|  1 | Tensor<[128, 49, 49]> self = ?,<br>Tensor<[128, 49, 32]> mat2 = ? | Done     |
|  2 | Tensor<[256, 49, 32]> self = ?,<br>Tensor<[256, 32, 49]> mat2 = ? | Done     |
|  3 | Tensor<[256, 49, 49]> self = ?,<br>Tensor<[256, 49, 32]> mat2 = ? | Done     |
|  4 | Tensor<[32, 49, 32]> self = ?,<br>Tensor<[32, 32, 49]> mat2 = ?   | Done     |
|  5 | Tensor<[32, 49, 49]> self = ?,<br>Tensor<[32, 49, 32]> mat2 = ?   | Done     |
|  6 | Tensor<[64, 49, 32]> self = ?,<br>Tensor<[64, 32, 49]> mat2 = ?   | Done     |
|  7 | Tensor<[64, 49, 49]> self = ?,<br>Tensor<[64, 49, 32]> mat2 = ?   | Done     |
### aten.cat.default
|    | ATen Input Variations                                                                                                                                                        | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([1, 14, 14, 256])', 'torch.Size([1, 14, 14, 256])', 'torch.Size([1, 14, 14, 256])', 'torch.Size([1, 14, 14, 256])'],<br>int<> dim = -1 | Unknown  |
|  1 | List[Tensor]<> tensors = ['torch.Size([1, 28, 28, 128])', 'torch.Size([1, 28, 28, 128])', 'torch.Size([1, 28, 28, 128])', 'torch.Size([1, 28, 28, 128])'],<br>int<> dim = -1 | Unknown  |
|  2 | List[Tensor]<> tensors = ['torch.Size([1, 7, 7, 512])', 'torch.Size([1, 7, 7, 512])', 'torch.Size([1, 7, 7, 512])', 'torch.Size([1, 7, 7, 512])'],<br>int<> dim = -1         | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 14, 2048]> self = ?                                                                | Done     |
|  1 | Tensor<[1, 14, 14, 512]> self = ?                                                                 | Unknown  |
|  2 | Tensor<[1, 2, 2, 7, 7, 512]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  3 | Tensor<[1, 2, 7, 2, 7, 512]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  4 | Tensor<[1, 28, 28, 1024]> self = ?                                                                | Done     |
|  5 | Tensor<[1, 28, 28, 256]> self = ?                                                                 | Unknown  |
|  6 | Tensor<[1, 32, 49, 49]> self = ?                                                                  | Done     |
|  7 | Tensor<[1, 4, 4, 7, 7, 256]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  8 | Tensor<[1, 4, 7, 4, 7, 256]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  9 | Tensor<[1, 49, 1024]> self = ?                                                                    | Done     |
| 10 | Tensor<[1, 49, 32, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 11 | Tensor<[1, 56, 56, 128]> self = ?                                                                 | Unknown  |
| 12 | Tensor<[1, 56, 56, 512]> self = ?                                                                 | Done     |
| 13 | Tensor<[1, 7, 7, 1024]> self = ?                                                                  | Unknown  |
| 14 | Tensor<[1, 7, 7, 4096]> self = ?                                                                  | Done     |
| 15 | Tensor<[1, 8, 7, 8, 7, 128]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
| 16 | Tensor<[1, 8, 8, 7, 7, 128]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
| 17 | Tensor<[16, 49, 256]> self = ?                                                                    | Done     |
| 18 | Tensor<[16, 49, 49]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Unknown  |
| 19 | Tensor<[16, 49, 8, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 20 | Tensor<[16, 8, 32, 49]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 21 | Tensor<[16, 8, 49, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 22 | Tensor<[16, 8, 49, 49]> self = ?                                                                  | Done     |
| 23 | Tensor<[2, 2, 7, 7]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Done     |
| 24 | Tensor<[32, 49, 49]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Unknown  |
| 25 | Tensor<[4, 16, 32, 49]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 26 | Tensor<[4, 16, 49, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 27 | Tensor<[4, 16, 49, 49]> self = ?                                                                  | Done     |
| 28 | Tensor<[4, 4, 7, 7]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Done     |
| 29 | Tensor<[4, 49, 16, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 30 | Tensor<[4, 49, 49]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format          | Unknown  |
| 31 | Tensor<[4, 49, 512]> self = ?                                                                     | Done     |
| 32 | Tensor<[64, 4, 32, 49]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 33 | Tensor<[64, 4, 49, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 34 | Tensor<[64, 4, 49, 49]> self = ?                                                                  | Done     |
| 35 | Tensor<[64, 49, 128]> self = ?                                                                    | Done     |
| 36 | Tensor<[64, 49, 4, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 37 | Tensor<[8, 49, 49]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format          | Unknown  |
| 38 | Tensor<[8, 8, 7, 7]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Done     |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 14, 512]> self = ?,<br>List[int]<> pad = [0, 0, 0, 0, 0, 0],<br>number<> value = 0.0 | Done     |
|  1 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int]<> pad = [0, 0, 0, 0, 0, 0],<br>number<> value = 0.0 | Done     |
|  2 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int]<> pad = [0, 0, 0, 0, 0, 0],<br>number<> value = 0.0 | Done     |
|  3 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int]<> pad = [0, 0, 0, 0, 0, 0],<br>number<> value = 0.0  | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                       | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[128, 3, 4, 4]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int]<> stride = [4, 4],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Unknown  |
### aten.eq.Scalar
|    | ATen Input Variations                                | Status   |
|---:|:-----------------------------------------------------|:---------|
|  0 | Tensor<[16, 49, 49]> self = ?,<br>number<> other = 0 | Unknown  |
|  1 | Tensor<[4, 49, 49]> self = ?,<br>number<> other = 0  | Unknown  |
|  2 | Tensor<[64, 49, 49]> self = ?,<br>number<> other = 0 | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 32, 49]> self = ?,<br>List[int]<> size = [1, 32, 32, 49] | Unknown  |
|  1 | Tensor<[1, 32, 49, 32]> self = ?,<br>List[int]<> size = [1, 32, 49, 32] | Unknown  |
|  2 | Tensor<[1, 32, 49, 49]> self = ?,<br>List[int]<> size = [1, 32, 49, 49] | Unknown  |
|  3 | Tensor<[16, 8, 32, 49]> self = ?,<br>List[int]<> size = [16, 8, 32, 49] | Unknown  |
|  4 | Tensor<[16, 8, 49, 32]> self = ?,<br>List[int]<> size = [16, 8, 49, 32] | Unknown  |
|  5 | Tensor<[16, 8, 49, 49]> self = ?,<br>List[int]<> size = [16, 8, 49, 49] | Unknown  |
|  6 | Tensor<[4, 16, 32, 49]> self = ?,<br>List[int]<> size = [4, 16, 32, 49] | Unknown  |
|  7 | Tensor<[4, 16, 49, 32]> self = ?,<br>List[int]<> size = [4, 16, 49, 32] | Unknown  |
|  8 | Tensor<[4, 16, 49, 49]> self = ?,<br>List[int]<> size = [4, 16, 49, 49] | Unknown  |
|  9 | Tensor<[64, 4, 32, 49]> self = ?,<br>List[int]<> size = [64, 4, 32, 49] | Unknown  |
| 10 | Tensor<[64, 4, 49, 32]> self = ?,<br>List[int]<> size = [64, 4, 49, 32] | Unknown  |
| 11 | Tensor<[64, 4, 49, 49]> self = ?,<br>List[int]<> size = [64, 4, 49, 49] | Unknown  |
### aten.gelu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 14, 14, 2048]> self = ? | Done     |
|  1 | Tensor<[1, 28, 28, 1024]> self = ? | Done     |
|  2 | Tensor<[1, 56, 56, 512]> self = ?  | Done     |
|  3 | Tensor<[1, 7, 7, 4096]> self = ?   | Done     |
### aten.index.Tensor
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[169, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([2401])'] | Unknown  |
|  1 | Tensor<[169, 32]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([2401])'] | Unknown  |
|  2 | Tensor<[169, 4]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([2401])']  | Unknown  |
|  3 | Tensor<[169, 8]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([2401])']  | Unknown  |
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
|    | ATen Input Variations                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Optional[List[int]]<> dim = [-1, -2],<br>bool<> keepdim = True | Done     |
### aten.mm.default
|    | ATen Input Variations                                         | Status   |
|---:|:--------------------------------------------------------------|:---------|
|  0 | Tensor<[196, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ? | Done     |
|  1 | Tensor<[49, 2048]> self = ?,<br>Tensor<[2048, 1024]> mat2 = ? | Done     |
|  2 | Tensor<[784, 512]> self = ?,<br>Tensor<[512, 256]> mat2 = ?   | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 49, 32]> self = ?,<br>Tensor<> other = 0.1767766952966369 | Done     |
|  1 | Tensor<[16, 8, 49, 32]> self = ?,<br>Tensor<> other = 0.1767766952966369 | Done     |
|  2 | Tensor<[4, 16, 49, 32]> self = ?,<br>Tensor<> other = 0.1767766952966369 | Done     |
|  3 | Tensor<[64, 4, 49, 32]> self = ?,<br>Tensor<> other = 0.1767766952966369 | Done     |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                               | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 14, 1024]> input = ?,<br>List[int]<> normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float<> eps = 1e-05 | Done     |
|  1 | Tensor<[1, 14, 14, 512]> input = ?,<br>List[int]<> normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float<> eps = 1e-05     | Done     |
|  2 | Tensor<[1, 28, 28, 256]> input = ?,<br>List[int]<> normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float<> eps = 1e-05     | Done     |
|  3 | Tensor<[1, 28, 28, 512]> input = ?,<br>List[int]<> normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float<> eps = 1e-05     | Done     |
|  4 | Tensor<[1, 56, 56, 128]> input = ?,<br>List[int]<> normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float<> eps = 1e-05     | Done     |
|  5 | Tensor<[1, 7, 7, 1024]> input = ?,<br>List[int]<> normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float<> eps = 1e-05   | Done     |
|  6 | Tensor<[1, 7, 7, 2048]> input = ?,<br>List[int]<> normalized_shape = [2048],<br>Optional[Tensor]<[2048]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>float<> eps = 1e-05   | Done     |
### aten.ne.Scalar
|    | ATen Input Variations                                | Status   |
|---:|:-----------------------------------------------------|:---------|
|  0 | Tensor<[16, 49, 49]> self = ?,<br>number<> other = 0 | Unknown  |
|  1 | Tensor<[4, 49, 49]> self = ?,<br>number<> other = 0  | Unknown  |
|  2 | Tensor<[64, 49, 49]> self = ?,<br>number<> other = 0 | Unknown  |
### aten.new_zeros.default
|    | ATen Input Variations                                                                                  | Status   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 49, 256]> self = ?,<br>List[int]<> size = [28, 28],<br>Optional[bool]<> pin_memory = False | Unknown  |
|  1 | Tensor<[4, 49, 512]> self = ?,<br>List[int]<> size = [14, 14],<br>Optional[bool]<> pin_memory = False  | Unknown  |
|  2 | Tensor<[64, 49, 128]> self = ?,<br>List[int]<> size = [56, 56],<br>Optional[bool]<> pin_memory = False | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                                            | Status   |
|---:|:---------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 7, 7, 1024]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5] | Done     |
|  1 | Tensor<[1, 1, 7, 1, 7, 1024]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5] | Done     |
|  2 | Tensor<[1, 128, 56, 56]> self = ?,<br>List[int]<> dims = [0, 2, 3, 1]            | Done     |
|  3 | Tensor<[1, 2, 2, 7, 7, 512]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5]  | Done     |
|  4 | Tensor<[1, 2, 7, 2, 7, 512]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5]  | Done     |
|  5 | Tensor<[1, 4, 4, 7, 7, 256]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5]  | Done     |
|  6 | Tensor<[1, 4, 7, 4, 7, 256]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5]  | Done     |
|  7 | Tensor<[1, 49, 3, 32, 32]> self = ?,<br>List[int]<> dims = [2, 0, 3, 1, 4]       | Done     |
|  8 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int]<> dims = [0, 3, 1, 2]             | Done     |
|  9 | Tensor<[1, 8, 7, 8, 7, 128]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5]  | Done     |
| 10 | Tensor<[1, 8, 8, 7, 7, 128]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5]  | Done     |
| 11 | Tensor<[16, 49, 3, 8, 32]> self = ?,<br>List[int]<> dims = [2, 0, 3, 1, 4]       | Done     |
| 12 | Tensor<[2, 7, 2, 7]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]                | Done     |
| 13 | Tensor<[4, 49, 3, 16, 32]> self = ?,<br>List[int]<> dims = [2, 0, 3, 1, 4]       | Done     |
| 14 | Tensor<[4, 7, 4, 7]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]                | Done     |
| 15 | Tensor<[49, 49, 16]> self = ?,<br>List[int]<> dims = [2, 0, 1]                   | Done     |
| 16 | Tensor<[49, 49, 32]> self = ?,<br>List[int]<> dims = [2, 0, 1]                   | Done     |
| 17 | Tensor<[49, 49, 4]> self = ?,<br>List[int]<> dims = [2, 0, 1]                    | Done     |
| 18 | Tensor<[49, 49, 8]> self = ?,<br>List[int]<> dims = [2, 0, 1]                    | Done     |
| 19 | Tensor<[64, 49, 3, 4, 32]> self = ?,<br>List[int]<> dims = [2, 0, 3, 1, 4]       | Done     |
| 20 | Tensor<[8, 7, 8, 7]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]                | Done     |
### aten.roll.default
|    | ATen Input Variations                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 14, 512]> self = ?,<br>List[int]<> shifts = [-3, -3],<br>List[int]<> dims = [1, 2] | Unknown  |
|  1 | Tensor<[1, 14, 14, 512]> self = ?,<br>List[int]<> shifts = [3, 3],<br>List[int]<> dims = [1, 2]   | Unknown  |
|  2 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int]<> shifts = [-3, -3],<br>List[int]<> dims = [1, 2] | Unknown  |
|  3 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int]<> shifts = [3, 3],<br>List[int]<> dims = [1, 2]   | Unknown  |
|  4 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int]<> shifts = [-3, -3],<br>List[int]<> dims = [1, 2] | Unknown  |
|  5 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int]<> shifts = [3, 3],<br>List[int]<> dims = [1, 2]   | Unknown  |
### aten.select.int
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 1, 32, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | Unknown  |
|  1 | Tensor<[3, 1, 32, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 1 | Unknown  |
|  2 | Tensor<[3, 1, 32, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 2 | Unknown  |
|  3 | Tensor<[3, 16, 8, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | Unknown  |
|  4 | Tensor<[3, 16, 8, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 1 | Unknown  |
|  5 | Tensor<[3, 16, 8, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 2 | Unknown  |
|  6 | Tensor<[3, 4, 16, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | Unknown  |
|  7 | Tensor<[3, 4, 16, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 1 | Unknown  |
|  8 | Tensor<[3, 4, 16, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 2 | Unknown  |
|  9 | Tensor<[3, 64, 4, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | Unknown  |
| 10 | Tensor<[3, 64, 4, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 1 | Unknown  |
| 11 | Tensor<[3, 64, 4, 49, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 2 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                             | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 14, 256]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
|  1 | Tensor<[1, 14, 14, 512]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
|  2 | Tensor<[1, 14, 14, 512]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
|  3 | Tensor<[1, 14, 14, 512]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
|  4 | Tensor<[1, 14, 14, 512]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
|  5 | Tensor<[1, 14, 28, 256]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
|  6 | Tensor<[1, 14, 28, 256]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
|  7 | Tensor<[1, 28, 28, 128]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
|  8 | Tensor<[1, 28, 28, 256]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
|  9 | Tensor<[1, 28, 28, 256]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
| 10 | Tensor<[1, 28, 28, 256]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
| 11 | Tensor<[1, 28, 28, 256]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
| 12 | Tensor<[1, 28, 56, 128]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
| 13 | Tensor<[1, 28, 56, 128]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
| 14 | Tensor<[1, 56, 56, 128]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
| 15 | Tensor<[1, 56, 56, 128]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
| 16 | Tensor<[1, 56, 56, 128]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
| 17 | Tensor<[1, 56, 56, 128]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
| 18 | Tensor<[1, 7, 14, 512]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2  | Unknown  |
| 19 | Tensor<[1, 7, 14, 512]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2  | Unknown  |
| 20 | Tensor<[1, 7, 7, 1024]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                     | Unknown  |
| 21 | Tensor<[1, 7, 7, 1024]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                     | Unknown  |
| 22 | Tensor<[1, 7, 7, 512]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                      | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 1, 49]> self = ?,<br>Tensor<[16, 49, 1]> other = ? | Done     |
|  1 | Tensor<[4, 1, 49]> self = ?,<br>Tensor<[4, 49, 1]> other = ?   | Done     |
|  2 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ? | Done     |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1000, 1024]> self = ? | Done     |
|  1 | Tensor<[1024, 1024]> self = ? | Done     |
|  2 | Tensor<[1024, 2048]> self = ? | Done     |
|  3 | Tensor<[1024, 256]> self = ?  | Done     |
|  4 | Tensor<[1024, 4096]> self = ? | Done     |
|  5 | Tensor<[128, 128]> self = ?   | Done     |
|  6 | Tensor<[128, 512]> self = ?   | Done     |
|  7 | Tensor<[1536, 512]> self = ?  | Done     |
|  8 | Tensor<[2048, 512]> self = ?  | Done     |
|  9 | Tensor<[256, 1024]> self = ?  | Done     |
| 10 | Tensor<[256, 256]> self = ?   | Done     |
| 11 | Tensor<[256, 512]> self = ?   | Done     |
| 12 | Tensor<[3072, 1024]> self = ? | Done     |
| 13 | Tensor<[384, 128]> self = ?   | Done     |
| 14 | Tensor<[4096, 1024]> self = ? | Done     |
| 15 | Tensor<[512, 1024]> self = ?  | Done     |
| 16 | Tensor<[512, 128]> self = ?   | Done     |
| 17 | Tensor<[512, 2048]> self = ?  | Done     |
| 18 | Tensor<[512, 512]> self = ?   | Done     |
| 19 | Tensor<[768, 256]> self = ?   | Done     |
### aten.transpose.int
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 49, 32]> self = ?,<br>int<> dim0 = -2,<br>int<> dim1 = -1 | Done     |
|  1 | Tensor<[1, 32, 49, 32]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
|  2 | Tensor<[16, 8, 49, 32]> self = ?,<br>int<> dim0 = -2,<br>int<> dim1 = -1 | Done     |
|  3 | Tensor<[16, 8, 49, 32]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
|  4 | Tensor<[4, 16, 49, 32]> self = ?,<br>int<> dim0 = -2,<br>int<> dim1 = -1 | Done     |
|  5 | Tensor<[4, 16, 49, 32]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
|  6 | Tensor<[64, 4, 49, 32]> self = ?,<br>int<> dim0 = -2,<br>int<> dim1 = -1 | Done     |
|  7 | Tensor<[64, 4, 49, 32]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[16, 1, 49, 49]> self = ?,<br>int<> dim = 0 | Done     |
|  1 | Tensor<[16, 49, 49]> self = ?,<br>int<> dim = 0    | Done     |
|  2 | Tensor<[16, 49, 49]> self = ?,<br>int<> dim = 1    | Done     |
|  3 | Tensor<[16, 49]> self = ?,<br>int<> dim = 1        | Done     |
|  4 | Tensor<[16, 49]> self = ?,<br>int<> dim = 2        | Unknown  |
|  5 | Tensor<[32, 49, 49]> self = ?,<br>int<> dim = 0    | Done     |
|  6 | Tensor<[4, 1, 49, 49]> self = ?,<br>int<> dim = 0  | Done     |
|  7 | Tensor<[4, 49, 49]> self = ?,<br>int<> dim = 0     | Done     |
|  8 | Tensor<[4, 49, 49]> self = ?,<br>int<> dim = 1     | Done     |
|  9 | Tensor<[4, 49]> self = ?,<br>int<> dim = 1         | Done     |
| 10 | Tensor<[4, 49]> self = ?,<br>int<> dim = 2         | Unknown  |
| 11 | Tensor<[64, 1, 49, 49]> self = ?,<br>int<> dim = 0 | Done     |
| 12 | Tensor<[64, 49, 49]> self = ?,<br>int<> dim = 1    | Done     |
| 13 | Tensor<[64, 49]> self = ?,<br>int<> dim = 1        | Done     |
| 14 | Tensor<[64, 49]> self = ?,<br>int<> dim = 2        | Unknown  |
| 15 | Tensor<[8, 49, 49]> self = ?,<br>int<> dim = 0     | Done     |
### aten.view.default
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 7, 7, 1024]> self = ?,<br>List[int]<> size = [1, 49, 1024]   | Unknown  |
|  1 | Tensor<[1, 1, 7, 1, 7, 1024]> self = ?,<br>List[int]<> size = [1, 7, 7, 1024] | Unknown  |
|  2 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int]<> size = [1, 1024]             | Unknown  |
|  3 | Tensor<[1, 14, 14, 1024]> self = ?,<br>List[int]<> size = [196, 1024]         | Unknown  |
|  4 | Tensor<[1, 14, 14, 2048]> self = ?,<br>List[int]<> size = [196, 2048]         | Unknown  |
|  5 | Tensor<[1, 14, 14, 512]> self = ?,<br>List[int]<> size = [1, 2, 7, 2, 7, 512] | Unknown  |
|  6 | Tensor<[1, 14, 14, 512]> self = ?,<br>List[int]<> size = [196, 512]           | Unknown  |
|  7 | Tensor<[1, 16, 8, 49, 49]> self = ?,<br>List[int]<> size = [-1, 8, 49, 49]    | Unknown  |
|  8 | Tensor<[1, 28, 28, 1024]> self = ?,<br>List[int]<> size = [784, 1024]         | Unknown  |
|  9 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int]<> size = [1, 4, 7, 4, 7, 256] | Unknown  |
| 10 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int]<> size = [784, 256]           | Unknown  |
| 11 | Tensor<[1, 28, 28, 512]> self = ?,<br>List[int]<> size = [784, 512]           | Unknown  |
| 12 | Tensor<[1, 32, 32, 49]> self = ?,<br>List[int]<> size = [32, 32, 49]          | Unknown  |
| 13 | Tensor<[1, 32, 49, 32]> self = ?,<br>List[int]<> size = [32, 49, 32]          | Unknown  |
| 14 | Tensor<[1, 32, 49, 49]> self = ?,<br>List[int]<> size = [32, 49, 49]          | Unknown  |
| 15 | Tensor<[1, 4, 16, 49, 49]> self = ?,<br>List[int]<> size = [-1, 16, 49, 49]   | Unknown  |
| 16 | Tensor<[1, 49, 1024]> self = ?,<br>List[int]<> size = [1, 1, 1, 7, 7, 1024]   | Unknown  |
| 17 | Tensor<[1, 49, 1024]> self = ?,<br>List[int]<> size = [49, 1024]              | Unknown  |
| 18 | Tensor<[1, 49, 3072]> self = ?,<br>List[int]<> size = [1, 49, 3, 32, 32]      | Unknown  |
| 19 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int]<> size = [1, 8, 7, 8, 7, 128] | Unknown  |
| 20 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int]<> size = [3136, 128]          | Unknown  |
| 21 | Tensor<[1, 56, 56, 512]> self = ?,<br>List[int]<> size = [3136, 512]          | Unknown  |
| 22 | Tensor<[1, 64, 4, 49, 49]> self = ?,<br>List[int]<> size = [-1, 4, 49, 49]    | Unknown  |
| 23 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int]<> size = [1, 1, 7, 1, 7, 1024] | Unknown  |
| 24 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int]<> size = [49, 1024]            | Unknown  |
| 25 | Tensor<[1, 7, 7, 2048]> self = ?,<br>List[int]<> size = [49, 2048]            | Unknown  |
| 26 | Tensor<[1, 7, 7, 4096]> self = ?,<br>List[int]<> size = [49, 4096]            | Unknown  |
| 27 | Tensor<[128, 49, 32]> self = ?,<br>List[int]<> size = [16, 8, 49, 32]         | Unknown  |
| 28 | Tensor<[128, 49, 49]> self = ?,<br>List[int]<> size = [16, 8, 49, 49]         | Unknown  |
| 29 | Tensor<[14, 14]> self = ?,<br>List[int]<> size = [2, 7, 2, 7]                 | Unknown  |
| 30 | Tensor<[16, 49, 256]> self = ?,<br>List[int]<> size = [1, 4, 4, 7, 7, 256]    | Unknown  |
| 31 | Tensor<[16, 49, 256]> self = ?,<br>List[int]<> size = [784, 256]              | Unknown  |
| 32 | Tensor<[16, 49, 768]> self = ?,<br>List[int]<> size = [16, 49, 3, 8, 32]      | Unknown  |
| 33 | Tensor<[16, 8, 49, 49]> self = ?,<br>List[int]<> size = [1, 16, 8, 49, 49]    | Unknown  |
| 34 | Tensor<[16, 8, 49, 49]> self = ?,<br>List[int]<> size = [128, 49, 49]         | Unknown  |
| 35 | Tensor<[196, 1536]> self = ?,<br>List[int]<> size = [4, 49, 1536]             | Unknown  |
| 36 | Tensor<[196, 2048]> self = ?,<br>List[int]<> size = [1, 14, 14, 2048]         | Unknown  |
| 37 | Tensor<[196, 512]> self = ?,<br>List[int]<> size = [1, 14, 14, 512]           | Unknown  |
| 38 | Tensor<[196, 512]> self = ?,<br>List[int]<> size = [4, 49, 512]               | Unknown  |
| 39 | Tensor<[2401, 16]> self = ?,<br>List[int]<> size = [49, 49, -1]               | Unknown  |
| 40 | Tensor<[2401, 32]> self = ?,<br>List[int]<> size = [49, 49, -1]               | Unknown  |
| 41 | Tensor<[2401, 4]> self = ?,<br>List[int]<> size = [49, 49, -1]                | Unknown  |
| 42 | Tensor<[2401, 8]> self = ?,<br>List[int]<> size = [49, 49, -1]                | Unknown  |
| 43 | Tensor<[256, 49, 32]> self = ?,<br>List[int]<> size = [64, 4, 49, 32]         | Unknown  |
| 44 | Tensor<[256, 49, 49]> self = ?,<br>List[int]<> size = [64, 4, 49, 49]         | Unknown  |
| 45 | Tensor<[28, 28]> self = ?,<br>List[int]<> size = [4, 7, 4, 7]                 | Unknown  |
| 46 | Tensor<[3136, 128]> self = ?,<br>List[int]<> size = [1, 56, 56, 128]          | Unknown  |
| 47 | Tensor<[3136, 128]> self = ?,<br>List[int]<> size = [64, 49, 128]             | Unknown  |
| 48 | Tensor<[3136, 384]> self = ?,<br>List[int]<> size = [64, 49, 384]             | Unknown  |
| 49 | Tensor<[3136, 512]> self = ?,<br>List[int]<> size = [1, 56, 56, 512]          | Unknown  |
| 50 | Tensor<[32, 49, 32]> self = ?,<br>List[int]<> size = [1, 32, 49, 32]          | Unknown  |
| 51 | Tensor<[32, 49, 49]> self = ?,<br>List[int]<> size = [1, 32, 49, 49]          | Unknown  |
| 52 | Tensor<[4, 16, 49, 49]> self = ?,<br>List[int]<> size = [1, 4, 16, 49, 49]    | Unknown  |
| 53 | Tensor<[4, 16, 49, 49]> self = ?,<br>List[int]<> size = [64, 49, 49]          | Unknown  |
| 54 | Tensor<[4, 49, 1536]> self = ?,<br>List[int]<> size = [4, 49, 3, 16, 32]      | Unknown  |
| 55 | Tensor<[4, 49, 512]> self = ?,<br>List[int]<> size = [1, 2, 2, 7, 7, 512]     | Unknown  |
| 56 | Tensor<[4, 49, 512]> self = ?,<br>List[int]<> size = [196, 512]               | Unknown  |
| 57 | Tensor<[49, 1024]> self = ?,<br>List[int]<> size = [1, 49, 1024]              | Unknown  |
| 58 | Tensor<[49, 1024]> self = ?,<br>List[int]<> size = [1, 7, 7, 1024]            | Unknown  |
| 59 | Tensor<[49, 3072]> self = ?,<br>List[int]<> size = [1, 49, 3072]              | Unknown  |
| 60 | Tensor<[49, 4096]> self = ?,<br>List[int]<> size = [1, 7, 7, 4096]            | Unknown  |
| 61 | Tensor<[56, 56]> self = ?,<br>List[int]<> size = [8, 7, 8, 7]                 | Unknown  |
| 62 | Tensor<[64, 4, 49, 49]> self = ?,<br>List[int]<> size = [1, 64, 4, 49, 49]    | Unknown  |
| 63 | Tensor<[64, 4, 49, 49]> self = ?,<br>List[int]<> size = [256, 49, 49]         | Unknown  |
| 64 | Tensor<[64, 49, 128]> self = ?,<br>List[int]<> size = [1, 8, 8, 7, 7, 128]    | Unknown  |
| 65 | Tensor<[64, 49, 128]> self = ?,<br>List[int]<> size = [3136, 128]             | Unknown  |
| 66 | Tensor<[64, 49, 32]> self = ?,<br>List[int]<> size = [4, 16, 49, 32]          | Unknown  |
| 67 | Tensor<[64, 49, 384]> self = ?,<br>List[int]<> size = [64, 49, 3, 4, 32]      | Unknown  |
| 68 | Tensor<[64, 49, 49]> self = ?,<br>List[int]<> size = [4, 16, 49, 49]          | Unknown  |
| 69 | Tensor<[784, 1024]> self = ?,<br>List[int]<> size = [1, 28, 28, 1024]         | Unknown  |
| 70 | Tensor<[784, 256]> self = ?,<br>List[int]<> size = [1, 28, 28, 256]           | Unknown  |
| 71 | Tensor<[784, 256]> self = ?,<br>List[int]<> size = [16, 49, 256]              | Unknown  |
| 72 | Tensor<[784, 768]> self = ?,<br>List[int]<> size = [16, 49, 768]              | Unknown  |

