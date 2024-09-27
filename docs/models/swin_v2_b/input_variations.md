# High Level Operations Status
|    | Operations                      |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Generality Score |
|---:|:--------------------------------|-------------------:|------------:|----------:|-----------:|:------------|-------------------:|
|  0 | aten._softmax.default           |                  4 |           4 |         0 |          0 | ✅          |               1    |
|  1 | aten._unsafe_view.default       |                 19 |           0 |         0 |          0 | ✘           |               0    |
|  2 | aten.add.Tensor                 |                 11 |          11 |         0 |          0 | ✅          |               1    |
|  3 | aten.addmm.default              |                 18 |          18 |         0 |          0 | ✅          |               1    |
|  4 | aten.as_strided.default         |                  1 |           0 |         0 |          0 | ✘           |               0    |
|  5 | aten.bmm.default                |                  8 |           8 |         0 |          0 | ✅          |               1    |
|  6 | aten.cat.default                |                  3 |           0 |         0 |          0 | ✘           |               0    |
|  7 | aten.clamp.default              |                  4 |           4 |         0 |          0 | ✅          |               1    |
|  8 | aten.clamp_min.default          |                  4 |           0 |         0 |          0 | ✘           |               0    |
|  9 | aten.clone.default              |                 38 |          38 |         0 |          0 | ✅          |               1    |
| 10 | aten.constant_pad_nd.default    |                  4 |           4 |         0 |          0 | ✅          |               1    |
| 11 | aten.convolution.default        |                  1 |           0 |         0 |          0 | ✘           |               0    |
| 12 | aten.div.Tensor                 |                  4 |           4 |         0 |          0 | ✅          |               1    |
| 13 | aten.eq.Scalar                  |                  3 |           3 |         0 |          0 | ✅          |               1    |
| 14 | aten.exp.default                |                  4 |           4 |         0 |          0 | ✅          |               1    |
| 15 | aten.expand.default             |                 16 |           0 |         0 |          0 | ✘           |               0    |
| 16 | aten.gelu.default               |                  4 |           4 |         0 |          0 | ✅          |               1    |
| 17 | aten.index.Tensor               |                  4 |           0 |         0 |          0 | ✘           |               0    |
| 18 | aten.linalg_vector_norm.default |                  4 |           0 |         0 |          0 | ✘           |               0    |
| 19 | aten.masked_fill.Scalar         |                  6 |           0 |         0 |          0 | ✘           |               0    |
| 20 | aten.mean.dim                   |                  1 |           1 |         0 |          0 | ✅          |               1    |
| 21 | aten.mm.default                 |                  7 |           7 |         0 |          0 | ✅          |               1    |
| 22 | aten.mul.Tensor                 |                  8 |           8 |         0 |          0 | ✅          |               1    |
| 23 | aten.native_layer_norm.default  |                  4 |           4 |         0 |          0 | ✅          |               1    |
| 24 | aten.ne.Scalar                  |                  3 |           3 |         0 |          0 | ✅          |               1    |
| 25 | aten.new_zeros.default          |                  3 |           0 |         0 |          0 | ✘           |               0    |
| 26 | aten.permute.default            |                 20 |          20 |         0 |          0 | ✅          |               1    |
| 27 | aten.relu.default               |                  1 |           1 |         0 |          0 | ✅          |               1    |
| 28 | aten.roll.default               |                  6 |           0 |         0 |          0 | ✘           |               0    |
| 29 | aten.select.int                 |                 12 |           0 |         0 |          0 | ✘           |               0    |
| 30 | aten.sigmoid.default            |                  4 |           4 |         0 |          0 | ✅          |               1    |
| 31 | aten.slice.Tensor               |                 23 |           0 |         0 |          0 | ✘           |               0    |
| 32 | aten.sub.Tensor                 |                  3 |           3 |         0 |          0 | ✅          |               1    |
| 33 | aten.t.default                  |                 25 |          25 |         0 |          0 | ✅          |               1    |
| 34 | aten.transpose.int              |                  8 |           8 |         0 |          0 | ✅          |               1    |
| 35 | aten.unsqueeze.default          |                 16 |          13 |         0 |          0 | 🚧          |               0.81 |
| 36 | aten.view.default               |                 84 |           8 |         0 |         76 | 🚧          |               0.1  |
***
### aten._softmax.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 64, 64]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Done     |
|  1 | Tensor<[16, 8, 64, 64]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Done     |
|  2 | Tensor<[4, 16, 64, 64]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Done     |
|  3 | Tensor<[64, 4, 64, 64]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Done     |
### aten._unsafe_view.default
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2, 2, 8, 8, 512]> self = ?,<br>List[int]<> size = [4, 64, 512]     | None     |
|  1 | Tensor<[1, 2, 8, 2, 8, 512]> self = ?,<br>List[int]<> size = [1, 16, 16, 512] | None     |
|  2 | Tensor<[1, 4, 4, 8, 8, 256]> self = ?,<br>List[int]<> size = [16, 64, 256]    | None     |
|  3 | Tensor<[1, 4, 8, 4, 8, 256]> self = ?,<br>List[int]<> size = [1, 32, 32, 256] | None     |
|  4 | Tensor<[1, 64, 32, 32]> self = ?,<br>List[int]<> size = [1, 64, 1024]         | None     |
|  5 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>List[int]<> size = [1, 64, 64, 128] | None     |
|  6 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>List[int]<> size = [64, 64, 128]    | None     |
|  7 | Tensor<[16, 64, 8, 32]> self = ?,<br>List[int]<> size = [16, 64, 256]         | None     |
|  8 | Tensor<[16, 8, 32, 64]> self = ?,<br>List[int]<> size = [128, 32, 64]         | None     |
|  9 | Tensor<[16, 8, 64, 32]> self = ?,<br>List[int]<> size = [128, 64, 32]         | None     |
| 10 | Tensor<[2, 2, 8, 8]> self = ?,<br>List[int]<> size = [4, 64]                  | None     |
| 11 | Tensor<[4, 16, 32, 64]> self = ?,<br>List[int]<> size = [64, 32, 64]          | None     |
| 12 | Tensor<[4, 16, 64, 32]> self = ?,<br>List[int]<> size = [64, 64, 32]          | None     |
| 13 | Tensor<[4, 4, 8, 8]> self = ?,<br>List[int]<> size = [16, 64]                 | None     |
| 14 | Tensor<[4, 64, 16, 32]> self = ?,<br>List[int]<> size = [4, 64, 512]          | None     |
| 15 | Tensor<[64, 4, 32, 64]> self = ?,<br>List[int]<> size = [256, 32, 64]         | None     |
| 16 | Tensor<[64, 4, 64, 32]> self = ?,<br>List[int]<> size = [256, 64, 32]         | None     |
| 17 | Tensor<[64, 64, 4, 32]> self = ?,<br>List[int]<> size = [64, 64, 128]         | None     |
| 18 | Tensor<[8, 8, 8, 8]> self = ?,<br>List[int]<> size = [64, 64]                 | None     |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   |
|---:|:-----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 512]> self = ?,<br>Tensor<[1, 16, 16, 512]> other = ?     | Done     |
|  1 | Tensor<[1, 16, 8, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ? | Done     |
|  2 | Tensor<[1, 32, 32, 256]> self = ?,<br>Tensor<[1, 32, 32, 256]> other = ?     | Done     |
|  3 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[1, 32, 64, 64]> other = ?       | Done     |
|  4 | Tensor<[1, 4, 16, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?  | Done     |
|  5 | Tensor<[1, 64, 4, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ? | Done     |
|  6 | Tensor<[1, 64, 64, 128]> self = ?,<br>Tensor<[1, 64, 64, 128]> other = ?     | Done     |
|  7 | Tensor<[1, 8, 8, 1024]> self = ?,<br>Tensor<[1, 8, 8, 1024]> other = ?       | Done     |
|  8 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[1, 8, 64, 64]> other = ?        | Done     |
|  9 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[1, 16, 64, 64]> other = ?       | Done     |
| 10 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[1, 4, 64, 64]> other = ?        | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1000]> mat2 = ?  | Done     |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[1024, 256]> mat1 = ?,<br>Tensor<[256, 1024]> mat2 = ? | Done     |
|  2 | Tensor<[1024]> self = ?,<br>Tensor<[64, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Done     |
|  3 | Tensor<[1024]> self = ?,<br>Tensor<[64, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Done     |
|  4 | Tensor<[128]> self = ?,<br>Tensor<[4096, 128]> mat1 = ?,<br>Tensor<[128, 128]> mat2 = ?   | Done     |
|  5 | Tensor<[128]> self = ?,<br>Tensor<[4096, 512]> mat1 = ?,<br>Tensor<[512, 128]> mat2 = ?   | Done     |
|  6 | Tensor<[1536]> self = ?,<br>Tensor<[256, 512]> mat1 = ?,<br>Tensor<[512, 1536]> mat2 = ?  | Done     |
|  7 | Tensor<[2048]> self = ?,<br>Tensor<[256, 512]> mat1 = ?,<br>Tensor<[512, 2048]> mat2 = ?  | Done     |
|  8 | Tensor<[256]> self = ?,<br>Tensor<[1024, 1024]> mat1 = ?,<br>Tensor<[1024, 256]> mat2 = ? | Done     |
|  9 | Tensor<[256]> self = ?,<br>Tensor<[1024, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?   | Done     |
| 10 | Tensor<[3072]> self = ?,<br>Tensor<[64, 1024]> mat1 = ?,<br>Tensor<[1024, 3072]> mat2 = ? | Done     |
| 11 | Tensor<[384]> self = ?,<br>Tensor<[4096, 128]> mat1 = ?,<br>Tensor<[128, 384]> mat2 = ?   | Done     |
| 12 | Tensor<[4096]> self = ?,<br>Tensor<[64, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Done     |
| 13 | Tensor<[512]> self = ?,<br>Tensor<[225, 2]> mat1 = ?,<br>Tensor<[2, 512]> mat2 = ?        | Done     |
| 14 | Tensor<[512]> self = ?,<br>Tensor<[256, 2048]> mat1 = ?,<br>Tensor<[2048, 512]> mat2 = ?  | Done     |
| 15 | Tensor<[512]> self = ?,<br>Tensor<[256, 512]> mat1 = ?,<br>Tensor<[512, 512]> mat2 = ?    | Done     |
| 16 | Tensor<[512]> self = ?,<br>Tensor<[4096, 128]> mat1 = ?,<br>Tensor<[128, 512]> mat2 = ?   | Done     |
| 17 | Tensor<[768]> self = ?,<br>Tensor<[1024, 256]> mat1 = ?,<br>Tensor<[256, 768]> mat2 = ?   | Done     |
### aten.as_strided.default
|    | ATen Input Variations                                                                                                  | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int]<> size = [1, 1024, 1, 1],<br>List[int]<> stride = [1024, 1, 1024, 1024] | None     |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[128, 64, 32]> self = ?,<br>Tensor<[128, 32, 64]> mat2 = ? | Done     |
|  1 | Tensor<[128, 64, 64]> self = ?,<br>Tensor<[128, 64, 32]> mat2 = ? | Done     |
|  2 | Tensor<[256, 64, 32]> self = ?,<br>Tensor<[256, 32, 64]> mat2 = ? | Done     |
|  3 | Tensor<[256, 64, 64]> self = ?,<br>Tensor<[256, 64, 32]> mat2 = ? | Done     |
|  4 | Tensor<[32, 64, 32]> self = ?,<br>Tensor<[32, 32, 64]> mat2 = ?   | Done     |
|  5 | Tensor<[32, 64, 64]> self = ?,<br>Tensor<[32, 64, 32]> mat2 = ?   | Done     |
|  6 | Tensor<[64, 64, 32]> self = ?,<br>Tensor<[64, 32, 64]> mat2 = ?   | Done     |
|  7 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 32]> mat2 = ?   | Done     |
### aten.cat.default
|    | ATen Input Variations                                                                                                                                                        | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([1, 16, 16, 256])', 'torch.Size([1, 16, 16, 256])', 'torch.Size([1, 16, 16, 256])', 'torch.Size([1, 16, 16, 256])'],<br>int<> dim = -1 | None     |
|  1 | List[Tensor]<> tensors = ['torch.Size([1, 32, 32, 128])', 'torch.Size([1, 32, 32, 128])', 'torch.Size([1, 32, 32, 128])', 'torch.Size([1, 32, 32, 128])'],<br>int<> dim = -1 | None     |
|  2 | List[Tensor]<> tensors = ['torch.Size([1, 8, 8, 512])', 'torch.Size([1, 8, 8, 512])', 'torch.Size([1, 8, 8, 512])', 'torch.Size([1, 8, 8, 512])'],<br>int<> dim = -1         | None     |
### aten.clamp.default
|    | ATen Input Variations                                                                                     | Status   |
|---:|:----------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 1, 1]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 4.605170185988092 | Done     |
|  1 | Tensor<[32, 1, 1]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 4.605170185988092 | Done     |
|  2 | Tensor<[4, 1, 1]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 4.605170185988092  | Done     |
|  3 | Tensor<[8, 1, 1]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 4.605170185988092  | Done     |
### aten.clamp_min.default
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 64, 1]> self = ?,<br>number<> min = 1e-12 | None     |
|  1 | Tensor<[16, 8, 64, 1]> self = ?,<br>number<> min = 1e-12 | None     |
|  2 | Tensor<[4, 16, 64, 1]> self = ?,<br>number<> min = 1e-12 | None     |
|  3 | Tensor<[64, 4, 64, 1]> self = ?,<br>number<> min = 1e-12 | None     |
### aten.clone.default
|    | ATen Input Variations                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 2048]> self = ?                                                                | Done     |
|  1 | Tensor<[1, 16, 16, 512]> self = ?                                                                 | Done     |
|  2 | Tensor<[1, 2, 2, 8, 8, 512]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  3 | Tensor<[1, 2, 8, 2, 8, 512]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  4 | Tensor<[1, 32, 32, 1024]> self = ?                                                                | Done     |
|  5 | Tensor<[1, 32, 32, 256]> self = ?                                                                 | Done     |
|  6 | Tensor<[1, 32, 64, 64]> self = ?                                                                  | Done     |
|  7 | Tensor<[1, 4, 4, 8, 8, 256]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  8 | Tensor<[1, 4, 8, 4, 8, 256]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  9 | Tensor<[1, 64, 1024]> self = ?                                                                    | Done     |
| 10 | Tensor<[1, 64, 32, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 11 | Tensor<[1, 64, 64, 128]> self = ?                                                                 | Done     |
| 12 | Tensor<[1, 64, 64, 512]> self = ?                                                                 | Done     |
| 13 | Tensor<[1, 8, 8, 1024]> self = ?                                                                  | Done     |
| 14 | Tensor<[1, 8, 8, 4096]> self = ?                                                                  | Done     |
| 15 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
| 16 | Tensor<[16, 64, 256]> self = ?                                                                    | Done     |
| 17 | Tensor<[16, 64, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Done     |
| 18 | Tensor<[16, 64, 8, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 19 | Tensor<[16, 8, 32, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 20 | Tensor<[16, 8, 64, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 21 | Tensor<[16, 8, 64, 64]> self = ?                                                                  | Done     |
| 22 | Tensor<[2, 2, 8, 8]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Done     |
| 23 | Tensor<[32, 64, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Done     |
| 24 | Tensor<[4, 16, 32, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 25 | Tensor<[4, 16, 64, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 26 | Tensor<[4, 16, 64, 64]> self = ?                                                                  | Done     |
| 27 | Tensor<[4, 4, 8, 8]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Done     |
| 28 | Tensor<[4, 64, 16, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 29 | Tensor<[4, 64, 512]> self = ?                                                                     | Done     |
| 30 | Tensor<[4, 64, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format          | Done     |
| 31 | Tensor<[64, 4, 32, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 32 | Tensor<[64, 4, 64, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 33 | Tensor<[64, 4, 64, 64]> self = ?                                                                  | Done     |
| 34 | Tensor<[64, 64, 128]> self = ?                                                                    | Done     |
| 35 | Tensor<[64, 64, 4, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Done     |
| 36 | Tensor<[8, 64, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format          | Done     |
| 37 | Tensor<[8, 8, 8, 8]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Done     |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int]<> pad = [0, 0, 0, 0, 0, 0],<br>number<> value = 0.0 | Done     |
|  1 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int]<> pad = [0, 0, 0, 0, 0, 0],<br>number<> value = 0.0 | Done     |
|  2 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int]<> pad = [0, 0, 0, 0, 0, 0],<br>number<> value = 0.0 | Done     |
|  3 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int]<> pad = [0, 0, 0, 0, 0, 0],<br>number<> value = 0.0  | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                       | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 256, 256]> input = ?,<br>Tensor<[128, 3, 4, 4]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int]<> stride = [4, 4],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | None     |
### aten.div.Tensor
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 64, 32]> self = ?,<br>Tensor<[1, 32, 64, 32]> other = ? | Done     |
|  1 | Tensor<[16, 8, 64, 32]> self = ?,<br>Tensor<[16, 8, 64, 32]> other = ? | Done     |
|  2 | Tensor<[4, 16, 64, 32]> self = ?,<br>Tensor<[4, 16, 64, 32]> other = ? | Done     |
|  3 | Tensor<[64, 4, 64, 32]> self = ?,<br>Tensor<[64, 4, 64, 32]> other = ? | Done     |
### aten.eq.Scalar
|    | ATen Input Variations                                | Status   |
|---:|:-----------------------------------------------------|:---------|
|  0 | Tensor<[16, 64, 64]> self = ?,<br>number<> other = 0 | Done     |
|  1 | Tensor<[4, 64, 64]> self = ?,<br>number<> other = 0  | Done     |
|  2 | Tensor<[64, 64, 64]> self = ?,<br>number<> other = 0 | Done     |
### aten.exp.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[16, 1, 1]> self = ? | Done     |
|  1 | Tensor<[32, 1, 1]> self = ? | Done     |
|  2 | Tensor<[4, 1, 1]> self = ?  | Done     |
|  3 | Tensor<[8, 1, 1]> self = ?  | Done     |
### aten.expand.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 32, 64]> self = ?,<br>List[int]<> size = [1, 32, 32, 64] | Unknown  |
|  1 | Tensor<[1, 32, 64, 1]> self = ?,<br>List[int]<> size = [1, 32, 64, 32]  | None     |
|  2 | Tensor<[1, 32, 64, 32]> self = ?,<br>List[int]<> size = [1, 32, 64, 32] | Unknown  |
|  3 | Tensor<[1, 32, 64, 64]> self = ?,<br>List[int]<> size = [1, 32, 64, 64] | Unknown  |
|  4 | Tensor<[16, 8, 32, 64]> self = ?,<br>List[int]<> size = [16, 8, 32, 64] | Unknown  |
|  5 | Tensor<[16, 8, 64, 1]> self = ?,<br>List[int]<> size = [16, 8, 64, 32]  | None     |
|  6 | Tensor<[16, 8, 64, 32]> self = ?,<br>List[int]<> size = [16, 8, 64, 32] | Unknown  |
|  7 | Tensor<[16, 8, 64, 64]> self = ?,<br>List[int]<> size = [16, 8, 64, 64] | Unknown  |
|  8 | Tensor<[4, 16, 32, 64]> self = ?,<br>List[int]<> size = [4, 16, 32, 64] | Unknown  |
|  9 | Tensor<[4, 16, 64, 1]> self = ?,<br>List[int]<> size = [4, 16, 64, 32]  | None     |
| 10 | Tensor<[4, 16, 64, 32]> self = ?,<br>List[int]<> size = [4, 16, 64, 32] | Unknown  |
| 11 | Tensor<[4, 16, 64, 64]> self = ?,<br>List[int]<> size = [4, 16, 64, 64] | Unknown  |
| 12 | Tensor<[64, 4, 32, 64]> self = ?,<br>List[int]<> size = [64, 4, 32, 64] | Unknown  |
| 13 | Tensor<[64, 4, 64, 1]> self = ?,<br>List[int]<> size = [64, 4, 64, 32]  | None     |
| 14 | Tensor<[64, 4, 64, 32]> self = ?,<br>List[int]<> size = [64, 4, 64, 32] | Unknown  |
| 15 | Tensor<[64, 4, 64, 64]> self = ?,<br>List[int]<> size = [64, 4, 64, 64] | Unknown  |
### aten.gelu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 2048]> self = ? | Done     |
|  1 | Tensor<[1, 32, 32, 1024]> self = ? | Done     |
|  2 | Tensor<[1, 64, 64, 512]> self = ?  | Done     |
|  3 | Tensor<[1, 8, 8, 4096]> self = ?   | Done     |
### aten.index.Tensor
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[225, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([4096])'] | None     |
|  1 | Tensor<[225, 32]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([4096])'] | None     |
|  2 | Tensor<[225, 4]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([4096])']  | None     |
|  3 | Tensor<[225, 8]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([4096])']  | None     |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                                  | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 64, 32]> self = ?,<br>number<> ord = 2.0,<br>Optional[List[int]]<> dim = [-1],<br>bool<> keepdim = True | None     |
|  1 | Tensor<[16, 8, 64, 32]> self = ?,<br>number<> ord = 2.0,<br>Optional[List[int]]<> dim = [-1],<br>bool<> keepdim = True | None     |
|  2 | Tensor<[4, 16, 64, 32]> self = ?,<br>number<> ord = 2.0,<br>Optional[List[int]]<> dim = [-1],<br>bool<> keepdim = True | None     |
|  3 | Tensor<[64, 4, 64, 32]> self = ?,<br>number<> ord = 2.0,<br>Optional[List[int]]<> dim = [-1],<br>bool<> keepdim = True | None     |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 64, 64]> self = ?,<br>Tensor<[16, 64, 64]> mask = ?,<br>number<> value = -100.0 | None     |
|  1 | Tensor<[16, 64, 64]> self = ?,<br>Tensor<[16, 64, 64]> mask = ?,<br>number<> value = 0.0    | None     |
|  2 | Tensor<[4, 64, 64]> self = ?,<br>Tensor<[4, 64, 64]> mask = ?,<br>number<> value = -100.0   | None     |
|  3 | Tensor<[4, 64, 64]> self = ?,<br>Tensor<[4, 64, 64]> mask = ?,<br>number<> value = 0.0      | None     |
|  4 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 64]> mask = ?,<br>number<> value = -100.0 | None     |
|  5 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 64]> mask = ?,<br>number<> value = 0.0    | None     |
### aten.mean.dim
|    | ATen Input Variations                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 8, 8]> self = ?,<br>Optional[List[int]]<> dim = [-1, -2],<br>bool<> keepdim = True | Done     |
### aten.mm.default
|    | ATen Input Variations                                         | Status   |
|---:|:--------------------------------------------------------------|:---------|
|  0 | Tensor<[1024, 512]> self = ?,<br>Tensor<[512, 256]> mat2 = ?  | Done     |
|  1 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 16]> mat2 = ?    | Done     |
|  2 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 32]> mat2 = ?    | Done     |
|  3 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 4]> mat2 = ?     | Done     |
|  4 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 8]> mat2 = ?     | Done     |
|  5 | Tensor<[256, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ? | Done     |
|  6 | Tensor<[64, 2048]> self = ?,<br>Tensor<[2048, 1024]> mat2 = ? | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 64, 64]> self = ?,<br>Tensor<> other = 16          | Done     |
|  1 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<> other = 16          | Done     |
|  2 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[32, 1, 1]> other = ? | Done     |
|  3 | Tensor<[1, 4, 64, 64]> self = ?,<br>Tensor<> other = 16           | Done     |
|  4 | Tensor<[1, 8, 64, 64]> self = ?,<br>Tensor<> other = 16           | Done     |
|  5 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[8, 1, 1]> other = ?  | Done     |
|  6 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[16, 1, 1]> other = ? | Done     |
|  7 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[4, 1, 1]> other = ?  | Done     |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                             | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 512]> input = ?,<br>List[int]<> normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float<> eps = 1e-05   | Done     |
|  1 | Tensor<[1, 32, 32, 256]> input = ?,<br>List[int]<> normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float<> eps = 1e-05   | Done     |
|  2 | Tensor<[1, 64, 64, 128]> input = ?,<br>List[int]<> normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float<> eps = 1e-05   | Done     |
|  3 | Tensor<[1, 8, 8, 1024]> input = ?,<br>List[int]<> normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float<> eps = 1e-05 | Done     |
### aten.ne.Scalar
|    | ATen Input Variations                                | Status   |
|---:|:-----------------------------------------------------|:---------|
|  0 | Tensor<[16, 64, 64]> self = ?,<br>number<> other = 0 | Done     |
|  1 | Tensor<[4, 64, 64]> self = ?,<br>number<> other = 0  | Done     |
|  2 | Tensor<[64, 64, 64]> self = ?,<br>number<> other = 0 | Done     |
### aten.new_zeros.default
|    | ATen Input Variations                                                                                  | Status   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 64, 256]> self = ?,<br>List[int]<> size = [32, 32],<br>Optional[bool]<> pin_memory = False | None     |
|  1 | Tensor<[4, 64, 512]> self = ?,<br>List[int]<> size = [16, 16],<br>Optional[bool]<> pin_memory = False  | None     |
|  2 | Tensor<[64, 64, 128]> self = ?,<br>List[int]<> size = [64, 64],<br>Optional[bool]<> pin_memory = False | None     |
### aten.permute.default
|    | ATen Input Variations                                                            | Status   |
|---:|:---------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 8, 8, 1024]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5] | Done     |
|  1 | Tensor<[1, 1, 8, 1, 8, 1024]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5] | Done     |
|  2 | Tensor<[1, 128, 64, 64]> self = ?,<br>List[int]<> dims = [0, 2, 3, 1]            | Done     |
|  3 | Tensor<[1, 2, 2, 8, 8, 512]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5]  | Done     |
|  4 | Tensor<[1, 2, 8, 2, 8, 512]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5]  | Done     |
|  5 | Tensor<[1, 4, 4, 8, 8, 256]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5]  | Done     |
|  6 | Tensor<[1, 4, 8, 4, 8, 256]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5]  | Done     |
|  7 | Tensor<[1, 64, 3, 32, 32]> self = ?,<br>List[int]<> dims = [2, 0, 3, 1, 4]       | Done     |
|  8 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int]<> dims = [0, 3, 1, 2]             | Done     |
|  9 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2, 4, 5]  | Done     |
| 10 | Tensor<[16, 64, 3, 8, 32]> self = ?,<br>List[int]<> dims = [2, 0, 3, 1, 4]       | Done     |
| 11 | Tensor<[2, 8, 2, 8]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]                | Done     |
| 12 | Tensor<[4, 64, 3, 16, 32]> self = ?,<br>List[int]<> dims = [2, 0, 3, 1, 4]       | Done     |
| 13 | Tensor<[4, 8, 4, 8]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]                | Done     |
| 14 | Tensor<[64, 64, 16]> self = ?,<br>List[int]<> dims = [2, 0, 1]                   | Done     |
| 15 | Tensor<[64, 64, 3, 4, 32]> self = ?,<br>List[int]<> dims = [2, 0, 3, 1, 4]       | Done     |
| 16 | Tensor<[64, 64, 32]> self = ?,<br>List[int]<> dims = [2, 0, 1]                   | Done     |
| 17 | Tensor<[64, 64, 4]> self = ?,<br>List[int]<> dims = [2, 0, 1]                    | Done     |
| 18 | Tensor<[64, 64, 8]> self = ?,<br>List[int]<> dims = [2, 0, 1]                    | Done     |
| 19 | Tensor<[8, 8, 8, 8]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]                | Done     |
### aten.relu.default
|    | ATen Input Variations             | Status   |
|---:|:----------------------------------|:---------|
|  0 | Tensor<[1, 15, 15, 512]> self = ? | Done     |
### aten.roll.default
|    | ATen Input Variations                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int]<> shifts = [-4, -4],<br>List[int]<> dims = [1, 2] | None     |
|  1 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int]<> shifts = [4, 4],<br>List[int]<> dims = [1, 2]   | None     |
|  2 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int]<> shifts = [-4, -4],<br>List[int]<> dims = [1, 2] | None     |
|  3 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int]<> shifts = [4, 4],<br>List[int]<> dims = [1, 2]   | None     |
|  4 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int]<> shifts = [-4, -4],<br>List[int]<> dims = [1, 2] | None     |
|  5 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int]<> shifts = [4, 4],<br>List[int]<> dims = [1, 2]   | None     |
### aten.select.int
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 1, 32, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | None     |
|  1 | Tensor<[3, 1, 32, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 1 | None     |
|  2 | Tensor<[3, 1, 32, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 2 | None     |
|  3 | Tensor<[3, 16, 8, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | None     |
|  4 | Tensor<[3, 16, 8, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 1 | None     |
|  5 | Tensor<[3, 16, 8, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 2 | None     |
|  6 | Tensor<[3, 4, 16, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | None     |
|  7 | Tensor<[3, 4, 16, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 1 | None     |
|  8 | Tensor<[3, 4, 16, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 2 | None     |
|  9 | Tensor<[3, 64, 4, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | None     |
| 10 | Tensor<[3, 64, 4, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 1 | None     |
| 11 | Tensor<[3, 64, 4, 64, 32]> self = ?,<br>int<> dim = 0,<br>int<> index = 2 | None     |
### aten.sigmoid.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 16, 64, 64]> self = ? | Done     |
|  1 | Tensor<[1, 32, 64, 64]> self = ? | Done     |
|  2 | Tensor<[1, 4, 64, 64]> self = ?  | Done     |
|  3 | Tensor<[1, 8, 64, 64]> self = ?  | Done     |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 256]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807                    | Unknown  |
|  1 | Tensor<[1, 16, 16, 512]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807                    | Unknown  |
|  2 | Tensor<[1, 16, 16, 512]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807,<br>int<> step = 2 | None     |
|  3 | Tensor<[1, 16, 16, 512]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = 9223372036854775807,<br>int<> step = 2 | None     |
|  4 | Tensor<[1, 16, 16, 512]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807                    | Unknown  |
|  5 | Tensor<[1, 16, 32, 256]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807,<br>int<> step = 2 | None     |
|  6 | Tensor<[1, 16, 32, 256]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = 9223372036854775807,<br>int<> step = 2 | None     |
|  7 | Tensor<[1, 32, 32, 128]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807                    | Unknown  |
|  8 | Tensor<[1, 32, 32, 256]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807                    | Unknown  |
|  9 | Tensor<[1, 32, 32, 256]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807,<br>int<> step = 2 | None     |
| 10 | Tensor<[1, 32, 32, 256]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = 9223372036854775807,<br>int<> step = 2 | None     |
| 11 | Tensor<[1, 32, 32, 256]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807                    | Unknown  |
| 12 | Tensor<[1, 32, 64, 128]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807,<br>int<> step = 2 | None     |
| 13 | Tensor<[1, 32, 64, 128]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = 9223372036854775807,<br>int<> step = 2 | None     |
| 14 | Tensor<[1, 64, 64, 128]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807                    | Unknown  |
| 15 | Tensor<[1, 64, 64, 128]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807,<br>int<> step = 2 | None     |
| 16 | Tensor<[1, 64, 64, 128]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = 9223372036854775807,<br>int<> step = 2 | None     |
| 17 | Tensor<[1, 64, 64, 128]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807                    | Unknown  |
| 18 | Tensor<[1, 8, 16, 512]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807,<br>int<> step = 2  | None     |
| 19 | Tensor<[1, 8, 16, 512]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = 9223372036854775807,<br>int<> step = 2  | None     |
| 20 | Tensor<[1, 8, 8, 1024]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807                     | Unknown  |
| 21 | Tensor<[1, 8, 8, 1024]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807                     | Unknown  |
| 22 | Tensor<[1, 8, 8, 512]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807                      | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ? | Done     |
|  1 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?   | Done     |
|  2 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ? | Done     |
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
|  8 | Tensor<[16, 512]> self = ?    | Done     |
|  9 | Tensor<[2048, 512]> self = ?  | Done     |
| 10 | Tensor<[256, 1024]> self = ?  | Done     |
| 11 | Tensor<[256, 256]> self = ?   | Done     |
| 12 | Tensor<[256, 512]> self = ?   | Done     |
| 13 | Tensor<[3072, 1024]> self = ? | Done     |
| 14 | Tensor<[32, 512]> self = ?    | Done     |
| 15 | Tensor<[384, 128]> self = ?   | Done     |
| 16 | Tensor<[4, 512]> self = ?     | Done     |
| 17 | Tensor<[4096, 1024]> self = ? | Done     |
| 18 | Tensor<[512, 1024]> self = ?  | Done     |
| 19 | Tensor<[512, 128]> self = ?   | Done     |
| 20 | Tensor<[512, 2048]> self = ?  | Done     |
| 21 | Tensor<[512, 2]> self = ?     | Done     |
| 22 | Tensor<[512, 512]> self = ?   | Done     |
| 23 | Tensor<[768, 256]> self = ?   | Done     |
| 24 | Tensor<[8, 512]> self = ?     | Done     |
### aten.transpose.int
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 64, 32]> self = ?,<br>int<> dim0 = -2,<br>int<> dim1 = -1 | Done     |
|  1 | Tensor<[1, 32, 64, 32]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
|  2 | Tensor<[16, 8, 64, 32]> self = ?,<br>int<> dim0 = -2,<br>int<> dim1 = -1 | Done     |
|  3 | Tensor<[16, 8, 64, 32]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
|  4 | Tensor<[4, 16, 64, 32]> self = ?,<br>int<> dim0 = -2,<br>int<> dim1 = -1 | Done     |
|  5 | Tensor<[4, 16, 64, 32]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
|  6 | Tensor<[64, 4, 64, 32]> self = ?,<br>int<> dim0 = -2,<br>int<> dim1 = -1 | Done     |
|  7 | Tensor<[64, 4, 64, 32]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[16, 1, 64, 64]> self = ?,<br>int<> dim = 0 | Done     |
|  1 | Tensor<[16, 64, 64]> self = ?,<br>int<> dim = 0    | Done     |
|  2 | Tensor<[16, 64, 64]> self = ?,<br>int<> dim = 1    | Done     |
|  3 | Tensor<[16, 64]> self = ?,<br>int<> dim = 1        | Done     |
|  4 | Tensor<[16, 64]> self = ?,<br>int<> dim = 2        | None     |
|  5 | Tensor<[32, 64, 64]> self = ?,<br>int<> dim = 0    | Done     |
|  6 | Tensor<[4, 1, 64, 64]> self = ?,<br>int<> dim = 0  | Done     |
|  7 | Tensor<[4, 64, 64]> self = ?,<br>int<> dim = 0     | Done     |
|  8 | Tensor<[4, 64, 64]> self = ?,<br>int<> dim = 1     | Done     |
|  9 | Tensor<[4, 64]> self = ?,<br>int<> dim = 1         | Done     |
| 10 | Tensor<[4, 64]> self = ?,<br>int<> dim = 2         | None     |
| 11 | Tensor<[64, 1, 64, 64]> self = ?,<br>int<> dim = 0 | Done     |
| 12 | Tensor<[64, 64, 64]> self = ?,<br>int<> dim = 1    | Done     |
| 13 | Tensor<[64, 64]> self = ?,<br>int<> dim = 1        | Done     |
| 14 | Tensor<[64, 64]> self = ?,<br>int<> dim = 2        | None     |
| 15 | Tensor<[8, 64, 64]> self = ?,<br>int<> dim = 0     | Done     |
### aten.view.default
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 8, 8, 1024]> self = ?,<br>List[int]<> size = [1, 64, 1024]   | Fallback |
|  1 | Tensor<[1, 1, 8, 1, 8, 1024]> self = ?,<br>List[int]<> size = [1, 8, 8, 1024] | Fallback |
|  2 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int]<> size = [1, 1024]             | Fallback |
|  3 | Tensor<[1, 15, 15, 16]> self = ?,<br>List[int]<> size = [-1, 16]              | Fallback |
|  4 | Tensor<[1, 15, 15, 2]> self = ?,<br>List[int]<> size = [225, 2]               | Fallback |
|  5 | Tensor<[1, 15, 15, 32]> self = ?,<br>List[int]<> size = [-1, 32]              | Fallback |
|  6 | Tensor<[1, 15, 15, 4]> self = ?,<br>List[int]<> size = [-1, 4]                | Fallback |
|  7 | Tensor<[1, 15, 15, 512]> self = ?,<br>List[int]<> size = [225, 512]           | Fallback |
|  8 | Tensor<[1, 15, 15, 8]> self = ?,<br>List[int]<> size = [-1, 8]                | Fallback |
|  9 | Tensor<[1, 16, 16, 1024]> self = ?,<br>List[int]<> size = [256, 1024]         | Fallback |
| 10 | Tensor<[1, 16, 16, 2048]> self = ?,<br>List[int]<> size = [256, 2048]         | Fallback |
| 11 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int]<> size = [1, 2, 8, 2, 8, 512] | Fallback |
| 12 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int]<> size = [256, 512]           | Fallback |
| 13 | Tensor<[1, 16, 8, 64, 64]> self = ?,<br>List[int]<> size = [-1, 8, 64, 64]    | Fallback |
| 14 | Tensor<[1, 32, 32, 1024]> self = ?,<br>List[int]<> size = [1024, 1024]        | Fallback |
| 15 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int]<> size = [1, 4, 8, 4, 8, 256] | Fallback |
| 16 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int]<> size = [1024, 256]          | Fallback |
| 17 | Tensor<[1, 32, 32, 512]> self = ?,<br>List[int]<> size = [1024, 512]          | Fallback |
| 18 | Tensor<[1, 32, 32, 64]> self = ?,<br>List[int]<> size = [32, 32, 64]          | Done     |
| 19 | Tensor<[1, 32, 64, 32]> self = ?,<br>List[int]<> size = [32, 64, 32]          | Done     |
| 20 | Tensor<[1, 32, 64, 64]> self = ?,<br>List[int]<> size = [32, 64, 64]          | Done     |
| 21 | Tensor<[1, 4, 16, 64, 64]> self = ?,<br>List[int]<> size = [-1, 16, 64, 64]   | Fallback |
| 22 | Tensor<[1, 64, 1024]> self = ?,<br>List[int]<> size = [1, 1, 1, 8, 8, 1024]   | Fallback |
| 23 | Tensor<[1, 64, 1024]> self = ?,<br>List[int]<> size = [64, 1024]              | Done     |
| 24 | Tensor<[1, 64, 3072]> self = ?,<br>List[int]<> size = [1, 64, 3, 32, 32]      | Fallback |
| 25 | Tensor<[1, 64, 4, 64, 64]> self = ?,<br>List[int]<> size = [-1, 4, 64, 64]    | Fallback |
| 26 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int]<> size = [1, 8, 8, 8, 8, 128] | Fallback |
| 27 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int]<> size = [4096, 128]          | Fallback |
| 28 | Tensor<[1, 64, 64, 512]> self = ?,<br>List[int]<> size = [4096, 512]          | Fallback |
| 29 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int]<> size = [1, 1, 8, 1, 8, 1024] | Fallback |
| 30 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int]<> size = [64, 1024]            | Fallback |
| 31 | Tensor<[1, 8, 8, 2048]> self = ?,<br>List[int]<> size = [64, 2048]            | Fallback |
| 32 | Tensor<[1, 8, 8, 4096]> self = ?,<br>List[int]<> size = [64, 4096]            | Fallback |
| 33 | Tensor<[1024, 1024]> self = ?,<br>List[int]<> size = [1, 32, 32, 1024]        | Fallback |
| 34 | Tensor<[1024, 256]> self = ?,<br>List[int]<> size = [1, 32, 32, 256]          | Fallback |
| 35 | Tensor<[1024, 256]> self = ?,<br>List[int]<> size = [16, 64, 256]             | Fallback |
| 36 | Tensor<[1024, 768]> self = ?,<br>List[int]<> size = [16, 64, 768]             | Fallback |
| 37 | Tensor<[128, 64, 32]> self = ?,<br>List[int]<> size = [16, 8, 64, 32]         | Fallback |
| 38 | Tensor<[128, 64, 64]> self = ?,<br>List[int]<> size = [16, 8, 64, 64]         | Fallback |
| 39 | Tensor<[16, 16]> self = ?,<br>List[int]<> size = [2, 8, 2, 8]                 | Fallback |
| 40 | Tensor<[16, 64, 256]> self = ?,<br>List[int]<> size = [1, 4, 4, 8, 8, 256]    | Fallback |
| 41 | Tensor<[16, 64, 256]> self = ?,<br>List[int]<> size = [1024, 256]             | Fallback |
| 42 | Tensor<[16, 64, 768]> self = ?,<br>List[int]<> size = [16, 64, 3, 8, 32]      | Fallback |
| 43 | Tensor<[16, 8, 64, 64]> self = ?,<br>List[int]<> size = [1, 16, 8, 64, 64]    | Fallback |
| 44 | Tensor<[16, 8, 64, 64]> self = ?,<br>List[int]<> size = [128, 64, 64]         | Fallback |
| 45 | Tensor<[225, 16]> self = ?,<br>List[int]<> size = [1, 15, 15, 16]             | Fallback |
| 46 | Tensor<[225, 32]> self = ?,<br>List[int]<> size = [1, 15, 15, 32]             | Fallback |
| 47 | Tensor<[225, 4]> self = ?,<br>List[int]<> size = [1, 15, 15, 4]               | Fallback |
| 48 | Tensor<[225, 512]> self = ?,<br>List[int]<> size = [1, 15, 15, 512]           | Fallback |
| 49 | Tensor<[225, 8]> self = ?,<br>List[int]<> size = [1, 15, 15, 8]               | Fallback |
| 50 | Tensor<[256, 1536]> self = ?,<br>List[int]<> size = [4, 64, 1536]             | Fallback |
| 51 | Tensor<[256, 2048]> self = ?,<br>List[int]<> size = [1, 16, 16, 2048]         | Fallback |
| 52 | Tensor<[256, 512]> self = ?,<br>List[int]<> size = [1, 16, 16, 512]           | Fallback |
| 53 | Tensor<[256, 512]> self = ?,<br>List[int]<> size = [4, 64, 512]               | Fallback |
| 54 | Tensor<[256, 64, 32]> self = ?,<br>List[int]<> size = [64, 4, 64, 32]         | Fallback |
| 55 | Tensor<[256, 64, 64]> self = ?,<br>List[int]<> size = [64, 4, 64, 64]         | Fallback |
| 56 | Tensor<[32, 32]> self = ?,<br>List[int]<> size = [4, 8, 4, 8]                 | Fallback |
| 57 | Tensor<[32, 64, 32]> self = ?,<br>List[int]<> size = [1, 32, 64, 32]          | Done     |
| 58 | Tensor<[32, 64, 64]> self = ?,<br>List[int]<> size = [1, 32, 64, 64]          | Done     |
| 59 | Tensor<[4, 16, 64, 64]> self = ?,<br>List[int]<> size = [1, 4, 16, 64, 64]    | Fallback |
| 60 | Tensor<[4, 16, 64, 64]> self = ?,<br>List[int]<> size = [64, 64, 64]          | Fallback |
| 61 | Tensor<[4, 64, 1536]> self = ?,<br>List[int]<> size = [4, 64, 3, 16, 32]      | Fallback |
| 62 | Tensor<[4, 64, 512]> self = ?,<br>List[int]<> size = [1, 2, 2, 8, 8, 512]     | Fallback |
| 63 | Tensor<[4, 64, 512]> self = ?,<br>List[int]<> size = [256, 512]               | Fallback |
| 64 | Tensor<[4096, 128]> self = ?,<br>List[int]<> size = [1, 64, 64, 128]          | Fallback |
| 65 | Tensor<[4096, 128]> self = ?,<br>List[int]<> size = [64, 64, 128]             | Fallback |
| 66 | Tensor<[4096, 16]> self = ?,<br>List[int]<> size = [64, 64, -1]               | Fallback |
| 67 | Tensor<[4096, 32]> self = ?,<br>List[int]<> size = [64, 64, -1]               | Fallback |
| 68 | Tensor<[4096, 384]> self = ?,<br>List[int]<> size = [64, 64, 384]             | Fallback |
| 69 | Tensor<[4096, 4]> self = ?,<br>List[int]<> size = [64, 64, -1]                | Fallback |
| 70 | Tensor<[4096, 512]> self = ?,<br>List[int]<> size = [1, 64, 64, 512]          | Fallback |
| 71 | Tensor<[4096, 8]> self = ?,<br>List[int]<> size = [64, 64, -1]                | Fallback |
| 72 | Tensor<[64, 1024]> self = ?,<br>List[int]<> size = [1, 64, 1024]              | Done     |
| 73 | Tensor<[64, 1024]> self = ?,<br>List[int]<> size = [1, 8, 8, 1024]            | Fallback |
| 74 | Tensor<[64, 3072]> self = ?,<br>List[int]<> size = [1, 64, 3072]              | Done     |
| 75 | Tensor<[64, 4, 64, 64]> self = ?,<br>List[int]<> size = [1, 64, 4, 64, 64]    | Fallback |
| 76 | Tensor<[64, 4, 64, 64]> self = ?,<br>List[int]<> size = [256, 64, 64]         | Fallback |
| 77 | Tensor<[64, 4096]> self = ?,<br>List[int]<> size = [1, 8, 8, 4096]            | Fallback |
| 78 | Tensor<[64, 64, 128]> self = ?,<br>List[int]<> size = [1, 8, 8, 8, 8, 128]    | Fallback |
| 79 | Tensor<[64, 64, 128]> self = ?,<br>List[int]<> size = [4096, 128]             | Fallback |
| 80 | Tensor<[64, 64, 32]> self = ?,<br>List[int]<> size = [4, 16, 64, 32]          | Fallback |
| 81 | Tensor<[64, 64, 384]> self = ?,<br>List[int]<> size = [64, 64, 3, 4, 32]      | Fallback |
| 82 | Tensor<[64, 64, 64]> self = ?,<br>List[int]<> size = [4, 16, 64, 64]          | Fallback |
| 83 | Tensor<[64, 64]> self = ?,<br>List[int]<> size = [8, 8, 8, 8]                 | Fallback |

