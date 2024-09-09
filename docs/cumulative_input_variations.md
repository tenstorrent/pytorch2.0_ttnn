# High Level Operations Status
|     | Operations                                        |   Input Variations |
|----:|:--------------------------------------------------|-------------------:|
|   0 | aten._adaptive_avg_pool2d.default                 |                  1 |
|   1 | aten._log_softmax.default                         |                  2 |
|   2 | aten._native_batch_norm_legit_functional.default  |                  1 |
|   3 | aten._native_batch_norm_legit_no_training.default |                 20 |
|   4 | aten._scaled_dot_product_flash_attention.default  |                  7 |
|   5 | aten._softmax.default                             |                 34 |
|   6 | aten._to_copy.default                             |                 42 |
|   7 | aten._unsafe_index.Tensor                         |                 30 |
|   8 | aten._unsafe_view.default                         |                109 |
|   9 | aten.abs.default                                  |                  2 |
|  10 | aten.add.Tensor                                   |                 95 |
|  11 | aten.addmm.default                                |                 62 |
|  12 | aten.all.default                                  |                  1 |
|  13 | aten.all.dim                                      |                  1 |
|  14 | aten.any.default                                  |                  1 |
|  15 | aten.arange.default                               |                 14 |
|  16 | aten.arange.start                                 |                  9 |
|  17 | aten.argmax.default                               |                  3 |
|  18 | aten.as_strided.default                           |                  2 |
|  19 | aten.avg_pool2d.default                           |                  4 |
|  20 | aten.baddbmm.default                              |                  2 |
|  21 | aten.bernoulli.p                                  |                  1 |
|  22 | aten.bitwise_not.default                          |                  2 |
|  23 | aten.bmm.default                                  |                 35 |
|  24 | aten.cat.default                                  |                 29 |
|  25 | aten.ceil.default                                 |                  5 |
|  26 | aten.clamp.default                                |                 33 |
|  27 | aten.clamp_min.default                            |                  4 |
|  28 | aten.clone.default                                |                 90 |
|  29 | aten.constant_pad_nd.default                      |                 17 |
|  30 | aten.convolution.default                          |                421 |
|  31 | aten.cos.default                                  |                  2 |
|  32 | aten.cumsum.default                               |                  5 |
|  33 | aten.detach.default                               |                  1 |
|  34 | aten.div.Tensor                                   |                 51 |
|  35 | aten.embedding.default                            |                 33 |
|  36 | aten.empty.memory_format                          |                  1 |
|  37 | aten.eq.Scalar                                    |                  7 |
|  38 | aten.eq.Tensor                                    |                  1 |
|  39 | aten.exp.default                                  |                  6 |
|  40 | aten.expand.default                               |                249 |
|  41 | aten.fill.Scalar                                  |                  1 |
|  42 | aten.floor.default                                |                  1 |
|  43 | aten.floor_divide.default                         |                  1 |
|  44 | aten.full.default                                 |                  5 |
|  45 | aten.full_like.default                            |                  4 |
|  46 | aten.gelu.default                                 |                 25 |
|  47 | aten.gt.Scalar                                    |                  3 |
|  48 | aten.hardsigmoid.default                          |                  3 |
|  49 | aten.hardswish.default                            |                  2 |
|  50 | aten.hardtanh.default                             |                  6 |
|  51 | aten.index.Tensor                                 |                 32 |
|  52 | aten.index_select.default                         |                  1 |
|  53 | aten.le.Tensor                                    |                  1 |
|  54 | aten.leaky_relu.default                           |                  2 |
|  55 | aten.lift_fresh_copy.default                      |                  1 |
|  56 | aten.linalg_vector_norm.default                   |                  5 |
|  57 | aten.log.default                                  |                  2 |
|  58 | aten.logical_not.default                          |                  1 |
|  59 | aten.lt.Scalar                                    |                  3 |
|  60 | aten.lt.Tensor                                    |                  1 |
|  61 | aten.masked_fill.Scalar                           |                 12 |
|  62 | aten.masked_fill.Tensor                           |                  1 |
|  63 | aten.max.default                                  |                  2 |
|  64 | aten.max_pool2d_with_indices.default              |                 16 |
|  65 | aten.maximum.default                              |                  1 |
|  66 | aten.mean.dim                                     |                 41 |
|  67 | aten.min.default                                  |                  1 |
|  68 | aten.minimum.default                              |                  2 |
|  69 | aten.mm.default                                   |                 23 |
|  70 | aten.mul.Scalar                                   |                  2 |
|  71 | aten.mul.Tensor                                   |                108 |
|  72 | aten.native_dropout.default                       |                  3 |
|  73 | aten.native_group_norm.default                    |                  5 |
|  74 | aten.native_layer_norm.default                    |                 64 |
|  75 | aten.ne.Scalar                                    |                  4 |
|  76 | aten.neg.default                                  |                  4 |
|  77 | aten.new_full.default                             |                  3 |
|  78 | aten.new_ones.default                             |                  2 |
|  79 | aten.new_zeros.default                            |                 13 |
|  80 | aten.nll_loss_forward.default                     |                  1 |
|  81 | aten.ones.default                                 |                  4 |
|  82 | aten.permute.default                              |                 75 |
|  83 | aten.pow.Scalar                                   |                  1 |
|  84 | aten.pow.Tensor_Scalar                            |                 15 |
|  85 | aten.pow.Tensor_Tensor                            |                  1 |
|  86 | aten.relu.default                                 |                 24 |
|  87 | aten.remainder.Scalar                             |                  1 |
|  88 | aten.repeat.default                               |                  7 |
|  89 | aten.roll.default                                 |                  8 |
|  90 | aten.rsqrt.default                                |                  4 |
|  91 | aten.rsub.Scalar                                  |                 25 |
|  92 | aten.scalar_tensor.default                        |                  1 |
|  93 | aten.select.int                                   |                 43 |
|  94 | aten.sigmoid.default                              |                 14 |
|  95 | aten.silu.default                                 |                  1 |
|  96 | aten.sin.default                                  |                  2 |
|  97 | aten.slice.Tensor                                 |                129 |
|  98 | aten.slice_scatter.default                        |                  3 |
|  99 | aten.split.Tensor                                 |                  7 |
| 100 | aten.split_with_sizes.default                     |                  2 |
| 101 | aten.squeeze.dim                                  |                 11 |
| 102 | aten.stack.default                                |                  7 |
| 103 | aten.sub.Tensor                                   |                 22 |
| 104 | aten.sum.default                                  |                  1 |
| 105 | aten.sum.dim_IntList                              |                  1 |
| 106 | aten.sym_size.int                                 |                  9 |
| 107 | aten.t.default                                    |                 50 |
| 108 | aten.tanh.default                                 |                 13 |
| 109 | aten.topk.default                                 |                  1 |
| 110 | aten.transpose.int                                |                 74 |
| 111 | aten.tril.default                                 |                  1 |
| 112 | aten.unbind.int                                   |                  3 |
| 113 | aten.unsqueeze.default                            |                 79 |
| 114 | aten.view.default                                 |                940 |
| 115 | aten.where.self                                   |                  6 |
| 116 | aten.zeros.default                                |                  5 |
| 117 | aten.zeros_like.default                           |                  6 |
***
### aten._adaptive_avg_pool2d.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 512, 7, 7]> self = ?,<br>List[int] output_size = [7, 7] | Unknown  |
### aten._log_softmax.default
|    | ATen Input Variations                                                        | Status   |
|---:|:-----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1,<br>bool half_to_float = False      | Unknown  |
|  1 | Tensor<[19, 256008]> self = ?,<br>int dim = 1,<br>bool half_to_float = False | Unknown  |
### aten._native_batch_norm_legit_functional.default
|    | ATen Input Variations                                                                                                                                                                                                                                    | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 256, 256]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>bool training = True,<br>float momentum = 0.1,<br>float eps = 1e-05 | Unknown  |
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 112, 112]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001     | Unknown  |
|  1 | Tensor<[1, 16, 112, 112]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Unknown  |
|  2 | Tensor<[1, 16, 160, 160]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001     | Unknown  |
|  3 | Tensor<[1, 16, 224, 224]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Unknown  |
|  4 | Tensor<[1, 256, 100]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Unknown  |
|  5 | Tensor<[1, 256, 128, 128]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Unknown  |
|  6 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Unknown  |
|  7 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Unknown  |
|  8 | Tensor<[1, 32, 120, 120]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Unknown  |
|  9 | Tensor<[1, 32, 130, 130]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Unknown  |
| 10 | Tensor<[1, 32, 149, 149]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Unknown  |
| 11 | Tensor<[1, 32, 150, 150]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Unknown  |
| 12 | Tensor<[1, 32, 190, 190]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Unknown  |
| 13 | Tensor<[1, 32, 192, 192]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Unknown  |
| 14 | Tensor<[1, 64, 112, 112]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Unknown  |
| 15 | Tensor<[1, 64, 112, 112]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Unknown  |
| 16 | Tensor<[1, 64, 224, 224]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Unknown  |
| 17 | Tensor<[1, 64, 30, 40]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05        | Unknown  |
| 18 | Tensor<[1, 64, 400, 544]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Unknown  |
| 19 | Tensor<[1, 96, 112, 112]> input = ?,<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>Tensor<[96]> running_mean = ?,<br>Tensor<[96]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Unknown  |
### aten._scaled_dot_product_flash_attention.default
|    | ATen Input Variations                                                                                                                                        | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 1500, 64]> query = ?,<br>Tensor<[1, 12, 1500, 64]> key = ?,<br>Tensor<[1, 12, 1500, 64]> value = ?                                            | Unknown  |
|  1 | Tensor<[1, 12, 197, 64]> query = ?,<br>Tensor<[1, 12, 197, 64]> key = ?,<br>Tensor<[1, 12, 197, 64]> value = ?                                               | Unknown  |
|  2 | Tensor<[1, 12, 4, 64]> query = ?,<br>Tensor<[1, 12, 4, 64]> key = ?,<br>Tensor<[1, 12, 4, 64]> value = ?,<br>float dropout_p = 0.0,<br>bool is_causal = True | Unknown  |
|  3 | Tensor<[1, 12, 50, 64]> query = ?,<br>Tensor<[1, 12, 50, 64]> key = ?,<br>Tensor<[1, 12, 50, 64]> value = ?                                                  | Unknown  |
|  4 | Tensor<[1, 16, 1370, 80]> query = ?,<br>Tensor<[1, 16, 1370, 80]> key = ?,<br>Tensor<[1, 16, 1370, 80]> value = ?                                            | Unknown  |
|  5 | Tensor<[1, 16, 197, 64]> query = ?,<br>Tensor<[1, 16, 197, 64]> key = ?,<br>Tensor<[1, 16, 197, 64]> value = ?                                               | Unknown  |
|  6 | Tensor<[1, 16, 50, 64]> query = ?,<br>Tensor<[1, 16, 50, 64]> key = ?,<br>Tensor<[1, 16, 50, 64]> value = ?                                                  | Unknown  |
### aten._softmax.default
|    | ATen Input Variations                                                               | Status   |
|---:|:------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
|  1 | Tensor<[1, 1, 19200, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
|  2 | Tensor<[1, 12, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
|  3 | Tensor<[1, 12, 12, 12]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
|  4 | Tensor<[1, 12, 14, 14]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
|  5 | Tensor<[1, 12, 16, 16]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
|  6 | Tensor<[1, 12, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  |
|  7 | Tensor<[1, 12, 201, 201]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  |
|  8 | Tensor<[1, 12, 25, 25]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
|  9 | Tensor<[1, 12, 45, 45]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
| 10 | Tensor<[1, 12, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  |
| 11 | Tensor<[1, 12, 8, 8]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  |
| 12 | Tensor<[1, 12, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  |
| 13 | Tensor<[1, 16, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
| 14 | Tensor<[1, 16, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  |
| 15 | Tensor<[1, 16, 256, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  |
| 16 | Tensor<[1, 16, 32, 32]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
| 17 | Tensor<[1, 16, 5, 5]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  |
| 18 | Tensor<[1, 16, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  |
| 19 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
| 20 | Tensor<[1, 32, 32, 32]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
| 21 | Tensor<[1, 6, 15, 15]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  |
| 22 | Tensor<[1, 64, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  |
| 23 | Tensor<[1, 71, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  |
| 24 | Tensor<[1, 8, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  |
| 25 | Tensor<[1, 8, 256, 2048]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  |
| 26 | Tensor<[12, 24, 24]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  |
| 27 | Tensor<[12, 50, 50]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  |
| 28 | Tensor<[16, 19, 19]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  |
| 29 | Tensor<[64, 3, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
| 30 | Tensor<[64, 3, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
| 31 | Tensor<[64, 4, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
| 32 | Tensor<[64, 4, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
| 33 | Tensor<[8, 920, 920]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                                                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>Optional[int] dtype = torch.float32                                                                              | Unknown  |
|  1 | Tensor<[1, 1, 1, 12]> self = ?,<br>Optional[int] dtype = torch.float32                                                                              | Unknown  |
|  2 | Tensor<[1, 1, 1, 14]> self = ?,<br>Optional[int] dtype = torch.float32                                                                              | Unknown  |
|  3 | Tensor<[1, 1, 1, 15]> self = ?,<br>Optional[int] dtype = torch.float32                                                                              | Unknown  |
|  4 | Tensor<[1, 1, 1, 2048]> self = ?,<br>Optional[int] dtype = torch.float32                                                                            | Unknown  |
|  5 | Tensor<[1, 1, 1, 24]> self = ?,<br>Optional[int] dtype = torch.bool                                                                                 | Unknown  |
|  6 | Tensor<[1, 1, 1, 256]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                            | Unknown  |
|  7 | Tensor<[1, 1, 1, 25]> self = ?,<br>Optional[int] dtype = torch.float32                                                                              | Unknown  |
|  8 | Tensor<[1, 1, 1, 42]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                | Unknown  |
|  9 | Tensor<[1, 1, 1, 46]> self = ?,<br>Optional[int] dtype = torch.bool                                                                                 | Unknown  |
| 10 | Tensor<[1, 1, 1, 5]> self = ?,<br>Optional[int] dtype = torch.float32                                                                               | Unknown  |
| 11 | Tensor<[1, 1, 1, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                              | Unknown  |
| 12 | Tensor<[1, 1, 1, 8]> self = ?,<br>Optional[int] dtype = torch.float32                                                                               | Unknown  |
| 13 | Tensor<[1, 1, 1, 9]> self = ?,<br>Optional[int] dtype = torch.float32                                                                               | Unknown  |
| 14 | Tensor<[1, 1, 19, 19]> self = ?,<br>Optional[int] dtype = torch.float32                                                                             | Unknown  |
| 15 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                        | Unknown  |
| 16 | Tensor<[1, 1, 23, 40]> self = ?,<br>Optional[int] dtype = torch.bool                                                                                | Unknown  |
| 17 | Tensor<[1, 1, 24, 24]> self = ?,<br>Optional[int] dtype = torch.float32                                                                             | Unknown  |
| 18 | Tensor<[1, 1, 32, 32]> self = ?,<br>Optional[int] dtype = torch.bool                                                                                | Unknown  |
| 19 | Tensor<[1, 1, 384, 512]> self = ?,<br>Optional[int] dtype = torch.float32                                                                           | Unknown  |
| 20 | Tensor<[1, 1, 45, 45]> self = ?,<br>Optional[int] dtype = torch.float32                                                                             | Unknown  |
| 21 | Tensor<[1, 1, 720, 1280]> self = ?,<br>Optional[int] dtype = torch.float32                                                                          | Unknown  |
| 22 | Tensor<[1, 10]> self = ?,<br>Optional[int] dtype = torch.int32                                                                                      | Unknown  |
| 23 | Tensor<[1, 10]> self = ?,<br>Optional[int] dtype = torch.int32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu           | Unknown  |
| 24 | Tensor<[1, 16, 32, 32]> self = ?,<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  |
| 25 | Tensor<[1, 3, 224, 224]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                          | Unknown  |
| 26 | Tensor<[1, 32, 4096]> self = ?,<br>Optional[int] dtype = torch.float32                                                                              | Unknown  |
| 27 | Tensor<[1, 7]> self = ?,<br>Optional[int] dtype = torch.int32                                                                                       | Unknown  |
| 28 | Tensor<[10, 10]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                     | Unknown  |
| 29 | Tensor<[128]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                        | Unknown  |
| 30 | Tensor<[12]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                         | Unknown  |
| 31 | Tensor<[15, 15]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                     | Unknown  |
| 32 | Tensor<[16, 1, 32]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                               | Unknown  |
| 33 | Tensor<[2, 1, 7, 7]> self = ?,<br>Optional[int] dtype = torch.bool                                                                                  | Unknown  |
| 34 | Tensor<[2, 7]> self = ?,<br>Optional[int] dtype = torch.int32,<br>Optional[Device] device = cpu                                                     | Unknown  |
| 35 | Tensor<[23]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                         | Unknown  |
| 36 | Tensor<[25]> self = ?,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu                                                     | Unknown  |
| 37 | Tensor<[300]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                        | Unknown  |
| 38 | Tensor<[30]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                         | Unknown  |
| 39 | Tensor<[320]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                        | Unknown  |
| 40 | Tensor<[56]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                         | Unknown  |
| 41 | Tensor<[800]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                        | Unknown  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                           | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 384, 512]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_1, _to_copy_2]    | Unknown  |
|  1 | Tensor<[1, 1, 720, 1280]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_1, _to_copy_2]   | Unknown  |
|  2 | Tensor<[1, 120, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_2, _to_copy_5]    | Unknown  |
|  3 | Tensor<[1, 18, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_2, _to_copy_5]     | Unknown  |
|  4 | Tensor<[1, 18, 28, 28]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze, _to_copy_1]       | Unknown  |
|  5 | Tensor<[1, 18, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_15, _to_copy_31]     | Unknown  |
|  6 | Tensor<[1, 184, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_5, _to_copy_11]     | Unknown  |
|  7 | Tensor<[1, 192, 50, 83]> self = ?,<br>List[Optional[Tensor]] indices = [view_2, view_3, clamp, clamp_1]         | Unknown  |
|  8 | Tensor<[1, 200, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_4, _to_copy_9]      | Unknown  |
|  9 | Tensor<[1, 240, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_3, _to_copy_7]    | Unknown  |
| 10 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_1, _to_copy_2]  | Unknown  |
| 11 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_10, _to_copy_14]  | Unknown  |
| 12 | Tensor<[1, 256, 25, 34]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_8, _to_copy_5]    | Unknown  |
| 13 | Tensor<[1, 256, 32, 32]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_7, _to_copy_10]   | Unknown  |
| 14 | Tensor<[1, 256, 50, 68]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_9, _to_copy_7]    | Unknown  |
| 15 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_4, _to_copy_6]    | Unknown  |
| 16 | Tensor<[1, 3, 320, 320]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_6, _to_copy_2]    | Unknown  |
| 17 | Tensor<[1, 3, 480, 640]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_6, _to_copy_2]    | Unknown  |
| 18 | Tensor<[1, 36, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_3, _to_copy_7]     | Unknown  |
| 19 | Tensor<[1, 36, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_17, _to_copy_35]     | Unknown  |
| 20 | Tensor<[1, 480, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_7, _to_copy_15]     | Unknown  |
| 21 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_16, _to_copy_14] | Unknown  |
| 22 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_1, _to_copy_2]     | Unknown  |
| 23 | Tensor<[1, 64, 240, 320]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_19, _to_copy_18] | Unknown  |
| 24 | Tensor<[1, 64, 30, 40]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_6, _to_copy_6]     | Unknown  |
| 25 | Tensor<[1, 64, 60, 80]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_11, _to_copy_10]   | Unknown  |
| 26 | Tensor<[1, 672, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_8, _to_copy_17]     | Unknown  |
| 27 | Tensor<[1, 72, 28, 28]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze, _to_copy_1]       | Unknown  |
| 28 | Tensor<[1, 72, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_18, _to_copy_37]     | Unknown  |
| 29 | Tensor<[1, 960, 3, 3]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_10, _to_copy_21]    | Unknown  |
### aten._unsafe_view.default
|     | ATen Input Variations                                                       | Status   |
|----:|:----------------------------------------------------------------------------|:---------|
|   0 | Tensor<[1, 1, 4, 4, 64]> self = ?,<br>List[int] size = [1, 1, 16, 64]       | Unknown  |
|   1 | Tensor<[1, 10, 10, 6, 4]> self = ?,<br>List[int] size = [1, 600, 4]         | Unknown  |
|   2 | Tensor<[1, 10, 10, 6, 91]> self = ?,<br>List[int] size = [1, 600, 91]       | Unknown  |
|   3 | Tensor<[1, 100, 136, 9, 4]> self = ?,<br>List[int] size = [1, 122400, 4]    | Unknown  |
|   4 | Tensor<[1, 100, 136, 9, 91]> self = ?,<br>List[int] size = [1, 122400, 91]  | Unknown  |
|   5 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] size = [1, 12, 768]          | Unknown  |
|   6 | Tensor<[1, 13, 17, 9, 4]> self = ?,<br>List[int] size = [1, 1989, 4]        | Unknown  |
|   7 | Tensor<[1, 13, 17, 9, 91]> self = ?,<br>List[int] size = [1, 1989, 91]      | Unknown  |
|   8 | Tensor<[1, 14, 12, 64]> self = ?,<br>List[int] size = [1, 14, 768]          | Unknown  |
|   9 | Tensor<[1, 16, 16, 16, 16, 3]> self = ?,<br>List[int] size = [1, 256, 768]  | Unknown  |
|  10 | Tensor<[1, 19, 16, 64]> self = ?,<br>List[int] size = [1, 19, 1024]         | Unknown  |
|  11 | Tensor<[1, 19, 19, 6, 4]> self = ?,<br>List[int] size = [1, 2166, 4]        | Unknown  |
|  12 | Tensor<[1, 19, 19, 6, 91]> self = ?,<br>List[int] size = [1, 2166, 91]      | Unknown  |
|  13 | Tensor<[1, 2, 2, 6, 4]> self = ?,<br>List[int] size = [1, 24, 4]            | Unknown  |
|  14 | Tensor<[1, 2, 2, 6, 91]> self = ?,<br>List[int] size = [1, 24, 91]          | Unknown  |
|  15 | Tensor<[1, 2, 2, 7, 7, 384]> self = ?,<br>List[int] size = [4, 49, 384]     | Unknown  |
|  16 | Tensor<[1, 2, 2, 7, 7, 512]> self = ?,<br>List[int] size = [4, 49, 512]     | Unknown  |
|  17 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>List[int] size = [4, 64, 384]     | Unknown  |
|  18 | Tensor<[1, 2, 2, 8, 8, 512]> self = ?,<br>List[int] size = [4, 64, 512]     | Unknown  |
|  19 | Tensor<[1, 2, 7, 2, 7, 384]> self = ?,<br>List[int] size = [1, 14, 14, 384] | Unknown  |
|  20 | Tensor<[1, 2, 7, 2, 7, 512]> self = ?,<br>List[int] size = [1, 14, 14, 512] | Unknown  |
|  21 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>List[int] size = [1, 16, 16, 384] | Unknown  |
|  22 | Tensor<[1, 2, 8, 2, 8, 512]> self = ?,<br>List[int] size = [1, 16, 16, 512] | Unknown  |
|  23 | Tensor<[1, 20, 20, 6, 4]> self = ?,<br>List[int] size = [1, 2400, 4]        | Unknown  |
|  24 | Tensor<[1, 20, 20, 6, 91]> self = ?,<br>List[int] size = [1, 2400, 91]      | Unknown  |
|  25 | Tensor<[1, 24, 12, 64]> self = ?,<br>List[int] size = [1, 24, 768]          | Unknown  |
|  26 | Tensor<[1, 25, 34, 9, 4]> self = ?,<br>List[int] size = [1, 7650, 4]        | Unknown  |
|  27 | Tensor<[1, 25, 34, 9, 91]> self = ?,<br>List[int] size = [1, 7650, 91]      | Unknown  |
|  28 | Tensor<[1, 3, 3, 4, 4]> self = ?,<br>List[int] size = [1, 36, 4]            | Unknown  |
|  29 | Tensor<[1, 3, 3, 4, 91]> self = ?,<br>List[int] size = [1, 36, 91]          | Unknown  |
|  30 | Tensor<[1, 3, 3, 6, 4]> self = ?,<br>List[int] size = [1, 54, 4]            | Unknown  |
|  31 | Tensor<[1, 3, 3, 6, 91]> self = ?,<br>List[int] size = [1, 54, 91]          | Unknown  |
|  32 | Tensor<[1, 32, 16, 96]> self = ?,<br>List[int] size = [1, 32, 1536]         | Unknown  |
|  33 | Tensor<[1, 38, 38, 4, 4]> self = ?,<br>List[int] size = [1, 5776, 4]        | Unknown  |
|  34 | Tensor<[1, 38, 38, 4, 91]> self = ?,<br>List[int] size = [1, 5776, 91]      | Unknown  |
|  35 | Tensor<[1, 4, 4, 7, 7, 192]> self = ?,<br>List[int] size = [16, 49, 192]    | Unknown  |
|  36 | Tensor<[1, 4, 4, 7, 7, 256]> self = ?,<br>List[int] size = [16, 49, 256]    | Unknown  |
|  37 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>List[int] size = [16, 64, 192]    | Unknown  |
|  38 | Tensor<[1, 4, 4, 8, 8, 256]> self = ?,<br>List[int] size = [16, 64, 256]    | Unknown  |
|  39 | Tensor<[1, 4, 7, 4, 7, 192]> self = ?,<br>List[int] size = [1, 28, 28, 192] | Unknown  |
|  40 | Tensor<[1, 4, 7, 4, 7, 256]> self = ?,<br>List[int] size = [1, 28, 28, 256] | Unknown  |
|  41 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>List[int] size = [1, 32, 32, 192] | Unknown  |
|  42 | Tensor<[1, 4, 8, 4, 8, 256]> self = ?,<br>List[int] size = [1, 32, 32, 256] | Unknown  |
|  43 | Tensor<[1, 49, 24, 32]> self = ?,<br>List[int] size = [1, 49, 768]          | Unknown  |
|  44 | Tensor<[1, 49, 32, 32]> self = ?,<br>List[int] size = [1, 49, 1024]         | Unknown  |
|  45 | Tensor<[1, 5, 4, 4, 64]> self = ?,<br>List[int] size = [1, 5, 16, 64]       | Unknown  |
|  46 | Tensor<[1, 5, 5, 6, 4]> self = ?,<br>List[int] size = [1, 150, 4]           | Unknown  |
|  47 | Tensor<[1, 5, 5, 6, 91]> self = ?,<br>List[int] size = [1, 150, 91]         | Unknown  |
|  48 | Tensor<[1, 50, 12, 64]> self = ?,<br>List[int] size = [1, 50, 768]          | Unknown  |
|  49 | Tensor<[1, 50, 68, 9, 4]> self = ?,<br>List[int] size = [1, 30600, 4]       | Unknown  |
|  50 | Tensor<[1, 50, 68, 9, 91]> self = ?,<br>List[int] size = [1, 30600, 91]     | Unknown  |
|  51 | Tensor<[1, 64, 24, 32]> self = ?,<br>List[int] size = [1, 64, 768]          | Unknown  |
|  52 | Tensor<[1, 64, 32, 32]> self = ?,<br>List[int] size = [1, 64, 1024]         | Unknown  |
|  53 | Tensor<[1, 7, 71, 64]> self = ?,<br>List[int] size = [1, 7, 4544]           | Unknown  |
|  54 | Tensor<[1, 7, 9, 9, 4]> self = ?,<br>List[int] size = [1, 567, 4]           | Unknown  |
|  55 | Tensor<[1, 7, 9, 9, 91]> self = ?,<br>List[int] size = [1, 567, 91]         | Unknown  |
|  56 | Tensor<[1, 8, 7, 8, 7, 128]> self = ?,<br>List[int] size = [1, 56, 56, 128] | Unknown  |
|  57 | Tensor<[1, 8, 7, 8, 7, 96]> self = ?,<br>List[int] size = [1, 56, 56, 96]   | Unknown  |
|  58 | Tensor<[1, 8, 8, 7, 7, 128]> self = ?,<br>List[int] size = [64, 49, 128]    | Unknown  |
|  59 | Tensor<[1, 8, 8, 7, 7, 96]> self = ?,<br>List[int] size = [64, 49, 96]      | Unknown  |
|  60 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>List[int] size = [64, 64, 128]    | Unknown  |
|  61 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>List[int] size = [64, 64, 96]      | Unknown  |
|  62 | Tensor<[1, 9, 12, 64]> self = ?,<br>List[int] size = [1, 9, 768]            | Unknown  |
|  63 | Tensor<[1, 9, 16, 128]> self = ?,<br>List[int] size = [1, 9, 2048]          | Unknown  |
|  64 | Tensor<[1, 9, 16, 64]> self = ?,<br>List[int] size = [1, 9, 1024]           | Unknown  |
|  65 | Tensor<[1, 9, 64, 64]> self = ?,<br>List[int] size = [1, 9, 4096]           | Unknown  |
|  66 | Tensor<[10, 10]> self = ?,<br>List[int] size = [100]                        | Unknown  |
|  67 | Tensor<[100, 136]> self = ?,<br>List[int] size = [13600]                    | Unknown  |
|  68 | Tensor<[13, 17]> self = ?,<br>List[int] size = [221]                        | Unknown  |
|  69 | Tensor<[16, 6, 32, 49]> self = ?,<br>List[int] size = [96, 32, 49]          | Unknown  |
|  70 | Tensor<[16, 6, 32, 64]> self = ?,<br>List[int] size = [96, 32, 64]          | Unknown  |
|  71 | Tensor<[16, 6, 49, 32]> self = ?,<br>List[int] size = [96, 49, 32]          | Unknown  |
|  72 | Tensor<[16, 6, 64, 32]> self = ?,<br>List[int] size = [96, 64, 32]          | Unknown  |
|  73 | Tensor<[16, 8, 32, 49]> self = ?,<br>List[int] size = [128, 32, 49]         | Unknown  |
|  74 | Tensor<[16, 8, 32, 64]> self = ?,<br>List[int] size = [128, 32, 64]         | Unknown  |
|  75 | Tensor<[16, 8, 49, 32]> self = ?,<br>List[int] size = [128, 49, 32]         | Unknown  |
|  76 | Tensor<[16, 8, 64, 32]> self = ?,<br>List[int] size = [128, 64, 32]         | Unknown  |
|  77 | Tensor<[19, 19]> self = ?,<br>List[int] size = [361]                        | Unknown  |
|  78 | Tensor<[2, 2, 7, 7]> self = ?,<br>List[int] size = [4, 49]                  | Unknown  |
|  79 | Tensor<[2, 2, 8, 8]> self = ?,<br>List[int] size = [4, 64]                  | Unknown  |
|  80 | Tensor<[2, 2]> self = ?,<br>List[int] size = [4]                            | Unknown  |
|  81 | Tensor<[2, 7, 8, 64]> self = ?,<br>List[int] size = [2, 7, 512]             | Unknown  |
|  82 | Tensor<[20, 20]> self = ?,<br>List[int] size = [400]                        | Unknown  |
|  83 | Tensor<[25, 34]> self = ?,<br>List[int] size = [850]                        | Unknown  |
|  84 | Tensor<[3, 3]> self = ?,<br>List[int] size = [9]                            | Unknown  |
|  85 | Tensor<[38, 38]> self = ?,<br>List[int] size = [1444]                       | Unknown  |
|  86 | Tensor<[4, 12, 32, 49]> self = ?,<br>List[int] size = [48, 32, 49]          | Unknown  |
|  87 | Tensor<[4, 12, 32, 64]> self = ?,<br>List[int] size = [48, 32, 64]          | Unknown  |
|  88 | Tensor<[4, 12, 49, 32]> self = ?,<br>List[int] size = [48, 49, 32]          | Unknown  |
|  89 | Tensor<[4, 12, 64, 32]> self = ?,<br>List[int] size = [48, 64, 32]          | Unknown  |
|  90 | Tensor<[4, 16, 32, 49]> self = ?,<br>List[int] size = [64, 32, 49]          | Unknown  |
|  91 | Tensor<[4, 16, 32, 64]> self = ?,<br>List[int] size = [64, 32, 64]          | Unknown  |
|  92 | Tensor<[4, 16, 49, 32]> self = ?,<br>List[int] size = [64, 49, 32]          | Unknown  |
|  93 | Tensor<[4, 16, 64, 32]> self = ?,<br>List[int] size = [64, 64, 32]          | Unknown  |
|  94 | Tensor<[4, 4, 7, 7]> self = ?,<br>List[int] size = [16, 49]                 | Unknown  |
|  95 | Tensor<[4, 4, 8, 8]> self = ?,<br>List[int] size = [16, 64]                 | Unknown  |
|  96 | Tensor<[5, 5]> self = ?,<br>List[int] size = [25]                           | Unknown  |
|  97 | Tensor<[50, 68]> self = ?,<br>List[int] size = [3400]                       | Unknown  |
|  98 | Tensor<[64, 3, 32, 49]> self = ?,<br>List[int] size = [192, 32, 49]         | Unknown  |
|  99 | Tensor<[64, 3, 32, 64]> self = ?,<br>List[int] size = [192, 32, 64]         | Unknown  |
| 100 | Tensor<[64, 3, 49, 32]> self = ?,<br>List[int] size = [192, 49, 32]         | Unknown  |
| 101 | Tensor<[64, 3, 64, 32]> self = ?,<br>List[int] size = [192, 64, 32]         | Unknown  |
| 102 | Tensor<[64, 4, 32, 49]> self = ?,<br>List[int] size = [256, 32, 49]         | Unknown  |
| 103 | Tensor<[64, 4, 32, 64]> self = ?,<br>List[int] size = [256, 32, 64]         | Unknown  |
| 104 | Tensor<[64, 4, 49, 32]> self = ?,<br>List[int] size = [256, 49, 32]         | Unknown  |
| 105 | Tensor<[64, 4, 64, 32]> self = ?,<br>List[int] size = [256, 64, 32]         | Unknown  |
| 106 | Tensor<[7, 9]> self = ?,<br>List[int] size = [63]                           | Unknown  |
| 107 | Tensor<[8, 8, 7, 7]> self = ?,<br>List[int] size = [64, 49]                 | Unknown  |
| 108 | Tensor<[8, 8, 8, 8]> self = ?,<br>List[int] size = [64, 64]                 | Unknown  |
### aten.abs.default
|    | ATen Input Variations     | Status   |
|---:|:--------------------------|:---------|
|  0 | Tensor<[10, 10]> self = ? | Unknown  |
|  1 | Tensor<[15, 15]> self = ? | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 0.5                      | Unknown  |
|  1 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.030000000000000027 | Unknown  |
|  2 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                        | Unknown  |
|  3 | Tensor<[1, 1, 40]> self = ?,<br>Tensor other = 1e-06                       | Unknown  |
|  4 | Tensor<[1, 10, 1]> self = ?,<br>Tensor other = 1e-06                       | Unknown  |
|  5 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?           | Unknown  |
|  6 | Tensor<[1, 10]> self = ?,<br>Tensor other = 0                              | Unknown  |
|  7 | Tensor<[1, 12, 128]> self = ?,<br>Tensor<[1, 12, 128]> other = ?           | Unknown  |
|  8 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor<[1, 12, 197, 197]> other = ? | Unknown  |
|  9 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 1.0                      | Unknown  |
| 10 | Tensor<[1, 128, 75, 75]> self = ?,<br>Tensor<[1, 128, 75, 75]> other = ?   | Unknown  |
| 11 | Tensor<[1, 1370, 1280]> self = ?,<br>Tensor<[1, 1370, 1280]> other = ?     | Unknown  |
| 12 | Tensor<[1, 14, 128]> self = ?,<br>Tensor<[1, 14, 128]> other = ?           | Unknown  |
| 13 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 1.0                      | Unknown  |
| 14 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 1.0                      | Unknown  |
| 15 | Tensor<[1, 15, 1]> self = ?,<br>Tensor other = 1e-06                       | Unknown  |
| 16 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1500, 768]> other = ?          | Unknown  |
| 17 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> other = ? | Unknown  |
| 18 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor<[1, 16, 197, 197]> other = ? | Unknown  |
| 19 | Tensor<[1, 16, 768]> self = ?,<br>Tensor<[1, 16, 768]> other = ?           | Unknown  |
| 20 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 16384, 32]> other = ?       | Unknown  |
| 21 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor<[1, 19, 1024]> other = ?         | Unknown  |
| 22 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 192, 32, 42]> other = ?   | Unknown  |
| 23 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 19200, 64]> other = ?       | Unknown  |
| 24 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?       | Unknown  |
| 25 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?         | Unknown  |
| 26 | Tensor<[1, 19]> self = ?,<br>Tensor other = 2                              | Unknown  |
| 27 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                              | Unknown  |
| 28 | Tensor<[1, 2048, 768]> self = ?,<br>Tensor<[2048, 768]> other = ?          | Unknown  |
| 29 | Tensor<[1, 224, 56, 56]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?   | Unknown  |
| 30 | Tensor<[1, 232, 56, 56]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?   | Unknown  |
| 31 | Tensor<[1, 24, 28, 28]> self = ?,<br>Tensor<[1, 24, 28, 28]> other = ?     | Unknown  |
| 32 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> other = ?     | Unknown  |
| 33 | Tensor<[1, 24, 60, 60]> self = ?,<br>Tensor<[1, 24, 60, 60]> other = ?     | Unknown  |
| 34 | Tensor<[1, 24, 65, 65]> self = ?,<br>Tensor<[1, 24, 65, 65]> other = ?     | Unknown  |
| 35 | Tensor<[1, 24, 768]> self = ?,<br>Tensor<[1, 24, 768]> other = ?           | Unknown  |
| 36 | Tensor<[1, 25, 768]> self = ?,<br>Tensor<[1, 25, 768]> other = ?           | Unknown  |
| 37 | Tensor<[1, 256, 1024]> self = ?,<br>Tensor<[1, 256, 1024]> other = ?       | Unknown  |
| 38 | Tensor<[1, 256, 512]> self = ?,<br>Tensor<[1, 256, 512]> other = ?         | Unknown  |
| 39 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?   | Unknown  |
| 40 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[1, 3, 300, 300]> other = ?   | Unknown  |
| 41 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[1, 3, 320, 320]> other = ?   | Unknown  |
| 42 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[1, 3, 800, 1066]> other = ? | Unknown  |
| 43 | Tensor<[1, 32, 1536]> self = ?,<br>Tensor<[1, 32, 1536]> other = ?         | Unknown  |
| 44 | Tensor<[1, 32, 1]> self = ?,<br>Tensor other = 1e-06                       | Unknown  |
| 45 | Tensor<[1, 32, 32, 128]> self = ?,<br>Tensor<[1, 32, 32, 128]> other = ?   | Unknown  |
| 46 | Tensor<[1, 32, 56, 56]> self = ?,<br>Tensor<[1, 32, 56, 56]> other = ?     | Unknown  |
| 47 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1                        | Unknown  |
| 48 | Tensor<[1, 32, 75, 75]> self = ?,<br>Tensor<[1, 32, 75, 75]> other = ?     | Unknown  |
| 49 | Tensor<[1, 32, 95, 95]> self = ?,<br>Tensor<[1, 32, 95, 95]> other = ?     | Unknown  |
| 50 | Tensor<[1, 336, 56, 56]> self = ?,<br>Tensor<[1, 336, 56, 56]> other = ?   | Unknown  |
| 51 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 1.0                      | Unknown  |
| 52 | Tensor<[1, 45, 768]> self = ?,<br>Tensor<[1, 45, 768]> other = ?           | Unknown  |
| 53 | Tensor<[1, 48, 56, 56]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?     | Unknown  |
| 54 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 16, 32]> other = ?       | Unknown  |
| 55 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 1.0                       | Unknown  |
| 56 | Tensor<[1, 50, 1024]> self = ?,<br>Tensor<[1, 50, 1024]> other = ?         | Unknown  |
| 57 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<[1, 50, 768]> other = ?           | Unknown  |
| 58 | Tensor<[1, 528, 96, 96]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?   | Unknown  |
| 59 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor other = 0.0                      | Unknown  |
| 60 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor other = 1e-05                    | Unknown  |
| 61 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?     | Unknown  |
| 62 | Tensor<[1, 64, 56, 56]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?     | Unknown  |
| 63 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 1.0                       | Unknown  |
| 64 | Tensor<[1, 7, 768]> self = ?,<br>Tensor<[1, 7, 768]> other = ?             | Unknown  |
| 65 | Tensor<[1, 71, 7, 64]> self = ?,<br>Tensor<[1, 71, 7, 64]> other = ?       | Unknown  |
| 66 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?     | Unknown  |
| 67 | Tensor<[1, 768, 384]> self = ?,<br>Tensor<[384]> other = ?                 | Unknown  |
| 68 | Tensor<[1, 8, 768]> self = ?,<br>Tensor<[1, 8, 768]> other = ?             | Unknown  |
| 69 | Tensor<[1, 80, 56, 56]> self = ?,<br>Tensor<[1, 80, 56, 56]> other = ?     | Unknown  |
| 70 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?             | Unknown  |
| 71 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 1.0                      | Unknown  |
| 72 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 1.0                       | Unknown  |
| 73 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 1.0                       | Unknown  |
| 74 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 1.0                       | Unknown  |
| 75 | Tensor<[1, 96, 56, 56]> self = ?,<br>Tensor<[1, 96, 56, 56]> other = ?     | Unknown  |
| 76 | Tensor<[10, 10]> self = ?,<br>Tensor other = 0                             | Unknown  |
| 77 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                   | Unknown  |
| 78 | Tensor<[128]> self = ?,<br>Tensor other = 0.5                              | Unknown  |
| 79 | Tensor<[12]> self = ?,<br>Tensor other = 0.0                               | Unknown  |
| 80 | Tensor<[15, 15]> self = ?,<br>Tensor other = 0                             | Unknown  |
| 81 | Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?                   | Unknown  |
| 82 | Tensor<[23]> self = ?,<br>Tensor other = 0.0                               | Unknown  |
| 83 | Tensor<[24, 24]> self = ?,<br>Tensor other = 160                           | Unknown  |
| 84 | Tensor<[300]> self = ?,<br>Tensor other = 0.5                              | Unknown  |
| 85 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                               | Unknown  |
| 86 | Tensor<[320]> self = ?,<br>Tensor other = 0.5                              | Unknown  |
| 87 | Tensor<[50]> self = ?,<br>Tensor other = 0.0                               | Unknown  |
| 88 | Tensor<[56]> self = ?,<br>Tensor other = 0.0                               | Unknown  |
| 89 | Tensor<[64, 3, 49, 49]> self = ?,<br>Tensor<[1, 3, 49, 49]> other = ?      | Unknown  |
| 90 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[1, 3, 64, 64]> other = ?      | Unknown  |
| 91 | Tensor<[64, 4, 49, 49]> self = ?,<br>Tensor<[1, 4, 49, 49]> other = ?      | Unknown  |
| 92 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[1, 4, 64, 64]> other = ?      | Unknown  |
| 93 | Tensor<[800]> self = ?,<br>Tensor other = 0.5                              | Unknown  |
| 94 | Tensor<[]> self = ?,<br>Tensor other = 1                                   | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1008]> mat1 = ?,<br>Tensor<[1008, 1000]> mat2 = ?    | Unknown  |
|  1 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1000]> mat2 = ?    | Unknown  |
|  2 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 1000]> mat2 = ?    | Unknown  |
|  3 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1512]> mat1 = ?,<br>Tensor<[1512, 1000]> mat2 = ?    | Unknown  |
|  4 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1536]> mat1 = ?,<br>Tensor<[1536, 1000]> mat2 = ?    | Unknown  |
|  5 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1664]> mat1 = ?,<br>Tensor<[1664, 1000]> mat2 = ?    | Unknown  |
|  6 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1920]> mat1 = ?,<br>Tensor<[1920, 1000]> mat2 = ?    | Unknown  |
|  7 | Tensor<[1000]> self = ?,<br>Tensor<[1, 2016]> mat1 = ?,<br>Tensor<[2016, 1000]> mat2 = ?    | Unknown  |
|  8 | Tensor<[1000]> self = ?,<br>Tensor<[1, 2048]> mat1 = ?,<br>Tensor<[2048, 1000]> mat2 = ?    | Unknown  |
|  9 | Tensor<[1000]> self = ?,<br>Tensor<[1, 2208]> mat1 = ?,<br>Tensor<[2208, 1000]> mat2 = ?    | Unknown  |
| 10 | Tensor<[1000]> self = ?,<br>Tensor<[1, 2520]> mat1 = ?,<br>Tensor<[2520, 1000]> mat2 = ?    | Unknown  |
| 11 | Tensor<[1000]> self = ?,<br>Tensor<[1, 3024]> mat1 = ?,<br>Tensor<[3024, 1000]> mat2 = ?    | Unknown  |
| 12 | Tensor<[1000]> self = ?,<br>Tensor<[1, 3712]> mat1 = ?,<br>Tensor<[3712, 1000]> mat2 = ?    | Unknown  |
| 13 | Tensor<[1000]> self = ?,<br>Tensor<[1, 400]> mat1 = ?,<br>Tensor<[400, 1000]> mat2 = ?      | Unknown  |
| 14 | Tensor<[1000]> self = ?,<br>Tensor<[1, 440]> mat1 = ?,<br>Tensor<[440, 1000]> mat2 = ?      | Unknown  |
| 15 | Tensor<[1000]> self = ?,<br>Tensor<[1, 512]> mat1 = ?,<br>Tensor<[512, 1000]> mat2 = ?      | Unknown  |
| 16 | Tensor<[1000]> self = ?,<br>Tensor<[1, 672]> mat1 = ?,<br>Tensor<[672, 1000]> mat2 = ?      | Unknown  |
| 17 | Tensor<[1000]> self = ?,<br>Tensor<[1, 7392]> mat1 = ?,<br>Tensor<[7392, 1000]> mat2 = ?    | Unknown  |
| 18 | Tensor<[1000]> self = ?,<br>Tensor<[1, 784]> mat1 = ?,<br>Tensor<[784, 1000]> mat2 = ?      | Unknown  |
| 19 | Tensor<[1000]> self = ?,<br>Tensor<[1, 888]> mat1 = ?,<br>Tensor<[888, 1000]> mat2 = ?      | Unknown  |
| 20 | Tensor<[1000]> self = ?,<br>Tensor<[1, 912]> mat1 = ?,<br>Tensor<[912, 1000]> mat2 = ?      | Unknown  |
| 21 | Tensor<[1024]> self = ?,<br>Tensor<[1, 576]> mat1 = ?,<br>Tensor<[576, 1024]> mat2 = ?      | Unknown  |
| 22 | Tensor<[1024]> self = ?,<br>Tensor<[19, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ?   | Unknown  |
| 23 | Tensor<[1024]> self = ?,<br>Tensor<[197, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ?  | Unknown  |
| 24 | Tensor<[1024]> self = ?,<br>Tensor<[256, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ?  | Unknown  |
| 25 | Tensor<[1024]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 1024]> mat2 = ?      | Unknown  |
| 26 | Tensor<[1280]> self = ?,<br>Tensor<[1, 960]> mat1 = ?,<br>Tensor<[960, 1280]> mat2 = ?      | Unknown  |
| 27 | Tensor<[128]> self = ?,<br>Tensor<[1, 9216]> mat1 = ?,<br>Tensor<[9216, 128]> mat2 = ?      | Unknown  |
| 28 | Tensor<[192]> self = ?,<br>Tensor<[1445, 192]> mat1 = ?,<br>Tensor<[192, 192]> mat2 = ?     | Unknown  |
| 29 | Tensor<[196]> self = ?,<br>Tensor<[768, 384]> mat1 = ?,<br>Tensor<[384, 196]> mat2 = ?      | Unknown  |
| 30 | Tensor<[2048]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 2048]> mat2 = ?      | Unknown  |
| 31 | Tensor<[2304]> self = ?,<br>Tensor<[197, 768]> mat1 = ?,<br>Tensor<[768, 2304]> mat2 = ?    | Unknown  |
| 32 | Tensor<[2304]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 2304]> mat2 = ?     | Unknown  |
| 33 | Tensor<[2304]> self = ?,<br>Tensor<[7, 768]> mat1 = ?,<br>Tensor<[768, 2304]> mat2 = ?      | Unknown  |
| 34 | Tensor<[256]> self = ?,<br>Tensor<[256, 1280]> mat1 = ?,<br>Tensor<[1280, 256]> mat2 = ?    | Unknown  |
| 35 | Tensor<[256]> self = ?,<br>Tensor<[920, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?      | Unknown  |
| 36 | Tensor<[288]> self = ?,<br>Tensor<[3136, 96]> mat1 = ?,<br>Tensor<[96, 288]> mat2 = ?       | Unknown  |
| 37 | Tensor<[3072]> self = ?,<br>Tensor<[197, 1024]> mat1 = ?,<br>Tensor<[1024, 3072]> mat2 = ?  | Unknown  |
| 38 | Tensor<[3072]> self = ?,<br>Tensor<[50, 1024]> mat1 = ?,<br>Tensor<[1024, 3072]> mat2 = ?   | Unknown  |
| 39 | Tensor<[32]> self = ?,<br>Tensor<[16384, 32]> mat1 = ?,<br>Tensor<[32, 32]> mat2 = ?        | Unknown  |
| 40 | Tensor<[3840]> self = ?,<br>Tensor<[1370, 1280]> mat1 = ?,<br>Tensor<[1280, 3840]> mat2 = ? | Unknown  |
| 41 | Tensor<[384]> self = ?,<br>Tensor<[3136, 128]> mat1 = ?,<br>Tensor<[128, 384]> mat2 = ?     | Unknown  |
| 42 | Tensor<[4096]> self = ?,<br>Tensor<[1, 25088]> mat1 = ?,<br>Tensor<[25088, 4096]> mat2 = ?  | Unknown  |
| 43 | Tensor<[4096]> self = ?,<br>Tensor<[5, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ?    | Unknown  |
| 44 | Tensor<[4096]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 4096]> mat2 = ?      | Unknown  |
| 45 | Tensor<[4608]> self = ?,<br>Tensor<[32, 1536]> mat1 = ?,<br>Tensor<[1536, 4608]> mat2 = ?   | Unknown  |
| 46 | Tensor<[512]> self = ?,<br>Tensor<[225, 2]> mat1 = ?,<br>Tensor<[2, 512]> mat2 = ?          | Unknown  |
| 47 | Tensor<[512]> self = ?,<br>Tensor<[256, 768]> mat1 = ?,<br>Tensor<[768, 512]> mat2 = ?      | Unknown  |
| 48 | Tensor<[64]> self = ?,<br>Tensor<[19200, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ?        | Unknown  |
| 49 | Tensor<[768]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?        | Unknown  |
| 50 | Tensor<[768]> self = ?,<br>Tensor<[10, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?       | Unknown  |
| 51 | Tensor<[768]> self = ?,<br>Tensor<[12, 128]> mat1 = ?,<br>Tensor<[128, 768]> mat2 = ?       | Unknown  |
| 52 | Tensor<[768]> self = ?,<br>Tensor<[14, 128]> mat1 = ?,<br>Tensor<[128, 768]> mat2 = ?       | Unknown  |
| 53 | Tensor<[768]> self = ?,<br>Tensor<[1500, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?     | Unknown  |
| 54 | Tensor<[768]> self = ?,<br>Tensor<[16, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?       | Unknown  |
| 55 | Tensor<[768]> self = ?,<br>Tensor<[197, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?      | Unknown  |
| 56 | Tensor<[768]> self = ?,<br>Tensor<[201, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?      | Unknown  |
| 57 | Tensor<[768]> self = ?,<br>Tensor<[24, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?       | Unknown  |
| 58 | Tensor<[768]> self = ?,<br>Tensor<[25, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?       | Unknown  |
| 59 | Tensor<[768]> self = ?,<br>Tensor<[45, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?       | Unknown  |
| 60 | Tensor<[768]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?       | Unknown  |
| 61 | Tensor<[768]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 768]> mat2 = ?        | Unknown  |
### aten.all.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[1, 7]> self = ? | Unknown  |
### aten.all.dim
|    | ATen Input Variations                                | Status   |
|---:|:-----------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = -1 | Unknown  |
### aten.any.default
|    | ATen Input Variations    | Status   |
|---:|:-------------------------|:---------|
|  0 | Tensor<[1, 32]> self = ? | Unknown  |
### aten.arange.default
|    | ATen Input Variations                                                                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number end = 1,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                               | Unknown  |
|  1 | number end = 10,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  |
|  2 | number end = 12,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                              | Unknown  |
|  3 | number end = 12,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False      | Unknown  |
|  4 | number end = 128,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False     | Unknown  |
|  5 | number end = 15,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  |
|  6 | number end = 2,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                               | Unknown  |
|  7 | number end = 23,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False      | Unknown  |
|  8 | number end = 30,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False      | Unknown  |
|  9 | number end = 300,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False     | Unknown  |
| 10 | number end = 320,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False     | Unknown  |
| 11 | number end = 56,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False      | Unknown  |
| 12 | number end = 800,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False     | Unknown  |
| 13 | number<s0 + 1> end = ?,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.arange.start
|    | ATen Input Variations                                                                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number start = 0,<br>number end = 136,<br>Optional[int] dtype = torch.int32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
|  1 | number start = 0,<br>number end = 19,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | Unknown  |
|  2 | number start = 0,<br>number end = 20,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                        | Unknown  |
|  3 | number start = 0,<br>number end = 2048,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                      | Unknown  |
|  4 | number start = 0,<br>number end = 24,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                        | Unknown  |
|  5 | number start = 0,<br>number end = 32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                        | Unknown  |
|  6 | number start = 0,<br>number end = 38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                        | Unknown  |
|  7 | number start = 0,<br>number end = 7,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False   | Unknown  |
|  8 | number start = 1,<br>number end = 17,<br>Optional[int] dtype = torch.int32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | Unknown  |
### aten.argmax.default
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 51865]> self = ?,<br>Optional[int] dim = -1 | Unknown  |
|  1 | Tensor<[1, 7]> self = ?,<br>Optional[int] dim = -1     | Unknown  |
|  2 | Tensor<[2, 7]> self = ?,<br>Optional[int] dim = -1     | Unknown  |
### aten.as_strided.default
|    | ATen Input Variations                                                                                              | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int] size = [1, 1024, 1, 1],<br>List[int] stride = [1024, 1, 1024, 1024] | Unknown  |
|  1 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int] size = [1, 768, 1, 1],<br>List[int] stride = [768, 1, 768, 768]      | Unknown  |
### aten.avg_pool2d.default
|    | ATen Input Variations                                                                                                                                                                           | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128, 56, 56]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]                                                                                              | Unknown  |
|  1 | Tensor<[1, 192, 56, 56]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]                                                                                              | Unknown  |
|  2 | Tensor<[1, 24, 56, 56]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]                                                                                               | Unknown  |
|  3 | Tensor<[1, 384, 35, 35]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>bool ceil_mode = False,<br>bool count_include_pad = False | Unknown  |
### aten.baddbmm.default
|    | ATen Input Variations                                                                                                                                             | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 1, 32]> self = ?,<br>Tensor<[16, 32, 96]> batch1 = ?,<br>Tensor<[16, 96, 32]> batch2 = ?,<br>number beta = 1.0,<br>number alpha = 0.10206207261596577 | Unknown  |
|  1 | Tensor<[8, 1, 920]> self = ?,<br>Tensor<[8, 920, 32]> batch1 = ?,<br>Tensor<[8, 32, 920]> batch2 = ?                                                              | Unknown  |
### aten.bernoulli.p
|    | ATen Input Variations                       | Status   |
|---:|:--------------------------------------------|:---------|
|  0 | Tensor<[1, 256]> self = ?,<br>float p = 0.5 | Unknown  |
### aten.bitwise_not.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 1]> self = ? | Unknown  |
|  1 | Tensor<[1, 23, 40]> self = ?     | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 32, 256]> mat2 = ? | Unknown  |
|  1 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 64, 300]> mat2 = ? | Unknown  |
|  2 | Tensor<[1, 64, 1]> self = ?,<br>Tensor<[1, 1, 32]> mat2 = ?       | Unknown  |
|  3 | Tensor<[12, 10, 64]> self = ?,<br>Tensor<[12, 64, 10]> mat2 = ?   | Unknown  |
|  4 | Tensor<[12, 12, 64]> self = ?,<br>Tensor<[12, 64, 12]> mat2 = ?   | Unknown  |
|  5 | Tensor<[12, 14, 64]> self = ?,<br>Tensor<[12, 64, 14]> mat2 = ?   | Unknown  |
|  6 | Tensor<[12, 16, 64]> self = ?,<br>Tensor<[12, 64, 16]> mat2 = ?   | Unknown  |
|  7 | Tensor<[12, 197, 64]> self = ?,<br>Tensor<[12, 64, 197]> mat2 = ? | Unknown  |
|  8 | Tensor<[12, 201, 64]> self = ?,<br>Tensor<[12, 64, 201]> mat2 = ? | Unknown  |
|  9 | Tensor<[12, 24, 64]> self = ?,<br>Tensor<[12, 64, 24]> mat2 = ?   | Unknown  |
| 10 | Tensor<[12, 25, 64]> self = ?,<br>Tensor<[12, 64, 25]> mat2 = ?   | Unknown  |
| 11 | Tensor<[12, 45, 64]> self = ?,<br>Tensor<[12, 64, 45]> mat2 = ?   | Unknown  |
| 12 | Tensor<[12, 50, 64]> self = ?,<br>Tensor<[12, 64, 50]> mat2 = ?   | Unknown  |
| 13 | Tensor<[12, 7, 64]> self = ?,<br>Tensor<[12, 64, 7]> mat2 = ?     | Unknown  |
| 14 | Tensor<[12, 8, 64]> self = ?,<br>Tensor<[12, 64, 8]> mat2 = ?     | Unknown  |
| 15 | Tensor<[12, 9, 64]> self = ?,<br>Tensor<[12, 64, 9]> mat2 = ?     | Unknown  |
| 16 | Tensor<[16, 10, 64]> self = ?,<br>Tensor<[16, 64, 10]> mat2 = ?   | Unknown  |
| 17 | Tensor<[16, 19, 64]> self = ?,<br>Tensor<[16, 64, 19]> mat2 = ?   | Unknown  |
| 18 | Tensor<[16, 197, 64]> self = ?,<br>Tensor<[16, 64, 197]> mat2 = ? | Unknown  |
| 19 | Tensor<[16, 256, 64]> self = ?,<br>Tensor<[16, 64, 256]> mat2 = ? | Unknown  |
| 20 | Tensor<[16, 32, 32]> self = ?,<br>Tensor<[16, 32, 96]> mat2 = ?   | Unknown  |
| 21 | Tensor<[16, 5, 64]> self = ?,<br>Tensor<[16, 64, 5]> mat2 = ?     | Unknown  |
| 22 | Tensor<[16, 9, 128]> self = ?,<br>Tensor<[16, 128, 9]> mat2 = ?   | Unknown  |
| 23 | Tensor<[16, 9, 64]> self = ?,<br>Tensor<[16, 64, 9]> mat2 = ?     | Unknown  |
| 24 | Tensor<[192, 49, 32]> self = ?,<br>Tensor<[192, 32, 49]> mat2 = ? | Unknown  |
| 25 | Tensor<[192, 64, 32]> self = ?,<br>Tensor<[192, 32, 64]> mat2 = ? | Unknown  |
| 26 | Tensor<[256, 49, 32]> self = ?,<br>Tensor<[256, 32, 49]> mat2 = ? | Unknown  |
| 27 | Tensor<[256, 64, 32]> self = ?,<br>Tensor<[256, 32, 64]> mat2 = ? | Unknown  |
| 28 | Tensor<[3, 1445, 64]> self = ?,<br>Tensor<[3, 64, 1445]> mat2 = ? | Unknown  |
| 29 | Tensor<[6, 15, 64]> self = ?,<br>Tensor<[6, 64, 15]> mat2 = ?     | Unknown  |
| 30 | Tensor<[64, 9, 64]> self = ?,<br>Tensor<[64, 64, 9]> mat2 = ?     | Unknown  |
| 31 | Tensor<[71, 7, 64]> self = ?,<br>Tensor<[71, 64, 7]> mat2 = ?     | Unknown  |
| 32 | Tensor<[8, 10, 64]> self = ?,<br>Tensor<[8, 64, 10]> mat2 = ?     | Unknown  |
| 33 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 2048]> mat2 = ?  | Unknown  |
| 34 | Tensor<[8, 920, 920]> self = ?,<br>Tensor<[8, 920, 32]> mat2 = ?  | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                                                                                         | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [_unsafe_view, _unsafe_view_1, _unsafe_view_2, _unsafe_view_3, _unsafe_view_4, view_6],<br>int dim = 1 | Unknown  |
|  1 | List[Tensor] tensors = [_unsafe_view, _unsafe_view_1, _unsafe_view_2, _unsafe_view_3, _unsafe_view_4, view_7],<br>int dim = 1 | Unknown  |
|  2 | List[Tensor] tensors = [_unsafe_view, _unsafe_view_1, _unsafe_view_2, _unsafe_view_3, _unsafe_view_4],<br>int dim = 1         | Unknown  |
|  3 | List[Tensor] tensors = [add, add_1, add_2],<br>int dim = 1                                                                    | Unknown  |
|  4 | List[Tensor] tensors = [add, add_1],<br>int dim = 1                                                                           | Unknown  |
|  5 | List[Tensor] tensors = [add, slice_10],<br>int dim = -1                                                                       | Unknown  |
|  6 | List[Tensor] tensors = [arg0_1, new_ones],<br>int dim = -1                                                                    | Unknown  |
|  7 | List[Tensor] tensors = [cat_2, cat_3, cat_4, cat_5, cat_6, cat_7]                                                             | Unknown  |
|  8 | List[Tensor] tensors = [clone_2, expand_1],<br>int dim = -1                                                                   | Unknown  |
|  9 | List[Tensor] tensors = [clone_46, clone_45, clone_44, clone_43],<br>int dim = 1                                               | Unknown  |
| 10 | List[Tensor] tensors = [convolution_10, relu_7],<br>int dim = 1                                                               | Unknown  |
| 11 | List[Tensor] tensors = [convolution_84, add_86],<br>int dim = 1                                                               | Unknown  |
| 12 | List[Tensor] tensors = [expand, permute],<br>int dim = 1                                                                      | Unknown  |
| 13 | List[Tensor] tensors = [expand, transpose, expand_1],<br>int dim = 1                                                          | Unknown  |
| 14 | List[Tensor] tensors = [expand, transpose],<br>int dim = 1                                                                    | Unknown  |
| 15 | List[Tensor] tensors = [getitem_3],<br>int dim = 1                                                                            | Unknown  |
| 16 | List[Tensor] tensors = [getitem_9, relu_3],<br>int dim = 1                                                                    | Unknown  |
| 17 | List[Tensor] tensors = [mul, mul_1, mul_2, mul_3],<br>int dim = -1                                                            | Unknown  |
| 18 | List[Tensor] tensors = [neg, slice_1],<br>int dim = -1                                                                        | Unknown  |
| 19 | List[Tensor] tensors = [ones_1, _to_copy],<br>int dim = -1                                                                    | Unknown  |
| 20 | List[Tensor] tensors = [primals_1]                                                                                            | Unknown  |
| 21 | List[Tensor] tensors = [relu_1, relu_2],<br>int dim = 1                                                                       | Unknown  |
| 22 | List[Tensor] tensors = [relu_2, relu_4, relu_5, relu_6],<br>int dim = 1                                                       | Unknown  |
| 23 | List[Tensor] tensors = [relu_6, relu_4],<br>int dim = 1                                                                       | Unknown  |
| 24 | List[Tensor] tensors = [slice_7, slice_10, slice_13, slice_16],<br>int dim = -1                                               | Unknown  |
| 25 | List[Tensor] tensors = [transpose_3, transpose_3],<br>int dim = -1                                                            | Unknown  |
| 26 | List[Tensor] tensors = [view_14, view_19, view_24, view_29, view_34]                                                          | Unknown  |
| 27 | List[Tensor] tensors = [view_213, view_212],<br>int dim = 3                                                                   | Unknown  |
| 28 | List[Tensor] tensors = [view_226, view_231, view_236, view_241, view_246]                                                     | Unknown  |
### aten.ceil.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[128]> self = ?  | Unknown  |
|  1 | Tensor<[300]> self = ?  | Unknown  |
|  2 | Tensor<[30]> self = ?   | Unknown  |
|  3 | Tensor<[320]> self = ?  | Unknown  |
|  4 | Tensor<[800]> self = ?  | Unknown  |
### aten.clamp.default
|    | ATen Input Variations                                                                                   | Status   |
|---:|:--------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[0, 1]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 4.135166556742356    | Unknown  |
|  1 | Tensor<[0, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 1066                    | Unknown  |
|  2 | Tensor<[1, 1, 1, 42]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 82               | Unknown  |
|  3 | Tensor<[1, 1, 32, 1]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 49               | Unknown  |
|  4 | Tensor<[1066]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 639                  | Unknown  |
|  5 | Tensor<[120]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 59                    | Unknown  |
|  6 | Tensor<[128]> self = ?,<br>Optional[number] min = 0.0                                                   | Unknown  |
|  7 | Tensor<[128]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 127                   | Unknown  |
|  8 | Tensor<[160]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 79                    | Unknown  |
|  9 | Tensor<[240]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 119                   | Unknown  |
| 10 | Tensor<[3, 1, 1]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 4.605170185988092 | Unknown  |
| 11 | Tensor<[300]> self = ?,<br>Optional[number] min = 0.0                                                   | Unknown  |
| 12 | Tensor<[300]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 479                   | Unknown  |
| 13 | Tensor<[30]> self = ?,<br>Optional[number] min = 0.0                                                    | Unknown  |
| 14 | Tensor<[30]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 14                     | Unknown  |
| 15 | Tensor<[320]> self = ?,<br>Optional[number] min = 0.0                                                   | Unknown  |
| 16 | Tensor<[320]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 159                   | Unknown  |
| 17 | Tensor<[320]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 319                   | Unknown  |
| 18 | Tensor<[320]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 479                   | Unknown  |
| 19 | Tensor<[3234, 1]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 4.135166556742356 | Unknown  |
| 20 | Tensor<[3234, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 320                  | Unknown  |
| 21 | Tensor<[4, 1, 1]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 4.605170185988092 | Unknown  |
| 22 | Tensor<[4, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 1                       | Unknown  |
| 23 | Tensor<[40]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 19                     | Unknown  |
| 24 | Tensor<[480]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 239                   | Unknown  |
| 25 | Tensor<[6, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 1                       | Unknown  |
| 26 | Tensor<[60]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 29                     | Unknown  |
| 27 | Tensor<[640]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 319                   | Unknown  |
| 28 | Tensor<[800]> self = ?,<br>Optional[number] min = 0.0                                                   | Unknown  |
| 29 | Tensor<[800]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 479                   | Unknown  |
| 30 | Tensor<[80]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 39                     | Unknown  |
| 31 | Tensor<[8732, 1]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 4.135166556742356 | Unknown  |
| 32 | Tensor<[8732, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 300                  | Unknown  |
### aten.clamp_min.default
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 38, 38]> self = ?,<br>number min = 1e-12 | Unknown  |
|  1 | Tensor<[1, 1]> self = ?,<br>number min = 1e-12         | Unknown  |
|  2 | Tensor<[64, 3, 64, 1]> self = ?,<br>number min = 1e-12 | Unknown  |
|  3 | Tensor<[64, 4, 64, 1]> self = ?,<br>number min = 1e-12 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?                                                               | Unknown  |
|  1 | Tensor<[1, 1, 19200, 300]> self = ?                                                               | Unknown  |
|  2 | Tensor<[1, 1, 45]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Unknown  |
|  3 | Tensor<[1, 10, 1024]> self = ?                                                                    | Unknown  |
|  4 | Tensor<[1, 10, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  |
|  5 | Tensor<[1, 10, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  |
|  6 | Tensor<[1, 10, 512]> self = ?                                                                     | Unknown  |
|  7 | Tensor<[1, 10, 768]> self = ?                                                                     | Unknown  |
|  8 | Tensor<[1, 10, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  |
|  9 | Tensor<[1, 100, 136, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  |
| 10 | Tensor<[1, 1024, 512]> self = ?                                                                   | Unknown  |
| 11 | Tensor<[1, 1024]> self = ?                                                                        | Unknown  |
| 12 | Tensor<[1, 12, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  |
| 13 | Tensor<[1, 12, 128]> self = ?                                                                     | Unknown  |
| 14 | Tensor<[1, 12, 1500, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  |
| 15 | Tensor<[1, 12, 24, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  |
| 16 | Tensor<[1, 12, 50, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  |
| 17 | Tensor<[1, 12, 64, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  |
| 18 | Tensor<[1, 1280]> self = ?                                                                        | Unknown  |
| 19 | Tensor<[1, 1370, 1280]> self = ?                                                                  | Unknown  |
| 20 | Tensor<[1, 14, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  |
| 21 | Tensor<[1, 14, 128]> self = ?                                                                     | Unknown  |
| 22 | Tensor<[1, 1445, 192]> self = ?                                                                   | Unknown  |
| 23 | Tensor<[1, 1445, 3, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  |
| 24 | Tensor<[1, 15, 512]> self = ?                                                                     | Unknown  |
| 25 | Tensor<[1, 15, 6, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  |
| 26 | Tensor<[1, 1500, 768]> self = ?                                                                   | Unknown  |
| 27 | Tensor<[1, 1536]> self = ?                                                                        | Unknown  |
| 28 | Tensor<[1, 16, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  |
| 29 | Tensor<[1, 16, 16, 16, 16, 3]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
| 30 | Tensor<[1, 16, 19, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  |
| 31 | Tensor<[1, 16, 32, 32]> self = ?                                                                  | Unknown  |
| 32 | Tensor<[1, 16, 768]> self = ?                                                                     | Unknown  |
| 33 | Tensor<[1, 19, 1024]> self = ?                                                                    | Unknown  |
| 34 | Tensor<[1, 192, 32, 42]> self = ?,<br>Optional[int] memory_format = torch.channels_last           | Unknown  |
| 35 | Tensor<[1, 197, 1024]> self = ?                                                                   | Unknown  |
| 36 | Tensor<[1, 197, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  |
| 37 | Tensor<[1, 197, 768]> self = ?                                                                    | Unknown  |
| 38 | Tensor<[1, 20, 20, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  |
| 39 | Tensor<[1, 201, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  |
| 40 | Tensor<[1, 2048]> self = ?                                                                        | Unknown  |
| 41 | Tensor<[1, 24, 768]> self = ?                                                                     | Unknown  |
| 42 | Tensor<[1, 25, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  |
| 43 | Tensor<[1, 25, 768]> self = ?                                                                     | Unknown  |
| 44 | Tensor<[1, 256, 1024]> self = ?                                                                   | Unknown  |
| 45 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.channels_last         | Unknown  |
| 46 | Tensor<[1, 256, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  |
| 47 | Tensor<[1, 256, 8, 160]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  |
| 48 | Tensor<[1, 32, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  |
| 49 | Tensor<[1, 32, 16, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  |
| 50 | Tensor<[1, 32, 32, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  |
| 51 | Tensor<[1, 38, 38, 4, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  |
| 52 | Tensor<[1, 4096]> self = ?                                                                        | Unknown  |
| 53 | Tensor<[1, 45, 768]> self = ?                                                                     | Unknown  |
| 54 | Tensor<[1, 5, 1024]> self = ?                                                                     | Unknown  |
| 55 | Tensor<[1, 5, 4, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  |
| 56 | Tensor<[1, 50, 1024]> self = ?                                                                    | Unknown  |
| 57 | Tensor<[1, 50, 768]> self = ?                                                                     | Unknown  |
| 58 | Tensor<[1, 512, 1, 1]> self = ?                                                                   | Unknown  |
| 59 | Tensor<[1, 64, 12, 12]> self = ?                                                                  | Unknown  |
| 60 | Tensor<[1, 64, 120, 160]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  |
| 61 | Tensor<[1, 7, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  |
| 62 | Tensor<[1, 7, 4544]> self = ?                                                                     | Unknown  |
| 63 | Tensor<[1, 7, 71, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  |
| 64 | Tensor<[1, 7, 768]> self = ?                                                                      | Unknown  |
| 65 | Tensor<[1, 768, 384]> self = ?                                                                    | Unknown  |
| 66 | Tensor<[1, 8, 256, 2048]> self = ?                                                                | Unknown  |
| 67 | Tensor<[1, 8, 768]> self = ?                                                                      | Unknown  |
| 68 | Tensor<[1, 9, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  |
| 69 | Tensor<[1, 9, 128]> self = ?                                                                      | Unknown  |
| 70 | Tensor<[1, 9, 16, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  |
| 71 | Tensor<[1, 9, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  |
| 72 | Tensor<[1, 9, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  |
| 73 | Tensor<[12, 197, 197]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  |
| 74 | Tensor<[12, 50, 50]> self = ?                                                                     | Unknown  |
| 75 | Tensor<[16, 197, 197]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  |
| 76 | Tensor<[3, 1370, 1, 1280]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  |
| 77 | Tensor<[3, 197, 1, 1024]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  |
| 78 | Tensor<[3, 197, 1, 768]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  |
| 79 | Tensor<[3, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Unknown  |
| 80 | Tensor<[3, 50, 1, 1024]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  |
| 81 | Tensor<[3, 50, 1, 768]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  |
| 82 | Tensor<[3, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Unknown  |
| 83 | Tensor<[4, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Unknown  |
| 84 | Tensor<[4, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Unknown  |
| 85 | Tensor<[64, 3, 49, 49]> self = ?                                                                  | Unknown  |
| 86 | Tensor<[64, 3, 64, 64]> self = ?                                                                  | Unknown  |
| 87 | Tensor<[64, 4, 49, 49]> self = ?                                                                  | Unknown  |
| 88 | Tensor<[64, 4, 64, 64]> self = ?                                                                  | Unknown  |
| 89 | Tensor<[920, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Unknown  |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                           | Status   |
|---:|:------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 144, 56, 56]> self = ?,<br>List[int] pad = [1, 2, 1, 2],<br>number value = 0.0       | Unknown  |
|  1 | Tensor<[1, 144, 60, 60]> self = ?,<br>List[int] pad = [1, 2, 1, 2],<br>number value = 0.0       | Unknown  |
|  2 | Tensor<[1, 144, 65, 65]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0       | Unknown  |
|  3 | Tensor<[1, 192, 75, 75]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0       | Unknown  |
|  4 | Tensor<[1, 192, 95, 95]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0       | Unknown  |
|  5 | Tensor<[1, 288, 33, 33]> self = ?,<br>List[int] pad = [1, 1, 1, 1],<br>number value = 0.0       | Unknown  |
|  6 | Tensor<[1, 3, 224, 224]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | Unknown  |
|  7 | Tensor<[1, 3, 240, 240]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | Unknown  |
|  8 | Tensor<[1, 3, 260, 260]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | Unknown  |
|  9 | Tensor<[1, 3, 300, 300]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | Unknown  |
| 10 | Tensor<[1, 3, 380, 380]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | Unknown  |
| 11 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Unknown  |
| 12 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0  | Unknown  |
| 13 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Unknown  |
| 14 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0  | Unknown  |
| 15 | Tensor<[1, 672, 15, 15]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0       | Unknown  |
| 16 | Tensor<[1, 960, 24, 24]> self = ?,<br>List[int] pad = [1, 2, 1, 2],<br>number value = 0.0       | Unknown  |
### aten.convolution.default
|     | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   |
|----:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|   0 | Tensor<[1, 1, 28, 28]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
|   1 | Tensor<[1, 100, 14, 14]> input = ?,<br>Tensor<[100, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 100         | Unknown  |
|   2 | Tensor<[1, 1008, 14, 14]> input = ?,<br>Tensor<[1008, 48, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 21       | Unknown  |
|   3 | Tensor<[1, 1008, 7, 7]> input = ?,<br>Tensor<[1008, 48, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 21         | Unknown  |
|   4 | Tensor<[1, 1024, 10, 10]> input = ?,<br>Tensor<[1024, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1024      | Unknown  |
|   5 | Tensor<[1, 1024, 128, 128]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
|   6 | Tensor<[1, 1024, 16, 16]> input = ?,<br>Tensor<[1024, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1024 | Unknown  |
|   7 | Tensor<[1, 1024, 19, 19]> input = ?,<br>Tensor<[1024, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1024      | Unknown  |
|   8 | Tensor<[1, 1024, 19, 19]> input = ?,<br>Tensor<[1024, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
|   9 | Tensor<[1, 1024, 7, 7]> input = ?,<br>Tensor<[1024, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1024        | Unknown  |
|  10 | Tensor<[1, 1024, 7, 7]> input = ?,<br>Tensor<[2048, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
|  11 | Tensor<[1, 104, 28, 28]> input = ?,<br>Tensor<[104, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 13          | Unknown  |
|  12 | Tensor<[1, 104, 56, 56]> input = ?,<br>Tensor<[104, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 13          | Unknown  |
|  13 | Tensor<[1, 1056, 48, 48]> input = ?,<br>Tensor<[1056, 264, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4       | Unknown  |
|  14 | Tensor<[1, 1056, 96, 96]> input = ?,<br>Tensor<[1056, 264, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4       | Unknown  |
|  15 | Tensor<[1, 112, 14, 14]> input = ?,<br>Tensor<[112, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 112         | Unknown  |
|  16 | Tensor<[1, 1152, 7, 7]> input = ?,<br>Tensor<[1152, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1152        | Unknown  |
|  17 | Tensor<[1, 1152, 7, 7]> input = ?,<br>Tensor<[1152, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1152        | Unknown  |
|  18 | Tensor<[1, 1152, 8, 8]> input = ?,<br>Tensor<[1152, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1152        | Unknown  |
|  19 | Tensor<[1, 1152, 8, 8]> input = ?,<br>Tensor<[1152, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1152        | Unknown  |
|  20 | Tensor<[1, 12, 56, 56]> input = ?,<br>Tensor<[12, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 12            | Unknown  |
|  21 | Tensor<[1, 120, 14, 14]> input = ?,<br>Tensor<[120, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 120         | Unknown  |
|  22 | Tensor<[1, 120, 14, 14]> input = ?,<br>Tensor<[120, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 120         | Unknown  |
|  23 | Tensor<[1, 120, 14, 14]> input = ?,<br>Tensor<[120, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 120         | Unknown  |
|  24 | Tensor<[1, 120, 28, 28]> input = ?,<br>Tensor<[120, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 120         | Unknown  |
|  25 | Tensor<[1, 120, 28, 28]> input = ?,<br>Tensor<[120, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 120         | Unknown  |
|  26 | Tensor<[1, 120, 28, 28]> input = ?,<br>Tensor<[120, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 5          | Unknown  |
|  27 | Tensor<[1, 120, 40, 40]> input = ?,<br>Tensor<[120, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 120         | Unknown  |
|  28 | Tensor<[1, 120, 56, 56]> input = ?,<br>Tensor<[120, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 5          | Unknown  |
|  29 | Tensor<[1, 1232, 14, 14]> input = ?,<br>Tensor<[1232, 112, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 11      | Unknown  |
|  30 | Tensor<[1, 1232, 28, 28]> input = ?,<br>Tensor<[1232, 112, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 11      | Unknown  |
|  31 | Tensor<[1, 1248, 9, 9]> input = ?,<br>Tensor<[1248, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1248        | Unknown  |
|  32 | Tensor<[1, 1248, 9, 9]> input = ?,<br>Tensor<[1248, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1248        | Unknown  |
|  33 | Tensor<[1, 128, 1, 1]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128           | Unknown  |
|  34 | Tensor<[1, 128, 128, 128]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128   | Unknown  |
|  35 | Tensor<[1, 128, 150, 150]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128       | Unknown  |
|  36 | Tensor<[1, 128, 1600]> input = ?,<br>Tensor<[128, 128, 11]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [15],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1                    | Unknown  |
|  37 | Tensor<[1, 128, 1600]> input = ?,<br>Tensor<[128, 128, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1                      | Unknown  |
|  38 | Tensor<[1, 128, 1600]> input = ?,<br>Tensor<[128, 128, 7]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [15],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1                     | Unknown  |
|  39 | Tensor<[1, 128, 180, 320]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
|  40 | Tensor<[1, 128, 200, 272]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
|  41 | Tensor<[1, 128, 28, 28]> input = ?,<br>Tensor<[128, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 8          | Unknown  |
|  42 | Tensor<[1, 128, 30, 40]> input = ?,<br>Tensor<[64, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
|  43 | Tensor<[1, 128, 5, 5]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128           | Unknown  |
|  44 | Tensor<[1, 128, 56, 56]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128         | Unknown  |
|  45 | Tensor<[1, 128, 56, 56]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
|  46 | Tensor<[1, 128, 56, 56]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
|  47 | Tensor<[1, 128, 56, 56]> input = ?,<br>Tensor<[128, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 8          | Unknown  |
|  48 | Tensor<[1, 128, 56, 56]> input = ?,<br>Tensor<[128, 4, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 32          | Unknown  |
|  49 | Tensor<[1, 128, 56, 56]> input = ?,<br>Tensor<[256, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
|  50 | Tensor<[1, 128, 56, 56]> input = ?,<br>Tensor<[32, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
|  51 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[128, 128, 4, 4]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
|  52 | Tensor<[1, 1280, 30, 40]> input = ?,<br>Tensor<[1280, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1280 | Unknown  |
|  53 | Tensor<[1, 1344, 14, 14]> input = ?,<br>Tensor<[1344, 168, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 8       | Unknown  |
|  54 | Tensor<[1, 1344, 28, 28]> input = ?,<br>Tensor<[1344, 168, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 8       | Unknown  |
|  55 | Tensor<[1, 1392, 10, 10]> input = ?,<br>Tensor<[1392, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1392      | Unknown  |
|  56 | Tensor<[1, 1392, 10, 10]> input = ?,<br>Tensor<[1392, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1392      | Unknown  |
|  57 | Tensor<[1, 1392, 14, 14]> input = ?,<br>Tensor<[1392, 232, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 6       | Unknown  |
|  58 | Tensor<[1, 1392, 28, 28]> input = ?,<br>Tensor<[1392, 232, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 6       | Unknown  |
|  59 | Tensor<[1, 144, 14, 14]> input = ?,<br>Tensor<[144, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 144         | Unknown  |
|  60 | Tensor<[1, 144, 151, 151]> input = ?,<br>Tensor<[144, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 144       | Unknown  |
|  61 | Tensor<[1, 144, 191, 191]> input = ?,<br>Tensor<[144, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 144       | Unknown  |
|  62 | Tensor<[1, 144, 28, 28]> input = ?,<br>Tensor<[144, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 9          | Unknown  |
|  63 | Tensor<[1, 144, 56, 56]> input = ?,<br>Tensor<[144, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 144         | Unknown  |
|  64 | Tensor<[1, 144, 56, 56]> input = ?,<br>Tensor<[144, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 9          | Unknown  |
|  65 | Tensor<[1, 144, 59, 59]> input = ?,<br>Tensor<[144, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 144         | Unknown  |
|  66 | Tensor<[1, 144, 60, 60]> input = ?,<br>Tensor<[144, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 144         | Unknown  |
|  67 | Tensor<[1, 144, 63, 63]> input = ?,<br>Tensor<[144, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 144         | Unknown  |
|  68 | Tensor<[1, 144, 65, 65]> input = ?,<br>Tensor<[144, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 144         | Unknown  |
|  69 | Tensor<[1, 144, 69, 69]> input = ?,<br>Tensor<[144, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 144         | Unknown  |
|  70 | Tensor<[1, 1512, 14, 14]> input = ?,<br>Tensor<[1512, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 63       | Unknown  |
|  71 | Tensor<[1, 1536, 10, 10]> input = ?,<br>Tensor<[1536, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1536      | Unknown  |
|  72 | Tensor<[1, 16, 1, 1]> input = ?,<br>Tensor<[8, 16, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Unknown  |
|  73 | Tensor<[1, 16, 112, 112]> input = ?,<br>Tensor<[16, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16          | Unknown  |
|  74 | Tensor<[1, 16, 112, 112]> input = ?,<br>Tensor<[16, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16          | Unknown  |
|  75 | Tensor<[1, 16, 112, 112]> input = ?,<br>Tensor<[16, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
|  76 | Tensor<[1, 16, 112, 112]> input = ?,<br>Tensor<[8, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
|  77 | Tensor<[1, 16, 160, 160]> input = ?,<br>Tensor<[16, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16          | Unknown  |
|  78 | Tensor<[1, 16, 160, 160]> input = ?,<br>Tensor<[16, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
|  79 | Tensor<[1, 16, 224, 224]> input = ?,<br>Tensor<[16, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
|  80 | Tensor<[1, 16, 224, 224]> input = ?,<br>Tensor<[32, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
|  81 | Tensor<[1, 16, 56, 56]> input = ?,<br>Tensor<[16, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
|  82 | Tensor<[1, 160, 14, 14]> input = ?,<br>Tensor<[160, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 10         | Unknown  |
|  83 | Tensor<[1, 160, 28, 28]> input = ?,<br>Tensor<[160, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 160         | Unknown  |
|  84 | Tensor<[1, 160, 28, 28]> input = ?,<br>Tensor<[160, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 10         | Unknown  |
|  85 | Tensor<[1, 160, 32, 32]> input = ?,<br>Tensor<[160, 160, 2, 2]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
|  86 | Tensor<[1, 1632, 12, 12]> input = ?,<br>Tensor<[1632, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1632      | Unknown  |
|  87 | Tensor<[1, 1632, 12, 12]> input = ?,<br>Tensor<[1632, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1632      | Unknown  |
|  88 | Tensor<[1, 168, 28, 28]> input = ?,<br>Tensor<[168, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 7          | Unknown  |
|  89 | Tensor<[1, 168, 56, 56]> input = ?,<br>Tensor<[168, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 7          | Unknown  |
|  90 | Tensor<[1, 184, 14, 14]> input = ?,<br>Tensor<[184, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 184         | Unknown  |
|  91 | Tensor<[1, 184, 20, 20]> input = ?,<br>Tensor<[184, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 184         | Unknown  |
|  92 | Tensor<[1, 184, 7, 7]> input = ?,<br>Tensor<[184, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 184           | Unknown  |
|  93 | Tensor<[1, 184, 7, 7]> input = ?,<br>Tensor<[184, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 184           | Unknown  |
|  94 | Tensor<[1, 192, 14, 14]> input = ?,<br>Tensor<[192, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 192         | Unknown  |
|  95 | Tensor<[1, 192, 28, 28]> input = ?,<br>Tensor<[192, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 192         | Unknown  |
|  96 | Tensor<[1, 192, 28, 28]> input = ?,<br>Tensor<[192, 48, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4          | Unknown  |
|  97 | Tensor<[1, 192, 56, 56]> input = ?,<br>Tensor<[192, 48, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4          | Unknown  |
|  98 | Tensor<[1, 192, 56, 56]> input = ?,<br>Tensor<[48, 192, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
|  99 | Tensor<[1, 192, 75, 75]> input = ?,<br>Tensor<[192, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 192         | Unknown  |
| 100 | Tensor<[1, 192, 79, 79]> input = ?,<br>Tensor<[192, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 192         | Unknown  |
| 101 | Tensor<[1, 192, 95, 95]> input = ?,<br>Tensor<[192, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 192         | Unknown  |
| 102 | Tensor<[1, 192, 99, 99]> input = ?,<br>Tensor<[192, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 192         | Unknown  |
| 103 | Tensor<[1, 1920, 14, 14]> input = ?,<br>Tensor<[1920, 120, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16      | Unknown  |
| 104 | Tensor<[1, 20, 28, 28]> input = ?,<br>Tensor<[20, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 20            | Unknown  |
| 105 | Tensor<[1, 200, 14, 14]> input = ?,<br>Tensor<[200, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 200         | Unknown  |
| 106 | Tensor<[1, 200, 20, 20]> input = ?,<br>Tensor<[200, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 200         | Unknown  |
| 107 | Tensor<[1, 200, 7, 7]> input = ?,<br>Tensor<[200, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 200           | Unknown  |
| 108 | Tensor<[1, 200, 7, 7]> input = ?,<br>Tensor<[200, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 200           | Unknown  |
| 109 | Tensor<[1, 2016, 14, 14]> input = ?,<br>Tensor<[2016, 56, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 36       | Unknown  |
| 110 | Tensor<[1, 2048, 14, 14]> input = ?,<br>Tensor<[2048, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16      | Unknown  |
| 111 | Tensor<[1, 2048, 15, 20]> input = ?,<br>Tensor<[2048, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2048 | Unknown  |
| 112 | Tensor<[1, 2048, 23, 40]> input = ?,<br>Tensor<[256, 2048, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 113 | Tensor<[1, 2048, 25, 34]> input = ?,<br>Tensor<[256, 2048, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 114 | Tensor<[1, 2048, 25, 34]> input = ?,<br>Tensor<[256, 2048, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 115 | Tensor<[1, 208, 14, 14]> input = ?,<br>Tensor<[208, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 26          | Unknown  |
| 116 | Tensor<[1, 208, 28, 28]> input = ?,<br>Tensor<[208, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 26          | Unknown  |
| 117 | Tensor<[1, 216, 28, 28]> input = ?,<br>Tensor<[216, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 9          | Unknown  |
| 118 | Tensor<[1, 216, 56, 56]> input = ?,<br>Tensor<[216, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 9          | Unknown  |
| 119 | Tensor<[1, 224, 1, 1]> input = ?,<br>Tensor<[8, 224, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 120 | Tensor<[1, 224, 112, 112]> input = ?,<br>Tensor<[224, 112, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2       | Unknown  |
| 121 | Tensor<[1, 224, 112, 112]> input = ?,<br>Tensor<[224, 56, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4        | Unknown  |
| 122 | Tensor<[1, 224, 56, 56]> input = ?,<br>Tensor<[224, 112, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2         | Unknown  |
| 123 | Tensor<[1, 224, 56, 56]> input = ?,<br>Tensor<[224, 224, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 124 | Tensor<[1, 224, 56, 56]> input = ?,<br>Tensor<[224, 56, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4          | Unknown  |
| 125 | Tensor<[1, 224, 7, 7]> input = ?,<br>Tensor<[224, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 224           | Unknown  |
| 126 | Tensor<[1, 232, 1, 1]> input = ?,<br>Tensor<[8, 232, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 127 | Tensor<[1, 232, 56, 56]> input = ?,<br>Tensor<[232, 232, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 128 | Tensor<[1, 232, 56, 56]> input = ?,<br>Tensor<[232, 232, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 129 | Tensor<[1, 24, 112, 112]> input = ?,<br>Tensor<[24, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 24          | Unknown  |
| 130 | Tensor<[1, 24, 56, 56]> input = ?,<br>Tensor<[24, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 24            | Unknown  |
| 131 | Tensor<[1, 240, 14, 14]> input = ?,<br>Tensor<[240, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240         | Unknown  |
| 132 | Tensor<[1, 240, 14, 14]> input = ?,<br>Tensor<[240, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240         | Unknown  |
| 133 | Tensor<[1, 240, 14, 14]> input = ?,<br>Tensor<[240, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240         | Unknown  |
| 134 | Tensor<[1, 240, 14, 14]> input = ?,<br>Tensor<[240, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240         | Unknown  |
| 135 | Tensor<[1, 240, 28, 28]> input = ?,<br>Tensor<[240, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240         | Unknown  |
| 136 | Tensor<[1, 240, 28, 28]> input = ?,<br>Tensor<[240, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240         | Unknown  |
| 137 | Tensor<[1, 240, 28, 28]> input = ?,<br>Tensor<[240, 120, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2         | Unknown  |
| 138 | Tensor<[1, 240, 29, 29]> input = ?,<br>Tensor<[240, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240         | Unknown  |
| 139 | Tensor<[1, 240, 30, 30]> input = ?,<br>Tensor<[240, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240         | Unknown  |
| 140 | Tensor<[1, 240, 31, 31]> input = ?,<br>Tensor<[240, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240         | Unknown  |
| 141 | Tensor<[1, 240, 40, 40]> input = ?,<br>Tensor<[240, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240         | Unknown  |
| 142 | Tensor<[1, 240, 56, 56]> input = ?,<br>Tensor<[240, 120, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2         | Unknown  |
| 143 | Tensor<[1, 2520, 14, 14]> input = ?,<br>Tensor<[2520, 168, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 15      | Unknown  |
| 144 | Tensor<[1, 256, 1, 1]> input = ?,<br>Tensor<[256, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
| 145 | Tensor<[1, 256, 10, 10]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256         | Unknown  |
| 146 | Tensor<[1, 256, 112, 112]> input = ?,<br>Tensor<[256, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2       | Unknown  |
| 147 | Tensor<[1, 256, 120, 160]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256   | Unknown  |
| 148 | Tensor<[1, 256, 128, 128]> input = ?,<br>Tensor<[150, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[150]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 149 | Tensor<[1, 256, 13, 17]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 150 | Tensor<[1, 256, 180, 320]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
| 151 | Tensor<[1, 256, 19, 19]> input = ?,<br>Tensor<[512, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 152 | Tensor<[1, 256, 200, 272]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
| 153 | Tensor<[1, 256, 25, 34]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 154 | Tensor<[1, 256, 28, 28]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256         | Unknown  |
| 155 | Tensor<[1, 256, 3, 3]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256           | Unknown  |
| 156 | Tensor<[1, 256, 400]> input = ?,<br>Tensor<[256, 256, 11]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [5],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1                      | Unknown  |
| 157 | Tensor<[1, 256, 400]> input = ?,<br>Tensor<[256, 256, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [1],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1                       | Unknown  |
| 158 | Tensor<[1, 256, 400]> input = ?,<br>Tensor<[256, 256, 7]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [9],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1                       | Unknown  |
| 159 | Tensor<[1, 256, 512]> input = ?,<br>Tensor<[1024, 256, 1]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [0],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1                     | Unknown  |
| 160 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[256, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2         | Unknown  |
| 161 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[256, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 162 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 163 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[256, 4, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 64          | Unknown  |
| 164 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[256, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 32          | Unknown  |
| 165 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[256, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 32          | Unknown  |
| 166 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 167 | Tensor<[1, 256, 64, 64]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256     | Unknown  |
| 168 | Tensor<[1, 256, 75, 75]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256         | Unknown  |
| 169 | Tensor<[1, 256, 75, 75]> input = ?,<br>Tensor<[256, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 170 | Tensor<[1, 288, 14, 14]> input = ?,<br>Tensor<[288, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 288         | Unknown  |
| 171 | Tensor<[1, 288, 14, 14]> input = ?,<br>Tensor<[288, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 18         | Unknown  |
| 172 | Tensor<[1, 288, 28, 28]> input = ?,<br>Tensor<[288, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 18         | Unknown  |
| 173 | Tensor<[1, 288, 33, 33]> input = ?,<br>Tensor<[288, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 288         | Unknown  |
| 174 | Tensor<[1, 288, 35, 35]> input = ?,<br>Tensor<[288, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 288         | Unknown  |
| 175 | Tensor<[1, 288, 38, 38]> input = ?,<br>Tensor<[288, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 288         | Unknown  |
| 176 | Tensor<[1, 288, 39, 39]> input = ?,<br>Tensor<[288, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 288         | Unknown  |
| 177 | Tensor<[1, 2904, 24, 24]> input = ?,<br>Tensor<[2904, 264, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 11      | Unknown  |
| 178 | Tensor<[1, 2904, 48, 48]> input = ?,<br>Tensor<[2904, 264, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 11      | Unknown  |
| 179 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[1024, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
| 180 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[1024, 3, 32, 32]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
| 181 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[128, 3, 4, 4]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
| 182 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[16, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 183 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[16, 3, 7, 7]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 184 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 185 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[64, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 186 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[64, 3, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 187 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 188 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 189 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 32, 32]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
| 190 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 32, 32]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 191 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[96, 3, 4, 4]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 192 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[96, 3, 7, 7]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 193 | Tensor<[1, 3, 225, 225]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 194 | Tensor<[1, 3, 241, 241]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 195 | Tensor<[1, 3, 256, 256]> input = ?,<br>Tensor<[128, 3, 4, 4]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
| 196 | Tensor<[1, 3, 256, 256]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 197 | Tensor<[1, 3, 256, 256]> input = ?,<br>Tensor<[96, 3, 4, 4]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 198 | Tensor<[1, 3, 261, 261]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 199 | Tensor<[1, 3, 299, 299]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 200 | Tensor<[1, 3, 299, 299]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 201 | Tensor<[1, 3, 300, 300]> input = ?,<br>Tensor<[64, 3, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 202 | Tensor<[1, 3, 301, 301]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 203 | Tensor<[1, 3, 320, 320]> input = ?,<br>Tensor<[16, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 204 | Tensor<[1, 3, 381, 381]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 205 | Tensor<[1, 3, 384, 384]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 206 | Tensor<[1, 3, 384, 512]> input = ?,<br>Tensor<[768, 3, 32, 32]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 207 | Tensor<[1, 3, 480, 640]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 208 | Tensor<[1, 3, 512, 512]> input = ?,<br>Tensor<[32, 3, 7, 7]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 209 | Tensor<[1, 3, 512, 672]> input = ?,<br>Tensor<[192, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 210 | Tensor<[1, 3, 518, 518]> input = ?,<br>Tensor<[1280, 3, 14, 14]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [14, 14],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
| 211 | Tensor<[1, 3, 720, 1280]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 212 | Tensor<[1, 3, 800, 1088]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 213 | Tensor<[1, 3024, 14, 14]> input = ?,<br>Tensor<[3024, 112, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 27      | Unknown  |
| 214 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[16, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 215 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[224, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 216 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[232, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 217 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[256, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 218 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 32          | Unknown  |
| 219 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[32, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2          | Unknown  |
| 220 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[32, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 221 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[336, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 222 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[48, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 223 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[64, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 224 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[64, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 225 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[72, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 226 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[80, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 227 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[96, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 228 | Tensor<[1, 32, 120, 120]> input = ?,<br>Tensor<[16, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 229 | Tensor<[1, 32, 120, 120]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 32          | Unknown  |
| 230 | Tensor<[1, 32, 128, 128]> input = ?,<br>Tensor<[32, 32, 8, 8]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [8, 8],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
| 231 | Tensor<[1, 32, 128, 128]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
| 232 | Tensor<[1, 32, 130, 130]> input = ?,<br>Tensor<[16, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 233 | Tensor<[1, 32, 130, 130]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 32          | Unknown  |
| 234 | Tensor<[1, 32, 147, 147]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 235 | Tensor<[1, 32, 149, 149]> input = ?,<br>Tensor<[32, 32, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 236 | Tensor<[1, 32, 150, 150]> input = ?,<br>Tensor<[24, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 237 | Tensor<[1, 32, 150, 150]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 32          | Unknown  |
| 238 | Tensor<[1, 32, 150, 150]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 239 | Tensor<[1, 32, 190, 190]> input = ?,<br>Tensor<[24, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 240 | Tensor<[1, 32, 190, 190]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 32          | Unknown  |
| 241 | Tensor<[1, 32, 192, 192]> input = ?,<br>Tensor<[528, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 242 | Tensor<[1, 32, 256, 256]> input = ?,<br>Tensor<[1, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<[1]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 243 | Tensor<[1, 32, 56, 56]> input = ?,<br>Tensor<[32, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 244 | Tensor<[1, 32, 56, 56]> input = ?,<br>Tensor<[64, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 245 | Tensor<[1, 320, 14, 14]> input = ?,<br>Tensor<[320, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 20         | Unknown  |
| 246 | Tensor<[1, 320, 28, 28]> input = ?,<br>Tensor<[320, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 20         | Unknown  |
| 247 | Tensor<[1, 320, 30, 40]> input = ?,<br>Tensor<[320, 320, 2, 2]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 248 | Tensor<[1, 336, 112, 112]> input = ?,<br>Tensor<[336, 168, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2       | Unknown  |
| 249 | Tensor<[1, 336, 14, 14]> input = ?,<br>Tensor<[336, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 336         | Unknown  |
| 250 | Tensor<[1, 336, 14, 14]> input = ?,<br>Tensor<[336, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 14         | Unknown  |
| 251 | Tensor<[1, 336, 28, 28]> input = ?,<br>Tensor<[336, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 14         | Unknown  |
| 252 | Tensor<[1, 336, 48, 48]> input = ?,<br>Tensor<[336, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 336         | Unknown  |
| 253 | Tensor<[1, 336, 49, 49]> input = ?,<br>Tensor<[336, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 336         | Unknown  |
| 254 | Tensor<[1, 336, 56, 56]> input = ?,<br>Tensor<[336, 168, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2         | Unknown  |
| 255 | Tensor<[1, 336, 56, 56]> input = ?,<br>Tensor<[336, 336, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 256 | Tensor<[1, 36, 56, 56]> input = ?,<br>Tensor<[36, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 36            | Unknown  |
| 257 | Tensor<[1, 3712, 14, 14]> input = ?,<br>Tensor<[3712, 232, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16      | Unknown  |
| 258 | Tensor<[1, 384, 14, 14]> input = ?,<br>Tensor<[384, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 384         | Unknown  |
| 259 | Tensor<[1, 384, 8, 8]> input = ?,<br>Tensor<[256, 384, 1, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 260 | Tensor<[1, 384, 8, 8]> input = ?,<br>Tensor<[256, 384, 3, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 261 | Tensor<[1, 40, 14, 14]> input = ?,<br>Tensor<[40, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 40            | Unknown  |
| 262 | Tensor<[1, 40, 28, 28]> input = ?,<br>Tensor<[40, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 40            | Unknown  |
| 263 | Tensor<[1, 400, 14, 14]> input = ?,<br>Tensor<[400, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 25         | Unknown  |
| 264 | Tensor<[1, 400, 7, 7]> input = ?,<br>Tensor<[400, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 25           | Unknown  |
| 265 | Tensor<[1, 408, 14, 14]> input = ?,<br>Tensor<[408, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 17         | Unknown  |
| 266 | Tensor<[1, 408, 28, 28]> input = ?,<br>Tensor<[408, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 17         | Unknown  |
| 267 | Tensor<[1, 432, 14, 14]> input = ?,<br>Tensor<[432, 48, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 9          | Unknown  |
| 268 | Tensor<[1, 432, 28, 28]> input = ?,<br>Tensor<[432, 48, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 9          | Unknown  |
| 269 | Tensor<[1, 440, 14, 14]> input = ?,<br>Tensor<[440, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 55          | Unknown  |
| 270 | Tensor<[1, 440, 7, 7]> input = ?,<br>Tensor<[440, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 55            | Unknown  |
| 271 | Tensor<[1, 448, 28, 28]> input = ?,<br>Tensor<[448, 112, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4         | Unknown  |
| 272 | Tensor<[1, 448, 28, 28]> input = ?,<br>Tensor<[448, 56, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 8          | Unknown  |
| 273 | Tensor<[1, 448, 56, 56]> input = ?,<br>Tensor<[448, 112, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4         | Unknown  |
| 274 | Tensor<[1, 448, 56, 56]> input = ?,<br>Tensor<[448, 56, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 8          | Unknown  |
| 275 | Tensor<[1, 48, 1, 1]> input = ?,<br>Tensor<[8, 48, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Unknown  |
| 276 | Tensor<[1, 48, 112, 112]> input = ?,<br>Tensor<[48, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 48          | Unknown  |
| 277 | Tensor<[1, 48, 112, 112]> input = ?,<br>Tensor<[48, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2          | Unknown  |
| 278 | Tensor<[1, 48, 112, 112]> input = ?,<br>Tensor<[48, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 6           | Unknown  |
| 279 | Tensor<[1, 48, 56, 56]> input = ?,<br>Tensor<[48, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2            | Unknown  |
| 280 | Tensor<[1, 48, 56, 56]> input = ?,<br>Tensor<[48, 48, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 281 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[480, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480         | Unknown  |
| 282 | Tensor<[1, 480, 14, 14]> input = ?,<br>Tensor<[480, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480         | Unknown  |
| 283 | Tensor<[1, 480, 14, 14]> input = ?,<br>Tensor<[480, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480         | Unknown  |
| 284 | Tensor<[1, 480, 15, 15]> input = ?,<br>Tensor<[480, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480         | Unknown  |
| 285 | Tensor<[1, 480, 15, 15]> input = ?,<br>Tensor<[480, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480         | Unknown  |
| 286 | Tensor<[1, 480, 20, 20]> input = ?,<br>Tensor<[480, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480         | Unknown  |
| 287 | Tensor<[1, 480, 7, 7]> input = ?,<br>Tensor<[480, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480           | Unknown  |
| 288 | Tensor<[1, 480, 7, 7]> input = ?,<br>Tensor<[480, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480           | Unknown  |
| 289 | Tensor<[1, 480, 7, 7]> input = ?,<br>Tensor<[480, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480           | Unknown  |
| 290 | Tensor<[1, 512, 1, 1]> input = ?,<br>Tensor<[1000, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[1000]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 291 | Tensor<[1, 512, 100]> input = ?,<br>Tensor<[512, 256, 8]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [4],<br>List[int] padding = [2],<br>List[int] dilation = [1],<br>bool transposed = True,<br>List[int] output_padding = [0],<br>int groups = 1                        | Unknown  |
| 292 | Tensor<[1, 512, 14, 14]> input = ?,<br>Tensor<[512, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 512         | Unknown  |
| 293 | Tensor<[1, 512, 15, 20]> input = ?,<br>Tensor<[64, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
| 294 | Tensor<[1, 512, 16, 16]> input = ?,<br>Tensor<[512, 256, 2, 2]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = True,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Unknown  |
| 295 | Tensor<[1, 512, 19, 19]> input = ?,<br>Tensor<[1024, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [6, 6],<br>List[int] dilation = [6, 6],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 296 | Tensor<[1, 512, 28, 28]> input = ?,<br>Tensor<[512, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4         | Unknown  |
| 297 | Tensor<[1, 512, 5, 5]> input = ?,<br>Tensor<[512, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 512           | Unknown  |
| 298 | Tensor<[1, 512, 56, 56]> input = ?,<br>Tensor<[512, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4         | Unknown  |
| 299 | Tensor<[1, 512, 56, 56]> input = ?,<br>Tensor<[512, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 32         | Unknown  |
| 300 | Tensor<[1, 512, 56, 56]> input = ?,<br>Tensor<[512, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 64          | Unknown  |
| 301 | Tensor<[1, 512, 60, 80]> input = ?,<br>Tensor<[512, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 512     | Unknown  |
| 302 | Tensor<[1, 528, 1, 1]> input = ?,<br>Tensor<[8, 528, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 303 | Tensor<[1, 528, 17, 17]> input = ?,<br>Tensor<[528, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 528         | Unknown  |
| 304 | Tensor<[1, 528, 17, 17]> input = ?,<br>Tensor<[528, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 528         | Unknown  |
| 305 | Tensor<[1, 528, 192, 192]> input = ?,<br>Tensor<[528, 264, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2       | Unknown  |
| 306 | Tensor<[1, 528, 96, 96]> input = ?,<br>Tensor<[528, 264, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2         | Unknown  |
| 307 | Tensor<[1, 528, 96, 96]> input = ?,<br>Tensor<[528, 528, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 308 | Tensor<[1, 56, 14, 14]> input = ?,<br>Tensor<[56, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 56            | Unknown  |
| 309 | Tensor<[1, 576, 14, 14]> input = ?,<br>Tensor<[576, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 576         | Unknown  |
| 310 | Tensor<[1, 576, 14, 14]> input = ?,<br>Tensor<[576, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 24         | Unknown  |
| 311 | Tensor<[1, 576, 19, 19]> input = ?,<br>Tensor<[576, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 576         | Unknown  |
| 312 | Tensor<[1, 576, 19, 19]> input = ?,<br>Tensor<[576, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 576         | Unknown  |
| 313 | Tensor<[1, 576, 28, 28]> input = ?,<br>Tensor<[576, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 24         | Unknown  |
| 314 | Tensor<[1, 576, 7, 7]> input = ?,<br>Tensor<[576, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 576           | Unknown  |
| 315 | Tensor<[1, 60, 28, 28]> input = ?,<br>Tensor<[60, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 60            | Unknown  |
| 316 | Tensor<[1, 64, 1, 1]> input = ?,<br>Tensor<[8, 64, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Unknown  |
| 317 | Tensor<[1, 64, 112, 112]> input = ?,<br>Tensor<[64, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 64          | Unknown  |
| 318 | Tensor<[1, 64, 112, 112]> input = ?,<br>Tensor<[64, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 64          | Unknown  |
| 319 | Tensor<[1, 64, 112, 112]> input = ?,<br>Tensor<[64, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4          | Unknown  |
| 320 | Tensor<[1, 64, 112, 112]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 321 | Tensor<[1, 64, 120, 160]> input = ?,<br>Tensor<[128, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 322 | Tensor<[1, 64, 120, 160]> input = ?,<br>Tensor<[64, 64, 8, 8]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [8, 8],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
| 323 | Tensor<[1, 64, 150, 150]> input = ?,<br>Tensor<[128, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 324 | Tensor<[1, 64, 150, 150]> input = ?,<br>Tensor<[64, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 64          | Unknown  |
| 325 | Tensor<[1, 64, 160, 160]> input = ?,<br>Tensor<[64, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 64          | Unknown  |
| 326 | Tensor<[1, 64, 180, 320]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 327 | Tensor<[1, 64, 180, 320]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 328 | Tensor<[1, 64, 200, 272]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 329 | Tensor<[1, 64, 200, 272]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 330 | Tensor<[1, 64, 28, 28]> input = ?,<br>Tensor<[64, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4            | Unknown  |
| 331 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[128, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 332 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[128, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 333 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[128, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 334 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[192, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 335 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[256, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 336 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4            | Unknown  |
| 337 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 338 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 339 | Tensor<[1, 64, 64, 64]> input = ?,<br>Tensor<[64, 64, 4, 4]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 340 | Tensor<[1, 64, 6400]> input = ?,<br>Tensor<[64, 64, 11]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [25],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1                        | Unknown  |
| 341 | Tensor<[1, 64, 6400]> input = ?,<br>Tensor<[64, 64, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [5],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1                          | Unknown  |
| 342 | Tensor<[1, 64, 73, 73]> input = ?,<br>Tensor<[64, 64, 1, 7]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 343 | Tensor<[1, 64, 73, 73]> input = ?,<br>Tensor<[64, 64, 7, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [3, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 344 | Tensor<[1, 640, 32, 32]> input = ?,<br>Tensor<[640, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 640     | Unknown  |
| 345 | Tensor<[1, 672, 14, 14]> input = ?,<br>Tensor<[672, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672         | Unknown  |
| 346 | Tensor<[1, 672, 14, 14]> input = ?,<br>Tensor<[672, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672         | Unknown  |
| 347 | Tensor<[1, 672, 14, 14]> input = ?,<br>Tensor<[672, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672         | Unknown  |
| 348 | Tensor<[1, 672, 14, 14]> input = ?,<br>Tensor<[672, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 42         | Unknown  |
| 349 | Tensor<[1, 672, 15, 15]> input = ?,<br>Tensor<[672, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672         | Unknown  |
| 350 | Tensor<[1, 672, 17, 17]> input = ?,<br>Tensor<[672, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672         | Unknown  |
| 351 | Tensor<[1, 672, 19, 19]> input = ?,<br>Tensor<[672, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672         | Unknown  |
| 352 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[672, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672         | Unknown  |
| 353 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[672, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672         | Unknown  |
| 354 | Tensor<[1, 672, 24, 24]> input = ?,<br>Tensor<[672, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672         | Unknown  |
| 355 | Tensor<[1, 672, 24, 24]> input = ?,<br>Tensor<[672, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672         | Unknown  |
| 356 | Tensor<[1, 672, 28, 28]> input = ?,<br>Tensor<[672, 168, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4         | Unknown  |
| 357 | Tensor<[1, 672, 56, 56]> input = ?,<br>Tensor<[672, 168, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4         | Unknown  |
| 358 | Tensor<[1, 672, 7, 7]> input = ?,<br>Tensor<[672, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672           | Unknown  |
| 359 | Tensor<[1, 672, 7, 7]> input = ?,<br>Tensor<[672, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672           | Unknown  |
| 360 | Tensor<[1, 672, 7, 7]> input = ?,<br>Tensor<[672, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 42           | Unknown  |
| 361 | Tensor<[1, 696, 28, 28]> input = ?,<br>Tensor<[696, 232, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 3         | Unknown  |
| 362 | Tensor<[1, 696, 56, 56]> input = ?,<br>Tensor<[696, 232, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 3         | Unknown  |
| 363 | Tensor<[1, 72, 1, 1]> input = ?,<br>Tensor<[20, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<[20]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 364 | Tensor<[1, 72, 1, 1]> input = ?,<br>Tensor<[24, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 365 | Tensor<[1, 72, 1, 1]> input = ?,<br>Tensor<[8, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Unknown  |
| 366 | Tensor<[1, 72, 112, 112]> input = ?,<br>Tensor<[72, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 3          | Unknown  |
| 367 | Tensor<[1, 72, 28, 28]> input = ?,<br>Tensor<[72, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72            | Unknown  |
| 368 | Tensor<[1, 72, 28, 28]> input = ?,<br>Tensor<[72, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72            | Unknown  |
| 369 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[72, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72            | Unknown  |
| 370 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[72, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72            | Unknown  |
| 371 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[72, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72            | Unknown  |
| 372 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[72, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 3            | Unknown  |
| 373 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[72, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 374 | Tensor<[1, 72, 80, 80]> input = ?,<br>Tensor<[72, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72            | Unknown  |
| 375 | Tensor<[1, 72, 80, 80]> input = ?,<br>Tensor<[72, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72            | Unknown  |
| 376 | Tensor<[1, 720, 14, 14]> input = ?,<br>Tensor<[720, 120, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 6         | Unknown  |
| 377 | Tensor<[1, 720, 17, 17]> input = ?,<br>Tensor<[720, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 720         | Unknown  |
| 378 | Tensor<[1, 720, 21, 21]> input = ?,<br>Tensor<[720, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 720         | Unknown  |
| 379 | Tensor<[1, 720, 28, 28]> input = ?,<br>Tensor<[720, 120, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 6         | Unknown  |
| 380 | Tensor<[1, 728, 38, 38]> input = ?,<br>Tensor<[728, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 728         | Unknown  |
| 381 | Tensor<[1, 7392, 24, 24]> input = ?,<br>Tensor<[7392, 264, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 28      | Unknown  |
| 382 | Tensor<[1, 768, 3000]> input = ?,<br>Tensor<[768, 768, 3]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [2],<br>List[int] padding = [1],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1                      | Unknown  |
| 383 | Tensor<[1, 768, 8]> input = ?,<br>Tensor<[768, 192, 1]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [0],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 4                         | Unknown  |
| 384 | Tensor<[1, 768, 8]> input = ?,<br>Tensor<[768, 768, 1]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [0],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1                         | Unknown  |
| 385 | Tensor<[1, 784, 14, 14]> input = ?,<br>Tensor<[784, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 49         | Unknown  |
| 386 | Tensor<[1, 784, 7, 7]> input = ?,<br>Tensor<[784, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 49           | Unknown  |
| 387 | Tensor<[1, 8, 112, 112]> input = ?,<br>Tensor<[8, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 8             | Unknown  |
| 388 | Tensor<[1, 80, 100]> input = ?,<br>Tensor<[256, 80, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1],<br>List[int] padding = [2],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1                             | Unknown  |
| 389 | Tensor<[1, 80, 100]> input = ?,<br>Tensor<[512, 80, 7]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1                         | Unknown  |
| 390 | Tensor<[1, 80, 14, 14]> input = ?,<br>Tensor<[80, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 80            | Unknown  |
| 391 | Tensor<[1, 80, 3000]> input = ?,<br>Tensor<[768, 80, 3]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [1],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1                        | Unknown  |
| 392 | Tensor<[1, 80, 56, 56]> input = ?,<br>Tensor<[80, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 393 | Tensor<[1, 80, 56, 56]> input = ?,<br>Tensor<[80, 80, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 394 | Tensor<[1, 816, 19, 19]> input = ?,<br>Tensor<[816, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 816         | Unknown  |
| 395 | Tensor<[1, 816, 23, 23]> input = ?,<br>Tensor<[816, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 816         | Unknown  |
| 396 | Tensor<[1, 88, 28, 28]> input = ?,<br>Tensor<[88, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 88            | Unknown  |
| 397 | Tensor<[1, 888, 14, 14]> input = ?,<br>Tensor<[888, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 37         | Unknown  |
| 398 | Tensor<[1, 888, 7, 7]> input = ?,<br>Tensor<[888, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 37           | Unknown  |
| 399 | Tensor<[1, 896, 14, 14]> input = ?,<br>Tensor<[896, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 7         | Unknown  |
| 400 | Tensor<[1, 896, 14, 14]> input = ?,<br>Tensor<[896, 56, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16         | Unknown  |
| 401 | Tensor<[1, 896, 28, 28]> input = ?,<br>Tensor<[896, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 7         | Unknown  |
| 402 | Tensor<[1, 896, 28, 28]> input = ?,<br>Tensor<[896, 56, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16         | Unknown  |
| 403 | Tensor<[1, 912, 14, 14]> input = ?,<br>Tensor<[912, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 38         | Unknown  |
| 404 | Tensor<[1, 912, 7, 7]> input = ?,<br>Tensor<[912, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 38           | Unknown  |
| 405 | Tensor<[1, 92, 14, 14]> input = ?,<br>Tensor<[92, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 92            | Unknown  |
| 406 | Tensor<[1, 96, 112, 112]> input = ?,<br>Tensor<[96, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 96          | Unknown  |
| 407 | Tensor<[1, 96, 112, 112]> input = ?,<br>Tensor<[96, 48, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2          | Unknown  |
| 408 | Tensor<[1, 96, 113, 113]> input = ?,<br>Tensor<[96, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 96          | Unknown  |
| 409 | Tensor<[1, 96, 121, 121]> input = ?,<br>Tensor<[96, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 96          | Unknown  |
| 410 | Tensor<[1, 96, 131, 131]> input = ?,<br>Tensor<[96, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 96          | Unknown  |
| 411 | Tensor<[1, 96, 28, 28]> input = ?,<br>Tensor<[96, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 96            | Unknown  |
| 412 | Tensor<[1, 96, 56, 56]> input = ?,<br>Tensor<[192, 96, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 413 | Tensor<[1, 96, 56, 56]> input = ?,<br>Tensor<[96, 48, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2            | Unknown  |
| 414 | Tensor<[1, 96, 56, 56]> input = ?,<br>Tensor<[96, 96, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 415 | Tensor<[1, 960, 24, 24]> input = ?,<br>Tensor<[960, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 960         | Unknown  |
| 416 | Tensor<[1, 960, 27, 27]> input = ?,<br>Tensor<[960, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 960         | Unknown  |
| 417 | Tensor<[1, 960, 3, 3]> input = ?,<br>Tensor<[960, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 960           | Unknown  |
| 418 | Tensor<[1, 960, 3, 3]> input = ?,<br>Tensor<[960, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 960           | Unknown  |
| 419 | Tensor<[1, 960, 7, 7]> input = ?,<br>Tensor<[960, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 960           | Unknown  |
| 420 | Tensor<[1, 960, 7, 7]> input = ?,<br>Tensor<[960, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 960           | Unknown  |
### aten.cos.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 23, 40, 64]> self = ? | Unknown  |
|  1 | Tensor<[1, 32, 128]> self = ?    | Unknown  |
### aten.cumsum.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1                                             | Unknown  |
|  1 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 1,<br>Optional[int] dtype = torch.float32 | Unknown  |
|  2 | Tensor<[1, 32]> self = ?,<br>int dim = -1                                            | Unknown  |
|  3 | Tensor<[1, 45]> self = ?,<br>int dim = -1                                            | Unknown  |
|  4 | Tensor<[1, 5]> self = ?,<br>int dim = -1                                             | Unknown  |
### aten.detach.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 19, 1024]> self = ? | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[0, 1]> self = ?,<br>Tensor other = 1.0                           | Unknown  |
|  1 | Tensor<[1, 1, 16384, 256]> self = ?,<br>Tensor other = 5.656854249492381 | Unknown  |
|  2 | Tensor<[1, 1, 19200, 300]> self = ?,<br>Tensor other = 8.0               | Unknown  |
|  3 | Tensor<[1, 1, 256]> self = ?,<br>Tensor other = 0.5                      | Unknown  |
|  4 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor other = 8.0                  | Unknown  |
|  5 | Tensor<[1, 12, 12, 12]> self = ?,<br>Tensor other = 8.0                  | Unknown  |
|  6 | Tensor<[1, 12, 14, 14]> self = ?,<br>Tensor other = 8.0                  | Unknown  |
|  7 | Tensor<[1, 12, 16, 64]> self = ?,<br>Tensor other = 8.0                  | Unknown  |
|  8 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor other = 8.0                | Unknown  |
|  9 | Tensor<[1, 12, 201, 201]> self = ?,<br>Tensor other = 8.0                | Unknown  |
| 10 | Tensor<[1, 12, 25, 25]> self = ?,<br>Tensor other = 8.0                  | Unknown  |
| 11 | Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  |
| 12 | Tensor<[1, 12, 8, 8]> self = ?,<br>Tensor other = 8.0                    | Unknown  |
| 13 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor other = 8.0                    | Unknown  |
| 14 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor other = 8.0                | Unknown  |
| 15 | Tensor<[1, 16, 256, 256]> self = ?,<br>Tensor other = 8.0                | Unknown  |
| 16 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  |
| 17 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor other = 11.313708498984761     | Unknown  |
| 18 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor other = 8.0                    | Unknown  |
| 19 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                            | Unknown  |
| 20 | Tensor<[1, 23, 40]> self = ?,<br>Tensor<[1, 1, 40]> other = ?            | Unknown  |
| 21 | Tensor<[1, 256, 400]> self = ?,<br>Tensor other = 3                      | Unknown  |
| 22 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>Tensor other = 8.0               | Unknown  |
| 23 | Tensor<[1, 50257]> self = ?,<br>Tensor other = 0.9                       | Unknown  |
| 24 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Unknown  |
| 25 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?                 | Unknown  |
| 26 | Tensor<[1, 64, 9, 9]> self = ?,<br>Tensor other = 8.0                    | Unknown  |
| 27 | Tensor<[1, 8, 256, 2048]> self = ?,<br>Tensor other = 5.656854249492381  | Unknown  |
| 28 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                           | Unknown  |
| 29 | Tensor<[10]> self = ?,<br>Tensor other = 10                              | Unknown  |
| 30 | Tensor<[10]> self = ?,<br>Tensor other = 9.375                           | Unknown  |
| 31 | Tensor<[128]> self = ?,<br>Tensor other = 128                            | Unknown  |
| 32 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                           | Unknown  |
| 33 | Tensor<[19]> self = ?,<br>Tensor other = 18.75                           | Unknown  |
| 34 | Tensor<[1]> self = ?,<br>Tensor other = 1                                | Unknown  |
| 35 | Tensor<[1]> self = ?,<br>Tensor other = 1.0                              | Unknown  |
| 36 | Tensor<[2, 2]> self = ?,<br>Tensor other = 2.0794415416798357            | Unknown  |
| 37 | Tensor<[20]> self = ?,<br>Tensor other = 20                              | Unknown  |
| 38 | Tensor<[2]> self = ?,<br>Tensor other = 2                                | Unknown  |
| 39 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?           | Unknown  |
| 40 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?           | Unknown  |
| 41 | Tensor<[3234, 1]> self = ?,<br>Tensor other = 10.0                       | Unknown  |
| 42 | Tensor<[38]> self = ?,<br>Tensor other = 37.5                            | Unknown  |
| 43 | Tensor<[3]> self = ?,<br>Tensor other = 3                                | Unknown  |
| 44 | Tensor<[3]> self = ?,<br>Tensor other = 3.0                              | Unknown  |
| 45 | Tensor<[5]> self = ?,<br>Tensor other = 4.6875                           | Unknown  |
| 46 | Tensor<[5]> self = ?,<br>Tensor other = 5                                | Unknown  |
| 47 | Tensor<[64, 3, 64, 32]> self = ?,<br>Tensor<[64, 3, 64, 32]> other = ?   | Unknown  |
| 48 | Tensor<[64, 4, 64, 32]> self = ?,<br>Tensor<[64, 4, 64, 32]> other = ?   | Unknown  |
| 49 | Tensor<[8, 920, 32]> self = ?,<br>Tensor other = 5.656854249492381       | Unknown  |
| 50 | Tensor<[8732, 1]> self = ?,<br>Tensor other = 10.0                       | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?                                | Unknown  |
|  1 | Tensor<[2, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?                              | Unknown  |
|  2 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?                                | Unknown  |
|  3 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?                                | Unknown  |
|  4 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                                 | Unknown  |
|  5 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?                                | Unknown  |
|  6 | Tensor<[250002, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?,<br>int padding_idx = 1   | Unknown  |
|  7 | Tensor<[250880, 1536]> weight = ?,<br>Tensor<[1, 32]> indices = ?                          | Unknown  |
|  8 | Tensor<[256008, 1024]> weight = ?,<br>Tensor<[1, 19]> indices = ?,<br>int padding_idx = 1  | Unknown  |
|  9 | Tensor<[262, 768]> weight = ?,<br>Tensor<[1, 2048]> indices = ?                            | Unknown  |
| 10 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?,<br>int padding_idx = 0    | Unknown  |
| 11 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?,<br>int padding_idx = 0    | Unknown  |
| 12 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?,<br>int padding_idx = 0     | Unknown  |
| 13 | Tensor<[30522, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?,<br>int padding_idx = 0  | Unknown  |
| 14 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?,<br>int padding_idx = 0    | Unknown  |
| 15 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?,<br>int padding_idx = 0    | Unknown  |
| 16 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                             | Unknown  |
| 17 | Tensor<[30528, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?,<br>int padding_idx = 0     | Unknown  |
| 18 | Tensor<[320, 64]> weight = ?,<br>Tensor<[24, 24]> indices = ?                              | Unknown  |
| 19 | Tensor<[32000, 4096]> weight = ?,<br>Tensor<[1, 32]> indices = ?,<br>int padding_idx = 0   | Unknown  |
| 20 | Tensor<[32128, 1024]> weight = ?,<br>Tensor<[1, 10]> indices = ?                           | Unknown  |
| 21 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 10]> indices = ?                            | Unknown  |
| 22 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 15]> indices = ?                            | Unknown  |
| 23 | Tensor<[32128, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?                            | Unknown  |
| 24 | Tensor<[50, 768]> weight = ?,<br>Tensor<[1, 50]> indices = ?                               | Unknown  |
| 25 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 45]> indices = ?                            | Unknown  |
| 26 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 7]> indices = ?                             | Unknown  |
| 27 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?                              | Unknown  |
| 28 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                               | Unknown  |
| 29 | Tensor<[51200, 1024]> weight = ?,<br>Tensor<[1, 5]> indices = ?                            | Unknown  |
| 30 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 50257 | Unknown  |
| 31 | Tensor<[65024, 4544]> weight = ?,<br>Tensor<[1, 7]> indices = ?                            | Unknown  |
| 32 | Tensor<[81, 768]> weight = ?,<br>Tensor<[1, 24]> indices = ?,<br>int padding_idx = 1       | Unknown  |
### aten.empty.memory_format
|    | ATen Input Variations                                                                                                             | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int] size = [],<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.eq.Scalar
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>number other = 1  | Unknown  |
|  1 | Tensor<[1, 16]> self = ?,<br>number other = 0      | Unknown  |
|  2 | Tensor<[1, 7]> self = ?,<br>number other = 1       | Unknown  |
|  3 | Tensor<[1, 7]> self = ?,<br>number other = 50256   | Unknown  |
|  4 | Tensor<[1]> self = ?,<br>number other = 50256      | Unknown  |
|  5 | Tensor<[64, 49, 49]> self = ?,<br>number other = 0 | Unknown  |
|  6 | Tensor<[64, 64, 64]> self = ?,<br>number other = 0 | Unknown  |
### aten.eq.Tensor
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Tensor<[]> other = ? | Unknown  |
### aten.exp.default
|    | ATen Input Variations      | Status   |
|---:|:---------------------------|:---------|
|  0 | Tensor<[0, 1]> self = ?    | Unknown  |
|  1 | Tensor<[3, 1, 1]> self = ? | Unknown  |
|  2 | Tensor<[3234, 1]> self = ? | Unknown  |
|  3 | Tensor<[4, 1, 1]> self = ? | Unknown  |
|  4 | Tensor<[8732, 1]> self = ? | Unknown  |
|  5 | Tensor<[]> self = ?        | Unknown  |
### aten.expand.default
|     | ATen Input Variations                                                                  | Status   |
|----:|:---------------------------------------------------------------------------------------|:---------|
|   0 | Tensor<[1, 1, 1, 16, 1]> self = ?,<br>List[int] size = [1, 1, 1, 16, 2]                | Unknown  |
|   1 | Tensor<[1, 1, 1, 16]> self = ?,<br>List[int] size = [1, 12, 16, 16]                    | Unknown  |
|   2 | Tensor<[1, 1, 1, 24]> self = ?,<br>List[int] size = [1, 1, 24, 24]                     | Unknown  |
|   3 | Tensor<[1, 1, 1, 46]> self = ?,<br>List[int] size = [1, 1, 1, 46]                      | Unknown  |
|   4 | Tensor<[1, 1, 1, 920]> self = ?,<br>List[int] size = [-1, 8, -1, -1]                   | Unknown  |
|   5 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 1, 1, sym_size_int]       | Unknown  |
|   6 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, -1, -1]                         | Unknown  |
|   7 | Tensor<[1, 1, 12, 16, 2]> self = ?,<br>List[int] size = [1, 1, -1, -1, -1]             | Unknown  |
|   8 | Tensor<[1, 1, 1280]> self = ?,<br>List[int] size = [1, -1, -1]                         | Unknown  |
|   9 | Tensor<[1, 1, 16384, 256]> self = ?,<br>List[int] size = [1, 1, 16384, 256]            | Unknown  |
|  10 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int] size = [1, 1, 16384, 32]              | Unknown  |
|  11 | Tensor<[1, 1, 19, 19]> self = ?,<br>List[int] size = [1, 1, 19, 19]                    | Unknown  |
|  12 | Tensor<[1, 1, 19200, 300]> self = ?,<br>List[int] size = [1, 1, 19200, 300]            | Unknown  |
|  13 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] size = [1, 1, 19200, 64]              | Unknown  |
|  14 | Tensor<[1, 1, 192]> self = ?,<br>List[int] size = [1, -1, -1]                          | Unknown  |
|  15 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int] size = [1, 1, 256, 32]                  | Unknown  |
|  16 | Tensor<[1, 1, 300, 64]> self = ?,<br>List[int] size = [1, 1, 300, 64]                  | Unknown  |
|  17 | Tensor<[1, 1, 32, 256]> self = ?,<br>List[int] size = [1, 1, 32, 256]                  | Unknown  |
|  18 | Tensor<[1, 1, 32, 32]> self = ?,<br>List[int] size = [1, 1, 32, 32]                    | Unknown  |
|  19 | Tensor<[1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32]                            | Unknown  |
|  20 | Tensor<[1, 1, 38, 38]> self = ?,<br>List[int] size = [1, 512, 38, 38]                  | Unknown  |
|  21 | Tensor<[1, 1, 45, 45]> self = ?,<br>List[int] size = [1, 1, 45, 45]                    | Unknown  |
|  22 | Tensor<[1, 1, 45]> self = ?,<br>List[int] size = [1, 1, 45]                            | Unknown  |
|  23 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [-1, 1, -1]                          | Unknown  |
|  24 | Tensor<[1, 1, 64, 300]> self = ?,<br>List[int] size = [1, 1, 64, 300]                  | Unknown  |
|  25 | Tensor<[1, 1, 64, 7]> self = ?,<br>List[int] size = [1, 71, 64, 7]                     | Unknown  |
|  26 | Tensor<[1, 1, 7, 7]> self = ?,<br>List[int] size = [2, 1, 7, 7]                        | Unknown  |
|  27 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, -1]                          | Unknown  |
|  28 | Tensor<[1, 10]> self = ?,<br>List[int] size = [1, 10]                                  | Unknown  |
|  29 | Tensor<[1, 12, 1, 10]> self = ?,<br>List[int] size = [1, 12, 1, 10]                    | Unknown  |
|  30 | Tensor<[1, 12, 1, 1]> self = ?,<br>List[int] size = [1, 12, 1, 1]                      | Unknown  |
|  31 | Tensor<[1, 12, 1, 2]> self = ?,<br>List[int] size = [1, 12, 1, 2]                      | Unknown  |
|  32 | Tensor<[1, 12, 1, 46]> self = ?,<br>List[int] size = [1, 12, 1, 46]                    | Unknown  |
|  33 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]                    | Unknown  |
|  34 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 12, 1, sym_size_int]      | Unknown  |
|  35 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 12, 1, sym_size_int_2]   | Unknown  |
|  36 | Tensor<[1, 12, 10, 10]> self = ?,<br>List[int] size = [1, 12, 10, 10]                  | Unknown  |
|  37 | Tensor<[1, 12, 10, 64]> self = ?,<br>List[int] size = [1, 12, 10, 64]                  | Unknown  |
|  38 | Tensor<[1, 12, 12, 12]> self = ?,<br>List[int] size = [1, 12, 12, 12]                  | Unknown  |
|  39 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] size = [1, 12, 12, 64]                  | Unknown  |
|  40 | Tensor<[1, 12, 14, 14]> self = ?,<br>List[int] size = [1, 12, 14, 14]                  | Unknown  |
|  41 | Tensor<[1, 12, 14, 64]> self = ?,<br>List[int] size = [1, 12, 14, 64]                  | Unknown  |
|  42 | Tensor<[1, 12, 16, 64]> self = ?,<br>List[int] size = [1, 12, 16, 64]                  | Unknown  |
|  43 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197]              | Unknown  |
|  44 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]                | Unknown  |
|  45 | Tensor<[1, 12, 2, 64]> self = ?,<br>List[int] size = [1, 12, 2, 64]                    | Unknown  |
|  46 | Tensor<[1, 12, 201, 201]> self = ?,<br>List[int] size = [1, 12, 201, 201]              | Unknown  |
|  47 | Tensor<[1, 12, 201, 64]> self = ?,<br>List[int] size = [1, 12, 201, 64]                | Unknown  |
|  48 | Tensor<[1, 12, 25, 25]> self = ?,<br>List[int] size = [1, 12, 25, 25]                  | Unknown  |
|  49 | Tensor<[1, 12, 25, 64]> self = ?,<br>List[int] size = [1, 12, 25, 64]                  | Unknown  |
|  50 | Tensor<[1, 12, 45, 45]> self = ?,<br>List[int] size = [1, 12, 45, 45]                  | Unknown  |
|  51 | Tensor<[1, 12, 45, 64]> self = ?,<br>List[int] size = [1, 12, 45, 64]                  | Unknown  |
|  52 | Tensor<[1, 12, 46, 64]> self = ?,<br>List[int] size = [1, 12, 46, 64]                  | Unknown  |
|  53 | Tensor<[1, 12, 64, 10]> self = ?,<br>List[int] size = [1, 12, 64, 10]                  | Unknown  |
|  54 | Tensor<[1, 12, 64, 12]> self = ?,<br>List[int] size = [1, 12, 64, 12]                  | Unknown  |
|  55 | Tensor<[1, 12, 64, 14]> self = ?,<br>List[int] size = [1, 12, 64, 14]                  | Unknown  |
|  56 | Tensor<[1, 12, 64, 16]> self = ?,<br>List[int] size = [1, 12, 64, 16]                  | Unknown  |
|  57 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [1, 12, 64, 197]                | Unknown  |
|  58 | Tensor<[1, 12, 64, 1]> self = ?,<br>List[int] size = [1, 12, 64, 1]                    | Unknown  |
|  59 | Tensor<[1, 12, 64, 201]> self = ?,<br>List[int] size = [1, 12, 64, 201]                | Unknown  |
|  60 | Tensor<[1, 12, 64, 25]> self = ?,<br>List[int] size = [1, 12, 64, 25]                  | Unknown  |
|  61 | Tensor<[1, 12, 64, 2]> self = ?,<br>List[int] size = [1, 12, 64, 2]                    | Unknown  |
|  62 | Tensor<[1, 12, 64, 45]> self = ?,<br>List[int] size = [1, 12, 64, 45]                  | Unknown  |
|  63 | Tensor<[1, 12, 64, 46]> self = ?,<br>List[int] size = [1, 12, 64, 46]                  | Unknown  |
|  64 | Tensor<[1, 12, 64, 7]> self = ?,<br>List[int] size = [1, 12, 64, 7]                    | Unknown  |
|  65 | Tensor<[1, 12, 64, 8]> self = ?,<br>List[int] size = [1, 12, 64, 8]                    | Unknown  |
|  66 | Tensor<[1, 12, 64, 9]> self = ?,<br>List[int] size = [1, 12, 64, 9]                    | Unknown  |
|  67 | Tensor<[1, 12, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 12, 64, sym_size_int]    | Unknown  |
|  68 | Tensor<[1, 12, 64, s10 + 1]> self = ?,<br>List[int] size = [1, 12, 64, sym_size_int_1] | Unknown  |
|  69 | Tensor<[1, 12, 7, 64]> self = ?,<br>List[int] size = [1, 12, 7, 64]                    | Unknown  |
|  70 | Tensor<[1, 12, 7, 7]> self = ?,<br>List[int] size = [1, 12, 7, 7]                      | Unknown  |
|  71 | Tensor<[1, 12, 8, 64]> self = ?,<br>List[int] size = [1, 12, 8, 64]                    | Unknown  |
|  72 | Tensor<[1, 12, 8, 8]> self = ?,<br>List[int] size = [1, 12, 8, 8]                      | Unknown  |
|  73 | Tensor<[1, 12, 9, 64]> self = ?,<br>List[int] size = [1, 12, 9, 64]                    | Unknown  |
|  74 | Tensor<[1, 12, 9, 9]> self = ?,<br>List[int] size = [1, 12, 9, 9]                      | Unknown  |
|  75 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 12, sym_size_int_1, 64]  | Unknown  |
|  76 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>List[int] size = [1, 12, sym_size_int_3, 64] | Unknown  |
|  77 | Tensor<[1, 16, 1, 10]> self = ?,<br>List[int] size = [1, 16, 1, 10]                    | Unknown  |
|  78 | Tensor<[1, 16, 1, 1]> self = ?,<br>List[int] size = [1, 16, 1, 1]                      | Unknown  |
|  79 | Tensor<[1, 16, 1, 2]> self = ?,<br>List[int] size = [1, 16, 1, 2]                      | Unknown  |
|  80 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [1, 16, 1, 64]                    | Unknown  |
|  81 | Tensor<[1, 16, 1, 6]> self = ?,<br>List[int] size = [1, 16, 1, 6]                      | Unknown  |
|  82 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 16, 1, sym_size_int]      | Unknown  |
|  83 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 16, 1, sym_size_int_1]   | Unknown  |
|  84 | Tensor<[1, 16, 10, 10]> self = ?,<br>List[int] size = [1, 16, 10, 10]                  | Unknown  |
|  85 | Tensor<[1, 16, 10, 64]> self = ?,<br>List[int] size = [1, 16, 10, 64]                  | Unknown  |
|  86 | Tensor<[1, 16, 128, 9]> self = ?,<br>List[int] size = [1, 16, 128, 9]                  | Unknown  |
|  87 | Tensor<[1, 16, 197, 197]> self = ?,<br>List[int] size = [1, 16, 197, 197]              | Unknown  |
|  88 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] size = [1, 16, 197, 64]                | Unknown  |
|  89 | Tensor<[1, 16, 2, 64]> self = ?,<br>List[int] size = [1, 16, 2, 64]                    | Unknown  |
|  90 | Tensor<[1, 16, 256, 256]> self = ?,<br>List[int] size = [1, 16, 256, 256]              | Unknown  |
|  91 | Tensor<[1, 16, 256, 64]> self = ?,<br>List[int] size = [1, 16, 256, 64]                | Unknown  |
|  92 | Tensor<[1, 16, 5, 5]> self = ?,<br>List[int] size = [1, 16, 5, 5]                      | Unknown  |
|  93 | Tensor<[1, 16, 5, 64]> self = ?,<br>List[int] size = [1, 16, 5, 64]                    | Unknown  |
|  94 | Tensor<[1, 16, 6, 64]> self = ?,<br>List[int] size = [1, 16, 6, 64]                    | Unknown  |
|  95 | Tensor<[1, 16, 64, 10]> self = ?,<br>List[int] size = [1, 16, 64, 10]                  | Unknown  |
|  96 | Tensor<[1, 16, 64, 197]> self = ?,<br>List[int] size = [1, 16, 64, 197]                | Unknown  |
|  97 | Tensor<[1, 16, 64, 1]> self = ?,<br>List[int] size = [1, 16, 64, 1]                    | Unknown  |
|  98 | Tensor<[1, 16, 64, 256]> self = ?,<br>List[int] size = [1, 16, 64, 256]                | Unknown  |
|  99 | Tensor<[1, 16, 64, 2]> self = ?,<br>List[int] size = [1, 16, 64, 2]                    | Unknown  |
| 100 | Tensor<[1, 16, 64, 5]> self = ?,<br>List[int] size = [1, 16, 64, 5]                    | Unknown  |
| 101 | Tensor<[1, 16, 64, 6]> self = ?,<br>List[int] size = [1, 16, 64, 6]                    | Unknown  |
| 102 | Tensor<[1, 16, 64, 9]> self = ?,<br>List[int] size = [1, 16, 64, 9]                    | Unknown  |
| 103 | Tensor<[1, 16, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 16, 64, sym_size_int]    | Unknown  |
| 104 | Tensor<[1, 16, 64, s10 + 1]> self = ?,<br>List[int] size = [1, 16, 64, sym_size_int]   | Unknown  |
| 105 | Tensor<[1, 16, 9, 128]> self = ?,<br>List[int] size = [1, 16, 9, 128]                  | Unknown  |
| 106 | Tensor<[1, 16, 9, 64]> self = ?,<br>List[int] size = [1, 16, 9, 64]                    | Unknown  |
| 107 | Tensor<[1, 16, 9, 9]> self = ?,<br>List[int] size = [1, 16, 9, 9]                      | Unknown  |
| 108 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 16, sym_size_int_1, 64]  | Unknown  |
| 109 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>List[int] size = [1, 16, sym_size_int_2, 64] | Unknown  |
| 110 | Tensor<[1, 1]> self = ?,<br>List[int] size = [1, 1]                                    | Unknown  |
| 111 | Tensor<[1, 1]> self = ?,<br>List[int] size = [1, 512]                                  | Unknown  |
| 112 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] size = [1, 2, 256, 32]                  | Unknown  |
| 113 | Tensor<[1, 2, 300, 64]> self = ?,<br>List[int] size = [1, 2, 300, 64]                  | Unknown  |
| 114 | Tensor<[1, 2, 32, 256]> self = ?,<br>List[int] size = [1, 2, 32, 256]                  | Unknown  |
| 115 | Tensor<[1, 2, 4096, 256]> self = ?,<br>List[int] size = [1, 2, 4096, 256]              | Unknown  |
| 116 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] size = [1, 2, 4096, 32]                | Unknown  |
| 117 | Tensor<[1, 2, 4800, 300]> self = ?,<br>List[int] size = [1, 2, 4800, 300]              | Unknown  |
| 118 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] size = [1, 2, 4800, 64]                | Unknown  |
| 119 | Tensor<[1, 2, 64, 300]> self = ?,<br>List[int] size = [1, 2, 64, 300]                  | Unknown  |
| 120 | Tensor<[1, 24, 32, 49]> self = ?,<br>List[int] size = [1, 24, 32, 49]                  | Unknown  |
| 121 | Tensor<[1, 24, 32, 64]> self = ?,<br>List[int] size = [1, 24, 32, 64]                  | Unknown  |
| 122 | Tensor<[1, 24, 49, 32]> self = ?,<br>List[int] size = [1, 24, 49, 32]                  | Unknown  |
| 123 | Tensor<[1, 24, 49, 49]> self = ?,<br>List[int] size = [1, 24, 49, 49]                  | Unknown  |
| 124 | Tensor<[1, 24, 64, 1]> self = ?,<br>List[int] size = [1, 24, 64, 32]                   | Unknown  |
| 125 | Tensor<[1, 24, 64, 64]> self = ?,<br>List[int] size = [1, 24, 64, 64]                  | Unknown  |
| 126 | Tensor<[1, 25]> self = ?,<br>List[int] size = [1, 25]                                  | Unknown  |
| 127 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>List[int] size = [1, 3, 1445, 1445]            | Unknown  |
| 128 | Tensor<[1, 3, 1445, 64]> self = ?,<br>List[int] size = [1, 3, 1445, 64]                | Unknown  |
| 129 | Tensor<[1, 3, 64, 1445]> self = ?,<br>List[int] size = [1, 3, 64, 1445]                | Unknown  |
| 130 | Tensor<[1, 32, 128, 32]> self = ?,<br>List[int] size = [1, 32, 128, 32]                | Unknown  |
| 131 | Tensor<[1, 32, 32, 128]> self = ?,<br>List[int] size = [1, 32, 32, 128]                | Unknown  |
| 132 | Tensor<[1, 32, 32, 32]> self = ?,<br>List[int] size = [1, 32, 32, 32]                  | Unknown  |
| 133 | Tensor<[1, 32, 32, 49]> self = ?,<br>List[int] size = [1, 32, 32, 49]                  | Unknown  |
| 134 | Tensor<[1, 32, 32, 64]> self = ?,<br>List[int] size = [1, 32, 32, 64]                  | Unknown  |
| 135 | Tensor<[1, 32, 49, 32]> self = ?,<br>List[int] size = [1, 32, 49, 32]                  | Unknown  |
| 136 | Tensor<[1, 32, 49, 49]> self = ?,<br>List[int] size = [1, 32, 49, 49]                  | Unknown  |
| 137 | Tensor<[1, 32, 64, 1]> self = ?,<br>List[int] size = [1, 32, 64, 32]                   | Unknown  |
| 138 | Tensor<[1, 32, 64, 64]> self = ?,<br>List[int] size = [1, 32, 64, 64]                  | Unknown  |
| 139 | Tensor<[1, 5, 1, 16, 1]> self = ?,<br>List[int] size = [1, 5, 1, 16, 2]                | Unknown  |
| 140 | Tensor<[1, 5, 1024, 256]> self = ?,<br>List[int] size = [1, 5, 1024, 256]              | Unknown  |
| 141 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] size = [1, 5, 1024, 32]                | Unknown  |
| 142 | Tensor<[1, 5, 1200, 300]> self = ?,<br>List[int] size = [1, 5, 1200, 300]              | Unknown  |
| 143 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] size = [1, 5, 1200, 64]                | Unknown  |
| 144 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] size = [1, 5, 256, 32]                  | Unknown  |
| 145 | Tensor<[1, 5, 300, 64]> self = ?,<br>List[int] size = [1, 5, 300, 64]                  | Unknown  |
| 146 | Tensor<[1, 5, 32, 256]> self = ?,<br>List[int] size = [1, 5, 32, 256]                  | Unknown  |
| 147 | Tensor<[1, 5, 64, 300]> self = ?,<br>List[int] size = [1, 5, 64, 300]                  | Unknown  |
| 148 | Tensor<[1, 6, 1, 15]> self = ?,<br>List[int] size = [1, 6, 1, 15]                      | Unknown  |
| 149 | Tensor<[1, 6, 1, 17]> self = ?,<br>List[int] size = [1, 6, 1, 17]                      | Unknown  |
| 150 | Tensor<[1, 6, 1, 1]> self = ?,<br>List[int] size = [1, 6, 1, 1]                        | Unknown  |
| 151 | Tensor<[1, 6, 1, 2]> self = ?,<br>List[int] size = [1, 6, 1, 2]                        | Unknown  |
| 152 | Tensor<[1, 6, 1, 64]> self = ?,<br>List[int] size = [1, 6, 1, 64]                      | Unknown  |
| 153 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 6, 1, sym_size_int]        | Unknown  |
| 154 | Tensor<[1, 6, 15, 15]> self = ?,<br>List[int] size = [1, 6, 15, 15]                    | Unknown  |
| 155 | Tensor<[1, 6, 15, 64]> self = ?,<br>List[int] size = [1, 6, 15, 64]                    | Unknown  |
| 156 | Tensor<[1, 6, 17, 64]> self = ?,<br>List[int] size = [1, 6, 17, 64]                    | Unknown  |
| 157 | Tensor<[1, 6, 2, 64]> self = ?,<br>List[int] size = [1, 6, 2, 64]                      | Unknown  |
| 158 | Tensor<[1, 6, 64, 15]> self = ?,<br>List[int] size = [1, 6, 64, 15]                    | Unknown  |
| 159 | Tensor<[1, 6, 64, 17]> self = ?,<br>List[int] size = [1, 6, 64, 17]                    | Unknown  |
| 160 | Tensor<[1, 6, 64, 1]> self = ?,<br>List[int] size = [1, 6, 64, 1]                      | Unknown  |
| 161 | Tensor<[1, 6, 64, 2]> self = ?,<br>List[int] size = [1, 6, 64, 2]                      | Unknown  |
| 162 | Tensor<[1, 6, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 6, 64, sym_size_int]      | Unknown  |
| 163 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 6, sym_size_int_1, 64]    | Unknown  |
| 164 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, -1, 1]                            | Unknown  |
| 165 | Tensor<[1, 64, 64, 9]> self = ?,<br>List[int] size = [1, 64, 64, 9]                    | Unknown  |
| 166 | Tensor<[1, 64, 9, 64]> self = ?,<br>List[int] size = [1, 64, 9, 64]                    | Unknown  |
| 167 | Tensor<[1, 64, 9, 9]> self = ?,<br>List[int] size = [1, 64, 9, 9]                      | Unknown  |
| 168 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64]                    | Unknown  |
| 169 | Tensor<[1, 71, 7, 7]> self = ?,<br>List[int] size = [1, 71, 7, 7]                      | Unknown  |
| 170 | Tensor<[1, 8, 1, 10]> self = ?,<br>List[int] size = [1, 8, 1, 10]                      | Unknown  |
| 171 | Tensor<[1, 8, 1, 1]> self = ?,<br>List[int] size = [1, 8, 1, 1]                        | Unknown  |
| 172 | Tensor<[1, 8, 1, 2]> self = ?,<br>List[int] size = [1, 8, 1, 2]                        | Unknown  |
| 173 | Tensor<[1, 8, 1, 64]> self = ?,<br>List[int] size = [1, 8, 1, 64]                      | Unknown  |
| 174 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 8, 1, sym_size_int]        | Unknown  |
| 175 | Tensor<[1, 8, 10, 10]> self = ?,<br>List[int] size = [1, 8, 10, 10]                    | Unknown  |
| 176 | Tensor<[1, 8, 10, 64]> self = ?,<br>List[int] size = [1, 8, 10, 64]                    | Unknown  |
| 177 | Tensor<[1, 8, 2, 64]> self = ?,<br>List[int] size = [1, 8, 2, 64]                      | Unknown  |
| 178 | Tensor<[1, 8, 2048, 160]> self = ?,<br>List[int] size = [1, 8, 2048, 160]              | Unknown  |
| 179 | Tensor<[1, 8, 2048, 256]> self = ?,<br>List[int] size = [1, 8, 2048, 256]              | Unknown  |
| 180 | Tensor<[1, 8, 2048, 32]> self = ?,<br>List[int] size = [1, 8, 2048, 32]                | Unknown  |
| 181 | Tensor<[1, 8, 256, 160]> self = ?,<br>List[int] size = [1, 8, 256, 160]                | Unknown  |
| 182 | Tensor<[1, 8, 256, 2048]> self = ?,<br>List[int] size = [1, 8, 256, 2048]              | Unknown  |
| 183 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]                | Unknown  |
| 184 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [1, 8, 256, 32]                  | Unknown  |
| 185 | Tensor<[1, 8, 256, 96]> self = ?,<br>List[int] size = [1, 8, 256, 96]                  | Unknown  |
| 186 | Tensor<[1, 8, 300, 300]> self = ?,<br>List[int] size = [1, 8, 300, 300]                | Unknown  |
| 187 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] size = [1, 8, 300, 64]                  | Unknown  |
| 188 | Tensor<[1, 8, 32, 2048]> self = ?,<br>List[int] size = [1, 8, 32, 2048]                | Unknown  |
| 189 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [1, 8, 32, 256]                  | Unknown  |
| 190 | Tensor<[1, 8, 64, 10]> self = ?,<br>List[int] size = [1, 8, 64, 10]                    | Unknown  |
| 191 | Tensor<[1, 8, 64, 1]> self = ?,<br>List[int] size = [1, 8, 64, 1]                      | Unknown  |
| 192 | Tensor<[1, 8, 64, 2]> self = ?,<br>List[int] size = [1, 8, 64, 2]                      | Unknown  |
| 193 | Tensor<[1, 8, 64, 300]> self = ?,<br>List[int] size = [1, 8, 64, 300]                  | Unknown  |
| 194 | Tensor<[1, 8, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 8, 64, sym_size_int]      | Unknown  |
| 195 | Tensor<[1, 8, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 8, sym_size_int_1, 64]    | Unknown  |
| 196 | Tensor<[10, 1]> self = ?,<br>List[int] size = [10, 10]                                 | Unknown  |
| 197 | Tensor<[100, 1]> self = ?,<br>List[int] size = [100, 136]                              | Unknown  |
| 198 | Tensor<[12, 1]> self = ?,<br>List[int] size = [12, 16]                                 | Unknown  |
| 199 | Tensor<[13, 1]> self = ?,<br>List[int] size = [13, 17]                                 | Unknown  |
| 200 | Tensor<[16, 6, 32, 49]> self = ?,<br>List[int] size = [16, 6, 32, 49]                  | Unknown  |
| 201 | Tensor<[16, 6, 32, 64]> self = ?,<br>List[int] size = [16, 6, 32, 64]                  | Unknown  |
| 202 | Tensor<[16, 6, 49, 32]> self = ?,<br>List[int] size = [16, 6, 49, 32]                  | Unknown  |
| 203 | Tensor<[16, 6, 49, 49]> self = ?,<br>List[int] size = [16, 6, 49, 49]                  | Unknown  |
| 204 | Tensor<[16, 6, 64, 1]> self = ?,<br>List[int] size = [16, 6, 64, 32]                   | Unknown  |
| 205 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int] size = [16, 6, 64, 64]                  | Unknown  |
| 206 | Tensor<[16, 8, 32, 49]> self = ?,<br>List[int] size = [16, 8, 32, 49]                  | Unknown  |
| 207 | Tensor<[16, 8, 32, 64]> self = ?,<br>List[int] size = [16, 8, 32, 64]                  | Unknown  |
| 208 | Tensor<[16, 8, 49, 32]> self = ?,<br>List[int] size = [16, 8, 49, 32]                  | Unknown  |
| 209 | Tensor<[16, 8, 49, 49]> self = ?,<br>List[int] size = [16, 8, 49, 49]                  | Unknown  |
| 210 | Tensor<[16, 8, 64, 1]> self = ?,<br>List[int] size = [16, 8, 64, 32]                   | Unknown  |
| 211 | Tensor<[16, 8, 64, 64]> self = ?,<br>List[int] size = [16, 8, 64, 64]                  | Unknown  |
| 212 | Tensor<[19, 1]> self = ?,<br>List[int] size = [19, 19]                                 | Unknown  |
| 213 | Tensor<[2, 1]> self = ?,<br>List[int] size = [2, 2]                                    | Unknown  |
| 214 | Tensor<[20, 1]> self = ?,<br>List[int] size = [20, 20]                                 | Unknown  |
| 215 | Tensor<[24, 12, 64]> self = ?,<br>List[int] size = [24, 12, 64]                        | Unknown  |
| 216 | Tensor<[24, 64, 24]> self = ?,<br>List[int] size = [24, 64, 24]                        | Unknown  |
| 217 | Tensor<[25, 1]> self = ?,<br>List[int] size = [25, 34]                                 | Unknown  |
| 218 | Tensor<[256, 1280]> self = ?,<br>List[int] size = [1, -1, -1]                          | Unknown  |
| 219 | Tensor<[3, 1]> self = ?,<br>List[int] size = [3, 3]                                    | Unknown  |
| 220 | Tensor<[38, 1]> self = ?,<br>List[int] size = [38, 38]                                 | Unknown  |
| 221 | Tensor<[4, 12, 32, 49]> self = ?,<br>List[int] size = [4, 12, 32, 49]                  | Unknown  |
| 222 | Tensor<[4, 12, 32, 64]> self = ?,<br>List[int] size = [4, 12, 32, 64]                  | Unknown  |
| 223 | Tensor<[4, 12, 49, 32]> self = ?,<br>List[int] size = [4, 12, 49, 32]                  | Unknown  |
| 224 | Tensor<[4, 12, 49, 49]> self = ?,<br>List[int] size = [4, 12, 49, 49]                  | Unknown  |
| 225 | Tensor<[4, 12, 64, 1]> self = ?,<br>List[int] size = [4, 12, 64, 32]                   | Unknown  |
| 226 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int] size = [4, 12, 64, 64]                  | Unknown  |
| 227 | Tensor<[4, 16, 32, 49]> self = ?,<br>List[int] size = [4, 16, 32, 49]                  | Unknown  |
| 228 | Tensor<[4, 16, 32, 64]> self = ?,<br>List[int] size = [4, 16, 32, 64]                  | Unknown  |
| 229 | Tensor<[4, 16, 49, 32]> self = ?,<br>List[int] size = [4, 16, 49, 32]                  | Unknown  |
| 230 | Tensor<[4, 16, 49, 49]> self = ?,<br>List[int] size = [4, 16, 49, 49]                  | Unknown  |
| 231 | Tensor<[4, 16, 64, 1]> self = ?,<br>List[int] size = [4, 16, 64, 32]                   | Unknown  |
| 232 | Tensor<[4, 16, 64, 64]> self = ?,<br>List[int] size = [4, 16, 64, 64]                  | Unknown  |
| 233 | Tensor<[5, 1]> self = ?,<br>List[int] size = [5, 5]                                    | Unknown  |
| 234 | Tensor<[50, 1]> self = ?,<br>List[int] size = [50, 68]                                 | Unknown  |
| 235 | Tensor<[64, 3, 32, 49]> self = ?,<br>List[int] size = [64, 3, 32, 49]                  | Unknown  |
| 236 | Tensor<[64, 3, 32, 64]> self = ?,<br>List[int] size = [64, 3, 32, 64]                  | Unknown  |
| 237 | Tensor<[64, 3, 49, 32]> self = ?,<br>List[int] size = [64, 3, 49, 32]                  | Unknown  |
| 238 | Tensor<[64, 3, 49, 49]> self = ?,<br>List[int] size = [64, 3, 49, 49]                  | Unknown  |
| 239 | Tensor<[64, 3, 64, 1]> self = ?,<br>List[int] size = [64, 3, 64, 32]                   | Unknown  |
| 240 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int] size = [64, 3, 64, 64]                  | Unknown  |
| 241 | Tensor<[64, 4, 32, 49]> self = ?,<br>List[int] size = [64, 4, 32, 49]                  | Unknown  |
| 242 | Tensor<[64, 4, 32, 64]> self = ?,<br>List[int] size = [64, 4, 32, 64]                  | Unknown  |
| 243 | Tensor<[64, 4, 49, 32]> self = ?,<br>List[int] size = [64, 4, 49, 32]                  | Unknown  |
| 244 | Tensor<[64, 4, 49, 49]> self = ?,<br>List[int] size = [64, 4, 49, 49]                  | Unknown  |
| 245 | Tensor<[64, 4, 64, 1]> self = ?,<br>List[int] size = [64, 4, 64, 32]                   | Unknown  |
| 246 | Tensor<[64, 4, 64, 64]> self = ?,<br>List[int] size = [64, 4, 64, 64]                  | Unknown  |
| 247 | Tensor<[7, 1]> self = ?,<br>List[int] size = [7, 9]                                    | Unknown  |
| 248 | Tensor<[768]> self = ?,<br>List[int] size = [1, 1, -1]                                 | Unknown  |
### aten.fill.Scalar
|    | ATen Input Variations                    | Status   |
|---:|:-----------------------------------------|:---------|
|  0 | Tensor<[]> self = ?,<br>number value = 8 | Unknown  |
### aten.floor.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 42]> self = ? | Unknown  |
### aten.floor_divide.default
|    | ATen Input Variations                       | Status   |
|---:|:--------------------------------------------|:---------|
|  0 | Tensor<[128]> self = ?,<br>Tensor other = 2 | Unknown  |
### aten.full.default
|    | ATen Input Variations                                                                                                                                            | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int] size = [19, 19],<br>number fill_value = -3.4028234663852886e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                | Unknown  |
|  1 | List[int] size = [32, 32],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                | Unknown  |
|  2 | List[int] size = [45, 45],<br>number fill_value = -3.4028234663852886e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                | Unknown  |
|  3 | List[int] size = [7, 7],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                  | Unknown  |
|  4 | List[int] size = [],<br>number fill_value = 8.0,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.full_like.default
|    | ATen Input Variations                                                                                                                                             | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 193]> self = ?,<br>number fill_value = 1,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
|  1 | Tensor<[1, 1]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False                                                                          | Unknown  |
|  2 | Tensor<[10, 10]> self = ?,<br>number fill_value = 15,<br>Optional[bool] pin_memory = False                                                                        | Unknown  |
|  3 | Tensor<[15, 15]> self = ?,<br>number fill_value = 15,<br>Optional[bool] pin_memory = False                                                                        | Unknown  |
### aten.gelu.default
|    | ATen Input Variations             | Status   |
|---:|:----------------------------------|:---------|
|  0 | Tensor<[1, 10, 3072]> self = ?    | Unknown  |
|  1 | Tensor<[1, 1024, 512]> self = ?   | Unknown  |
|  2 | Tensor<[1, 1370, 5120]> self = ?  | Unknown  |
|  3 | Tensor<[1, 1445, 768]> self = ?   | Unknown  |
|  4 | Tensor<[1, 16, 3072]> self = ?    | Unknown  |
|  5 | Tensor<[1, 16384, 128]> self = ?  | Unknown  |
|  6 | Tensor<[1, 19, 4096]> self = ?    | Unknown  |
|  7 | Tensor<[1, 19200, 256]> self = ?  | Unknown  |
|  8 | Tensor<[1, 197, 3072]> self = ?   | Unknown  |
|  9 | Tensor<[1, 197, 4096]> self = ?   | Unknown  |
| 10 | Tensor<[1, 201, 3072]> self = ?   | Unknown  |
| 11 | Tensor<[1, 24, 3072]> self = ?    | Unknown  |
| 12 | Tensor<[1, 25, 3072]> self = ?    | Unknown  |
| 13 | Tensor<[1, 256, 1280]> self = ?   | Unknown  |
| 14 | Tensor<[1, 256, 4096]> self = ?   | Unknown  |
| 15 | Tensor<[1, 3072, 8]> self = ?     | Unknown  |
| 16 | Tensor<[1, 50, 3072]> self = ?    | Unknown  |
| 17 | Tensor<[1, 50, 4096]> self = ?    | Unknown  |
| 18 | Tensor<[1, 56, 56, 384]> self = ? | Unknown  |
| 19 | Tensor<[1, 56, 56, 512]> self = ? | Unknown  |
| 20 | Tensor<[1, 64, 64, 384]> self = ? | Unknown  |
| 21 | Tensor<[1, 64, 64, 512]> self = ? | Unknown  |
| 22 | Tensor<[1, 7, 18176]> self = ?    | Unknown  |
| 23 | Tensor<[1, 768, 3000]> self = ?   | Unknown  |
| 24 | Tensor<[1, 768, 384]> self = ?    | Unknown  |
### aten.gt.Scalar
|    | ATen Input Variations                          | Status   |
|---:|:-----------------------------------------------|:---------|
|  0 | Tensor<[10, 10]> self = ?,<br>number other = 0 | Unknown  |
|  1 | Tensor<[15, 15]> self = ?,<br>number other = 0 | Unknown  |
|  2 | Tensor<[]> self = ?,<br>number other = 0       | Unknown  |
### aten.hardsigmoid.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 16, 1, 1]> self = ?  | Unknown  |
|  1 | Tensor<[1, 256, 1, 1]> self = ? | Unknown  |
|  2 | Tensor<[1, 72, 1, 1]> self = ?  | Unknown  |
### aten.hardswish.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 16, 112, 112]> self = ? | Unknown  |
|  1 | Tensor<[1, 16, 160, 160]> self = ? | Unknown  |
### aten.hardtanh.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 10, 10]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0  | Unknown  |
|  1 | Tensor<[1, 32, 112, 112]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | Unknown  |
|  2 | Tensor<[1, 32, 120, 120]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | Unknown  |
|  3 | Tensor<[1, 32, 130, 130]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | Unknown  |
|  4 | Tensor<[1, 32, 150, 150]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | Unknown  |
|  5 | Tensor<[1, 32, 190, 190]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | Unknown  |
### aten.index.Tensor
|    | ATen Input Variations                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 32]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, arg324_1]      | Unknown  |
|  1 | Tensor<[1, 7, 2]> self = ?,<br>List[Optional[Tensor]] indices = [arange_1, remainder]              | Unknown  |
|  2 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, lift_fresh_copy] | Unknown  |
|  3 | Tensor<[169, 12]> self = ?,<br>List[Optional[Tensor]] indices = [primals_178]                      | Unknown  |
|  4 | Tensor<[169, 12]> self = ?,<br>List[Optional[Tensor]] indices = [primals_334]                      | Unknown  |
|  5 | Tensor<[169, 16]> self = ?,<br>List[Optional[Tensor]] indices = [primals_334]                      | Unknown  |
|  6 | Tensor<[169, 24]> self = ?,<br>List[Optional[Tensor]] indices = [primals_184]                      | Unknown  |
|  7 | Tensor<[169, 24]> self = ?,<br>List[Optional[Tensor]] indices = [primals_352]                      | Unknown  |
|  8 | Tensor<[169, 32]> self = ?,<br>List[Optional[Tensor]] indices = [primals_352]                      | Unknown  |
|  9 | Tensor<[169, 3]> self = ?,<br>List[Optional[Tensor]] indices = [primals_174]                       | Unknown  |
| 10 | Tensor<[169, 3]> self = ?,<br>List[Optional[Tensor]] indices = [primals_330]                       | Unknown  |
| 11 | Tensor<[169, 4]> self = ?,<br>List[Optional[Tensor]] indices = [primals_330]                       | Unknown  |
| 12 | Tensor<[169, 6]> self = ?,<br>List[Optional[Tensor]] indices = [primals_176]                       | Unknown  |
| 13 | Tensor<[169, 6]> self = ?,<br>List[Optional[Tensor]] indices = [primals_332]                       | Unknown  |
| 14 | Tensor<[169, 8]> self = ?,<br>List[Optional[Tensor]] indices = [primals_332]                       | Unknown  |
| 15 | Tensor<[2, 7, 512]> self = ?,<br>List[Optional[Tensor]] indices = [arange, argmax]                 | Unknown  |
| 16 | Tensor<[2048, 32]> self = ?,<br>List[Optional[Tensor]] indices = [arg226_1]                        | Unknown  |
| 17 | Tensor<[225, 12]> self = ?,<br>List[Optional[Tensor]] indices = [primals_219]                      | Unknown  |
| 18 | Tensor<[225, 12]> self = ?,<br>List[Optional[Tensor]] indices = [primals_411]                      | Unknown  |
| 19 | Tensor<[225, 16]> self = ?,<br>List[Optional[Tensor]] indices = [primals_411]                      | Unknown  |
| 20 | Tensor<[225, 24]> self = ?,<br>List[Optional[Tensor]] indices = [primals_231]                      | Unknown  |
| 21 | Tensor<[225, 24]> self = ?,<br>List[Optional[Tensor]] indices = [primals_447]                      | Unknown  |
| 22 | Tensor<[225, 32]> self = ?,<br>List[Optional[Tensor]] indices = [primals_447]                      | Unknown  |
| 23 | Tensor<[225, 3]> self = ?,<br>List[Optional[Tensor]] indices = [primals_211]                       | Unknown  |
| 24 | Tensor<[225, 3]> self = ?,<br>List[Optional[Tensor]] indices = [primals_403]                       | Unknown  |
| 25 | Tensor<[225, 4]> self = ?,<br>List[Optional[Tensor]] indices = [primals_403]                       | Unknown  |
| 26 | Tensor<[225, 6]> self = ?,<br>List[Optional[Tensor]] indices = [primals_215]                       | Unknown  |
| 27 | Tensor<[225, 6]> self = ?,<br>List[Optional[Tensor]] indices = [primals_407]                       | Unknown  |
| 28 | Tensor<[225, 8]> self = ?,<br>List[Optional[Tensor]] indices = [primals_407]                       | Unknown  |
| 29 | Tensor<[7, 64]> self = ?,<br>List[Optional[Tensor]] indices = [primals_2]                          | Unknown  |
| 30 | Tensor<[732, 12]> self = ?,<br>List[Optional[Tensor]] indices = [view_13]                          | Unknown  |
| 31 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]] indices = [view_13]                          | Unknown  |
### aten.index_select.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[2050, 1024]> self = ?,<br>int dim = 0,<br>Tensor<[19]> index = ? | Unknown  |
### aten.le.Tensor
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1]> other = ? | Unknown  |
### aten.leaky_relu.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 25600]> self = ?                                | Unknown  |
|  1 | Tensor<[1, 512, 100]> self = ?,<br>number negative_slope = 0.1 | Unknown  |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor self = ?         | Unknown  |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                            | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 512, 38, 38]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [1],<br>bool keepdim = True | Unknown  |
|  1 | Tensor<[1, 512]> self = ?,<br>number ord = 2,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True          | Unknown  |
|  2 | Tensor<[1, 512]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [1],<br>bool keepdim = True         | Unknown  |
|  3 | Tensor<[64, 3, 64, 32]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | Unknown  |
|  4 | Tensor<[64, 4, 64, 32]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | Unknown  |
### aten.log.default
|    | ATen Input Variations     | Status   |
|---:|:--------------------------|:---------|
|  0 | Tensor<[10, 10]> self = ? | Unknown  |
|  1 | Tensor<[15, 15]> self = ? | Unknown  |
### aten.logical_not.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[7, 7]> self = ? | Unknown  |
### aten.lt.Scalar
|    | ATen Input Variations                          | Status   |
|---:|:-----------------------------------------------|:---------|
|  0 | Tensor<[1, 1]> self = ?,<br>number other = 16  | Unknown  |
|  1 | Tensor<[10, 10]> self = ?,<br>number other = 8 | Unknown  |
|  2 | Tensor<[15, 15]> self = ?,<br>number other = 8 | Unknown  |
### aten.lt.Tensor
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50257]> self = ?,<br>Tensor<[1, 1]> other = ? | Unknown  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                          | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 19, 19]> self = ?,<br>Tensor<[1, 1, 19, 19]> mask = ?,<br>number value = -3.4028234663852886e+38 | Unknown  |
|  1 | Tensor<[1, 1, 24, 24]> self = ?,<br>Tensor<[1, 1, 24, 24]> mask = ?,<br>number value = -3.4028234663852886e+38 | Unknown  |
|  2 | Tensor<[1, 1, 32, 32]> self = ?,<br>Tensor<[1, 1, 32, 32]> mask = ?,<br>number value = -3.3895313892515355e+38 | Unknown  |
|  3 | Tensor<[1, 1, 45, 45]> self = ?,<br>Tensor<[1, 1, 45, 45]> mask = ?,<br>number value = -3.4028234663852886e+38 | Unknown  |
|  4 | Tensor<[1, 50257]> self = ?,<br>Tensor<[1, 50257]> mask = ?,<br>number value = -inf                            | Unknown  |
|  5 | Tensor<[1, 920]> self = ?,<br>Tensor<[1, 920]> mask = ?,<br>number value = -inf                                | Unknown  |
|  6 | Tensor<[16, 49, 49]> self = ?,<br>Tensor<[16, 49, 49]> mask = ?,<br>number value = 0.0                         | Unknown  |
|  7 | Tensor<[16, 64, 64]> self = ?,<br>Tensor<[16, 64, 64]> mask = ?,<br>number value = 0.0                         | Unknown  |
|  8 | Tensor<[2, 1, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> mask = ?,<br>number value = -3.3895313892515355e+38     | Unknown  |
|  9 | Tensor<[64, 49, 49]> self = ?,<br>Tensor<[64, 49, 49]> mask = ?,<br>number value = -100.0                      | Unknown  |
| 10 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 64]> mask = ?,<br>number value = -100.0                      | Unknown  |
| 11 | Tensor<[7, 7]> self = ?,<br>Tensor<[7, 7]> mask = ?,<br>number value = -inf                                    | Unknown  |
### aten.masked_fill.Tensor
|    | ATen Input Variations                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 16, 16]> self = ?,<br>Tensor<[1, 12, 16, 16]> mask = ?,<br>Tensor<[]> value = ? | Unknown  |
### aten.max.default
|    | ATen Input Variations    | Status   |
|---:|:-------------------------|:---------|
|  0 | Tensor<[1]> self = ?     | Unknown  |
|  1 | Tensor<[25, 4]> self = ? | Unknown  |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                                                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 192, 28, 28]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True  | Unknown  |
|  1 | Tensor<[1, 256, 56, 56]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True  | Unknown  |
|  2 | Tensor<[1, 256, 75, 75]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True  | Unknown  |
|  3 | Tensor<[1, 32, 112, 112]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]                                                                                          | Unknown  |
|  4 | Tensor<[1, 32, 256, 256]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]                                                                                          | Unknown  |
|  5 | Tensor<[1, 512, 19, 19]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1]                                                            | Unknown  |
|  6 | Tensor<[1, 64, 112, 112]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True | Unknown  |
|  7 | Tensor<[1, 64, 112, 112]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1]                                                           | Unknown  |
|  8 | Tensor<[1, 64, 147, 147]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2]                                                                                          | Unknown  |
|  9 | Tensor<[1, 64, 224, 224]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]                                                                                          | Unknown  |
| 10 | Tensor<[1, 64, 24, 24]> self = ?,<br>List[int] kernel_size = [2, 2]                                                                                                                          | Unknown  |
| 11 | Tensor<[1, 64, 300, 300]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]                                                                                          | Unknown  |
| 12 | Tensor<[1, 64, 360, 640]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1]                                                           | Unknown  |
| 13 | Tensor<[1, 64, 400, 544]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1]                                                           | Unknown  |
| 14 | Tensor<[1, 832, 14, 14]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True  | Unknown  |
| 15 | Tensor<[1, 96, 112, 112]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1]                                                           | Unknown  |
### aten.maximum.default
|    | ATen Input Variations                                     | Status   |
|---:|:----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 19, 19]> self = ?,<br>Tensor<[]> other = ? | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 1024]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True         | Unknown  |
|  1 | Tensor<[1, 10, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True          | Unknown  |
|  2 | Tensor<[1, 10, 768]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True          | Unknown  |
|  3 | Tensor<[1, 1008, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Unknown  |
|  4 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Unknown  |
|  5 | Tensor<[1, 1024, 8, 8]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Unknown  |
|  6 | Tensor<[1, 1280, 10, 10]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Unknown  |
|  7 | Tensor<[1, 1280, 12, 12]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Unknown  |
|  8 | Tensor<[1, 1280, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Unknown  |
|  9 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Unknown  |
| 10 | Tensor<[1, 1280, 9, 9]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Unknown  |
| 11 | Tensor<[1, 15, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True          | Unknown  |
| 12 | Tensor<[1, 1536, 8, 8]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Unknown  |
| 13 | Tensor<[1, 16, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Unknown  |
| 14 | Tensor<[1, 1664, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Unknown  |
| 15 | Tensor<[1, 1920, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Unknown  |
| 16 | Tensor<[1, 196, 1024]> self = ?,<br>Optional[List[int]] dim = [1]                                 | Unknown  |
| 17 | Tensor<[1, 196, 768]> self = ?,<br>Optional[List[int]] dim = [1]                                  | Unknown  |
| 18 | Tensor<[1, 2048, 10, 10]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Unknown  |
| 19 | Tensor<[1, 2048, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Unknown  |
| 20 | Tensor<[1, 2208, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Unknown  |
| 21 | Tensor<[1, 224, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Unknown  |
| 22 | Tensor<[1, 232, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Unknown  |
| 23 | Tensor<[1, 2520, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Unknown  |
| 24 | Tensor<[1, 256, 512]> self = ?,<br>Optional[List[int]] dim = [1]                                  | Unknown  |
| 25 | Tensor<[1, 256, 56, 56]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True    | Unknown  |
| 26 | Tensor<[1, 32, 4096]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True         | Unknown  |
| 27 | Tensor<[1, 400, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Unknown  |
| 28 | Tensor<[1, 48, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Unknown  |
| 29 | Tensor<[1, 512, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Unknown  |
| 30 | Tensor<[1, 528, 96, 96]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Unknown  |
| 31 | Tensor<[1, 64, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Unknown  |
| 32 | Tensor<[1, 672, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Unknown  |
| 33 | Tensor<[1, 72, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Unknown  |
| 34 | Tensor<[1, 72, 28, 28]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True     | Unknown  |
| 35 | Tensor<[1, 72, 40, 40]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Unknown  |
| 36 | Tensor<[1, 72, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Unknown  |
| 37 | Tensor<[1, 768, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Unknown  |
| 38 | Tensor<[1, 768, 8, 8]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Unknown  |
| 39 | Tensor<[1, 912, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Unknown  |
| 40 | Tensor<[1, 960, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Unknown  |
### aten.min.default
|    | ATen Input Variations               | Status   |
|---:|:------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ? | Unknown  |
### aten.minimum.default
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ? | Unknown  |
|  1 | Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ? | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 512]> mat2 = ?       | Unknown  |
|  1 | Tensor<[10, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ?   | Unknown  |
|  2 | Tensor<[10, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ?      | Unknown  |
|  3 | Tensor<[10, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?      | Unknown  |
|  4 | Tensor<[15, 512]> self = ?,<br>Tensor<[512, 384]> mat2 = ?      | Unknown  |
|  5 | Tensor<[1500, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?    | Unknown  |
|  6 | Tensor<[16384, 32]> self = ?,<br>Tensor<[32, 256]> mat2 = ?     | Unknown  |
|  7 | Tensor<[19, 1024]> self = ?,<br>Tensor<[1024, 256008]> mat2 = ? | Unknown  |
|  8 | Tensor<[197, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ?  | Unknown  |
|  9 | Tensor<[197, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?     | Unknown  |
| 10 | Tensor<[2048, 768]> self = ?,<br>Tensor<[768, 262]> mat2 = ?    | Unknown  |
| 11 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 3]> mat2 = ?       | Unknown  |
| 12 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 4]> mat2 = ?       | Unknown  |
| 13 | Tensor<[32, 1536]> self = ?,<br>Tensor<[1536, 250880]> mat2 = ? | Unknown  |
| 14 | Tensor<[32, 4096]> self = ?,<br>Tensor<[4096, 4096]> mat2 = ?   | Unknown  |
| 15 | Tensor<[45, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?      | Unknown  |
| 16 | Tensor<[5, 1024]> self = ?,<br>Tensor<[1024, 3072]> mat2 = ?    | Unknown  |
| 17 | Tensor<[7, 4544]> self = ?,<br>Tensor<[4544, 4672]> mat2 = ?    | Unknown  |
| 18 | Tensor<[7, 768]> self = ?,<br>Tensor<[768, 2]> mat2 = ?         | Unknown  |
| 19 | Tensor<[768, 196]> self = ?,<br>Tensor<[196, 384]> mat2 = ?     | Unknown  |
| 20 | Tensor<[784, 384]> self = ?,<br>Tensor<[384, 192]> mat2 = ?     | Unknown  |
| 21 | Tensor<[784, 512]> self = ?,<br>Tensor<[512, 256]> mat2 = ?     | Unknown  |
| 22 | Tensor<[920, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ?     | Unknown  |
### aten.mul.Scalar
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 32, 128]> self = ?,<br>number other = 0.29730177875068026 | Unknown  |
|  1 | Tensor<[1, 71, 7, 64]> self = ?,<br>number other = 0.3535533905932738    | Unknown  |
### aten.mul.Tensor
|     | ATen Input Variations                                                          | Status   |
|----:|:-------------------------------------------------------------------------------|:---------|
|   0 | Tensor<[1, 1, 1, 10]> self = ?,<br>Tensor other = -3.4028234663852886e+38      | Unknown  |
|   1 | Tensor<[1, 1, 1, 12]> self = ?,<br>Tensor other = -3.4028234663852886e+38      | Unknown  |
|   2 | Tensor<[1, 1, 1, 14]> self = ?,<br>Tensor other = -3.4028234663852886e+38      | Unknown  |
|   3 | Tensor<[1, 1, 1, 15]> self = ?,<br>Tensor other = -3.4028234663852886e+38      | Unknown  |
|   4 | Tensor<[1, 1, 1, 201]> self = ?,<br>Tensor other = -3.4028234663852886e+38     | Unknown  |
|   5 | Tensor<[1, 1, 1, 2048]> self = ?,<br>Tensor other = -3.4028234663852886e+38    | Unknown  |
|   6 | Tensor<[1, 1, 1, 256]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Unknown  |
|   7 | Tensor<[1, 1, 1, 25]> self = ?,<br>Tensor other = -3.4028234663852886e+38      | Unknown  |
|   8 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.9761904761904763           | Unknown  |
|   9 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?             | Unknown  |
|  10 | Tensor<[1, 1, 1, 5]> self = ?,<br>Tensor other = -3.4028234663852886e+38       | Unknown  |
|  11 | Tensor<[1, 1, 1, 7]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  |
|  12 | Tensor<[1, 1, 1, 8]> self = ?,<br>Tensor other = -3.4028234663852886e+38       | Unknown  |
|  13 | Tensor<[1, 1, 1, 9]> self = ?,<br>Tensor other = -3.4028234663852886e+38       | Unknown  |
|  14 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.03125                       | Unknown  |
|  15 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.044715                      | Unknown  |
|  16 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  |
|  17 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Tensor<[1, 1, 2048, 1]> other = ?      | Unknown  |
|  18 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.458                     | Unknown  |
|  19 | Tensor<[1, 1, 256]> self = ?,<br>Tensor other = 1                              | Unknown  |
|  20 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.044715                      | Unknown  |
|  21 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.5625                       | Unknown  |
|  22 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  |
|  23 | Tensor<[1, 1, 480, 640]> self = ?,<br>Tensor other = 10                        | Unknown  |
|  24 | Tensor<[1, 1, 512]> self = ?,<br>Tensor other = 0.04419417382415922            | Unknown  |
|  25 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.03608439182435161            | Unknown  |
|  26 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                | Unknown  |
|  27 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                 | Unknown  |
|  28 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                 | Unknown  |
|  29 | Tensor<[1, 10]> self = ?,<br>Tensor<[1, 10]> other = ?                         | Unknown  |
|  30 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.5                          | Unknown  |
|  31 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?             | Unknown  |
|  32 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.5                          | Unknown  |
|  33 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?             | Unknown  |
|  34 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.5                          | Unknown  |
|  35 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 1]> other = ?                 | Unknown  |
|  36 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 56, 56]> other = ?           | Unknown  |
|  37 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor other = 32.0                         | Unknown  |
|  38 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                                   | Unknown  |
|  39 | Tensor<[1, 1]> self = ?,<br>Tensor other = 50258                               | Unknown  |
|  40 | Tensor<[1, 224, 1, 1]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?         | Unknown  |
|  41 | Tensor<[1, 23, 40]> self = ?,<br>Tensor other = 6.283185307179586              | Unknown  |
|  42 | Tensor<[1, 232, 1, 1]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?         | Unknown  |
|  43 | Tensor<[1, 24, 768]> self = ?,<br>Tensor other = 0.125                         | Unknown  |
|  44 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128, 1]> other = ?             | Unknown  |
|  45 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Unknown  |
|  46 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300, 1]> other = ?               | Unknown  |
|  47 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320, 1]> other = ?               | Unknown  |
|  48 | Tensor<[1, 3, 64, 64]> self = ?,<br>Tensor other = 16                          | Unknown  |
|  49 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[800, 1]> other = ?              | Unknown  |
|  50 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.5                          | Unknown  |
|  51 | Tensor<[1, 32]> self = ?,<br>Tensor<[1, 32]> other = ?                         | Unknown  |
|  52 | Tensor<[1, 4, 64, 64]> self = ?,<br>Tensor other = 16                          | Unknown  |
|  53 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.5                          | Unknown  |
|  54 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?             | Unknown  |
|  55 | Tensor<[1, 48, 1, 1]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?           | Unknown  |
|  56 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 1, 32]> other = ?            | Unknown  |
|  57 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  |
|  58 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor other = 1.702                        | Unknown  |
|  59 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ?             | Unknown  |
|  60 | Tensor<[1, 50, 768]> self = ?,<br>Tensor other = 0.125                         | Unknown  |
|  61 | Tensor<[1, 528, 1, 1]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?         | Unknown  |
|  62 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?             | Unknown  |
|  63 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?           | Unknown  |
|  64 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[30, 1]> other = ?                 | Unknown  |
|  65 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.5                           | Unknown  |
|  66 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?               | Unknown  |
|  67 | Tensor<[1, 71, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?            | Unknown  |
|  68 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?           | Unknown  |
|  69 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?           | Unknown  |
|  70 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 1, 1]> other = ?           | Unknown  |
|  71 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?         | Unknown  |
|  72 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.044715                       | Unknown  |
|  73 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.5                          | Unknown  |
|  74 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?             | Unknown  |
|  75 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.5                           | Unknown  |
|  76 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?               | Unknown  |
|  77 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  |
|  78 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?               | Unknown  |
|  79 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.5                           | Unknown  |
|  80 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?               | Unknown  |
|  81 | Tensor<[10, 10]> self = ?,<br>Tensor other = 16                                | Unknown  |
|  82 | Tensor<[1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?                   | Unknown  |
|  83 | Tensor<[1066]> self = ?,<br>Tensor other = 0.600375234521576                   | Unknown  |
|  84 | Tensor<[128]> self = ?,<br>Tensor other = 1.0                                  | Unknown  |
|  85 | Tensor<[128]> self = ?,<br>Tensor other = 2                                    | Unknown  |
|  86 | Tensor<[12]> self = ?,<br>Tensor other = 32.0                                  | Unknown  |
|  87 | Tensor<[15, 15]> self = ?,<br>Tensor other = 16                                | Unknown  |
|  88 | Tensor<[1]> self = ?,<br>Tensor<[1]> other = ?                                 | Unknown  |
|  89 | Tensor<[23]> self = ?,<br>Tensor other = 31.304347826086957                    | Unknown  |
|  90 | Tensor<[28]> self = ?,<br>Tensor other = 0.25                                  | Unknown  |
|  91 | Tensor<[300]> self = ?,<br>Tensor other = 1.6                                  | Unknown  |
|  92 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                                   | Unknown  |
|  93 | Tensor<[320]> self = ?,<br>Tensor other = 1.0                                  | Unknown  |
|  94 | Tensor<[320]> self = ?,<br>Tensor other = 1.5                                  | Unknown  |
|  95 | Tensor<[3234, 2]> self = ?,<br>Tensor other = 0.5                              | Unknown  |
|  96 | Tensor<[40]> self = ?,<br>Tensor other = 32.0                                  | Unknown  |
|  97 | Tensor<[50]> self = ?,<br>Tensor other = 0.5                                   | Unknown  |
|  98 | Tensor<[56]> self = ?,<br>Tensor other = 0.5                                   | Unknown  |
|  99 | Tensor<[64, 3, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Unknown  |
| 100 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[3, 1, 1]> other = ?               | Unknown  |
| 101 | Tensor<[64, 4, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Unknown  |
| 102 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[4, 1, 1]> other = ?               | Unknown  |
| 103 | Tensor<[768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?                     | Unknown  |
| 104 | Tensor<[7]> self = ?,<br>Tensor other = 0.42857142857142855                    | Unknown  |
| 105 | Tensor<[800]> self = ?,<br>Tensor other = 0.6                                  | Unknown  |
| 106 | Tensor<[8732, 2]> self = ?,<br>Tensor other = 0.5                              | Unknown  |
| 107 | Tensor<[]> self = ?,<br>Tensor<[1, 24, 768]> other = ?                         | Unknown  |
### aten.native_dropout.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128]> input = ?,<br>float p = 0.5,<br>Optional[bool] train = True         | Unknown  |
|  1 | Tensor<[1, 64, 12, 12]> input = ?,<br>float p = 0.25,<br>Optional[bool] train = True | Unknown  |
|  2 | Tensor<[8, 920, 920]> input = ?,<br>float p = 0.1,<br>Optional[bool] train = True    | Unknown  |
### aten.native_group_norm.default
|    | ATen Input Variations                                                                                                                                                                                       | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 100, 136]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>int N = 1,<br>int C = 256,<br>int HxW = 13600,<br>int group = 32,<br>float eps = 1e-05 | Unknown  |
|  1 | Tensor<[1, 256, 13, 17]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>int N = 1,<br>int C = 256,<br>int HxW = 221,<br>int group = 32,<br>float eps = 1e-05     | Unknown  |
|  2 | Tensor<[1, 256, 25, 34]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>int N = 1,<br>int C = 256,<br>int HxW = 850,<br>int group = 32,<br>float eps = 1e-05     | Unknown  |
|  3 | Tensor<[1, 256, 50, 68]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>int N = 1,<br>int C = 256,<br>int HxW = 3400,<br>int group = 32,<br>float eps = 1e-05    | Unknown  |
|  4 | Tensor<[1, 256, 7, 9]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>int N = 1,<br>int C = 256,<br>int HxW = 63,<br>int group = 32,<br>float eps = 1e-05        | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                           | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05         | Unknown  |
|  1 | Tensor<[1, 1024, 160]> input = ?,<br>List[int] normalized_shape = [160],<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>float eps = 1e-05       | Unknown  |
|  2 | Tensor<[1, 12, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-12         | Unknown  |
|  3 | Tensor<[1, 12, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12         | Unknown  |
|  4 | Tensor<[1, 1200, 320]> input = ?,<br>List[int] normalized_shape = [320],<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>float eps = 1e-05       | Unknown  |
|  5 | Tensor<[1, 1370, 1280]> input = ?,<br>List[int] normalized_shape = [1280],<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>float eps = 1e-06   | Unknown  |
|  6 | Tensor<[1, 14, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-12         | Unknown  |
|  7 | Tensor<[1, 14, 14, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05 | Unknown  |
|  8 | Tensor<[1, 14, 14, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05     | Unknown  |
|  9 | Tensor<[1, 14, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12         | Unknown  |
| 10 | Tensor<[1, 1445, 192]> input = ?,<br>List[int] normalized_shape = [192],<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>float eps = 1e-12       | Unknown  |
| 11 | Tensor<[1, 1500, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05       | Unknown  |
| 12 | Tensor<[1, 1536]> input = ?,<br>List[int] normalized_shape = [1536],<br>Optional[Tensor]<[1536]> weight = ?,<br>Optional[Tensor]<[1536]> bias = ?,<br>float eps = 1e-05         | Unknown  |
| 13 | Tensor<[1, 16, 16, 384]> input = ?,<br>List[int] normalized_shape = [384],<br>Optional[Tensor]<[384]> weight = ?,<br>Optional[Tensor]<[384]> bias = ?,<br>float eps = 1e-05     | Unknown  |
| 14 | Tensor<[1, 16, 16, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05     | Unknown  |
| 15 | Tensor<[1, 16, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12         | Unknown  |
| 16 | Tensor<[1, 16384, 32]> input = ?,<br>List[int] normalized_shape = [32],<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>float eps = 1e-05          | Unknown  |
| 17 | Tensor<[1, 19, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05     | Unknown  |
| 18 | Tensor<[1, 19200, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float eps = 1e-05          | Unknown  |
| 19 | Tensor<[1, 196, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-06        | Unknown  |
| 20 | Tensor<[1, 197, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-06    | Unknown  |
| 21 | Tensor<[1, 197, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-12    | Unknown  |
| 22 | Tensor<[1, 197, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-06        | Unknown  |
| 23 | Tensor<[1, 197, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12        | Unknown  |
| 24 | Tensor<[1, 2048, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05       | Unknown  |
| 25 | Tensor<[1, 24, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05         | Unknown  |
| 26 | Tensor<[1, 25, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12         | Unknown  |
| 27 | Tensor<[1, 256, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-12    | Unknown  |
| 28 | Tensor<[1, 256, 1280]> input = ?,<br>List[int] normalized_shape = [1280],<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>float eps = 1e-05    | Unknown  |
| 29 | Tensor<[1, 256, 256]> input = ?,<br>List[int] normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float eps = 1e-05        | Unknown  |
| 30 | Tensor<[1, 256, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05        | Unknown  |
| 31 | Tensor<[1, 28, 28, 192]> input = ?,<br>List[int] normalized_shape = [192],<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>float eps = 1e-05     | Unknown  |
| 32 | Tensor<[1, 28, 28, 256]> input = ?,<br>List[int] normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float eps = 1e-05     | Unknown  |
| 33 | Tensor<[1, 28, 28, 384]> input = ?,<br>List[int] normalized_shape = [384],<br>Optional[Tensor]<[384]> weight = ?,<br>Optional[Tensor]<[384]> bias = ?,<br>float eps = 1e-05     | Unknown  |
| 34 | Tensor<[1, 28, 28, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05     | Unknown  |
| 35 | Tensor<[1, 300, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05        | Unknown  |
| 36 | Tensor<[1, 32, 1536]> input = ?,<br>List[int] normalized_shape = [1536],<br>Optional[Tensor]<[1536]> weight = ?,<br>Optional[Tensor]<[1536]> bias = ?,<br>float eps = 1e-05     | Unknown  |
| 37 | Tensor<[1, 32, 32, 192]> input = ?,<br>List[int] normalized_shape = [192],<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>float eps = 1e-05     | Unknown  |
| 38 | Tensor<[1, 32, 32, 256]> input = ?,<br>List[int] normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float eps = 1e-05     | Unknown  |
| 39 | Tensor<[1, 4096, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float eps = 1e-05           | Unknown  |
| 40 | Tensor<[1, 45, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05         | Unknown  |
| 41 | Tensor<[1, 4800, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-05       | Unknown  |
| 42 | Tensor<[1, 5, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05      | Unknown  |
| 43 | Tensor<[1, 50, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-06     | Unknown  |
| 44 | Tensor<[1, 50, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05         | Unknown  |
| 45 | Tensor<[1, 50, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-06         | Unknown  |
| 46 | Tensor<[1, 56, 56, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-05     | Unknown  |
| 47 | Tensor<[1, 56, 56, 96]> input = ?,<br>List[int] normalized_shape = [96],<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>float eps = 1e-05         | Unknown  |
| 48 | Tensor<[1, 64, 64, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-05     | Unknown  |
| 49 | Tensor<[1, 64, 64, 96]> input = ?,<br>List[int] normalized_shape = [96],<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>float eps = 1e-05         | Unknown  |
| 50 | Tensor<[1, 7, 4544]> input = ?,<br>List[int] normalized_shape = [4544],<br>Optional[Tensor]<[4544]> weight = ?,<br>Optional[Tensor]<[4544]> bias = ?,<br>float eps = 1e-05      | Unknown  |
| 51 | Tensor<[1, 7, 7, 1536]> input = ?,<br>List[int] normalized_shape = [1536],<br>Optional[Tensor]<[1536]> weight = ?,<br>Optional[Tensor]<[1536]> bias = ?,<br>float eps = 1e-05   | Unknown  |
| 52 | Tensor<[1, 7, 7, 2048]> input = ?,<br>List[int] normalized_shape = [2048],<br>Optional[Tensor]<[2048]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>float eps = 1e-05   | Unknown  |
| 53 | Tensor<[1, 7, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05          | Unknown  |
| 54 | Tensor<[1, 8, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12          | Unknown  |
| 55 | Tensor<[1, 8, 8, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05   | Unknown  |
| 56 | Tensor<[1, 8, 8, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05       | Unknown  |
| 57 | Tensor<[1, 9, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-12      | Unknown  |
| 58 | Tensor<[1, 9, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-12          | Unknown  |
| 59 | Tensor<[1, 9, 2048]> input = ?,<br>List[int] normalized_shape = [2048],<br>Optional[Tensor]<[2048]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>float eps = 1e-12      | Unknown  |
| 60 | Tensor<[1, 9, 4096]> input = ?,<br>List[int] normalized_shape = [4096],<br>Optional[Tensor]<[4096]> weight = ?,<br>Optional[Tensor]<[4096]> bias = ?,<br>float eps = 1e-12      | Unknown  |
| 61 | Tensor<[1, 9, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12          | Unknown  |
| 62 | Tensor<[2, 7, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05          | Unknown  |
| 63 | Tensor<[920, 1, 256]> input = ?,<br>List[int] normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float eps = 1e-05        | Unknown  |
### aten.ne.Scalar
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[1, 10]> self = ?,<br>number other = 1      | Unknown  |
|  1 | Tensor<[1, 32]> self = ?,<br>number other = 1      | Unknown  |
|  2 | Tensor<[64, 49, 49]> self = ?,<br>number other = 0 | Unknown  |
|  3 | Tensor<[64, 64, 64]> self = ?,<br>number other = 0 | Unknown  |
### aten.neg.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 1]> self = ?          | Unknown  |
|  1 | Tensor<[1, 32, 32, 64]> self = ? | Unknown  |
|  2 | Tensor<[1, 5, 16, 16]> self = ?  | Unknown  |
|  3 | Tensor<[1, 71, 7, 32]> self = ?  | Unknown  |
### aten.new_full.default
|    | ATen Input Variations                                                                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 300, 300]> self = ?,<br>List[int] size = [1, 3, 300, 300],<br>number fill_value = 0,<br>Optional[bool] pin_memory = False   | Unknown  |
|  1 | Tensor<[3, 320, 320]> self = ?,<br>List[int] size = [1, 3, 320, 320],<br>number fill_value = 0,<br>Optional[bool] pin_memory = False   | Unknown  |
|  2 | Tensor<[3, 800, 1066]> self = ?,<br>List[int] size = [1, 3, 800, 1088],<br>number fill_value = 0,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.new_ones.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 45]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False | Unknown  |
|  1 | Tensor<[1, 5]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False  | Unknown  |
### aten.new_zeros.default
|    | ATen Input Variations                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 19]> self = ?,<br>List[int] size = [1, 19],<br>Optional[bool] pin_memory = False        | Unknown  |
|  1 | Tensor<[16, 49, 192]> self = ?,<br>List[int] size = [28, 28],<br>Optional[bool] pin_memory = False | Unknown  |
|  2 | Tensor<[16, 49, 256]> self = ?,<br>List[int] size = [28, 28],<br>Optional[bool] pin_memory = False | Unknown  |
|  3 | Tensor<[16, 64, 192]> self = ?,<br>List[int] size = [32, 32],<br>Optional[bool] pin_memory = False | Unknown  |
|  4 | Tensor<[16, 64, 256]> self = ?,<br>List[int] size = [32, 32],<br>Optional[bool] pin_memory = False | Unknown  |
|  5 | Tensor<[4, 49, 384]> self = ?,<br>List[int] size = [14, 14],<br>Optional[bool] pin_memory = False  | Unknown  |
|  6 | Tensor<[4, 49, 512]> self = ?,<br>List[int] size = [14, 14],<br>Optional[bool] pin_memory = False  | Unknown  |
|  7 | Tensor<[4, 64, 384]> self = ?,<br>List[int] size = [16, 16],<br>Optional[bool] pin_memory = False  | Unknown  |
|  8 | Tensor<[4, 64, 512]> self = ?,<br>List[int] size = [16, 16],<br>Optional[bool] pin_memory = False  | Unknown  |
|  9 | Tensor<[64, 49, 128]> self = ?,<br>List[int] size = [56, 56],<br>Optional[bool] pin_memory = False | Unknown  |
| 10 | Tensor<[64, 49, 96]> self = ?,<br>List[int] size = [56, 56],<br>Optional[bool] pin_memory = False  | Unknown  |
| 11 | Tensor<[64, 64, 128]> self = ?,<br>List[int] size = [64, 64],<br>Optional[bool] pin_memory = False | Unknown  |
| 12 | Tensor<[64, 64, 96]> self = ?,<br>List[int] size = [64, 64],<br>Optional[bool] pin_memory = False  | Unknown  |
### aten.nll_loss_forward.default
|    | ATen Input Variations                                                                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[19, 256008]> self = ?,<br>Tensor<[19]> target = ?,<br>Optional[Tensor] weight = None,<br>int reduction = 1,<br>int ignore_index = -100 | Unknown  |
### aten.ones.default
|    | ATen Input Variations                                                                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int] size = [1, 1],<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                              | Unknown  |
|  1 | List[int] size = [1, 1],<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  |
|  2 | List[int] size = [1, 720, 1280],<br>Optional[int] dtype = torch.bool,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
|  3 | List[int] size = [7, 7],<br>Optional[int] dtype = torch.bool,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                                           | Status   |
|---:|:--------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  |
|  1 | Tensor<[1, 1024, 196]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Unknown  |
|  2 | Tensor<[1, 1024, 49]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Unknown  |
|  3 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  |
|  4 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] dims = [2, 0, 1, 3]             | Unknown  |
|  5 | Tensor<[1, 12, 50, 64]> self = ?,<br>List[int] dims = [2, 0, 1, 3]              | Unknown  |
|  6 | Tensor<[1, 12, 64, 8]> self = ?,<br>List[int] dims = [0, 1, 3, 2]               | Unknown  |
|  7 | Tensor<[1, 120, 160, 64]> self = ?,<br>List[int] dims = [0, 3, 1, 2]            | Unknown  |
|  8 | Tensor<[1, 128, 128, 32]> self = ?,<br>List[int] dims = [0, 3, 1, 2]            | Unknown  |
|  9 | Tensor<[1, 128, 56, 56]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Unknown  |
| 10 | Tensor<[1, 128, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Unknown  |
| 11 | Tensor<[1, 1280, 1369]> self = ?,<br>List[int] dims = [0, 2, 1]                 | Unknown  |
| 12 | Tensor<[1, 14, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  |
| 13 | Tensor<[1, 1445, 3, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Unknown  |
| 14 | Tensor<[1, 16, 1370, 80]> self = ?,<br>List[int] dims = [2, 0, 1, 3]            | Unknown  |
| 15 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] dims = [2, 0, 1, 3]             | Unknown  |
| 16 | Tensor<[1, 16, 32, 96]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  |
| 17 | Tensor<[1, 16, 50, 64]> self = ?,<br>List[int] dims = [2, 0, 1, 3]              | Unknown  |
| 18 | Tensor<[1, 16384, 1, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]            | Unknown  |
| 19 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Unknown  |
| 20 | Tensor<[1, 19200, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]            | Unknown  |
| 21 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Unknown  |
| 22 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Unknown  |
| 23 | Tensor<[1, 197, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Unknown  |
| 24 | Tensor<[1, 201, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Unknown  |
| 25 | Tensor<[1, 23, 40, 256]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Unknown  |
| 26 | Tensor<[1, 25, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  |
| 27 | Tensor<[1, 256, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Unknown  |
| 28 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  |
| 29 | Tensor<[1, 256, 920]> self = ?,<br>List[int] dims = [2, 0, 1]                   | Unknown  |
| 30 | Tensor<[1, 3, 16, 16, 16, 16]> self = ?,<br>List[int] dims = [0, 2, 4, 3, 5, 1] | Unknown  |
| 31 | Tensor<[1, 32, 16, 96]> self = ?,<br>List[int] dims = [0, 2, 3, 1]              | Unknown  |
| 32 | Tensor<[1, 4, 4, 38, 38]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]         | Unknown  |
| 33 | Tensor<[1, 45, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  |
| 34 | Tensor<[1, 5, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  |
| 35 | Tensor<[1, 512]> self = ?,<br>List[int] dims = [0, 1]                           | Unknown  |
| 36 | Tensor<[1, 6, 4, 20, 20]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]         | Unknown  |
| 37 | Tensor<[1, 7, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  |
| 38 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int] dims = [0, 3, 1, 2]              | Unknown  |
| 39 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int] dims = [0, 3, 1, 2]               | Unknown  |
| 40 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  |
| 41 | Tensor<[1, 768, 1500]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Unknown  |
| 42 | Tensor<[1, 768, 196]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Unknown  |
| 43 | Tensor<[1, 768, 49]> self = ?,<br>List[int] dims = [0, 2, 1]                    | Unknown  |
| 44 | Tensor<[1, 8, 7, 8, 7, 128]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Unknown  |
| 45 | Tensor<[1, 8, 7, 8, 7, 96]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]    | Unknown  |
| 46 | Tensor<[1, 8, 768]> self = ?,<br>List[int] dims = [0, 2, 1]                     | Unknown  |
| 47 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int] dims = [0, 3, 1, 2]              | Unknown  |
| 48 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] dims = [0, 3, 1, 2]               | Unknown  |
| 49 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Unknown  |
| 50 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]    | Unknown  |
| 51 | Tensor<[1, 9, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  |
| 52 | Tensor<[1, 9, 16, 128]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  |
| 53 | Tensor<[1, 9, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  |
| 54 | Tensor<[1, 9, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  |
| 55 | Tensor<[1, 9, 91, 100, 136]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]      | Unknown  |
| 56 | Tensor<[1, 96, 56, 56]> self = ?,<br>List[int] dims = [0, 2, 3, 1]              | Unknown  |
| 57 | Tensor<[1, 96, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]              | Unknown  |
| 58 | Tensor<[10, 10, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Unknown  |
| 59 | Tensor<[10, 10, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Unknown  |
| 60 | Tensor<[10, 10, 8]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Unknown  |
| 61 | Tensor<[15, 15, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Unknown  |
| 62 | Tensor<[197, 197, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                  | Unknown  |
| 63 | Tensor<[197, 197, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                  | Unknown  |
| 64 | Tensor<[4672, 4544]> self = ?,<br>List[int] dims = [1, 0]                       | Unknown  |
| 65 | Tensor<[49, 49, 3]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Unknown  |
| 66 | Tensor<[49, 49, 4]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Unknown  |
| 67 | Tensor<[64, 49, 3, 3, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | Unknown  |
| 68 | Tensor<[64, 49, 3, 4, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | Unknown  |
| 69 | Tensor<[64, 64, 3, 3, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | Unknown  |
| 70 | Tensor<[64, 64, 3, 4, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | Unknown  |
| 71 | Tensor<[64, 64, 3]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Unknown  |
| 72 | Tensor<[64, 64, 4]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Unknown  |
| 73 | Tensor<[8, 7, 8, 7]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                 | Unknown  |
| 74 | Tensor<[8, 8, 8, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                 | Unknown  |
### aten.pow.Scalar
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | number self = 10000,<br>Tensor<[128]> exponent = ? | Unknown  |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 1024]> self = ?,<br>number exponent = 2   | Unknown  |
|  1 | Tensor<[1, 10, 512]> self = ?,<br>number exponent = 2    | Unknown  |
|  2 | Tensor<[1, 10, 768]> self = ?,<br>number exponent = 2    | Unknown  |
|  3 | Tensor<[1, 12, 3072]> self = ?,<br>number exponent = 3.0 | Unknown  |
|  4 | Tensor<[1, 14, 3072]> self = ?,<br>number exponent = 3.0 | Unknown  |
|  5 | Tensor<[1, 15, 1024]> self = ?,<br>number exponent = 3.0 | Unknown  |
|  6 | Tensor<[1, 15, 512]> self = ?,<br>number exponent = 2    | Unknown  |
|  7 | Tensor<[1, 32, 4096]> self = ?,<br>number exponent = 2   | Unknown  |
|  8 | Tensor<[1, 45, 3072]> self = ?,<br>number exponent = 3.0 | Unknown  |
|  9 | Tensor<[1, 5, 4096]> self = ?,<br>number exponent = 3.0  | Unknown  |
| 10 | Tensor<[1, 7, 3072]> self = ?,<br>number exponent = 3.0  | Unknown  |
| 11 | Tensor<[1, 9, 16384]> self = ?,<br>number exponent = 3.0 | Unknown  |
| 12 | Tensor<[1, 9, 3072]> self = ?,<br>number exponent = 3.0  | Unknown  |
| 13 | Tensor<[1, 9, 4096]> self = ?,<br>number exponent = 3.0  | Unknown  |
| 14 | Tensor<[1, 9, 8192]> self = ?,<br>number exponent = 3.0  | Unknown  |
### aten.pow.Tensor_Tensor
|    | ATen Input Variations                             | Status   |
|---:|:--------------------------------------------------|:---------|
|  0 | Tensor<[]> self = ?,<br>Tensor<[16]> exponent = ? | Unknown  |
### aten.relu.default
|    | ATen Input Variations               | Status   |
|---:|:------------------------------------|:---------|
|  0 | Tensor<[1, 1, 256]> self = ?        | Unknown  |
|  1 | Tensor<[1, 10, 2048]> self = ?      | Unknown  |
|  2 | Tensor<[1, 10, 3072]> self = ?      | Unknown  |
|  3 | Tensor<[1, 10, 4096]> self = ?      | Unknown  |
|  4 | Tensor<[1, 100, 192]> self = ?      | Unknown  |
|  5 | Tensor<[1, 15, 15, 512]> self = ?   | Unknown  |
|  6 | Tensor<[1, 16, 112, 112]> self = ?  | Unknown  |
|  7 | Tensor<[1, 16, 160, 160]> self = ?  | Unknown  |
|  8 | Tensor<[1, 16, 224, 224]> self = ?  | Unknown  |
|  9 | Tensor<[1, 16, 56, 56]> self = ?    | Unknown  |
| 10 | Tensor<[1, 256, 128, 128]> self = ? | Unknown  |
| 11 | Tensor<[1, 32, 112, 112]> self = ?  | Unknown  |
| 12 | Tensor<[1, 32, 149, 149]> self = ?  | Unknown  |
| 13 | Tensor<[1, 32, 150, 150]> self = ?  | Unknown  |
| 14 | Tensor<[1, 32, 192, 192]> self = ?  | Unknown  |
| 15 | Tensor<[1, 32, 256, 256]> self = ?  | Unknown  |
| 16 | Tensor<[1, 32, 26, 26]> self = ?    | Unknown  |
| 17 | Tensor<[1, 64, 112, 112]> self = ?  | Unknown  |
| 18 | Tensor<[1, 64, 224, 224]> self = ?  | Unknown  |
| 19 | Tensor<[1, 64, 30, 40]> self = ?    | Unknown  |
| 20 | Tensor<[1, 64, 300, 300]> self = ?  | Unknown  |
| 21 | Tensor<[1, 64, 360, 640]> self = ?  | Unknown  |
| 22 | Tensor<[1, 64, 400, 544]> self = ?  | Unknown  |
| 23 | Tensor<[1, 96, 112, 112]> self = ?  | Unknown  |
### aten.remainder.Scalar
|    | ATen Input Variations                     | Status   |
|---:|:------------------------------------------|:---------|
|  0 | Tensor<[1]> self = ?,<br>number other = 7 | Unknown  |
### aten.repeat.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>List[int] repeats = [1, 1, 1]             | Unknown  |
|  1 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>List[int] repeats = [1, 1, 1, 1] | Unknown  |
|  2 | Tensor<[1, 1, 256]> self = ?,<br>List[int] repeats = [1, 1, 1]           | Unknown  |
|  3 | Tensor<[100, 1, 256]> self = ?,<br>List[int] repeats = [1, 1, 1]         | Unknown  |
|  4 | Tensor<[4, 2]> self = ?,<br>List[int] repeats = [1444, 1]                | Unknown  |
|  5 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [361, 1]                 | Unknown  |
|  6 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [400, 1]                 | Unknown  |
### aten.roll.default
|    | ATen Input Variations                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int] shifts = [3, 3],<br>List[int] dims = [1, 2]   | Unknown  |
|  1 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int] shifts = [3, 3],<br>List[int] dims = [1, 2]   | Unknown  |
|  2 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] shifts = [4, 4],<br>List[int] dims = [1, 2]   | Unknown  |
|  3 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int] shifts = [4, 4],<br>List[int] dims = [1, 2]   | Unknown  |
|  4 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int] shifts = [-3, -3],<br>List[int] dims = [1, 2] | Unknown  |
|  5 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int] shifts = [-3, -3],<br>List[int] dims = [1, 2]  | Unknown  |
|  6 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int] shifts = [-4, -4],<br>List[int] dims = [1, 2] | Unknown  |
|  7 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] shifts = [-4, -4],<br>List[int] dims = [1, 2]  | Unknown  |
### aten.rsqrt.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 10, 1]> self = ?    | Unknown  |
|  1 | Tensor<[1, 15, 1]> self = ?    | Unknown  |
|  2 | Tensor<[1, 32, 1]> self = ?    | Unknown  |
|  3 | Tensor<[1, 64, 1, 1]> self = ? | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                                   | Status   |
|---:|:--------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>number other = 1.0   | Unknown  |
|  1 | Tensor<[1, 1, 1, 12]> self = ?,<br>number other = 1.0   | Unknown  |
|  2 | Tensor<[1, 1, 1, 14]> self = ?,<br>number other = 1.0   | Unknown  |
|  3 | Tensor<[1, 1, 1, 15]> self = ?,<br>number other = 1.0   | Unknown  |
|  4 | Tensor<[1, 1, 1, 201]> self = ?,<br>number other = 1.0  | Unknown  |
|  5 | Tensor<[1, 1, 1, 2048]> self = ?,<br>number other = 1.0 | Unknown  |
|  6 | Tensor<[1, 1, 1, 256]> self = ?,<br>number other = 1.0  | Unknown  |
|  7 | Tensor<[1, 1, 1, 25]> self = ?,<br>number other = 1.0   | Unknown  |
|  8 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 1.0   | Unknown  |
|  9 | Tensor<[1, 1, 1, 5]> self = ?,<br>number other = 1.0    | Unknown  |
| 10 | Tensor<[1, 1, 1, 7]> self = ?,<br>number other = 1.0    | Unknown  |
| 11 | Tensor<[1, 1, 1, 8]> self = ?,<br>number other = 1.0    | Unknown  |
| 12 | Tensor<[1, 1, 1, 9]> self = ?,<br>number other = 1.0    | Unknown  |
| 13 | Tensor<[1, 1, 19, 19]> self = ?,<br>number other = 1.0  | Unknown  |
| 14 | Tensor<[1, 1, 24, 24]> self = ?,<br>number other = 1.0  | Unknown  |
| 15 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 2.0   | Unknown  |
| 16 | Tensor<[1, 1, 32, 32]> self = ?,<br>number other = 1.0  | Unknown  |
| 17 | Tensor<[1, 1, 45, 45]> self = ?,<br>number other = 1.0  | Unknown  |
| 18 | Tensor<[1, 192]> self = ?,<br>number other = 1          | Unknown  |
| 19 | Tensor<[128, 1]> self = ?,<br>number other = 1.0        | Unknown  |
| 20 | Tensor<[2, 1, 7, 7]> self = ?,<br>number other = 1.0    | Unknown  |
| 21 | Tensor<[30, 1]> self = ?,<br>number other = 1.0         | Unknown  |
| 22 | Tensor<[300, 1]> self = ?,<br>number other = 1.0        | Unknown  |
| 23 | Tensor<[320, 1]> self = ?,<br>number other = 1.0        | Unknown  |
| 24 | Tensor<[800, 1]> self = ?,<br>number other = 1.0        | Unknown  |
### aten.scalar_tensor.default
|    | ATen Input Variations                                                                                                           | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number s = 0,<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  |
### aten.select.int
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>int index = 2             | Unknown  |
|  1 | Tensor<[1, 1, 12, 16]> self = ?,<br>int dim = 1,<br>int index = 0     | Unknown  |
|  2 | Tensor<[1, 1, 23, 40]> self = ?,<br>int dim = 0,<br>int index = 0     | Unknown  |
|  3 | Tensor<[1, 1, 256]> self = ?,<br>int dim = 0,<br>int index = 0        | Unknown  |
|  4 | Tensor<[1, 1, 51865]> self = ?,<br>int dim = 1,<br>int index = -1     | Unknown  |
|  5 | Tensor<[1, 1370, 1280]> self = ?,<br>int dim = 1,<br>int index = 0    | Unknown  |
|  6 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 1,<br>int index = 0     | Unknown  |
|  7 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>int index = 0      | Unknown  |
|  8 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 1,<br>int index = 0     | Unknown  |
|  9 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 1,<br>int index = 1     | Unknown  |
| 10 | Tensor<[1, 25, 768]> self = ?,<br>int dim = 1,<br>int index = 0       | Unknown  |
| 11 | Tensor<[1, 3, 224, 224]> self = ?,<br>int dim = 1,<br>int index = 0   | Unknown  |
| 12 | Tensor<[1, 3, 320, 320]> self = ?,<br>int dim = 0,<br>int index = 0   | Unknown  |
| 13 | Tensor<[1, 3, 480, 640]> self = ?,<br>int dim = 0,<br>int index = 0   | Unknown  |
| 14 | Tensor<[1, 32, 16, 3, 96]> self = ?,<br>int dim = 3,<br>int index = 0 | Unknown  |
| 15 | Tensor<[1, 4251, 192]> self = ?,<br>int dim = 1,<br>int index = 0     | Unknown  |
| 16 | Tensor<[1, 45]> self = ?,<br>int dim = 1,<br>int index = -1           | Unknown  |
| 17 | Tensor<[1, 50, 1024]> self = ?,<br>int dim = 1,<br>int index = 0      | Unknown  |
| 18 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>int index = 0       | Unknown  |
| 19 | Tensor<[1, 5]> self = ?,<br>int dim = 1,<br>int index = -1            | Unknown  |
| 20 | Tensor<[1, 8, 768]> self = ?,<br>int dim = 1,<br>int index = 0        | Unknown  |
| 21 | Tensor<[1, 9, 768]> self = ?,<br>int dim = 1,<br>int index = 0        | Unknown  |
| 22 | Tensor<[1]> self = ?,<br>int dim = 0,<br>int index = 0                | Unknown  |
| 23 | Tensor<[3, 1370, 1, 1280]> self = ?,<br>int dim = 0,<br>int index = 0 | Unknown  |
| 24 | Tensor<[3, 16, 6, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Unknown  |
| 25 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Unknown  |
| 26 | Tensor<[3, 16, 8, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Unknown  |
| 27 | Tensor<[3, 16, 8, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Unknown  |
| 28 | Tensor<[3, 197, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 0  | Unknown  |
| 29 | Tensor<[3, 197, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 0   | Unknown  |
| 30 | Tensor<[3, 4, 12, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Unknown  |
| 31 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Unknown  |
| 32 | Tensor<[3, 4, 16, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Unknown  |
| 33 | Tensor<[3, 4, 16, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Unknown  |
| 34 | Tensor<[3, 50, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 0   | Unknown  |
| 35 | Tensor<[3, 50, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 0    | Unknown  |
| 36 | Tensor<[3, 64, 3, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Unknown  |
| 37 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Unknown  |
| 38 | Tensor<[3, 64, 4, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Unknown  |
| 39 | Tensor<[3, 64, 4, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Unknown  |
| 40 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 2          | Unknown  |
| 41 | Tensor<[6, 1, 100, 92]> self = ?,<br>int dim = 0,<br>int index = -1   | Unknown  |
| 42 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>int index = 2          | Unknown  |
### aten.sigmoid.default
|    | ATen Input Variations             | Status   |
|---:|:----------------------------------|:---------|
|  0 | Tensor<[1, 1, 256, 256]> self = ? | Unknown  |
|  1 | Tensor<[1, 100, 4]> self = ?      | Unknown  |
|  2 | Tensor<[1, 2, 30, 40]> self = ?   | Unknown  |
|  3 | Tensor<[1, 224, 1, 1]> self = ?   | Unknown  |
|  4 | Tensor<[1, 232, 1, 1]> self = ?   | Unknown  |
|  5 | Tensor<[1, 3, 64, 64]> self = ?   | Unknown  |
|  6 | Tensor<[1, 4, 64, 64]> self = ?   | Unknown  |
|  7 | Tensor<[1, 48, 1, 1]> self = ?    | Unknown  |
|  8 | Tensor<[1, 50, 3072]> self = ?    | Unknown  |
|  9 | Tensor<[1, 528, 1, 1]> self = ?   | Unknown  |
| 10 | Tensor<[1, 64, 1, 1]> self = ?    | Unknown  |
| 11 | Tensor<[1, 72, 1, 1]> self = ?    | Unknown  |
| 12 | Tensor<[1, 72, 28, 28]> self = ?  | Unknown  |
| 13 | Tensor<[6, 1, 100, 4]> self = ?   | Unknown  |
### aten.silu.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 32, 11008]> self = ? | Unknown  |
### aten.sin.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 23, 40, 64]> self = ? | Unknown  |
|  1 | Tensor<[1, 32, 128]> self = ?    | Unknown  |
### aten.slice.Tensor
|     | ATen Input Variations                                                                                                     | Status   |
|----:|:--------------------------------------------------------------------------------------------------------------------------|:---------|
|   0 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 4           | Unknown  |
|   1 | Tensor<[1, 1, 1, 10]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                     | Unknown  |
|   2 | Tensor<[1, 1, 1, 15]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                     | Unknown  |
|   3 | Tensor<[1, 1, 1, 19]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                     | Unknown  |
|   4 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                   | Unknown  |
|   5 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 46                   | Unknown  |
|   6 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 6                    | Unknown  |
|   7 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int]<s10 + 1> end = ?           | Unknown  |
|   8 | Tensor<[1, 1, 1, 24]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                     | Unknown  |
|   9 | Tensor<[1, 1, 1, 256]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                    | Unknown  |
|  10 | Tensor<[1, 1, 1, 25]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                     | Unknown  |
|  11 | Tensor<[1, 1, 1, 45]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                     | Unknown  |
|  12 | Tensor<[1, 1, 1, 5]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                      | Unknown  |
|  13 | Tensor<[1, 1, 1, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                      | Unknown  |
|  14 | Tensor<[1, 1, 1, 8]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                      | Unknown  |
|  15 | Tensor<[1, 1, 1024, 1024]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1                | Unknown  |
|  16 | Tensor<[1, 1, 12, 16, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                 | Unknown  |
|  17 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 1,<br>Optional[int] end = -1,<br>int step = 2   | Unknown  |
|  18 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                    | Unknown  |
|  19 | Tensor<[1, 1, 19, 19]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                    | Unknown  |
|  20 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                         | Unknown  |
|  21 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1                | Unknown  |
|  22 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                | Unknown  |
|  23 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 5                 | Unknown  |
|  24 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int]<s10> start = ?,<br>Optional[int]<s10 + 1> end = ?   | Unknown  |
|  25 | Tensor<[1, 1, 32, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                    | Unknown  |
|  26 | Tensor<[1, 1, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                        | Unknown  |
|  27 | Tensor<[1, 1, 384, 512]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                  | Unknown  |
|  28 | Tensor<[1, 1, 40]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                        | Unknown  |
|  29 | Tensor<[1, 1, 45, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 45                  | Unknown  |
|  30 | Tensor<[1, 1, 45, 45]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                    | Unknown  |
|  31 | Tensor<[1, 1, 5, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 5                    | Unknown  |
|  32 | Tensor<[1, 1, 7, 1024]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 7                    | Unknown  |
|  33 | Tensor<[1, 1, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 32,<br>Optional[int] end = -1                    | Unknown  |
|  34 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                      | Unknown  |
|  35 | Tensor<[1, 100, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                     | Unknown  |
|  36 | Tensor<[1, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                           | Unknown  |
|  37 | Tensor<[1, 12, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = -1                    | Unknown  |
|  38 | Tensor<[1, 1370, 1280]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                   | Unknown  |
|  39 | Tensor<[1, 14, 28, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  40 | Tensor<[1, 14, 28, 256]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  41 | Tensor<[1, 1445, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = -100,<br>Optional[int] end = -1                 | Unknown  |
|  42 | Tensor<[1, 145, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = -1                     | Unknown  |
|  43 | Tensor<[1, 15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                           | Unknown  |
|  44 | Tensor<[1, 16, 112, 112]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                 | Unknown  |
|  45 | Tensor<[1, 16, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = -1                    | Unknown  |
|  46 | Tensor<[1, 16, 32, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  47 | Tensor<[1, 16, 32, 256]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  48 | Tensor<[1, 1876, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 1                     | Unknown  |
|  49 | Tensor<[1, 1876, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int]<s0> end = ?                 | Unknown  |
|  50 | Tensor<[1, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1                          | Unknown  |
|  51 | Tensor<[1, 196, 1024]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                    | Unknown  |
|  52 | Tensor<[1, 196, 768]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                     | Unknown  |
|  53 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                    | Unknown  |
|  54 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                     | Unknown  |
|  55 | Tensor<[1, 19]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                           | Unknown  |
|  56 | Tensor<[1, 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1                            | Unknown  |
|  57 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                    | Unknown  |
|  58 | Tensor<[1, 2048]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                         | Unknown  |
|  59 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1                  | Unknown  |
|  60 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  61 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                       | Unknown  |
|  62 | Tensor<[1, 24, 56, 56]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                   | Unknown  |
|  63 | Tensor<[1, 24]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1                           | Unknown  |
|  64 | Tensor<[1, 256]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                          | Unknown  |
|  65 | Tensor<[1, 28, 28, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                  | Unknown  |
|  66 | Tensor<[1, 28, 28, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  67 | Tensor<[1, 28, 28, 256]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  68 | Tensor<[1, 28, 28, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                   | Unknown  |
|  69 | Tensor<[1, 28, 56, 128]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  70 | Tensor<[1, 28, 56, 96]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 2  | Unknown  |
|  71 | Tensor<[1, 3, 224, 224]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                  | Unknown  |
|  72 | Tensor<[1, 30, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1                       | Unknown  |
|  73 | Tensor<[1, 32, 32, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                  | Unknown  |
|  74 | Tensor<[1, 32, 32, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 64                  | Unknown  |
|  75 | Tensor<[1, 32, 32, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  76 | Tensor<[1, 32, 32, 256]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  77 | Tensor<[1, 32, 32, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                   | Unknown  |
|  78 | Tensor<[1, 32, 64, 128]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  79 | Tensor<[1, 32, 64, 96]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 2  | Unknown  |
|  80 | Tensor<[1, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                           | Unknown  |
|  81 | Tensor<[1, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                           | Unknown  |
|  82 | Tensor<[1, 4251, 192]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                    | Unknown  |
|  83 | Tensor<[1, 45]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                           | Unknown  |
|  84 | Tensor<[1, 46]> self = ?,<br>int dim = 1,<br>Optional[int] start = 45,<br>Optional[int] end = -1                          | Unknown  |
|  85 | Tensor<[1, 48, 112, 112]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                 | Unknown  |
|  86 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                    | Unknown  |
|  87 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 2   | Unknown  |
|  88 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1                    | Unknown  |
|  89 | Tensor<[1, 50, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                     | Unknown  |
|  90 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                      | Unknown  |
|  91 | Tensor<[1, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                          | Unknown  |
|  92 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256                         | Unknown  |
|  93 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 8                           | Unknown  |
|  94 | Tensor<[1, 514]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                          | Unknown  |
|  95 | Tensor<[1, 56, 56, 128]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                  | Unknown  |
|  96 | Tensor<[1, 56, 56, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  97 | Tensor<[1, 56, 56, 96]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                   | Unknown  |
|  98 | Tensor<[1, 56, 56, 96]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 2  | Unknown  |
|  99 | Tensor<[1, 5]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                            | Unknown  |
| 100 | Tensor<[1, 6, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = -1                     | Unknown  |
| 101 | Tensor<[1, 60, 80]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                       | Unknown  |
| 102 | Tensor<[1, 600, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                     | Unknown  |
| 103 | Tensor<[1, 64, 64, 128]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                  | Unknown  |
| 104 | Tensor<[1, 64, 64, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
| 105 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                   | Unknown  |
| 106 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 2  | Unknown  |
| 107 | Tensor<[1, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1                           | Unknown  |
| 108 | Tensor<[1, 6]> self = ?,<br>int dim = 1,<br>Optional[int] start = 5,<br>Optional[int] end = -1                            | Unknown  |
| 109 | Tensor<[1, 7, 71, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                    | Unknown  |
| 110 | Tensor<[1, 7, 73, 64]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -2                    | Unknown  |
| 111 | Tensor<[1, 71, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                    | Unknown  |
| 112 | Tensor<[1, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1                          | Unknown  |
| 113 | Tensor<[1, 77]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 7                            | Unknown  |
| 114 | Tensor<[1, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                            | Unknown  |
| 115 | Tensor<[1, 8, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = -1                     | Unknown  |
| 116 | Tensor<[1, 80, 3000]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                     | Unknown  |
| 117 | Tensor<[1, 8]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                            | Unknown  |
| 118 | Tensor<[1, s0]> self = ?,<br>int dim = 1,<br>Optional[int] start = -1,<br>Optional[int] end = -1                          | Unknown  |
| 119 | Tensor<[1, s1 + 1]> self = ?,<br>int dim = 1,<br>Optional[int]<s1> start = ?,<br>Optional[int] end = -1                   | Unknown  |
| 120 | Tensor<[2, 1, 1, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                      | Unknown  |
| 121 | Tensor<[2048, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 7                         | Unknown  |
| 122 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 4        | Unknown  |
| 123 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 2                          | Unknown  |
| 124 | Tensor<[3]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                               | Unknown  |
| 125 | Tensor<[448, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 1                         | Unknown  |
| 126 | Tensor<[448, 768]> self = ?,<br>int dim = 0,<br>Optional[int]<s2> start = ?,<br>Optional[int]<s2 + 1> end = ?             | Unknown  |
| 127 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 4        | Unknown  |
| 128 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 2                          | Unknown  |
### aten.slice_scatter.default
|    | ATen Input Variations                                                                                                                           | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> src = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
|  1 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1     | Unknown  |
|  2 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1     | Unknown  |
### aten.split.Tensor
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1       | Unknown  |
|  1 | Tensor<[1, 25, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1       | Unknown  |
|  2 | Tensor<[1, 256, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1      | Unknown  |
|  3 | Tensor<[1, 5, 32]> self = ?,<br>int split_size = 16,<br>int dim = -1      | Unknown  |
|  4 | Tensor<[1, 5, 4, 768]> self = ?,<br>int split_size = 256,<br>int dim = -1 | Unknown  |
|  5 | Tensor<[1, 7, 2304]> self = ?,<br>int split_size = 768,<br>int dim = 2    | Unknown  |
|  6 | Tensor<[768, 256]> self = ?,<br>int split_size = 256                      | Unknown  |
### aten.split_with_sizes.default
|    | ATen Input Variations                                                                                         | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 163206, 91]> self = ?,<br>List[int] split_sizes = [122400, 30600, 7650, 1989, 567],<br>int dim = 1 | Unknown  |
|  1 | Tensor<[163206, 4]> self = ?,<br>List[int] split_sizes = [122400, 30600, 7650, 1989, 567]                     | Unknown  |
### aten.squeeze.dim
|    | ATen Input Variations                                   | Status   |
|---:|:--------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 25600]> self = ?,<br>int dim = 0          | Unknown  |
|  1 | Tensor<[1, 1, 480, 640]> self = ?,<br>int dim = 1       | Unknown  |
|  2 | Tensor<[1, 14, 1]> self = ?,<br>int dim = -1            | Unknown  |
|  3 | Tensor<[1, 19]> self = ?,<br>int dim = 0                | Unknown  |
|  4 | Tensor<[1, 25, 1]> self = ?,<br>int dim = -1            | Unknown  |
|  5 | Tensor<[1, 256, 1]> self = ?,<br>int dim = -1           | Unknown  |
|  6 | Tensor<[3, 1370, 1, 1, 1280]> self = ?,<br>int dim = -2 | Unknown  |
|  7 | Tensor<[3, 197, 1, 1, 1024]> self = ?,<br>int dim = -2  | Unknown  |
|  8 | Tensor<[3, 197, 1, 1, 768]> self = ?,<br>int dim = -2   | Unknown  |
|  9 | Tensor<[3, 50, 1, 1, 1024]> self = ?,<br>int dim = -2   | Unknown  |
| 10 | Tensor<[3, 50, 1, 1, 768]> self = ?,<br>int dim = -2    | Unknown  |
### aten.stack.default
|    | ATen Input Variations                                                                                                                                                                                                                                | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [_unsafe_view_10, _unsafe_view_11, _unsafe_view_10, _unsafe_view_11, _unsafe_view_10, _unsafe_view_11, _unsafe_view_10, _unsafe_view_11, _unsafe_view_10, _unsafe_view_11, _unsafe_view_10, _unsafe_view_11],<br>int dim = -1 | Unknown  |
|  1 | List[Tensor] tensors = [_unsafe_view_10, _unsafe_view_11, _unsafe_view_10, _unsafe_view_11, _unsafe_view_10, _unsafe_view_11, _unsafe_view_10, _unsafe_view_11],<br>int dim = -1                                                                     | Unknown  |
|  2 | List[Tensor] tensors = [_unsafe_view_10, _unsafe_view_11, _unsafe_view_10, _unsafe_view_11],<br>int dim = 1                                                                                                                                          | Unknown  |
|  3 | List[Tensor] tensors = [expand, expand_1],<br>int dim = -1                                                                                                                                                                                           | Unknown  |
|  4 | List[Tensor] tensors = [getitem_155, getitem_191, getitem_227, getitem_263, getitem_299, getitem_335]                                                                                                                                                | Unknown  |
|  5 | List[Tensor] tensors = [neg, slice_28],<br>int dim = -1                                                                                                                                                                                              | Unknown  |
|  6 | List[Tensor] tensors = [sin, cos],<br>int dim = 4                                                                                                                                                                                                    | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 0.5              | Unknown  |
|  1 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ? | Unknown  |
|  2 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                | Unknown  |
|  3 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?             | Unknown  |
|  4 | Tensor<[1, 15]> self = ?,<br>Tensor<[15, 1]> other = ?             | Unknown  |
|  5 | Tensor<[1, 32]> self = ?,<br>Tensor other = 1                      | Unknown  |
|  6 | Tensor<[1, 45]> self = ?,<br>Tensor other = 1                      | Unknown  |
|  7 | Tensor<[1, 5]> self = ?,<br>Tensor other = 1                       | Unknown  |
|  8 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ? | Unknown  |
|  9 | Tensor<[128, 1]> self = ?,<br>Tensor<[128, 1]> other = ?           | Unknown  |
| 10 | Tensor<[128]> self = ?,<br>Tensor other = 0.5                      | Unknown  |
| 11 | Tensor<[1]> self = ?,<br>Tensor other = 1                          | Unknown  |
| 12 | Tensor<[24, 1]> self = ?,<br>Tensor<[1, 24]> other = ?             | Unknown  |
| 13 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?     | Unknown  |
| 14 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?     | Unknown  |
| 15 | Tensor<[30, 1]> self = ?,<br>Tensor<[30, 1]> other = ?             | Unknown  |
| 16 | Tensor<[300]> self = ?,<br>Tensor other = 0.5                      | Unknown  |
| 17 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                       | Unknown  |
| 18 | Tensor<[320]> self = ?,<br>Tensor other = 0.5                      | Unknown  |
| 19 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ?     | Unknown  |
| 20 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ?     | Unknown  |
| 21 | Tensor<[800]> self = ?,<br>Tensor other = 0.5                      | Unknown  |
### aten.sum.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[1]> self = ?    | Unknown  |
### aten.sum.dim_IntList
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 16]> self = ?,<br>Optional[List[int]] dim = [1] | Unknown  |
### aten.sym_size.int
|    | ATen Input Variations                                 | Status   |
|---:|:------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>int dim = 3   | Unknown  |
|  1 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>int dim = 2  | Unknown  |
|  2 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>int dim = 2 | Unknown  |
|  3 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>int dim = 2  | Unknown  |
|  4 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>int dim = 2 | Unknown  |
|  5 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>int dim = 2   | Unknown  |
|  6 | Tensor<[1, 8, s0 + 1, 64]> self = ?,<br>int dim = 2   | Unknown  |
|  7 | Tensor<[1, s0, 256]> self = ?,<br>int dim = 1         | Unknown  |
|  8 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1         | Unknown  |
### aten.t.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1000, 1008]> self = ?  | Unknown  |
|  1 | Tensor<[1000, 1024]> self = ?  | Unknown  |
|  2 | Tensor<[1000, 1280]> self = ?  | Unknown  |
|  3 | Tensor<[1000, 1512]> self = ?  | Unknown  |
|  4 | Tensor<[1000, 1536]> self = ?  | Unknown  |
|  5 | Tensor<[1000, 1664]> self = ?  | Unknown  |
|  6 | Tensor<[1000, 1920]> self = ?  | Unknown  |
|  7 | Tensor<[1000, 2016]> self = ?  | Unknown  |
|  8 | Tensor<[1000, 2048]> self = ?  | Unknown  |
|  9 | Tensor<[1000, 2208]> self = ?  | Unknown  |
| 10 | Tensor<[1000, 2520]> self = ?  | Unknown  |
| 11 | Tensor<[1000, 3024]> self = ?  | Unknown  |
| 12 | Tensor<[1000, 3712]> self = ?  | Unknown  |
| 13 | Tensor<[1000, 400]> self = ?   | Unknown  |
| 14 | Tensor<[1000, 440]> self = ?   | Unknown  |
| 15 | Tensor<[1000, 512]> self = ?   | Unknown  |
| 16 | Tensor<[1000, 672]> self = ?   | Unknown  |
| 17 | Tensor<[1000, 7392]> self = ?  | Unknown  |
| 18 | Tensor<[1000, 784]> self = ?   | Unknown  |
| 19 | Tensor<[1000, 888]> self = ?   | Unknown  |
| 20 | Tensor<[1000, 912]> self = ?   | Unknown  |
| 21 | Tensor<[1024, 1024]> self = ?  | Unknown  |
| 22 | Tensor<[1024, 128]> self = ?   | Unknown  |
| 23 | Tensor<[1024, 576]> self = ?   | Unknown  |
| 24 | Tensor<[128, 9216]> self = ?   | Unknown  |
| 25 | Tensor<[1280, 960]> self = ?   | Unknown  |
| 26 | Tensor<[192, 192]> self = ?    | Unknown  |
| 27 | Tensor<[2, 768]> self = ?      | Unknown  |
| 28 | Tensor<[2048, 128]> self = ?   | Unknown  |
| 29 | Tensor<[2304, 768]> self = ?   | Unknown  |
| 30 | Tensor<[256, 1280]> self = ?   | Unknown  |
| 31 | Tensor<[256, 256]> self = ?    | Unknown  |
| 32 | Tensor<[288, 96]> self = ?     | Unknown  |
| 33 | Tensor<[3072, 1024]> self = ?  | Unknown  |
| 34 | Tensor<[32, 32]> self = ?      | Unknown  |
| 35 | Tensor<[384, 128]> self = ?    | Unknown  |
| 36 | Tensor<[384, 196]> self = ?    | Unknown  |
| 37 | Tensor<[384, 512]> self = ?    | Unknown  |
| 38 | Tensor<[3840, 1280]> self = ?  | Unknown  |
| 39 | Tensor<[4096, 128]> self = ?   | Unknown  |
| 40 | Tensor<[4096, 25088]> self = ? | Unknown  |
| 41 | Tensor<[4096, 4096]> self = ?  | Unknown  |
| 42 | Tensor<[4608, 1536]> self = ?  | Unknown  |
| 43 | Tensor<[512, 2]> self = ?      | Unknown  |
| 44 | Tensor<[512, 512]> self = ?    | Unknown  |
| 45 | Tensor<[512, 768]> self = ?    | Unknown  |
| 46 | Tensor<[64, 64]> self = ?      | Unknown  |
| 47 | Tensor<[65024, 4544]> self = ? | Unknown  |
| 48 | Tensor<[768, 128]> self = ?    | Unknown  |
| 49 | Tensor<[768, 768]> self = ?    | Unknown  |
### aten.tanh.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 12, 3072]> self = ? | Unknown  |
|  1 | Tensor<[1, 14, 3072]> self = ? | Unknown  |
|  2 | Tensor<[1, 15, 1024]> self = ? | Unknown  |
|  3 | Tensor<[1, 256, 100]> self = ? | Unknown  |
|  4 | Tensor<[1, 32, 6144]> self = ? | Unknown  |
|  5 | Tensor<[1, 45, 3072]> self = ? | Unknown  |
|  6 | Tensor<[1, 5, 4096]> self = ?  | Unknown  |
|  7 | Tensor<[1, 7, 3072]> self = ?  | Unknown  |
|  8 | Tensor<[1, 768]> self = ?      | Unknown  |
|  9 | Tensor<[1, 9, 16384]> self = ? | Unknown  |
| 10 | Tensor<[1, 9, 3072]> self = ?  | Unknown  |
| 11 | Tensor<[1, 9, 4096]> self = ?  | Unknown  |
| 12 | Tensor<[1, 9, 8192]> self = ?  | Unknown  |
### aten.topk.default
|    | ATen Input Variations                      | Status   |
|---:|:-------------------------------------------|:---------|
|  0 | Tensor<[1, 50257]> self = ?,<br>int k = 50 | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  |
|  1 | Tensor<[1, 1, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  |
|  2 | Tensor<[1, 1, 7, 64]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1        | Unknown  |
|  3 | Tensor<[1, 10, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Unknown  |
|  4 | Tensor<[1, 10, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Unknown  |
|  5 | Tensor<[1, 10, 8, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  |
|  6 | Tensor<[1, 100, 80]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1           | Unknown  |
|  7 | Tensor<[1, 1024, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  |
|  8 | Tensor<[1, 12, 10, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  |
|  9 | Tensor<[1, 12, 10, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2        | Unknown  |
| 10 | Tensor<[1, 12, 12, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  |
| 11 | Tensor<[1, 12, 14, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  |
| 12 | Tensor<[1, 12, 16, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 3        | Unknown  |
| 13 | Tensor<[1, 12, 197, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Unknown  |
| 14 | Tensor<[1, 12, 201, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Unknown  |
| 15 | Tensor<[1, 12, 25, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  |
| 16 | Tensor<[1, 12, 45, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  |
| 17 | Tensor<[1, 12, 7, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Unknown  |
| 18 | Tensor<[1, 12, 9, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Unknown  |
| 19 | Tensor<[1, 1370, 1, 3, 1280]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2 | Unknown  |
| 20 | Tensor<[1, 1370, 1280]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0        | Unknown  |
| 21 | Tensor<[1, 144, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  |
| 22 | Tensor<[1, 15, 6, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  |
| 23 | Tensor<[1, 1500, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  |
| 24 | Tensor<[1, 16, 10, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2        | Unknown  |
| 25 | Tensor<[1, 16, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Unknown  |
| 26 | Tensor<[1, 16, 197, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Unknown  |
| 27 | Tensor<[1, 16, 256, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Unknown  |
| 28 | Tensor<[1, 16, 5, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Unknown  |
| 29 | Tensor<[1, 16, 9, 128]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  |
| 30 | Tensor<[1, 16, 9, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Unknown  |
| 31 | Tensor<[1, 19, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Unknown  |
| 32 | Tensor<[1, 192, 1344]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  |
| 33 | Tensor<[1, 197, 1, 3, 1024]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2  | Unknown  |
| 34 | Tensor<[1, 197, 1, 3, 768]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2   | Unknown  |
| 35 | Tensor<[1, 197, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0         | Unknown  |
| 36 | Tensor<[1, 197, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0          | Unknown  |
| 37 | Tensor<[1, 24, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Unknown  |
| 38 | Tensor<[1, 25600]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0             | Unknown  |
| 39 | Tensor<[1, 3, 1445, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Unknown  |
| 40 | Tensor<[1, 32, 16, 96]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Unknown  |
| 41 | Tensor<[1, 32, 16384]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  |
| 42 | Tensor<[1, 32, 32, 128]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Unknown  |
| 43 | Tensor<[1, 50, 1, 3, 1024]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2   | Unknown  |
| 44 | Tensor<[1, 50, 1, 3, 768]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2    | Unknown  |
| 45 | Tensor<[1, 50, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0          | Unknown  |
| 46 | Tensor<[1, 50, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0           | Unknown  |
| 47 | Tensor<[1, 6, 15, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Unknown  |
| 48 | Tensor<[1, 64, 19200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  |
| 49 | Tensor<[1, 64, 9, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Unknown  |
| 50 | Tensor<[1, 7, 71, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  |
| 51 | Tensor<[1, 768, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  |
| 52 | Tensor<[1, 768, 49]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  |
| 53 | Tensor<[1, 8, 10, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Unknown  |
| 54 | Tensor<[1, 8, 2048, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Unknown  |
| 55 | Tensor<[12, 24, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Unknown  |
| 56 | Tensor<[1370, 16, 80]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1         | Unknown  |
| 57 | Tensor<[16, 6, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Unknown  |
| 58 | Tensor<[16, 6, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Unknown  |
| 59 | Tensor<[16, 8, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Unknown  |
| 60 | Tensor<[16, 8, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Unknown  |
| 61 | Tensor<[197, 12, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1          | Unknown  |
| 62 | Tensor<[197, 16, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1          | Unknown  |
| 63 | Tensor<[24, 24, 64]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1         | Unknown  |
| 64 | Tensor<[262, 768]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1             | Unknown  |
| 65 | Tensor<[50, 12, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Unknown  |
| 66 | Tensor<[50, 16, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Unknown  |
| 67 | Tensor<[6, 100, 1, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Unknown  |
| 68 | Tensor<[64, 3, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Unknown  |
| 69 | Tensor<[64, 3, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Unknown  |
| 70 | Tensor<[64, 4, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Unknown  |
| 71 | Tensor<[64, 4, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Unknown  |
| 72 | Tensor<[8, 920, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1         | Unknown  |
| 73 | Tensor<[920, 8, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Unknown  |
### aten.tril.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[7, 7]> self = ? | Unknown  |
### aten.unbind.int
|    | ATen Input Variations                     | Status   |
|---:|:------------------------------------------|:---------|
|  0 | Tensor<[0, 4]> self = ?,<br>int dim = 1   | Unknown  |
|  1 | Tensor<[12, 4]> self = ?,<br>int dim = 1  | Unknown  |
|  2 | Tensor<[300, 4]> self = ?,<br>int dim = 1 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                               | Status   |
|---:|:----------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 10]> self = ?,<br>int dim = 2         | Unknown  |
|  1 | Tensor<[1, 1, 12]> self = ?,<br>int dim = 2         | Unknown  |
|  2 | Tensor<[1, 1, 14]> self = ?,<br>int dim = 2         | Unknown  |
|  3 | Tensor<[1, 1, 15]> self = ?,<br>int dim = 2         | Unknown  |
|  4 | Tensor<[1, 1, 19]> self = ?,<br>int dim = 2         | Unknown  |
|  5 | Tensor<[1, 1, 201]> self = ?,<br>int dim = 2        | Unknown  |
|  6 | Tensor<[1, 1, 2048]> self = ?,<br>int dim = 2       | Unknown  |
|  7 | Tensor<[1, 1, 2048]> self = ?,<br>int dim = 3       | Unknown  |
|  8 | Tensor<[1, 1, 24]> self = ?,<br>int dim = 2         | Unknown  |
|  9 | Tensor<[1, 1, 256]> self = ?,<br>int dim = 2        | Unknown  |
| 10 | Tensor<[1, 1, 25]> self = ?,<br>int dim = 2         | Unknown  |
| 11 | Tensor<[1, 1, 32]> self = ?,<br>int dim = 2         | Unknown  |
| 12 | Tensor<[1, 1, 45]> self = ?,<br>int dim = 2         | Unknown  |
| 13 | Tensor<[1, 1, 5]> self = ?,<br>int dim = 2          | Unknown  |
| 14 | Tensor<[1, 1, 7]> self = ?,<br>int dim = 2          | Unknown  |
| 15 | Tensor<[1, 1, 8]> self = ?,<br>int dim = 2          | Unknown  |
| 16 | Tensor<[1, 1, 9]> self = ?,<br>int dim = 2          | Unknown  |
| 17 | Tensor<[1, 10]> self = ?,<br>int dim = 1            | Unknown  |
| 18 | Tensor<[1, 12]> self = ?,<br>int dim = 1            | Unknown  |
| 19 | Tensor<[1, 14]> self = ?,<br>int dim = 1            | Unknown  |
| 20 | Tensor<[1, 15]> self = ?,<br>int dim = 1            | Unknown  |
| 21 | Tensor<[1, 19, 19]> self = ?,<br>int dim = 1        | Unknown  |
| 22 | Tensor<[1, 192]> self = ?,<br>int dim = 1           | Unknown  |
| 23 | Tensor<[1, 2048, 2048]> self = ?,<br>int dim = 1    | Unknown  |
| 24 | Tensor<[1, 2048]> self = ?,<br>int dim = 1          | Unknown  |
| 25 | Tensor<[1, 224, 224]> self = ?,<br>int dim = 1      | Unknown  |
| 26 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 3        | Unknown  |
| 27 | Tensor<[1, 24]> self = ?,<br>int dim = 1            | Unknown  |
| 28 | Tensor<[1, 256]> self = ?,<br>int dim = 1           | Unknown  |
| 29 | Tensor<[1, 25]> self = ?,<br>int dim = 1            | Unknown  |
| 30 | Tensor<[1, 32]> self = ?,<br>int dim = 1            | Unknown  |
| 31 | Tensor<[1, 384, 512]> self = ?,<br>int dim = 1      | Unknown  |
| 32 | Tensor<[1, 45]> self = ?,<br>int dim = 1            | Unknown  |
| 33 | Tensor<[1, 5, 1, 16]> self = ?,<br>int dim = 4      | Unknown  |
| 34 | Tensor<[1, 5]> self = ?,<br>int dim = 1             | Unknown  |
| 35 | Tensor<[1, 64]> self = ?,<br>int dim = 2            | Unknown  |
| 36 | Tensor<[1, 7, 64]> self = ?,<br>int dim = 1         | Unknown  |
| 37 | Tensor<[1, 7, 7]> self = ?,<br>int dim = 1          | Unknown  |
| 38 | Tensor<[1, 720, 1280]> self = ?,<br>int dim = 0     | Unknown  |
| 39 | Tensor<[1, 7]> self = ?,<br>int dim = 1             | Unknown  |
| 40 | Tensor<[1, 8]> self = ?,<br>int dim = 1             | Unknown  |
| 41 | Tensor<[1, 9]> self = ?,<br>int dim = 1             | Unknown  |
| 42 | Tensor<[100, 256]> self = ?,<br>int dim = 1         | Unknown  |
| 43 | Tensor<[10]> self = ?,<br>int dim = 0               | Unknown  |
| 44 | Tensor<[12, 16, 2]> self = ?,<br>int dim = 0        | Unknown  |
| 45 | Tensor<[12, 197, 197]> self = ?,<br>int dim = 0     | Unknown  |
| 46 | Tensor<[128]> self = ?,<br>int dim = 1              | Unknown  |
| 47 | Tensor<[12]> self = ?,<br>int dim = -1              | Unknown  |
| 48 | Tensor<[1370, 1, 3, 1280]> self = ?,<br>int dim = 0 | Unknown  |
| 49 | Tensor<[15]> self = ?,<br>int dim = 0               | Unknown  |
| 50 | Tensor<[16, 197, 197]> self = ?,<br>int dim = 0     | Unknown  |
| 51 | Tensor<[16, 49]> self = ?,<br>int dim = 2           | Unknown  |
| 52 | Tensor<[16, 64]> self = ?,<br>int dim = 2           | Unknown  |
| 53 | Tensor<[197, 1, 3, 1024]> self = ?,<br>int dim = 0  | Unknown  |
| 54 | Tensor<[197, 1, 3, 768]> self = ?,<br>int dim = 0   | Unknown  |
| 55 | Tensor<[19]> self = ?,<br>int dim = 0               | Unknown  |
| 56 | Tensor<[2, 1, 7]> self = ?,<br>int dim = 2          | Unknown  |
| 57 | Tensor<[23]> self = ?,<br>int dim = -1              | Unknown  |
| 58 | Tensor<[24]> self = ?,<br>int dim = 0               | Unknown  |
| 59 | Tensor<[3, 1]> self = ?,<br>int dim = 2             | Unknown  |
| 60 | Tensor<[3, 320, 320]> self = ?,<br>int dim = 0      | Unknown  |
| 61 | Tensor<[3, 480, 640]> self = ?,<br>int dim = 0      | Unknown  |
| 62 | Tensor<[3, 49, 49]> self = ?,<br>int dim = 0        | Unknown  |
| 63 | Tensor<[3, 64, 64]> self = ?,<br>int dim = 0        | Unknown  |
| 64 | Tensor<[30]> self = ?,<br>int dim = 1               | Unknown  |
| 65 | Tensor<[32, 32]> self = ?,<br>int dim = 0           | Unknown  |
| 66 | Tensor<[32]> self = ?,<br>int dim = 0               | Unknown  |
| 67 | Tensor<[3]> self = ?,<br>int dim = 1                | Unknown  |
| 68 | Tensor<[4, 49, 49]> self = ?,<br>int dim = 0        | Unknown  |
| 69 | Tensor<[4, 64, 64]> self = ?,<br>int dim = 0        | Unknown  |
| 70 | Tensor<[45, 45]> self = ?,<br>int dim = 0           | Unknown  |
| 71 | Tensor<[50, 1, 3, 1024]> self = ?,<br>int dim = 0   | Unknown  |
| 72 | Tensor<[50, 1, 3, 768]> self = ?,<br>int dim = 0    | Unknown  |
| 73 | Tensor<[50]> self = ?,<br>int dim = -1              | Unknown  |
| 74 | Tensor<[56]> self = ?,<br>int dim = -1              | Unknown  |
| 75 | Tensor<[64, 49]> self = ?,<br>int dim = 1           | Unknown  |
| 76 | Tensor<[64, 64]> self = ?,<br>int dim = 1           | Unknown  |
| 77 | Tensor<[7, 7]> self = ?,<br>int dim = 0             | Unknown  |
| 78 | Tensor<[7]> self = ?,<br>int dim = 0                | Unknown  |
### aten.view.default
|     | ATen Input Variations                                                               | Status   |
|----:|:------------------------------------------------------------------------------------|:---------|
|   0 | Tensor<[0, 1, 4]> self = ?,<br>List[int] size = [0, 4]                              | Unknown  |
|   1 | Tensor<[1, 1, 1, 16, 2]> self = ?,<br>List[int] size = [1, 1, 1, 32]                | Unknown  |
|   2 | Tensor<[1, 1, 1, 4, 4]> self = ?,<br>List[int] size = [1, -1, 4]                    | Unknown  |
|   3 | Tensor<[1, 1, 1, 4, 91]> self = ?,<br>List[int] size = [1, -1, 91]                  | Unknown  |
|   4 | Tensor<[1, 1, 1, 6, 4]> self = ?,<br>List[int] size = [1, -1, 4]                    | Unknown  |
|   5 | Tensor<[1, 1, 1, 6, 91]> self = ?,<br>List[int] size = [1, -1, 91]                  | Unknown  |
|   6 | Tensor<[1, 1, 1, 7, 7, 1024]> self = ?,<br>List[int] size = [1, 49, 1024]           | Unknown  |
|   7 | Tensor<[1, 1, 1, 7, 7, 768]> self = ?,<br>List[int] size = [1, 49, 768]             | Unknown  |
|   8 | Tensor<[1, 1, 1, 8, 8, 1024]> self = ?,<br>List[int] size = [1, 64, 1024]           | Unknown  |
|   9 | Tensor<[1, 1, 1, 8, 8, 768]> self = ?,<br>List[int] size = [1, 64, 768]             | Unknown  |
|  10 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1024]                        | Unknown  |
|  11 | Tensor<[1, 1, 12, 16, 2]> self = ?,<br>List[int] size = [1, 192, 2]                 | Unknown  |
|  12 | Tensor<[1, 1, 12, 16]> self = ?,<br>List[int] size = [1, 192]                       | Unknown  |
|  13 | Tensor<[1, 1, 1280]> self = ?,<br>List[int] size = [1, 1280]                        | Unknown  |
|  14 | Tensor<[1, 1, 16, 16, 2]> self = ?,<br>List[int] size = [1, 1, 16, 32]              | Unknown  |
|  15 | Tensor<[1, 1, 16, 64]> self = ?,<br>List[int] size = [1, 1, 1024]                   | Unknown  |
|  16 | Tensor<[1, 1, 16384, 256]> self = ?,<br>List[int] size = [1, 16384, 256]            | Unknown  |
|  17 | Tensor<[1, 1, 19200, 300]> self = ?,<br>List[int] size = [1, 19200, 300]            | Unknown  |
|  18 | Tensor<[1, 1, 2048]> self = ?,<br>List[int] size = [1, 2048]                        | Unknown  |
|  19 | Tensor<[1, 1, 256]> self = ?,<br>List[int] size = [1, 256]                          | Unknown  |
|  20 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 1, 4, -1]                    | Unknown  |
|  21 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 3072]                        | Unknown  |
|  22 | Tensor<[1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32]                         | Unknown  |
|  23 | Tensor<[1, 1, 384]> self = ?,<br>List[int] size = [1, 384]                          | Unknown  |
|  24 | Tensor<[1, 1, 4, 256]> self = ?,<br>List[int] size = [1, 1, 4, 4, 64]               | Unknown  |
|  25 | Tensor<[1, 1, 4096]> self = ?,<br>List[int] size = [1, 4096]                        | Unknown  |
|  26 | Tensor<[1, 1, 45]> self = ?,<br>List[int] size = [1, 45]                            | Unknown  |
|  27 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [1, 512]                          | Unknown  |
|  28 | Tensor<[1, 1, 7, 64]> self = ?,<br>List[int] size = [1, 1, 7, 64]                   | Unknown  |
|  29 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 768]                          | Unknown  |
|  30 | Tensor<[1, 1, 80]> self = ?,<br>List[int] size = [1, 80]                            | Unknown  |
|  31 | Tensor<[1, 10, 1024]> self = ?,<br>List[int] size = [10, 1024]                      | Unknown  |
|  32 | Tensor<[1, 10, 12, 64]> self = ?,<br>List[int] size = [1, -1, 768]                  | Unknown  |
|  33 | Tensor<[1, 10, 16, 64]> self = ?,<br>List[int] size = [1, -1, 1024]                 | Unknown  |
|  34 | Tensor<[1, 10, 2048]> self = ?,<br>List[int] size = [10, 2048]                      | Unknown  |
|  35 | Tensor<[1, 10, 3072]> self = ?,<br>List[int] size = [10, 3072]                      | Unknown  |
|  36 | Tensor<[1, 10, 4096]> self = ?,<br>List[int] size = [10, 4096]                      | Unknown  |
|  37 | Tensor<[1, 10, 512]> self = ?,<br>List[int] size = [10, 512]                        | Unknown  |
|  38 | Tensor<[1, 10, 768]> self = ?,<br>List[int] size = [10, 768]                        | Unknown  |
|  39 | Tensor<[1, 10, 8, 64]> self = ?,<br>List[int] size = [1, -1, 512]                   | Unknown  |
|  40 | Tensor<[1, 100, 192]> self = ?,<br>List[int] size = [100, 192]                      | Unknown  |
|  41 | Tensor<[1, 1000, 1, 1]> self = ?,<br>List[int] size = [1, 1000]                     | Unknown  |
|  42 | Tensor<[1, 1008, 1, 1]> self = ?,<br>List[int] size = [1, 1008]                     | Unknown  |
|  43 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int] size = [1, 1024]                     | Unknown  |
|  44 | Tensor<[1, 1024, 14, 14]> self = ?,<br>List[int] size = [1, 1024, 196]              | Unknown  |
|  45 | Tensor<[1, 1024, 16, 16]> self = ?,<br>List[int] size = [1, 1024, 256]              | Unknown  |
|  46 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1024, 160]                    | Unknown  |
|  47 | Tensor<[1, 1024, 256]> self = ?,<br>List[int] size = [1, 1024, 16, 16]              | Unknown  |
|  48 | Tensor<[1, 1024, 640]> self = ?,<br>List[int] size = [1024, 640]                    | Unknown  |
|  49 | Tensor<[1, 1024, 7, 7]> self = ?,<br>List[int] size = [1, 1024, 49]                 | Unknown  |
|  50 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1, 1, 1024]                        | Unknown  |
|  51 | Tensor<[1, 10]> self = ?,<br>List[int] size = [-1, 10]                              | Unknown  |
|  52 | Tensor<[1, 12, 1, 10]> self = ?,<br>List[int] size = [12, 1, 10]                    | Unknown  |
|  53 | Tensor<[1, 12, 1, 1]> self = ?,<br>List[int] size = [12, 1, 1]                      | Unknown  |
|  54 | Tensor<[1, 12, 1, 24]> self = ?,<br>List[int] size = [12, 1, 24]                    | Unknown  |
|  55 | Tensor<[1, 12, 1, 2]> self = ?,<br>List[int] size = [12, 1, 2]                      | Unknown  |
|  56 | Tensor<[1, 12, 1, 46]> self = ?,<br>List[int] size = [12, 1, 46]                    | Unknown  |
|  57 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [12, 1, 64]                    | Unknown  |
|  58 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>List[int] size = [12, 1, sym_size_int]      | Unknown  |
|  59 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>List[int] size = [12, 1, sym_size_int_2]   | Unknown  |
|  60 | Tensor<[1, 12, 10, 10]> self = ?,<br>List[int] size = [12, 10, 10]                  | Unknown  |
|  61 | Tensor<[1, 12, 10, 64]> self = ?,<br>List[int] size = [12, 10, 64]                  | Unknown  |
|  62 | Tensor<[1, 12, 12, 12]> self = ?,<br>List[int] size = [12, 12, 12]                  | Unknown  |
|  63 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] size = [12, 12, 64]                  | Unknown  |
|  64 | Tensor<[1, 12, 128]> self = ?,<br>List[int] size = [12, 128]                        | Unknown  |
|  65 | Tensor<[1, 12, 14, 14]> self = ?,<br>List[int] size = [12, 14, 14]                  | Unknown  |
|  66 | Tensor<[1, 12, 14, 64]> self = ?,<br>List[int] size = [12, 14, 64]                  | Unknown  |
|  67 | Tensor<[1, 12, 16, 16]> self = ?,<br>List[int] size = [12, 16, 16]                  | Unknown  |
|  68 | Tensor<[1, 12, 16, 64]> self = ?,<br>List[int] size = [12, 16, 64]                  | Unknown  |
|  69 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [12, 197, 197]              | Unknown  |
|  70 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [12, 197, 64]                | Unknown  |
|  71 | Tensor<[1, 12, 2, 64]> self = ?,<br>List[int] size = [12, 2, 64]                    | Unknown  |
|  72 | Tensor<[1, 12, 201, 201]> self = ?,<br>List[int] size = [12, 201, 201]              | Unknown  |
|  73 | Tensor<[1, 12, 201, 64]> self = ?,<br>List[int] size = [12, 201, 64]                | Unknown  |
|  74 | Tensor<[1, 12, 24, 64]> self = ?,<br>List[int] size = [12, -1, 64]                  | Unknown  |
|  75 | Tensor<[1, 12, 25, 25]> self = ?,<br>List[int] size = [12, 25, 25]                  | Unknown  |
|  76 | Tensor<[1, 12, 25, 64]> self = ?,<br>List[int] size = [12, 25, 64]                  | Unknown  |
|  77 | Tensor<[1, 12, 3072]> self = ?,<br>List[int] size = [12, 3072]                      | Unknown  |
|  78 | Tensor<[1, 12, 45, 45]> self = ?,<br>List[int] size = [12, 45, 45]                  | Unknown  |
|  79 | Tensor<[1, 12, 45, 64]> self = ?,<br>List[int] size = [12, 45, 64]                  | Unknown  |
|  80 | Tensor<[1, 12, 46, 64]> self = ?,<br>List[int] size = [12, 46, 64]                  | Unknown  |
|  81 | Tensor<[1, 12, 50, 64]> self = ?,<br>List[int] size = [12, -1, 64]                  | Unknown  |
|  82 | Tensor<[1, 12, 64, 10]> self = ?,<br>List[int] size = [12, 64, 10]                  | Unknown  |
|  83 | Tensor<[1, 12, 64, 12]> self = ?,<br>List[int] size = [12, 64, 12]                  | Unknown  |
|  84 | Tensor<[1, 12, 64, 14]> self = ?,<br>List[int] size = [12, 64, 14]                  | Unknown  |
|  85 | Tensor<[1, 12, 64, 16]> self = ?,<br>List[int] size = [12, 64, 16]                  | Unknown  |
|  86 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [12, 64, 197]                | Unknown  |
|  87 | Tensor<[1, 12, 64, 1]> self = ?,<br>List[int] size = [12, 64, 1]                    | Unknown  |
|  88 | Tensor<[1, 12, 64, 201]> self = ?,<br>List[int] size = [12, 64, 201]                | Unknown  |
|  89 | Tensor<[1, 12, 64, 25]> self = ?,<br>List[int] size = [12, 64, 25]                  | Unknown  |
|  90 | Tensor<[1, 12, 64, 2]> self = ?,<br>List[int] size = [12, 64, 2]                    | Unknown  |
|  91 | Tensor<[1, 12, 64, 45]> self = ?,<br>List[int] size = [12, 64, 45]                  | Unknown  |
|  92 | Tensor<[1, 12, 64, 46]> self = ?,<br>List[int] size = [12, 64, 46]                  | Unknown  |
|  93 | Tensor<[1, 12, 64, 7]> self = ?,<br>List[int] size = [12, 64, 7]                    | Unknown  |
|  94 | Tensor<[1, 12, 64, 8]> self = ?,<br>List[int] size = [12, 64, 8]                    | Unknown  |
|  95 | Tensor<[1, 12, 64, 9]> self = ?,<br>List[int] size = [12, 64, 9]                    | Unknown  |
|  96 | Tensor<[1, 12, 64, s0 + 1]> self = ?,<br>List[int] size = [12, 64, sym_size_int]    | Unknown  |
|  97 | Tensor<[1, 12, 64, s10 + 1]> self = ?,<br>List[int] size = [12, 64, sym_size_int_1] | Unknown  |
|  98 | Tensor<[1, 12, 7, 64]> self = ?,<br>List[int] size = [12, 7, 64]                    | Unknown  |
|  99 | Tensor<[1, 12, 7, 7]> self = ?,<br>List[int] size = [12, 7, 7]                      | Unknown  |
| 100 | Tensor<[1, 12, 768]> self = ?,<br>List[int] size = [12, 768]                        | Unknown  |
| 101 | Tensor<[1, 12, 8, 64]> self = ?,<br>List[int] size = [12, 8, 64]                    | Unknown  |
| 102 | Tensor<[1, 12, 8, 8]> self = ?,<br>List[int] size = [12, 8, 8]                      | Unknown  |
| 103 | Tensor<[1, 12, 9, 64]> self = ?,<br>List[int] size = [12, 9, 64]                    | Unknown  |
| 104 | Tensor<[1, 12, 9, 9]> self = ?,<br>List[int] size = [12, 9, 9]                      | Unknown  |
| 105 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>List[int] size = [12, sym_size_int_1, 64]  | Unknown  |
| 106 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>List[int] size = [12, sym_size_int_3, 64] | Unknown  |
| 107 | Tensor<[1, 1200, 1280]> self = ?,<br>List[int] size = [1200, 1280]                  | Unknown  |
| 108 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1200, 320]                    | Unknown  |
| 109 | Tensor<[1, 128, 128, 128]> self = ?,<br>List[int] size = [1, 128, 16384]            | Unknown  |
| 110 | Tensor<[1, 128, 15, 20]> self = ?,<br>List[int] size = [1, 128, 300]                | Unknown  |
| 111 | Tensor<[1, 128, 16384]> self = ?,<br>List[int] size = [1, 128, 128, 128]            | Unknown  |
| 112 | Tensor<[1, 128, 4800]> self = ?,<br>List[int] size = [1, 128, 60, 80]               | Unknown  |
| 113 | Tensor<[1, 128, 60, 80]> self = ?,<br>List[int] size = [1, 128, 4800]               | Unknown  |
| 114 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280]                     | Unknown  |
| 115 | Tensor<[1, 1280, 1200]> self = ?,<br>List[int] size = [1, 1280, 30, 40]             | Unknown  |
| 116 | Tensor<[1, 1280, 30, 40]> self = ?,<br>List[int] size = [1, 1280, 1200]             | Unknown  |
| 117 | Tensor<[1, 1280, 37, 37]> self = ?,<br>List[int] size = [1, 1280, 1369]             | Unknown  |
| 118 | Tensor<[1, 1370, 5120]> self = ?,<br>List[int] size = [1370, 5120]                  | Unknown  |
| 119 | Tensor<[1, 14, 128]> self = ?,<br>List[int] size = [14, 128]                        | Unknown  |
| 120 | Tensor<[1, 14, 14, 1024]> self = ?,<br>List[int] size = [196, 1024]                 | Unknown  |
| 121 | Tensor<[1, 14, 14, 1536]> self = ?,<br>List[int] size = [196, 1536]                 | Unknown  |
| 122 | Tensor<[1, 14, 14, 2048]> self = ?,<br>List[int] size = [196, 2048]                 | Unknown  |
| 123 | Tensor<[1, 14, 14, 384]> self = ?,<br>List[int] size = [1, 2, 7, 2, 7, 384]         | Unknown  |
| 124 | Tensor<[1, 14, 14, 512]> self = ?,<br>List[int] size = [1, 2, 7, 2, 7, 512]         | Unknown  |
| 125 | Tensor<[1, 14, 14, 768]> self = ?,<br>List[int] size = [196, 768]                   | Unknown  |
| 126 | Tensor<[1, 14, 3072]> self = ?,<br>List[int] size = [14, 3072]                      | Unknown  |
| 127 | Tensor<[1, 14, 768]> self = ?,<br>List[int] size = [14, 768]                        | Unknown  |
| 128 | Tensor<[1, 1445, 192]> self = ?,<br>List[int] size = [1445, 192]                    | Unknown  |
| 129 | Tensor<[1, 1445, 768]> self = ?,<br>List[int] size = [1445, 768]                    | Unknown  |
| 130 | Tensor<[1, 15, 1024]> self = ?,<br>List[int] size = [15, 1024]                      | Unknown  |
| 131 | Tensor<[1, 15, 15, 12]> self = ?,<br>List[int] size = [-1, 12]                      | Unknown  |
| 132 | Tensor<[1, 15, 15, 16]> self = ?,<br>List[int] size = [-1, 16]                      | Unknown  |
| 133 | Tensor<[1, 15, 15, 24]> self = ?,<br>List[int] size = [-1, 24]                      | Unknown  |
| 134 | Tensor<[1, 15, 15, 2]> self = ?,<br>List[int] size = [225, 2]                       | Unknown  |
| 135 | Tensor<[1, 15, 15, 32]> self = ?,<br>List[int] size = [-1, 32]                      | Unknown  |
| 136 | Tensor<[1, 15, 15, 3]> self = ?,<br>List[int] size = [-1, 3]                        | Unknown  |
| 137 | Tensor<[1, 15, 15, 4]> self = ?,<br>List[int] size = [-1, 4]                        | Unknown  |
| 138 | Tensor<[1, 15, 15, 512]> self = ?,<br>List[int] size = [225, 512]                   | Unknown  |
| 139 | Tensor<[1, 15, 15, 6]> self = ?,<br>List[int] size = [-1, 6]                        | Unknown  |
| 140 | Tensor<[1, 15, 15, 8]> self = ?,<br>List[int] size = [-1, 8]                        | Unknown  |
| 141 | Tensor<[1, 15, 384]> self = ?,<br>List[int] size = [1, -1, 6, 64]                   | Unknown  |
| 142 | Tensor<[1, 15, 512]> self = ?,<br>List[int] size = [15, 512]                        | Unknown  |
| 143 | Tensor<[1, 15, 6, 64]> self = ?,<br>List[int] size = [1, -1, 384]                   | Unknown  |
| 144 | Tensor<[1, 1500, 3072]> self = ?,<br>List[int] size = [1500, 3072]                  | Unknown  |
| 145 | Tensor<[1, 1500, 768]> self = ?,<br>List[int] size = [1500, 768]                    | Unknown  |
| 146 | Tensor<[1, 1512, 1, 1]> self = ?,<br>List[int] size = [1, 1512]                     | Unknown  |
| 147 | Tensor<[1, 1536, 1, 1]> self = ?,<br>List[int] size = [1, 1536]                     | Unknown  |
| 148 | Tensor<[1, 15]> self = ?,<br>List[int] size = [-1, 15]                              | Unknown  |
| 149 | Tensor<[1, 16, 1, 10]> self = ?,<br>List[int] size = [16, 1, 10]                    | Unknown  |
| 150 | Tensor<[1, 16, 1, 1]> self = ?,<br>List[int] size = [1, -1, 4, 1, 1]                | Unknown  |
| 151 | Tensor<[1, 16, 1, 1]> self = ?,<br>List[int] size = [16, 1, 1]                      | Unknown  |
| 152 | Tensor<[1, 16, 1, 2]> self = ?,<br>List[int] size = [16, 1, 2]                      | Unknown  |
| 153 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [16, 1, 64]                    | Unknown  |
| 154 | Tensor<[1, 16, 1, 6]> self = ?,<br>List[int] size = [16, 1, 6]                      | Unknown  |
| 155 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>List[int] size = [16, 1, sym_size_int]      | Unknown  |
| 156 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>List[int] size = [16, 1, sym_size_int_1]   | Unknown  |
| 157 | Tensor<[1, 16, 10, 10]> self = ?,<br>List[int] size = [16, 10, 10]                  | Unknown  |
| 158 | Tensor<[1, 16, 10, 64]> self = ?,<br>List[int] size = [16, 10, 64]                  | Unknown  |
| 159 | Tensor<[1, 16, 12, 64]> self = ?,<br>List[int] size = [1, -1, 768]                  | Unknown  |
| 160 | Tensor<[1, 16, 128, 9]> self = ?,<br>List[int] size = [16, 128, 9]                  | Unknown  |
| 161 | Tensor<[1, 16, 16, 1024]> self = ?,<br>List[int] size = [256, 1024]                 | Unknown  |
| 162 | Tensor<[1, 16, 16, 1536]> self = ?,<br>List[int] size = [256, 1536]                 | Unknown  |
| 163 | Tensor<[1, 16, 16, 2048]> self = ?,<br>List[int] size = [256, 2048]                 | Unknown  |
| 164 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] size = [1, 2, 8, 2, 8, 384]         | Unknown  |
| 165 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int] size = [1, 2, 8, 2, 8, 512]         | Unknown  |
| 166 | Tensor<[1, 16, 16, 768]> self = ?,<br>List[int] size = [256, 768]                   | Unknown  |
| 167 | Tensor<[1, 16, 19, 19]> self = ?,<br>List[int] size = [16, 19, 19]                  | Unknown  |
| 168 | Tensor<[1, 16, 19, 64]> self = ?,<br>List[int] size = [16, -1, 64]                  | Unknown  |
| 169 | Tensor<[1, 16, 197, 197]> self = ?,<br>List[int] size = [16, 197, 197]              | Unknown  |
| 170 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] size = [16, 197, 64]                | Unknown  |
| 171 | Tensor<[1, 16, 2, 64]> self = ?,<br>List[int] size = [16, 2, 64]                    | Unknown  |
| 172 | Tensor<[1, 16, 256, 256]> self = ?,<br>List[int] size = [16, 256, 256]              | Unknown  |
| 173 | Tensor<[1, 16, 256, 64]> self = ?,<br>List[int] size = [16, 256, 64]                | Unknown  |
| 174 | Tensor<[1, 16, 3, 3]> self = ?,<br>List[int] size = [1, -1, 4, 3, 3]                | Unknown  |
| 175 | Tensor<[1, 16, 3072]> self = ?,<br>List[int] size = [16, 3072]                      | Unknown  |
| 176 | Tensor<[1, 16, 32, 32]> self = ?,<br>List[int] size = [16, 32, 32]                  | Unknown  |
| 177 | Tensor<[1, 16, 32, 96]> self = ?,<br>List[int] size = [16, 32, 96]                  | Unknown  |
| 178 | Tensor<[1, 16, 32]> self = ?,<br>List[int] size = [16, 1, 32]                       | Unknown  |
| 179 | Tensor<[1, 16, 38, 38]> self = ?,<br>List[int] size = [1, -1, 4, 38, 38]            | Unknown  |
| 180 | Tensor<[1, 16, 5, 5]> self = ?,<br>List[int] size = [16, 5, 5]                      | Unknown  |
| 181 | Tensor<[1, 16, 5, 64]> self = ?,<br>List[int] size = [16, 5, 64]                    | Unknown  |
| 182 | Tensor<[1, 16, 6, 49, 49]> self = ?,<br>List[int] size = [-1, 6, 49, 49]            | Unknown  |
| 183 | Tensor<[1, 16, 6, 64, 64]> self = ?,<br>List[int] size = [-1, 6, 64, 64]            | Unknown  |
| 184 | Tensor<[1, 16, 6, 64]> self = ?,<br>List[int] size = [16, 6, 64]                    | Unknown  |
| 185 | Tensor<[1, 16, 64, 10]> self = ?,<br>List[int] size = [16, 64, 10]                  | Unknown  |
| 186 | Tensor<[1, 16, 64, 197]> self = ?,<br>List[int] size = [16, 64, 197]                | Unknown  |
| 187 | Tensor<[1, 16, 64, 1]> self = ?,<br>List[int] size = [16, 64, 1]                    | Unknown  |
| 188 | Tensor<[1, 16, 64, 256]> self = ?,<br>List[int] size = [16, 64, 256]                | Unknown  |
| 189 | Tensor<[1, 16, 64, 2]> self = ?,<br>List[int] size = [16, 64, 2]                    | Unknown  |
| 190 | Tensor<[1, 16, 64, 5]> self = ?,<br>List[int] size = [16, 64, 5]                    | Unknown  |
| 191 | Tensor<[1, 16, 64, 6]> self = ?,<br>List[int] size = [16, 64, 6]                    | Unknown  |
| 192 | Tensor<[1, 16, 64, 9]> self = ?,<br>List[int] size = [16, 64, 9]                    | Unknown  |
| 193 | Tensor<[1, 16, 64, s0 + 1]> self = ?,<br>List[int] size = [16, 64, sym_size_int]    | Unknown  |
| 194 | Tensor<[1, 16, 64, s10 + 1]> self = ?,<br>List[int] size = [16, 64, sym_size_int]   | Unknown  |
| 195 | Tensor<[1, 16, 768]> self = ?,<br>List[int] size = [16, 768]                        | Unknown  |
| 196 | Tensor<[1, 16, 8, 49, 49]> self = ?,<br>List[int] size = [-1, 8, 49, 49]            | Unknown  |
| 197 | Tensor<[1, 16, 8, 64, 64]> self = ?,<br>List[int] size = [-1, 8, 64, 64]            | Unknown  |
| 198 | Tensor<[1, 16, 9, 128]> self = ?,<br>List[int] size = [16, 9, 128]                  | Unknown  |
| 199 | Tensor<[1, 16, 9, 64]> self = ?,<br>List[int] size = [16, 9, 64]                    | Unknown  |
| 200 | Tensor<[1, 16, 9, 9]> self = ?,<br>List[int] size = [16, 9, 9]                      | Unknown  |
| 201 | Tensor<[1, 16, 96, 32]> self = ?,<br>List[int] size = [16, 96, 32]                  | Unknown  |
| 202 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>List[int] size = [16, sym_size_int_1, 64]  | Unknown  |
| 203 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>List[int] size = [16, sym_size_int_2, 64] | Unknown  |
| 204 | Tensor<[1, 160, 1024]> self = ?,<br>List[int] size = [1, 160, 32, 32]               | Unknown  |
| 205 | Tensor<[1, 160, 16, 16]> self = ?,<br>List[int] size = [1, 160, 256]                | Unknown  |
| 206 | Tensor<[1, 160, 32, 32]> self = ?,<br>List[int] size = [1, 160, 1024]               | Unknown  |
| 207 | Tensor<[1, 16384, 128]> self = ?,<br>List[int] size = [16384, 128]                  | Unknown  |
| 208 | Tensor<[1, 16384, 256]> self = ?,<br>List[int] size = [1, 1, 16384, 256]            | Unknown  |
| 209 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [16384, 32]                    | Unknown  |
| 210 | Tensor<[1, 1664, 1, 1]> self = ?,<br>List[int] size = [1, 1664]                     | Unknown  |
| 211 | Tensor<[1, 16]> self = ?,<br>List[int] size = [1, 1, 1, 16]                         | Unknown  |
| 212 | Tensor<[1, 19, 1024]> self = ?,<br>List[int] size = [19, 1024]                      | Unknown  |
| 213 | Tensor<[1, 19, 256008]> self = ?,<br>List[int] size = [-1, 256008]                  | Unknown  |
| 214 | Tensor<[1, 19, 4096]> self = ?,<br>List[int] size = [19, 4096]                      | Unknown  |
| 215 | Tensor<[1, 192, 32, 42]> self = ?,<br>List[int] size = [1, 192, 1344]               | Unknown  |
| 216 | Tensor<[1, 192, 4150]> self = ?,<br>List[int] size = [1, 192, 50, 83]               | Unknown  |
| 217 | Tensor<[1, 1920, 1, 1]> self = ?,<br>List[int] size = [1, 1920]                     | Unknown  |
| 218 | Tensor<[1, 19200, 256]> self = ?,<br>List[int] size = [19200, 256]                  | Unknown  |
| 219 | Tensor<[1, 19200, 300]> self = ?,<br>List[int] size = [1, 1, 19200, 300]            | Unknown  |
| 220 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [19200, 64]                    | Unknown  |
| 221 | Tensor<[1, 196, 3072]> self = ?,<br>List[int] size = [196, 3072]                    | Unknown  |
| 222 | Tensor<[1, 196, 768]> self = ?,<br>List[int] size = [196, 768]                      | Unknown  |
| 223 | Tensor<[1, 197, 1024]> self = ?,<br>List[int] size = [197, 1024]                    | Unknown  |
| 224 | Tensor<[1, 197, 3072]> self = ?,<br>List[int] size = [197, 3072]                    | Unknown  |
| 225 | Tensor<[1, 197, 4096]> self = ?,<br>List[int] size = [197, 4096]                    | Unknown  |
| 226 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [197, 768]                      | Unknown  |
| 227 | Tensor<[1, 19]> self = ?,<br>List[int] size = [-1, 19]                              | Unknown  |
| 228 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                                | Unknown  |
| 229 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1]                                   | Unknown  |
| 230 | Tensor<[1, 1]> self = ?,<br>List[int] size = [1]                                    | Unknown  |
| 231 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] size = [2, 256, 32]                  | Unknown  |
| 232 | Tensor<[1, 2, 300, 64]> self = ?,<br>List[int] size = [2, 300, 64]                  | Unknown  |
| 233 | Tensor<[1, 2, 32, 256]> self = ?,<br>List[int] size = [2, 32, 256]                  | Unknown  |
| 234 | Tensor<[1, 2, 4096, 256]> self = ?,<br>List[int] size = [2, 4096, 256]              | Unknown  |
| 235 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] size = [2, 4096, 32]                | Unknown  |
| 236 | Tensor<[1, 2, 4800, 300]> self = ?,<br>List[int] size = [2, 4800, 300]              | Unknown  |
| 237 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] size = [2, 4800, 64]                | Unknown  |
| 238 | Tensor<[1, 2, 64, 300]> self = ?,<br>List[int] size = [2, 64, 300]                  | Unknown  |
| 239 | Tensor<[1, 201, 3072]> self = ?,<br>List[int] size = [201, 3072]                    | Unknown  |
| 240 | Tensor<[1, 201, 768]> self = ?,<br>List[int] size = [201, 768]                      | Unknown  |
| 241 | Tensor<[1, 2016, 1, 1]> self = ?,<br>List[int] size = [1, 2016]                     | Unknown  |
| 242 | Tensor<[1, 2048, 1, 1]> self = ?,<br>List[int] size = [1, 2048]                     | Unknown  |
| 243 | Tensor<[1, 2048, 1280]> self = ?,<br>List[int] size = [1, 2048, 8, 160]             | Unknown  |
| 244 | Tensor<[1, 2048, 15, 20]> self = ?,<br>List[int] size = [1, 2048, 300]              | Unknown  |
| 245 | Tensor<[1, 2048, 256]> self = ?,<br>List[int] size = [1, 2048, 8, 32]               | Unknown  |
| 246 | Tensor<[1, 2048, 300]> self = ?,<br>List[int] size = [1, 2048, 15, 20]              | Unknown  |
| 247 | Tensor<[1, 2048, 768]> self = ?,<br>List[int] size = [2048, 768]                    | Unknown  |
| 248 | Tensor<[1, 2048, 8, 96]> self = ?,<br>List[int] size = [1, 2048, 768]               | Unknown  |
| 249 | Tensor<[1, 2048]> self = ?,<br>List[int] size = [1, 1, 2048]                        | Unknown  |
| 250 | Tensor<[1, 2208, 1, 1]> self = ?,<br>List[int] size = [1, 2208]                     | Unknown  |
| 251 | Tensor<[1, 23, 40, 64, 2]> self = ?,<br>List[int] size = [1, 23, 40, 128]           | Unknown  |
| 252 | Tensor<[1, 23, 40]> self = ?,<br>List[int] size = [1, 920]                          | Unknown  |
| 253 | Tensor<[1, 24, 1, 1]> self = ?,<br>List[int] size = [1, -1, 4, 1, 1]                | Unknown  |
| 254 | Tensor<[1, 24, 10, 10]> self = ?,<br>List[int] size = [1, -1, 4, 10, 10]            | Unknown  |
| 255 | Tensor<[1, 24, 19, 19]> self = ?,<br>List[int] size = [1, -1, 4, 19, 19]            | Unknown  |
| 256 | Tensor<[1, 24, 2, 2]> self = ?,<br>List[int] size = [1, -1, 4, 2, 2]                | Unknown  |
| 257 | Tensor<[1, 24, 20, 20]> self = ?,<br>List[int] size = [1, -1, 4, 20, 20]            | Unknown  |
| 258 | Tensor<[1, 24, 3, 3]> self = ?,<br>List[int] size = [1, -1, 4, 3, 3]                | Unknown  |
| 259 | Tensor<[1, 24, 3072]> self = ?,<br>List[int] size = [24, 3072]                      | Unknown  |
| 260 | Tensor<[1, 24, 32, 49]> self = ?,<br>List[int] size = [24, 32, 49]                  | Unknown  |
| 261 | Tensor<[1, 24, 32, 64]> self = ?,<br>List[int] size = [24, 32, 64]                  | Unknown  |
| 262 | Tensor<[1, 24, 49, 32]> self = ?,<br>List[int] size = [24, 49, 32]                  | Unknown  |
| 263 | Tensor<[1, 24, 49, 49]> self = ?,<br>List[int] size = [24, 49, 49]                  | Unknown  |
| 264 | Tensor<[1, 24, 5, 5]> self = ?,<br>List[int] size = [1, -1, 4, 5, 5]                | Unknown  |
| 265 | Tensor<[1, 24, 64, 32]> self = ?,<br>List[int] size = [24, 64, 32]                  | Unknown  |
| 266 | Tensor<[1, 24, 64, 64]> self = ?,<br>List[int] size = [24, 64, 64]                  | Unknown  |
| 267 | Tensor<[1, 24, 768]> self = ?,<br>List[int] size = [24, 768]                        | Unknown  |
| 268 | Tensor<[1, 25, 3072]> self = ?,<br>List[int] size = [25, 3072]                      | Unknown  |
| 269 | Tensor<[1, 25, 768]> self = ?,<br>List[int] size = [25, 768]                        | Unknown  |
| 270 | Tensor<[1, 2520, 1, 1]> self = ?,<br>List[int] size = [1, 2520]                     | Unknown  |
| 271 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [256, 1024]                    | Unknown  |
| 272 | Tensor<[1, 256, 120, 160]> self = ?,<br>List[int] size = [1, 256, 19200]            | Unknown  |
| 273 | Tensor<[1, 256, 1280]> self = ?,<br>List[int] size = [256, 1280]                    | Unknown  |
| 274 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[int] size = [1, 256, 256]                | Unknown  |
| 275 | Tensor<[1, 256, 160]> self = ?,<br>List[int] size = [256, 160]                      | Unknown  |
| 276 | Tensor<[1, 256, 16384]> self = ?,<br>List[int] size = [1, 256, 128, 128]            | Unknown  |
| 277 | Tensor<[1, 256, 19200]> self = ?,<br>List[int] size = [1, 256, 120, 160]            | Unknown  |
| 278 | Tensor<[1, 256, 23, 40]> self = ?,<br>List[int] size = [1, 256, 920]                | Unknown  |
| 279 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 256, 8, 32]                 | Unknown  |
| 280 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [256, 256]                      | Unknown  |
| 281 | Tensor<[1, 256, 32]> self = ?,<br>List[int] size = [256, 32]                        | Unknown  |
| 282 | Tensor<[1, 256, 4096]> self = ?,<br>List[int] size = [1, 256, 64, 64]               | Unknown  |
| 283 | Tensor<[1, 256, 4096]> self = ?,<br>List[int] size = [256, 4096]                    | Unknown  |
| 284 | Tensor<[1, 256, 512]> self = ?,<br>List[int] size = [256, 512]                      | Unknown  |
| 285 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[int] size = [1, 256, 4096]               | Unknown  |
| 286 | Tensor<[1, 256, 64]> self = ?,<br>List[int] size = [256, 64]                        | Unknown  |
| 287 | Tensor<[1, 256, 768]> self = ?,<br>List[int] size = [1, 256, 8, 96]                 | Unknown  |
| 288 | Tensor<[1, 256, 768]> self = ?,<br>List[int] size = [256, 768]                      | Unknown  |
| 289 | Tensor<[1, 256, 8, 160]> self = ?,<br>List[int] size = [1, 256, 1280]               | Unknown  |
| 290 | Tensor<[1, 256]> self = ?,<br>List[int] size = [1, 1, 256]                          | Unknown  |
| 291 | Tensor<[1, 25]> self = ?,<br>List[int] size = [1, 25]                               | Unknown  |
| 292 | Tensor<[1, 28, 28, 1024]> self = ?,<br>List[int] size = [784, 1024]                 | Unknown  |
| 293 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int] size = [1, 4, 7, 4, 7, 192]         | Unknown  |
| 294 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int] size = [1, 4, 7, 4, 7, 256]         | Unknown  |
| 295 | Tensor<[1, 28, 28, 384]> self = ?,<br>List[int] size = [784, 384]                   | Unknown  |
| 296 | Tensor<[1, 28, 28, 512]> self = ?,<br>List[int] size = [784, 512]                   | Unknown  |
| 297 | Tensor<[1, 28, 28, 768]> self = ?,<br>List[int] size = [784, 768]                   | Unknown  |
| 298 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>List[int] size = [3, 1445, 1445]            | Unknown  |
| 299 | Tensor<[1, 3, 1445, 64]> self = ?,<br>List[int] size = [3, 1445, 64]                | Unknown  |
| 300 | Tensor<[1, 3, 256, 256]> self = ?,<br>List[int] size = [1, 3, 16, 16, 16, 16]       | Unknown  |
| 301 | Tensor<[1, 3, 64, 1445]> self = ?,<br>List[int] size = [3, 64, 1445]                | Unknown  |
| 302 | Tensor<[1, 300, 128]> self = ?,<br>List[int] size = [300, 128]                      | Unknown  |
| 303 | Tensor<[1, 300, 2048]> self = ?,<br>List[int] size = [300, 2048]                    | Unknown  |
| 304 | Tensor<[1, 300, 320]> self = ?,<br>List[int] size = [300, 320]                      | Unknown  |
| 305 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [300, 512]                      | Unknown  |
| 306 | Tensor<[1, 300, 64]> self = ?,<br>List[int] size = [300, 64]                        | Unknown  |
| 307 | Tensor<[1, 3024, 1, 1]> self = ?,<br>List[int] size = [1, 3024]                     | Unknown  |
| 308 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [1, 1, 3072]                        | Unknown  |
| 309 | Tensor<[1, 32, 11008]> self = ?,<br>List[int] size = [32, 11008]                    | Unknown  |
| 310 | Tensor<[1, 32, 128, 128]> self = ?,<br>List[int] size = [1, 32, 16384]              | Unknown  |
| 311 | Tensor<[1, 32, 128, 32]> self = ?,<br>List[int] size = [32, 128, 32]                | Unknown  |
| 312 | Tensor<[1, 32, 1536]> self = ?,<br>List[int] size = [32, 1536]                      | Unknown  |
| 313 | Tensor<[1, 32, 16, 16]> self = ?,<br>List[int] size = [1, 32, 256]                  | Unknown  |
| 314 | Tensor<[1, 32, 16384]> self = ?,<br>List[int] size = [1, 32, 128, 128]              | Unknown  |
| 315 | Tensor<[1, 32, 32, 1024]> self = ?,<br>List[int] size = [1024, 1024]                | Unknown  |
| 316 | Tensor<[1, 32, 32, 128]> self = ?,<br>List[int] size = [32, 32, 128]                | Unknown  |
| 317 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] size = [1, 4, 8, 4, 8, 192]         | Unknown  |
| 318 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int] size = [1, 4, 8, 4, 8, 256]         | Unknown  |
| 319 | Tensor<[1, 32, 32, 32]> self = ?,<br>List[int] size = [32, 32, 32]                  | Unknown  |
| 320 | Tensor<[1, 32, 32, 384]> self = ?,<br>List[int] size = [1024, 384]                  | Unknown  |
| 321 | Tensor<[1, 32, 32, 49]> self = ?,<br>List[int] size = [32, 32, 49]                  | Unknown  |
| 322 | Tensor<[1, 32, 32, 512]> self = ?,<br>List[int] size = [1024, 512]                  | Unknown  |
| 323 | Tensor<[1, 32, 32, 64]> self = ?,<br>List[int] size = [32, 32, 64]                  | Unknown  |
| 324 | Tensor<[1, 32, 32, 768]> self = ?,<br>List[int] size = [1024, 768]                  | Unknown  |
| 325 | Tensor<[1, 32, 4096]> self = ?,<br>List[int] size = [32, 4096]                      | Unknown  |
| 326 | Tensor<[1, 32, 4608]> self = ?,<br>List[int] size = [1, 32, 16, 3, 96]              | Unknown  |
| 327 | Tensor<[1, 32, 49, 32]> self = ?,<br>List[int] size = [32, 49, 32]                  | Unknown  |
| 328 | Tensor<[1, 32, 49, 49]> self = ?,<br>List[int] size = [32, 49, 49]                  | Unknown  |
| 329 | Tensor<[1, 32, 6144]> self = ?,<br>List[int] size = [32, 6144]                      | Unknown  |
| 330 | Tensor<[1, 32, 64, 32]> self = ?,<br>List[int] size = [32, 64, 32]                  | Unknown  |
| 331 | Tensor<[1, 32, 64, 64]> self = ?,<br>List[int] size = [32, 64, 64]                  | Unknown  |
| 332 | Tensor<[1, 320, 1200]> self = ?,<br>List[int] size = [1, 320, 30, 40]               | Unknown  |
| 333 | Tensor<[1, 320, 15, 20]> self = ?,<br>List[int] size = [1, 320, 300]                | Unknown  |
| 334 | Tensor<[1, 320, 30, 40]> self = ?,<br>List[int] size = [1, 320, 1200]               | Unknown  |
| 335 | Tensor<[1, 32128]> self = ?,<br>List[int] size = [1, 1, 32128]                      | Unknown  |
| 336 | Tensor<[1, 36, 100, 136]> self = ?,<br>List[int] size = [1, -1, 4, 100, 136]        | Unknown  |
| 337 | Tensor<[1, 36, 13, 17]> self = ?,<br>List[int] size = [1, -1, 4, 13, 17]            | Unknown  |
| 338 | Tensor<[1, 36, 25, 34]> self = ?,<br>List[int] size = [1, -1, 4, 25, 34]            | Unknown  |
| 339 | Tensor<[1, 36, 50, 68]> self = ?,<br>List[int] size = [1, -1, 4, 50, 68]            | Unknown  |
| 340 | Tensor<[1, 36, 7, 9]> self = ?,<br>List[int] size = [1, -1, 4, 7, 9]                | Unknown  |
| 341 | Tensor<[1, 364, 1, 1]> self = ?,<br>List[int] size = [1, -1, 91, 1, 1]              | Unknown  |
| 342 | Tensor<[1, 364, 3, 3]> self = ?,<br>List[int] size = [1, -1, 91, 3, 3]              | Unknown  |
| 343 | Tensor<[1, 364, 38, 38]> self = ?,<br>List[int] size = [1, -1, 91, 38, 38]          | Unknown  |
| 344 | Tensor<[1, 3712, 1, 1]> self = ?,<br>List[int] size = [1, 3712]                     | Unknown  |
| 345 | Tensor<[1, 384]> self = ?,<br>List[int] size = [1, 1, 384]                          | Unknown  |
| 346 | Tensor<[1, 4, 12, 49, 49]> self = ?,<br>List[int] size = [-1, 12, 49, 49]           | Unknown  |
| 347 | Tensor<[1, 4, 12, 64, 64]> self = ?,<br>List[int] size = [-1, 12, 64, 64]           | Unknown  |
| 348 | Tensor<[1, 4, 16, 49, 49]> self = ?,<br>List[int] size = [-1, 16, 49, 49]           | Unknown  |
| 349 | Tensor<[1, 4, 16, 64, 64]> self = ?,<br>List[int] size = [-1, 16, 64, 64]           | Unknown  |
| 350 | Tensor<[1, 4, 3072]> self = ?,<br>List[int] size = [4, 3072]                        | Unknown  |
| 351 | Tensor<[1, 4, 768]> self = ?,<br>List[int] size = [4, 768]                          | Unknown  |
| 352 | Tensor<[1, 400, 1, 1]> self = ?,<br>List[int] size = [1, 400]                       | Unknown  |
| 353 | Tensor<[1, 4096, 256]> self = ?,<br>List[int] size = [4096, 256]                    | Unknown  |
| 354 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [4096, 64]                      | Unknown  |
| 355 | Tensor<[1, 4096]> self = ?,<br>List[int] size = [1, 1, 4096]                        | Unknown  |
| 356 | Tensor<[1, 440, 1, 1]> self = ?,<br>List[int] size = [1, 440]                       | Unknown  |
| 357 | Tensor<[1, 45, 3072]> self = ?,<br>List[int] size = [45, 3072]                      | Unknown  |
| 358 | Tensor<[1, 45, 768]> self = ?,<br>List[int] size = [45, 768]                        | Unknown  |
| 359 | Tensor<[1, 45]> self = ?,<br>List[int] size = [-1, 45]                              | Unknown  |
| 360 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [4800, 128]                    | Unknown  |
| 361 | Tensor<[1, 4800, 512]> self = ?,<br>List[int] size = [4800, 512]                    | Unknown  |
| 362 | Tensor<[1, 49, 1024]> self = ?,<br>List[int] size = [49, 1024]                      | Unknown  |
| 363 | Tensor<[1, 49, 2304]> self = ?,<br>List[int] size = [1, 49, 3, 24, 32]              | Unknown  |
| 364 | Tensor<[1, 49, 3072]> self = ?,<br>List[int] size = [1, 49, 3, 32, 32]              | Unknown  |
| 365 | Tensor<[1, 49, 768]> self = ?,<br>List[int] size = [49, 768]                        | Unknown  |
| 366 | Tensor<[1, 4]> self = ?,<br>List[int] size = [-1, 4]                                | Unknown  |
| 367 | Tensor<[1, 5, 1, 16, 2]> self = ?,<br>List[int] size = [1, 5, 1, 32]                | Unknown  |
| 368 | Tensor<[1, 5, 1024, 256]> self = ?,<br>List[int] size = [5, 1024, 256]              | Unknown  |
| 369 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] size = [5, 1024, 32]                | Unknown  |
| 370 | Tensor<[1, 5, 1024]> self = ?,<br>List[int] size = [5, 1024]                        | Unknown  |
| 371 | Tensor<[1, 5, 1200, 300]> self = ?,<br>List[int] size = [5, 1200, 300]              | Unknown  |
| 372 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] size = [5, 1200, 64]                | Unknown  |
| 373 | Tensor<[1, 5, 16, 16, 2]> self = ?,<br>List[int] size = [1, 5, 16, 32]              | Unknown  |
| 374 | Tensor<[1, 5, 16, 64]> self = ?,<br>List[int] size = [1, 5, 1024]                   | Unknown  |
| 375 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] size = [5, 256, 32]                  | Unknown  |
| 376 | Tensor<[1, 5, 300, 64]> self = ?,<br>List[int] size = [5, 300, 64]                  | Unknown  |
| 377 | Tensor<[1, 5, 3072]> self = ?,<br>List[int] size = [1, 5, 4, -1]                    | Unknown  |
| 378 | Tensor<[1, 5, 32, 256]> self = ?,<br>List[int] size = [5, 32, 256]                  | Unknown  |
| 379 | Tensor<[1, 5, 4, 256]> self = ?,<br>List[int] size = [1, 5, 4, 4, 64]               | Unknown  |
| 380 | Tensor<[1, 5, 4096]> self = ?,<br>List[int] size = [5, 4096]                        | Unknown  |
| 381 | Tensor<[1, 5, 64, 300]> self = ?,<br>List[int] size = [5, 64, 300]                  | Unknown  |
| 382 | Tensor<[1, 50, 3072]> self = ?,<br>List[int] size = [50, 3072]                      | Unknown  |
| 383 | Tensor<[1, 50, 4096]> self = ?,<br>List[int] size = [50, 4096]                      | Unknown  |
| 384 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [50, 768]                        | Unknown  |
| 385 | Tensor<[1, 50257]> self = ?,<br>List[int] size = [1, 1, 50257]                      | Unknown  |
| 386 | Tensor<[1, 512, 1, 1]> self = ?,<br>List[int] size = [1, 512]                       | Unknown  |
| 387 | Tensor<[1, 512, 15, 20]> self = ?,<br>List[int] size = [1, 512, 300]                | Unknown  |
| 388 | Tensor<[1, 512, 4800]> self = ?,<br>List[int] size = [1, 512, 60, 80]               | Unknown  |
| 389 | Tensor<[1, 512, 60, 80]> self = ?,<br>List[int] size = [1, 512, 4800]               | Unknown  |
| 390 | Tensor<[1, 512, 7, 7]> self = ?,<br>List[int] size = [1, 25088]                     | Unknown  |
| 391 | Tensor<[1, 51200]> self = ?,<br>List[int] size = [1, 1, 51200]                      | Unknown  |
| 392 | Tensor<[1, 512]> self = ?,<br>List[int] size = [1, 1, 512]                          | Unknown  |
| 393 | Tensor<[1, 512]> self = ?,<br>List[int] size = [1, 512]                             | Unknown  |
| 394 | Tensor<[1, 51865]> self = ?,<br>List[int] size = [1, 1, 51865]                      | Unknown  |
| 395 | Tensor<[1, 546, 1, 1]> self = ?,<br>List[int] size = [1, -1, 91, 1, 1]              | Unknown  |
| 396 | Tensor<[1, 546, 10, 10]> self = ?,<br>List[int] size = [1, -1, 91, 10, 10]          | Unknown  |
| 397 | Tensor<[1, 546, 19, 19]> self = ?,<br>List[int] size = [1, -1, 91, 19, 19]          | Unknown  |
| 398 | Tensor<[1, 546, 2, 2]> self = ?,<br>List[int] size = [1, -1, 91, 2, 2]              | Unknown  |
| 399 | Tensor<[1, 546, 20, 20]> self = ?,<br>List[int] size = [1, -1, 91, 20, 20]          | Unknown  |
| 400 | Tensor<[1, 546, 3, 3]> self = ?,<br>List[int] size = [1, -1, 91, 3, 3]              | Unknown  |
| 401 | Tensor<[1, 546, 5, 5]> self = ?,<br>List[int] size = [1, -1, 91, 5, 5]              | Unknown  |
| 402 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int] size = [1, 8, 7, 8, 7, 128]         | Unknown  |
| 403 | Tensor<[1, 56, 56, 384]> self = ?,<br>List[int] size = [3136, 384]                  | Unknown  |
| 404 | Tensor<[1, 56, 56, 512]> self = ?,<br>List[int] size = [3136, 512]                  | Unknown  |
| 405 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int] size = [1, 8, 7, 8, 7, 96]           | Unknown  |
| 406 | Tensor<[1, 576, 1, 1]> self = ?,<br>List[int] size = [1, 576]                       | Unknown  |
| 407 | Tensor<[1, 5]> self = ?,<br>List[int] size = [-1, 5]                                | Unknown  |
| 408 | Tensor<[1, 6, 1, 15]> self = ?,<br>List[int] size = [6, 1, 15]                      | Unknown  |
| 409 | Tensor<[1, 6, 1, 17]> self = ?,<br>List[int] size = [6, 1, 17]                      | Unknown  |
| 410 | Tensor<[1, 6, 1, 1]> self = ?,<br>List[int] size = [6, 1, 1]                        | Unknown  |
| 411 | Tensor<[1, 6, 1, 2]> self = ?,<br>List[int] size = [6, 1, 2]                        | Unknown  |
| 412 | Tensor<[1, 6, 1, 64]> self = ?,<br>List[int] size = [6, 1, 64]                      | Unknown  |
| 413 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>List[int] size = [6, 1, sym_size_int]        | Unknown  |
| 414 | Tensor<[1, 6, 15, 15]> self = ?,<br>List[int] size = [6, 15, 15]                    | Unknown  |
| 415 | Tensor<[1, 6, 15, 64]> self = ?,<br>List[int] size = [6, 15, 64]                    | Unknown  |
| 416 | Tensor<[1, 6, 17, 64]> self = ?,<br>List[int] size = [6, 17, 64]                    | Unknown  |
| 417 | Tensor<[1, 6, 2, 64]> self = ?,<br>List[int] size = [6, 2, 64]                      | Unknown  |
| 418 | Tensor<[1, 6, 64, 15]> self = ?,<br>List[int] size = [6, 64, 15]                    | Unknown  |
| 419 | Tensor<[1, 6, 64, 17]> self = ?,<br>List[int] size = [6, 64, 17]                    | Unknown  |
| 420 | Tensor<[1, 6, 64, 1]> self = ?,<br>List[int] size = [6, 64, 1]                      | Unknown  |
| 421 | Tensor<[1, 6, 64, 2]> self = ?,<br>List[int] size = [6, 64, 2]                      | Unknown  |
| 422 | Tensor<[1, 6, 64, s0 + 1]> self = ?,<br>List[int] size = [6, 64, sym_size_int]      | Unknown  |
| 423 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>List[int] size = [6, sym_size_int_1, 64]    | Unknown  |
| 424 | Tensor<[1, 64, 1024]> self = ?,<br>List[int] size = [64, 1024]                      | Unknown  |
| 425 | Tensor<[1, 64, 12, 12]> self = ?,<br>List[int] size = [1, 9216]                     | Unknown  |
| 426 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[int] size = [1, 64, 19200]              | Unknown  |
| 427 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[int] size = [1, 64, 300]                  | Unknown  |
| 428 | Tensor<[1, 64, 16, 16]> self = ?,<br>List[int] size = [1, 64, 256]                  | Unknown  |
| 429 | Tensor<[1, 64, 19200]> self = ?,<br>List[int] size = [1, 64, 120, 160]              | Unknown  |
| 430 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, 64, 1]                         | Unknown  |
| 431 | Tensor<[1, 64, 2304]> self = ?,<br>List[int] size = [1, 64, 3, 24, 32]              | Unknown  |
| 432 | Tensor<[1, 64, 3, 49, 49]> self = ?,<br>List[int] size = [-1, 3, 49, 49]            | Unknown  |
| 433 | Tensor<[1, 64, 3, 64, 64]> self = ?,<br>List[int] size = [-1, 3, 64, 64]            | Unknown  |
| 434 | Tensor<[1, 64, 3072]> self = ?,<br>List[int] size = [1, 64, 3, 32, 32]              | Unknown  |
| 435 | Tensor<[1, 64, 32]> self = ?,<br>List[int] size = [1, 64, 32]                       | Unknown  |
| 436 | Tensor<[1, 64, 4, 49, 49]> self = ?,<br>List[int] size = [-1, 4, 49, 49]            | Unknown  |
| 437 | Tensor<[1, 64, 4, 64, 64]> self = ?,<br>List[int] size = [-1, 4, 64, 64]            | Unknown  |
| 438 | Tensor<[1, 64, 4096]> self = ?,<br>List[int] size = [1, 64, 64, 64]                 | Unknown  |
| 439 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 128]         | Unknown  |
| 440 | Tensor<[1, 64, 64, 384]> self = ?,<br>List[int] size = [4096, 384]                  | Unknown  |
| 441 | Tensor<[1, 64, 64, 512]> self = ?,<br>List[int] size = [4096, 512]                  | Unknown  |
| 442 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] size = [1, 64, 4096]                 | Unknown  |
| 443 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 96]           | Unknown  |
| 444 | Tensor<[1, 64, 64, 9]> self = ?,<br>List[int] size = [64, 64, 9]                    | Unknown  |
| 445 | Tensor<[1, 64, 768]> self = ?,<br>List[int] size = [64, 768]                        | Unknown  |
| 446 | Tensor<[1, 64, 9, 64]> self = ?,<br>List[int] size = [64, 9, 64]                    | Unknown  |
| 447 | Tensor<[1, 64, 9, 9]> self = ?,<br>List[int] size = [64, 9, 9]                      | Unknown  |
| 448 | Tensor<[1, 640, 1024]> self = ?,<br>List[int] size = [1, 640, 32, 32]               | Unknown  |
| 449 | Tensor<[1, 640, 32, 32]> self = ?,<br>List[int] size = [1, 640, 1024]               | Unknown  |
| 450 | Tensor<[1, 672, 1, 1]> self = ?,<br>List[int] size = [1, 672]                       | Unknown  |
| 451 | Tensor<[1, 6]> self = ?,<br>List[int] size = [1, -1]                                | Unknown  |
| 452 | Tensor<[1, 7, 12, 64]> self = ?,<br>List[int] size = [1, 7, 768]                    | Unknown  |
| 453 | Tensor<[1, 7, 18176]> self = ?,<br>List[int] size = [7, 18176]                      | Unknown  |
| 454 | Tensor<[1, 7, 3072]> self = ?,<br>List[int] size = [-1, 3072]                       | Unknown  |
| 455 | Tensor<[1, 7, 4544]> self = ?,<br>List[int] size = [7, 4544]                        | Unknown  |
| 456 | Tensor<[1, 7, 4672]> self = ?,<br>List[int] size = [1, 7, 73, 64]                   | Unknown  |
| 457 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int] size = [1, 1, 7, 1, 7, 1024]         | Unknown  |
| 458 | Tensor<[1, 7, 7, 1536]> self = ?,<br>List[int] size = [49, 1536]                    | Unknown  |
| 459 | Tensor<[1, 7, 7, 2048]> self = ?,<br>List[int] size = [49, 2048]                    | Unknown  |
| 460 | Tensor<[1, 7, 7, 3072]> self = ?,<br>List[int] size = [49, 3072]                    | Unknown  |
| 461 | Tensor<[1, 7, 7, 4096]> self = ?,<br>List[int] size = [49, 4096]                    | Unknown  |
| 462 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int] size = [1, 1, 7, 1, 7, 768]           | Unknown  |
| 463 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [-1, 768]                         | Unknown  |
| 464 | Tensor<[1, 71, 64, 7]> self = ?,<br>List[int] size = [71, 64, 7]                    | Unknown  |
| 465 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64]                 | Unknown  |
| 466 | Tensor<[1, 71, 7, 7]> self = ?,<br>List[int] size = [71, 7, 7]                      | Unknown  |
| 467 | Tensor<[1, 7392, 1, 1]> self = ?,<br>List[int] size = [1, 7392]                     | Unknown  |
| 468 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int] size = [1, 768]                       | Unknown  |
| 469 | Tensor<[1, 768, 12, 16]> self = ?,<br>List[int] size = [1, 768, 192]                | Unknown  |
| 470 | Tensor<[1, 768, 14, 14]> self = ?,<br>List[int] size = [1, 768, 196]                | Unknown  |
| 471 | Tensor<[1, 768, 144]> self = ?,<br>List[int] size = [1, 768, 12, 12]                | Unknown  |
| 472 | Tensor<[1, 768, 196]> self = ?,<br>List[int] size = [768, 196]                      | Unknown  |
| 473 | Tensor<[1, 768, 384]> self = ?,<br>List[int] size = [768, 384]                      | Unknown  |
| 474 | Tensor<[1, 768, 7, 7]> self = ?,<br>List[int] size = [1, 768, 49]                   | Unknown  |
| 475 | Tensor<[1, 768, 8]> self = ?,<br>List[int] size = [1, 12, 64, 8]                    | Unknown  |
| 476 | Tensor<[1, 768]> self = ?,<br>List[int] size = [1, 1, 768]                          | Unknown  |
| 477 | Tensor<[1, 784, 1, 1]> self = ?,<br>List[int] size = [1, 784]                       | Unknown  |
| 478 | Tensor<[1, 7]> self = ?,<br>List[int] size = [-1, 7]                                | Unknown  |
| 479 | Tensor<[1, 8, 1, 10]> self = ?,<br>List[int] size = [8, 1, 10]                      | Unknown  |
| 480 | Tensor<[1, 8, 1, 1]> self = ?,<br>List[int] size = [8, 1, 1]                        | Unknown  |
| 481 | Tensor<[1, 8, 1, 2]> self = ?,<br>List[int] size = [8, 1, 2]                        | Unknown  |
| 482 | Tensor<[1, 8, 1, 64]> self = ?,<br>List[int] size = [8, 1, 64]                      | Unknown  |
| 483 | Tensor<[1, 8, 1, 920]> self = ?,<br>List[int] size = [8, 1, 920]                    | Unknown  |
| 484 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>List[int] size = [8, 1, sym_size_int]        | Unknown  |
| 485 | Tensor<[1, 8, 10, 10]> self = ?,<br>List[int] size = [8, 10, 10]                    | Unknown  |
| 486 | Tensor<[1, 8, 10, 64]> self = ?,<br>List[int] size = [8, 10, 64]                    | Unknown  |
| 487 | Tensor<[1, 8, 2, 64]> self = ?,<br>List[int] size = [8, 2, 64]                      | Unknown  |
| 488 | Tensor<[1, 8, 2048, 160]> self = ?,<br>List[int] size = [8, 2048, 160]              | Unknown  |
| 489 | Tensor<[1, 8, 2048, 256]> self = ?,<br>List[int] size = [8, 2048, 256]              | Unknown  |
| 490 | Tensor<[1, 8, 2048, 32]> self = ?,<br>List[int] size = [8, 2048, 32]                | Unknown  |
| 491 | Tensor<[1, 8, 256, 160]> self = ?,<br>List[int] size = [8, 256, 160]                | Unknown  |
| 492 | Tensor<[1, 8, 256, 2048]> self = ?,<br>List[int] size = [8, 256, 2048]              | Unknown  |
| 493 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [8, 256, 256]                | Unknown  |
| 494 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [8, 256, 32]                  | Unknown  |
| 495 | Tensor<[1, 8, 256, 96]> self = ?,<br>List[int] size = [8, 256, 96]                  | Unknown  |
| 496 | Tensor<[1, 8, 300, 300]> self = ?,<br>List[int] size = [8, 300, 300]                | Unknown  |
| 497 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] size = [8, 300, 64]                  | Unknown  |
| 498 | Tensor<[1, 8, 32, 2048]> self = ?,<br>List[int] size = [8, 32, 2048]                | Unknown  |
| 499 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [8, 32, 256]                  | Unknown  |
| 500 | Tensor<[1, 8, 64, 10]> self = ?,<br>List[int] size = [8, 64, 10]                    | Unknown  |
| 501 | Tensor<[1, 8, 64, 1]> self = ?,<br>List[int] size = [8, 64, 1]                      | Unknown  |
| 502 | Tensor<[1, 8, 64, 2]> self = ?,<br>List[int] size = [8, 64, 2]                      | Unknown  |
| 503 | Tensor<[1, 8, 64, 300]> self = ?,<br>List[int] size = [8, 64, 300]                  | Unknown  |
| 504 | Tensor<[1, 8, 64, s0 + 1]> self = ?,<br>List[int] size = [8, 64, sym_size_int]      | Unknown  |
| 505 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int] size = [1, 1, 8, 1, 8, 1024]         | Unknown  |
| 506 | Tensor<[1, 8, 8, 1536]> self = ?,<br>List[int] size = [64, 1536]                    | Unknown  |
| 507 | Tensor<[1, 8, 8, 2048]> self = ?,<br>List[int] size = [64, 2048]                    | Unknown  |
| 508 | Tensor<[1, 8, 8, 3072]> self = ?,<br>List[int] size = [64, 3072]                    | Unknown  |
| 509 | Tensor<[1, 8, 8, 4096]> self = ?,<br>List[int] size = [64, 4096]                    | Unknown  |
| 510 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] size = [1, 1, 8, 1, 8, 768]           | Unknown  |
| 511 | Tensor<[1, 8, s0 + 1, 64]> self = ?,<br>List[int] size = [8, sym_size_int_1, 64]    | Unknown  |
| 512 | Tensor<[1, 819, 100, 136]> self = ?,<br>List[int] size = [1, -1, 91, 100, 136]      | Unknown  |
| 513 | Tensor<[1, 819, 13, 17]> self = ?,<br>List[int] size = [1, -1, 91, 13, 17]          | Unknown  |
| 514 | Tensor<[1, 819, 25, 34]> self = ?,<br>List[int] size = [1, -1, 91, 25, 34]          | Unknown  |
| 515 | Tensor<[1, 819, 50, 68]> self = ?,<br>List[int] size = [1, -1, 91, 50, 68]          | Unknown  |
| 516 | Tensor<[1, 819, 7, 9]> self = ?,<br>List[int] size = [1, -1, 91, 7, 9]              | Unknown  |
| 517 | Tensor<[1, 888, 1, 1]> self = ?,<br>List[int] size = [1, 888]                       | Unknown  |
| 518 | Tensor<[1, 9, 1024]> self = ?,<br>List[int] size = [9, 1024]                        | Unknown  |
| 519 | Tensor<[1, 9, 128]> self = ?,<br>List[int] size = [9, 128]                          | Unknown  |
| 520 | Tensor<[1, 9, 16384]> self = ?,<br>List[int] size = [9, 16384]                      | Unknown  |
| 521 | Tensor<[1, 9, 2048]> self = ?,<br>List[int] size = [9, 2048]                        | Unknown  |
| 522 | Tensor<[1, 9, 3072]> self = ?,<br>List[int] size = [9, 3072]                        | Unknown  |
| 523 | Tensor<[1, 9, 4096]> self = ?,<br>List[int] size = [9, 4096]                        | Unknown  |
| 524 | Tensor<[1, 9, 768]> self = ?,<br>List[int] size = [9, 768]                          | Unknown  |
| 525 | Tensor<[1, 9, 8192]> self = ?,<br>List[int] size = [9, 8192]                        | Unknown  |
| 526 | Tensor<[1, 912, 1, 1]> self = ?,<br>List[int] size = [1, 912]                       | Unknown  |
| 527 | Tensor<[1, 920]> self = ?,<br>List[int] size = [1, 1, 1, 920]                       | Unknown  |
| 528 | Tensor<[1, 960, 1, 1]> self = ?,<br>List[int] size = [1, 960]                       | Unknown  |
| 529 | Tensor<[1, s0, 1280]> self = ?,<br>List[int] size = [sym_size_int_2, 1280]          | Unknown  |
| 530 | Tensor<[1, s0, 256]> self = ?,<br>List[int] size = [sym_size_int, 256]              | Unknown  |
| 531 | Tensor<[1, s0, 80]> self = ?,<br>List[int] size = [arg10_1, 80]                     | Unknown  |
| 532 | Tensor<[10, 1024]> self = ?,<br>List[int] size = [1, 10, 1024]                      | Unknown  |
| 533 | Tensor<[10, 2048]> self = ?,<br>List[int] size = [1, 10, 2048]                      | Unknown  |
| 534 | Tensor<[10, 250002]> self = ?,<br>List[int] size = [1, 10, 250002]                  | Unknown  |
| 535 | Tensor<[10, 3072]> self = ?,<br>List[int] size = [1, 10, 3072]                      | Unknown  |
| 536 | Tensor<[10, 4096]> self = ?,<br>List[int] size = [1, 10, 4096]                      | Unknown  |
| 537 | Tensor<[10, 512]> self = ?,<br>List[int] size = [1, 10, 512]                        | Unknown  |
| 538 | Tensor<[10, 768]> self = ?,<br>List[int] size = [1, 10, 768]                        | Unknown  |
| 539 | Tensor<[100, 1, 2048]> self = ?,<br>List[int] size = [100, 2048]                    | Unknown  |
| 540 | Tensor<[100, 1, 256]> self = ?,<br>List[int] size = [100, 256]                      | Unknown  |
| 541 | Tensor<[100, 192]> self = ?,<br>List[int] size = [1, 100, 192]                      | Unknown  |
| 542 | Tensor<[100, 2048]> self = ?,<br>List[int] size = [100, 1, 2048]                    | Unknown  |
| 543 | Tensor<[100, 256]> self = ?,<br>List[int] size = [100, 1, 256]                      | Unknown  |
| 544 | Tensor<[100, 4]> self = ?,<br>List[int] size = [1, 100, 4]                          | Unknown  |
| 545 | Tensor<[100, 92]> self = ?,<br>List[int] size = [1, 100, 92]                        | Unknown  |
| 546 | Tensor<[100]> self = ?,<br>List[int] size = [-1, 1]                                 | Unknown  |
| 547 | Tensor<[1024, 1024]> self = ?,<br>List[int] size = [1, 32, 32, 1024]                | Unknown  |
| 548 | Tensor<[1024, 160]> self = ?,<br>List[int] size = [1, 1024, 160]                    | Unknown  |
| 549 | Tensor<[1024, 192]> self = ?,<br>List[int] size = [1, 32, 32, 192]                  | Unknown  |
| 550 | Tensor<[1024, 256]> self = ?,<br>List[int] size = [1, 32, 32, 256]                  | Unknown  |
| 551 | Tensor<[1024, 576]> self = ?,<br>List[int] size = [16, 64, 576]                     | Unknown  |
| 552 | Tensor<[1024, 640]> self = ?,<br>List[int] size = [1, 1024, 640]                    | Unknown  |
| 553 | Tensor<[1024, 768]> self = ?,<br>List[int] size = [1, 32, 32, 768]                  | Unknown  |
| 554 | Tensor<[1024, 768]> self = ?,<br>List[int] size = [16, 64, 768]                     | Unknown  |
| 555 | Tensor<[10]> self = ?,<br>List[int] size = [1, -1]                                  | Unknown  |
| 556 | Tensor<[12, 1, 10]> self = ?,<br>List[int] size = [1, 12, 1, 10]                    | Unknown  |
| 557 | Tensor<[12, 1, 1]> self = ?,<br>List[int] size = [1, 12, 1, 1]                      | Unknown  |
| 558 | Tensor<[12, 1, 24]> self = ?,<br>List[int] size = [1, 12, 1, 24]                    | Unknown  |
| 559 | Tensor<[12, 1, 2]> self = ?,<br>List[int] size = [1, 12, 1, 2]                      | Unknown  |
| 560 | Tensor<[12, 1, 46]> self = ?,<br>List[int] size = [1, 12, 1, 46]                    | Unknown  |
| 561 | Tensor<[12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]                    | Unknown  |
| 562 | Tensor<[12, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 12, 1, sym_size_int]      | Unknown  |
| 563 | Tensor<[12, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 12, 1, sym_size_int_1]   | Unknown  |
| 564 | Tensor<[12, 10, 10]> self = ?,<br>List[int] size = [1, 12, 10, 10]                  | Unknown  |
| 565 | Tensor<[12, 10, 64]> self = ?,<br>List[int] size = [1, 12, 10, 64]                  | Unknown  |
| 566 | Tensor<[12, 12, 12]> self = ?,<br>List[int] size = [1, 12, 12, 12]                  | Unknown  |
| 567 | Tensor<[12, 12, 64]> self = ?,<br>List[int] size = [1, 12, 12, 64]                  | Unknown  |
| 568 | Tensor<[12, 14, 14]> self = ?,<br>List[int] size = [1, 12, 14, 14]                  | Unknown  |
| 569 | Tensor<[12, 14, 64]> self = ?,<br>List[int] size = [1, 12, 14, 64]                  | Unknown  |
| 570 | Tensor<[12, 16, 16]> self = ?,<br>List[int] size = [1, 12, 16, 16]                  | Unknown  |
| 571 | Tensor<[12, 16, 64]> self = ?,<br>List[int] size = [1, 12, 16, 64]                  | Unknown  |
| 572 | Tensor<[12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197]              | Unknown  |
| 573 | Tensor<[12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]                | Unknown  |
| 574 | Tensor<[12, 201, 201]> self = ?,<br>List[int] size = [1, 12, 201, 201]              | Unknown  |
| 575 | Tensor<[12, 201, 64]> self = ?,<br>List[int] size = [1, 12, 201, 64]                | Unknown  |
| 576 | Tensor<[12, 24, 24]> self = ?,<br>List[int] size = [12, 24, 24]                     | Unknown  |
| 577 | Tensor<[12, 24, 64]> self = ?,<br>List[int] size = [1, 12, 24, 64]                  | Unknown  |
| 578 | Tensor<[12, 25, 25]> self = ?,<br>List[int] size = [1, 12, 25, 25]                  | Unknown  |
| 579 | Tensor<[12, 25, 64]> self = ?,<br>List[int] size = [1, 12, 25, 64]                  | Unknown  |
| 580 | Tensor<[12, 2]> self = ?,<br>List[int] size = [1, 12, 2]                            | Unknown  |
| 581 | Tensor<[12, 3072]> self = ?,<br>List[int] size = [1, 12, 3072]                      | Unknown  |
| 582 | Tensor<[12, 45, 45]> self = ?,<br>List[int] size = [1, 12, 45, 45]                  | Unknown  |
| 583 | Tensor<[12, 45, 64]> self = ?,<br>List[int] size = [1, 12, 45, 64]                  | Unknown  |
| 584 | Tensor<[12, 50, 64]> self = ?,<br>List[int] size = [1, 12, 50, 64]                  | Unknown  |
| 585 | Tensor<[12, 7, 64]> self = ?,<br>List[int] size = [1, 12, 7, 64]                    | Unknown  |
| 586 | Tensor<[12, 7, 7]> self = ?,<br>List[int] size = [1, 12, 7, 7]                      | Unknown  |
| 587 | Tensor<[12, 768]> self = ?,<br>List[int] size = [1, 12, 768]                        | Unknown  |
| 588 | Tensor<[12, 8, 64]> self = ?,<br>List[int] size = [1, 12, 8, 64]                    | Unknown  |
| 589 | Tensor<[12, 8, 8]> self = ?,<br>List[int] size = [1, 12, 8, 8]                      | Unknown  |
| 590 | Tensor<[12, 9, 64]> self = ?,<br>List[int] size = [1, 12, 9, 64]                    | Unknown  |
| 591 | Tensor<[12, 9, 9]> self = ?,<br>List[int] size = [1, 12, 9, 9]                      | Unknown  |
| 592 | Tensor<[1200, 1280]> self = ?,<br>List[int] size = [1, 1200, 1280]                  | Unknown  |
| 593 | Tensor<[1200, 320]> self = ?,<br>List[int] size = [1, 1200, 320]                    | Unknown  |
| 594 | Tensor<[128, 49, 32]> self = ?,<br>List[int] size = [16, 8, 49, 32]                 | Unknown  |
| 595 | Tensor<[128, 49, 49]> self = ?,<br>List[int] size = [16, 8, 49, 49]                 | Unknown  |
| 596 | Tensor<[128, 64, 32]> self = ?,<br>List[int] size = [16, 8, 64, 32]                 | Unknown  |
| 597 | Tensor<[128, 64, 64]> self = ?,<br>List[int] size = [16, 8, 64, 64]                 | Unknown  |
| 598 | Tensor<[12]> self = ?,<br>List[int] size = [-1, 1]                                  | Unknown  |
| 599 | Tensor<[13600, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                         | Unknown  |
| 600 | Tensor<[13600, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                         | Unknown  |
| 601 | Tensor<[136]> self = ?,<br>List[int] size = [1, -1]                                 | Unknown  |
| 602 | Tensor<[1370, 1, 1280]> self = ?,<br>List[int] size = [1370, 1280]                  | Unknown  |
| 603 | Tensor<[1370, 1, 3840]> self = ?,<br>List[int] size = [1370, 1, 3, 1280]            | Unknown  |
| 604 | Tensor<[1370, 1280]> self = ?,<br>List[int] size = [1370, 1, 1280]                  | Unknown  |
| 605 | Tensor<[1370, 3840]> self = ?,<br>List[int] size = [1370, 1, 3840]                  | Unknown  |
| 606 | Tensor<[1370, 5120]> self = ?,<br>List[int] size = [1, 1370, 5120]                  | Unknown  |
| 607 | Tensor<[14, 14]> self = ?,<br>List[int] size = [2, 7, 2, 7]                         | Unknown  |
| 608 | Tensor<[14, 2048]> self = ?,<br>List[int] size = [2, 7, 2048]                       | Unknown  |
| 609 | Tensor<[14, 2]> self = ?,<br>List[int] size = [1, 14, 2]                            | Unknown  |
| 610 | Tensor<[14, 3072]> self = ?,<br>List[int] size = [1, 14, 3072]                      | Unknown  |
| 611 | Tensor<[14, 512]> self = ?,<br>List[int] size = [2, 7, 512]                         | Unknown  |
| 612 | Tensor<[14, 768]> self = ?,<br>List[int] size = [1, 14, 768]                        | Unknown  |
| 613 | Tensor<[1444, 8]> self = ?,<br>List[int] size = [-1, 2]                             | Unknown  |
| 614 | Tensor<[1445, 192]> self = ?,<br>List[int] size = [1, 1445, 192]                    | Unknown  |
| 615 | Tensor<[1445, 768]> self = ?,<br>List[int] size = [1, 1445, 768]                    | Unknown  |
| 616 | Tensor<[15, 1024]> self = ?,<br>List[int] size = [1, 15, 1024]                      | Unknown  |
| 617 | Tensor<[15, 384]> self = ?,<br>List[int] size = [1, 15, 384]                        | Unknown  |
| 618 | Tensor<[15, 512]> self = ?,<br>List[int] size = [1, 15, 512]                        | Unknown  |
| 619 | Tensor<[1500, 3072]> self = ?,<br>List[int] size = [1, 1500, 3072]                  | Unknown  |
| 620 | Tensor<[1500, 768]> self = ?,<br>List[int] size = [1, 1500, 768]                    | Unknown  |
| 621 | Tensor<[16, 1, 10]> self = ?,<br>List[int] size = [1, 16, 1, 10]                    | Unknown  |
| 622 | Tensor<[16, 1, 1]> self = ?,<br>List[int] size = [1, 16, 1, 1]                      | Unknown  |
| 623 | Tensor<[16, 1, 2]> self = ?,<br>List[int] size = [1, 16, 1, 2]                      | Unknown  |
| 624 | Tensor<[16, 1, 64]> self = ?,<br>List[int] size = [1, 16, 1, 64]                    | Unknown  |
| 625 | Tensor<[16, 1, 6]> self = ?,<br>List[int] size = [1, 16, 1, 6]                      | Unknown  |
| 626 | Tensor<[16, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 16, 1, sym_size_int]      | Unknown  |
| 627 | Tensor<[16, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 16, 1, sym_size_int]     | Unknown  |
| 628 | Tensor<[16, 10, 10]> self = ?,<br>List[int] size = [1, 16, 10, 10]                  | Unknown  |
| 629 | Tensor<[16, 10, 64]> self = ?,<br>List[int] size = [1, 16, 10, 64]                  | Unknown  |
| 630 | Tensor<[16, 1370, 80]> self = ?,<br>List[int] size = [1, 16, 1370, 80]              | Unknown  |
| 631 | Tensor<[16, 16]> self = ?,<br>List[int] size = [2, 8, 2, 8]                         | Unknown  |
| 632 | Tensor<[16, 19, 19]> self = ?,<br>List[int] size = [1, 16, 19, 19]                  | Unknown  |
| 633 | Tensor<[16, 19, 64]> self = ?,<br>List[int] size = [1, 16, 19, 64]                  | Unknown  |
| 634 | Tensor<[16, 197, 197]> self = ?,<br>List[int] size = [1, 16, 197, 197]              | Unknown  |
| 635 | Tensor<[16, 197, 64]> self = ?,<br>List[int] size = [1, 16, 197, 64]                | Unknown  |
| 636 | Tensor<[16, 256, 256]> self = ?,<br>List[int] size = [1, 16, 256, 256]              | Unknown  |
| 637 | Tensor<[16, 256, 64]> self = ?,<br>List[int] size = [1, 16, 256, 64]                | Unknown  |
| 638 | Tensor<[16, 3072]> self = ?,<br>List[int] size = [1, 16, 3072]                      | Unknown  |
| 639 | Tensor<[16, 32, 32]> self = ?,<br>List[int] size = [1, 16, 32, 32]                  | Unknown  |
| 640 | Tensor<[16, 32, 96]> self = ?,<br>List[int] size = [1, 16, 32, 96]                  | Unknown  |
| 641 | Tensor<[16, 49, 192]> self = ?,<br>List[int] size = [784, 192]                      | Unknown  |
| 642 | Tensor<[16, 49, 256]> self = ?,<br>List[int] size = [784, 256]                      | Unknown  |
| 643 | Tensor<[16, 49, 576]> self = ?,<br>List[int] size = [16, 49, 3, 6, 32]              | Unknown  |
| 644 | Tensor<[16, 49, 768]> self = ?,<br>List[int] size = [16, 49, 3, 8, 32]              | Unknown  |
| 645 | Tensor<[16, 5, 5]> self = ?,<br>List[int] size = [1, 16, 5, 5]                      | Unknown  |
| 646 | Tensor<[16, 5, 64]> self = ?,<br>List[int] size = [1, 16, 5, 64]                    | Unknown  |
| 647 | Tensor<[16, 50, 64]> self = ?,<br>List[int] size = [1, 16, 50, 64]                  | Unknown  |
| 648 | Tensor<[16, 6, 49, 49]> self = ?,<br>List[int] size = [96, 49, 49]                  | Unknown  |
| 649 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int] size = [96, 64, 64]                  | Unknown  |
| 650 | Tensor<[16, 64, 192]> self = ?,<br>List[int] size = [1024, 192]                     | Unknown  |
| 651 | Tensor<[16, 64, 256]> self = ?,<br>List[int] size = [1024, 256]                     | Unknown  |
| 652 | Tensor<[16, 64, 576]> self = ?,<br>List[int] size = [16, 64, 3, 6, 32]              | Unknown  |
| 653 | Tensor<[16, 64, 768]> self = ?,<br>List[int] size = [16, 64, 3, 8, 32]              | Unknown  |
| 654 | Tensor<[16, 7, 64]> self = ?,<br>List[int] size = [2, 8, 7, 64]                     | Unknown  |
| 655 | Tensor<[16, 7, 7]> self = ?,<br>List[int] size = [2, 8, 7, 7]                       | Unknown  |
| 656 | Tensor<[16, 768]> self = ?,<br>List[int] size = [1, 16, 768]                        | Unknown  |
| 657 | Tensor<[16, 8, 49, 49]> self = ?,<br>List[int] size = [128, 49, 49]                 | Unknown  |
| 658 | Tensor<[16, 8, 64, 64]> self = ?,<br>List[int] size = [128, 64, 64]                 | Unknown  |
| 659 | Tensor<[16, 9, 128]> self = ?,<br>List[int] size = [1, 16, 9, 128]                  | Unknown  |
| 660 | Tensor<[16, 9, 64]> self = ?,<br>List[int] size = [1, 16, 9, 64]                    | Unknown  |
| 661 | Tensor<[16, 9, 9]> self = ?,<br>List[int] size = [1, 16, 9, 9]                      | Unknown  |
| 662 | Tensor<[16384, 128]> self = ?,<br>List[int] size = [1, 16384, 128]                  | Unknown  |
| 663 | Tensor<[16384, 32]> self = ?,<br>List[int] size = [1, 16384, 32]                    | Unknown  |
| 664 | Tensor<[16]> self = ?,<br>List[int] size = [1, -1]                                  | Unknown  |
| 665 | Tensor<[19, 1024]> self = ?,<br>List[int] size = [1, 19, 1024]                      | Unknown  |
| 666 | Tensor<[19, 256008]> self = ?,<br>List[int] size = [1, 19, 256008]                  | Unknown  |
| 667 | Tensor<[19, 4096]> self = ?,<br>List[int] size = [1, 19, 4096]                      | Unknown  |
| 668 | Tensor<[192, 49, 32]> self = ?,<br>List[int] size = [64, 3, 49, 32]                 | Unknown  |
| 669 | Tensor<[192, 49, 49]> self = ?,<br>List[int] size = [64, 3, 49, 49]                 | Unknown  |
| 670 | Tensor<[192, 64, 32]> self = ?,<br>List[int] size = [64, 3, 64, 32]                 | Unknown  |
| 671 | Tensor<[192, 64, 64]> self = ?,<br>List[int] size = [64, 3, 64, 64]                 | Unknown  |
| 672 | Tensor<[19200, 256]> self = ?,<br>List[int] size = [1, 19200, 256]                  | Unknown  |
| 673 | Tensor<[19200, 64]> self = ?,<br>List[int] size = [1, 19200, 64]                    | Unknown  |
| 674 | Tensor<[192]> self = ?,<br>List[int] size = [1, 192, 1, 1]                          | Unknown  |
| 675 | Tensor<[196, 1152]> self = ?,<br>List[int] size = [4, 49, 1152]                     | Unknown  |
| 676 | Tensor<[196, 1536]> self = ?,<br>List[int] size = [1, 14, 14, 1536]                 | Unknown  |
| 677 | Tensor<[196, 1536]> self = ?,<br>List[int] size = [4, 49, 1536]                     | Unknown  |
| 678 | Tensor<[196, 2048]> self = ?,<br>List[int] size = [1, 14, 14, 2048]                 | Unknown  |
| 679 | Tensor<[196, 3072]> self = ?,<br>List[int] size = [1, 196, 3072]                    | Unknown  |
| 680 | Tensor<[196, 384]> self = ?,<br>List[int] size = [1, 14, 14, 384]                   | Unknown  |
| 681 | Tensor<[196, 512]> self = ?,<br>List[int] size = [1, 14, 14, 512]                   | Unknown  |
| 682 | Tensor<[196, 768]> self = ?,<br>List[int] size = [1, 196, 768]                      | Unknown  |
| 683 | Tensor<[197, 1, 1024]> self = ?,<br>List[int] size = [197, 1024]                    | Unknown  |
| 684 | Tensor<[197, 1, 2304]> self = ?,<br>List[int] size = [197, 1, 3, 768]               | Unknown  |
| 685 | Tensor<[197, 1, 3072]> self = ?,<br>List[int] size = [197, 1, 3, 1024]              | Unknown  |
| 686 | Tensor<[197, 1, 768]> self = ?,<br>List[int] size = [197, 768]                      | Unknown  |
| 687 | Tensor<[197, 1024]> self = ?,<br>List[int] size = [1, 197, 1024]                    | Unknown  |
| 688 | Tensor<[197, 1024]> self = ?,<br>List[int] size = [197, 1, 1024]                    | Unknown  |
| 689 | Tensor<[197, 197]> self = ?,<br>List[int] size = [-1]                               | Unknown  |
| 690 | Tensor<[197, 2304]> self = ?,<br>List[int] size = [197, 1, 2304]                    | Unknown  |
| 691 | Tensor<[197, 3072]> self = ?,<br>List[int] size = [1, 197, 3072]                    | Unknown  |
| 692 | Tensor<[197, 3072]> self = ?,<br>List[int] size = [197, 1, 3072]                    | Unknown  |
| 693 | Tensor<[197, 4096]> self = ?,<br>List[int] size = [1, 197, 4096]                    | Unknown  |
| 694 | Tensor<[197, 768]> self = ?,<br>List[int] size = [1, 197, 768]                      | Unknown  |
| 695 | Tensor<[197, 768]> self = ?,<br>List[int] size = [197, 1, 768]                      | Unknown  |
| 696 | Tensor<[19]> self = ?,<br>List[int] size = [1, -1]                                  | Unknown  |
| 697 | Tensor<[1]> self = ?,<br>List[int] size = [1, 1, 1, 1]                              | Unknown  |
| 698 | Tensor<[2, 4096, 256]> self = ?,<br>List[int] size = [1, 2, 4096, 256]              | Unknown  |
| 699 | Tensor<[2, 4096, 32]> self = ?,<br>List[int] size = [1, 2, 4096, 32]                | Unknown  |
| 700 | Tensor<[2, 4800, 300]> self = ?,<br>List[int] size = [1, 2, 4800, 300]              | Unknown  |
| 701 | Tensor<[2, 4800, 64]> self = ?,<br>List[int] size = [1, 2, 4800, 64]                | Unknown  |
| 702 | Tensor<[2, 7, 2048]> self = ?,<br>List[int] size = [14, 2048]                       | Unknown  |
| 703 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [14, 512]                         | Unknown  |
| 704 | Tensor<[2, 7]> self = ?,<br>List[int] size = [-1, 7]                                | Unknown  |
| 705 | Tensor<[2, 8, 7, 64]> self = ?,<br>List[int] size = [16, -1, 64]                    | Unknown  |
| 706 | Tensor<[2, 8, 7, 7]> self = ?,<br>List[int] size = [16, 7, 7]                       | Unknown  |
| 707 | Tensor<[201, 3072]> self = ?,<br>List[int] size = [1, 201, 3072]                    | Unknown  |
| 708 | Tensor<[201, 768]> self = ?,<br>List[int] size = [1, 201, 768]                      | Unknown  |
| 709 | Tensor<[2048, 1280]> self = ?,<br>List[int] size = [1, 2048, 1280]                  | Unknown  |
| 710 | Tensor<[2048, 256]> self = ?,<br>List[int] size = [1, 2048, 256]                    | Unknown  |
| 711 | Tensor<[2048, 262]> self = ?,<br>List[int] size = [1, 2048, 262]                    | Unknown  |
| 712 | Tensor<[20]> self = ?,<br>List[int] size = [-1, 1]                                  | Unknown  |
| 713 | Tensor<[225, 12]> self = ?,<br>List[int] size = [1, 15, 15, 12]                     | Unknown  |
| 714 | Tensor<[225, 16]> self = ?,<br>List[int] size = [1, 15, 15, 16]                     | Unknown  |
| 715 | Tensor<[225, 24]> self = ?,<br>List[int] size = [1, 15, 15, 24]                     | Unknown  |
| 716 | Tensor<[225, 32]> self = ?,<br>List[int] size = [1, 15, 15, 32]                     | Unknown  |
| 717 | Tensor<[225, 3]> self = ?,<br>List[int] size = [1, 15, 15, 3]                       | Unknown  |
| 718 | Tensor<[225, 4]> self = ?,<br>List[int] size = [1, 15, 15, 4]                       | Unknown  |
| 719 | Tensor<[225, 512]> self = ?,<br>List[int] size = [1, 15, 15, 512]                   | Unknown  |
| 720 | Tensor<[225, 6]> self = ?,<br>List[int] size = [1, 15, 15, 6]                       | Unknown  |
| 721 | Tensor<[225, 8]> self = ?,<br>List[int] size = [1, 15, 15, 8]                       | Unknown  |
| 722 | Tensor<[24, 12, 24]> self = ?,<br>List[int] size = [24, 12, 24]                     | Unknown  |
| 723 | Tensor<[24, 12, 64]> self = ?,<br>List[int] size = [24, 12, 64]                     | Unknown  |
| 724 | Tensor<[24, 3072]> self = ?,<br>List[int] size = [1, 24, 3072]                      | Unknown  |
| 725 | Tensor<[24, 49, 32]> self = ?,<br>List[int] size = [1, 24, 49, 32]                  | Unknown  |
| 726 | Tensor<[24, 49, 49]> self = ?,<br>List[int] size = [1, 24, 49, 49]                  | Unknown  |
| 727 | Tensor<[24, 64, 24]> self = ?,<br>List[int] size = [24, 64, 24]                     | Unknown  |
| 728 | Tensor<[24, 64, 32]> self = ?,<br>List[int] size = [1, 24, 64, 32]                  | Unknown  |
| 729 | Tensor<[24, 64, 64]> self = ?,<br>List[int] size = [1, 24, 64, 64]                  | Unknown  |
| 730 | Tensor<[24, 768]> self = ?,<br>List[int] size = [1, 24, 768]                        | Unknown  |
| 731 | Tensor<[2401, 3]> self = ?,<br>List[int] size = [49, 49, -1]                        | Unknown  |
| 732 | Tensor<[2401, 4]> self = ?,<br>List[int] size = [49, 49, -1]                        | Unknown  |
| 733 | Tensor<[25, 2]> self = ?,<br>List[int] size = [1, 25, 2]                            | Unknown  |
| 734 | Tensor<[25, 3072]> self = ?,<br>List[int] size = [1, 25, 3072]                      | Unknown  |
| 735 | Tensor<[25, 768]> self = ?,<br>List[int] size = [1, 25, 768]                        | Unknown  |
| 736 | Tensor<[256, 1024]> self = ?,<br>List[int] size = [1, 256, 1024]                    | Unknown  |
| 737 | Tensor<[256, 1152]> self = ?,<br>List[int] size = [4, 64, 1152]                     | Unknown  |
| 738 | Tensor<[256, 1536]> self = ?,<br>List[int] size = [1, 16, 16, 1536]                 | Unknown  |
| 739 | Tensor<[256, 1536]> self = ?,<br>List[int] size = [4, 64, 1536]                     | Unknown  |
| 740 | Tensor<[256, 160]> self = ?,<br>List[int] size = [1, 256, 160]                      | Unknown  |
| 741 | Tensor<[256, 2048]> self = ?,<br>List[int] size = [1, 16, 16, 2048]                 | Unknown  |
| 742 | Tensor<[256, 256]> self = ?,<br>List[int] size = [1, 256, 256]                      | Unknown  |
| 743 | Tensor<[256, 2]> self = ?,<br>List[int] size = [1, 256, 2]                          | Unknown  |
| 744 | Tensor<[256, 32]> self = ?,<br>List[int] size = [1, 256, 32]                        | Unknown  |
| 745 | Tensor<[256, 384]> self = ?,<br>List[int] size = [1, 16, 16, 384]                   | Unknown  |
| 746 | Tensor<[256, 4096]> self = ?,<br>List[int] size = [1, 256, 4096]                    | Unknown  |
| 747 | Tensor<[256, 49, 32]> self = ?,<br>List[int] size = [64, 4, 49, 32]                 | Unknown  |
| 748 | Tensor<[256, 49, 49]> self = ?,<br>List[int] size = [64, 4, 49, 49]                 | Unknown  |
| 749 | Tensor<[256, 512]> self = ?,<br>List[int] size = [1, 16, 16, 512]                   | Unknown  |
| 750 | Tensor<[256, 512]> self = ?,<br>List[int] size = [1, 256, 512]                      | Unknown  |
| 751 | Tensor<[256, 64, 32]> self = ?,<br>List[int] size = [64, 4, 64, 32]                 | Unknown  |
| 752 | Tensor<[256, 64, 64]> self = ?,<br>List[int] size = [64, 4, 64, 64]                 | Unknown  |
| 753 | Tensor<[256, 64]> self = ?,<br>List[int] size = [1, 256, 64]                        | Unknown  |
| 754 | Tensor<[256, 768]> self = ?,<br>List[int] size = [1, 256, 768]                      | Unknown  |
| 755 | Tensor<[25600, 1]> self = ?,<br>List[int] size = [-1]                               | Unknown  |
| 756 | Tensor<[28, 28]> self = ?,<br>List[int] size = [4, 7, 4, 7]                         | Unknown  |
| 757 | Tensor<[3, 1445, 1445]> self = ?,<br>List[int] size = [1, 3, 1445, 1445]            | Unknown  |
| 758 | Tensor<[3, 1445, 64]> self = ?,<br>List[int] size = [1, 3, 1445, 64]                | Unknown  |
| 759 | Tensor<[300, 128]> self = ?,<br>List[int] size = [1, 300, 128]                      | Unknown  |
| 760 | Tensor<[300, 2048]> self = ?,<br>List[int] size = [1, 300, 2048]                    | Unknown  |
| 761 | Tensor<[300, 320]> self = ?,<br>List[int] size = [1, 300, 320]                      | Unknown  |
| 762 | Tensor<[300, 512]> self = ?,<br>List[int] size = [1, 300, 512]                      | Unknown  |
| 763 | Tensor<[300, 64]> self = ?,<br>List[int] size = [1, 300, 64]                        | Unknown  |
| 764 | Tensor<[3136, 128]> self = ?,<br>List[int] size = [64, 49, 128]                     | Unknown  |
| 765 | Tensor<[3136, 288]> self = ?,<br>List[int] size = [64, 49, 288]                     | Unknown  |
| 766 | Tensor<[3136, 384]> self = ?,<br>List[int] size = [1, 56, 56, 384]                  | Unknown  |
| 767 | Tensor<[3136, 384]> self = ?,<br>List[int] size = [64, 49, 384]                     | Unknown  |
| 768 | Tensor<[3136, 512]> self = ?,<br>List[int] size = [1, 56, 56, 512]                  | Unknown  |
| 769 | Tensor<[3136, 96]> self = ?,<br>List[int] size = [64, 49, 96]                       | Unknown  |
| 770 | Tensor<[32, 11008]> self = ?,<br>List[int] size = [1, 32, 11008]                    | Unknown  |
| 771 | Tensor<[32, 1536]> self = ?,<br>List[int] size = [1, 32, 1536]                      | Unknown  |
| 772 | Tensor<[32, 250880]> self = ?,<br>List[int] size = [1, 32, 250880]                  | Unknown  |
| 773 | Tensor<[32, 32, 128]> self = ?,<br>List[int] size = [1, 32, 32, 128]                | Unknown  |
| 774 | Tensor<[32, 32, 32]> self = ?,<br>List[int] size = [1, 32, 32, 32]                  | Unknown  |
| 775 | Tensor<[32, 32000]> self = ?,<br>List[int] size = [1, 32, 32000]                    | Unknown  |
| 776 | Tensor<[32, 32]> self = ?,<br>List[int] size = [4, 8, 4, 8]                         | Unknown  |
| 777 | Tensor<[32, 4096]> self = ?,<br>List[int] size = [1, 32, 4096]                      | Unknown  |
| 778 | Tensor<[32, 4608]> self = ?,<br>List[int] size = [1, 32, 4608]                      | Unknown  |
| 779 | Tensor<[32, 49, 32]> self = ?,<br>List[int] size = [1, 32, 49, 32]                  | Unknown  |
| 780 | Tensor<[32, 49, 49]> self = ?,<br>List[int] size = [1, 32, 49, 49]                  | Unknown  |
| 781 | Tensor<[32, 6144]> self = ?,<br>List[int] size = [1, 32, 6144]                      | Unknown  |
| 782 | Tensor<[32, 64, 32]> self = ?,<br>List[int] size = [1, 32, 64, 32]                  | Unknown  |
| 783 | Tensor<[32, 64, 64]> self = ?,<br>List[int] size = [1, 32, 64, 64]                  | Unknown  |
| 784 | Tensor<[3234, 1, 4]> self = ?,<br>List[int] size = [3234, 4]                        | Unknown  |
| 785 | Tensor<[32]> self = ?,<br>List[int] size = [1, 1, 32, 1]                            | Unknown  |
| 786 | Tensor<[38809, 12]> self = ?,<br>List[int] size = [197, 197, -1]                    | Unknown  |
| 787 | Tensor<[38809, 16]> self = ?,<br>List[int] size = [197, 197, -1]                    | Unknown  |
| 788 | Tensor<[38]> self = ?,<br>List[int] size = [-1, 1]                                  | Unknown  |
| 789 | Tensor<[4, 12, 49, 49]> self = ?,<br>List[int] size = [48, 49, 49]                  | Unknown  |
| 790 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int] size = [48, 64, 64]                  | Unknown  |
| 791 | Tensor<[4, 16, 49, 49]> self = ?,<br>List[int] size = [64, 49, 49]                  | Unknown  |
| 792 | Tensor<[4, 16, 64, 64]> self = ?,<br>List[int] size = [64, 64, 64]                  | Unknown  |
| 793 | Tensor<[4, 3072]> self = ?,<br>List[int] size = [1, 4, 3072]                        | Unknown  |
| 794 | Tensor<[4, 49, 1152]> self = ?,<br>List[int] size = [4, 49, 3, 12, 32]              | Unknown  |
| 795 | Tensor<[4, 49, 1536]> self = ?,<br>List[int] size = [4, 49, 3, 16, 32]              | Unknown  |
| 796 | Tensor<[4, 49, 384]> self = ?,<br>List[int] size = [196, 384]                       | Unknown  |
| 797 | Tensor<[4, 49, 512]> self = ?,<br>List[int] size = [196, 512]                       | Unknown  |
| 798 | Tensor<[4, 51865]> self = ?,<br>List[int] size = [1, 4, 51865]                      | Unknown  |
| 799 | Tensor<[4, 64, 1152]> self = ?,<br>List[int] size = [4, 64, 3, 12, 32]              | Unknown  |
| 800 | Tensor<[4, 64, 1536]> self = ?,<br>List[int] size = [4, 64, 3, 16, 32]              | Unknown  |
| 801 | Tensor<[4, 64, 384]> self = ?,<br>List[int] size = [256, 384]                       | Unknown  |
| 802 | Tensor<[4, 64, 512]> self = ?,<br>List[int] size = [256, 512]                       | Unknown  |
| 803 | Tensor<[4, 768]> self = ?,<br>List[int] size = [1, 4, 768]                          | Unknown  |
| 804 | Tensor<[400, 12]> self = ?,<br>List[int] size = [-1, 2]                             | Unknown  |
| 805 | Tensor<[4096, 128]> self = ?,<br>List[int] size = [64, 64, 128]                     | Unknown  |
| 806 | Tensor<[4096, 256]> self = ?,<br>List[int] size = [1, 4096, 256]                    | Unknown  |
| 807 | Tensor<[4096, 288]> self = ?,<br>List[int] size = [64, 64, 288]                     | Unknown  |
| 808 | Tensor<[4096, 384]> self = ?,<br>List[int] size = [1, 64, 64, 384]                  | Unknown  |
| 809 | Tensor<[4096, 384]> self = ?,<br>List[int] size = [64, 64, 384]                     | Unknown  |
| 810 | Tensor<[4096, 3]> self = ?,<br>List[int] size = [64, 64, -1]                        | Unknown  |
| 811 | Tensor<[4096, 4]> self = ?,<br>List[int] size = [64, 64, -1]                        | Unknown  |
| 812 | Tensor<[4096, 512]> self = ?,<br>List[int] size = [1, 64, 64, 512]                  | Unknown  |
| 813 | Tensor<[4096, 64]> self = ?,<br>List[int] size = [1, 4096, 64]                      | Unknown  |
| 814 | Tensor<[4096, 96]> self = ?,<br>List[int] size = [64, 64, 96]                       | Unknown  |
| 815 | Tensor<[42]> self = ?,<br>List[int] size = [1, 1, 1, 42]                            | Unknown  |
| 816 | Tensor<[45, 3072]> self = ?,<br>List[int] size = [1, 45, 3072]                      | Unknown  |
| 817 | Tensor<[45, 50257]> self = ?,<br>List[int] size = [1, 45, 50257]                    | Unknown  |
| 818 | Tensor<[45, 768]> self = ?,<br>List[int] size = [1, 45, 768]                        | Unknown  |
| 819 | Tensor<[48, 49, 32]> self = ?,<br>List[int] size = [4, 12, 49, 32]                  | Unknown  |
| 820 | Tensor<[48, 49, 49]> self = ?,<br>List[int] size = [4, 12, 49, 49]                  | Unknown  |
| 821 | Tensor<[48, 64, 32]> self = ?,<br>List[int] size = [4, 12, 64, 32]                  | Unknown  |
| 822 | Tensor<[48, 64, 64]> self = ?,<br>List[int] size = [4, 12, 64, 64]                  | Unknown  |
| 823 | Tensor<[4800, 128]> self = ?,<br>List[int] size = [1, 4800, 128]                    | Unknown  |
| 824 | Tensor<[4800, 512]> self = ?,<br>List[int] size = [1, 4800, 512]                    | Unknown  |
| 825 | Tensor<[49, 1024]> self = ?,<br>List[int] size = [1, 7, 7, 1024]                    | Unknown  |
| 826 | Tensor<[49, 2304]> self = ?,<br>List[int] size = [1, 49, 2304]                      | Unknown  |
| 827 | Tensor<[49, 3072]> self = ?,<br>List[int] size = [1, 49, 3072]                      | Unknown  |
| 828 | Tensor<[49, 3072]> self = ?,<br>List[int] size = [1, 7, 7, 3072]                    | Unknown  |
| 829 | Tensor<[49, 4096]> self = ?,<br>List[int] size = [1, 7, 7, 4096]                    | Unknown  |
| 830 | Tensor<[49, 768]> self = ?,<br>List[int] size = [1, 7, 7, 768]                      | Unknown  |
| 831 | Tensor<[5, 1024, 256]> self = ?,<br>List[int] size = [1, 5, 1024, 256]              | Unknown  |
| 832 | Tensor<[5, 1024, 32]> self = ?,<br>List[int] size = [1, 5, 1024, 32]                | Unknown  |
| 833 | Tensor<[5, 1200, 300]> self = ?,<br>List[int] size = [1, 5, 1200, 300]              | Unknown  |
| 834 | Tensor<[5, 1200, 64]> self = ?,<br>List[int] size = [1, 5, 1200, 64]                | Unknown  |
| 835 | Tensor<[5, 3072]> self = ?,<br>List[int] size = [1, 5, 3072]                        | Unknown  |
| 836 | Tensor<[5, 4096]> self = ?,<br>List[int] size = [1, 5, 4096]                        | Unknown  |
| 837 | Tensor<[5, 51200]> self = ?,<br>List[int] size = [1, 5, 51200]                      | Unknown  |
| 838 | Tensor<[50, 1, 1024]> self = ?,<br>List[int] size = [50, 1024]                      | Unknown  |
| 839 | Tensor<[50, 1, 2304]> self = ?,<br>List[int] size = [50, 1, 3, 768]                 | Unknown  |
| 840 | Tensor<[50, 1, 3072]> self = ?,<br>List[int] size = [50, 1, 3, 1024]                | Unknown  |
| 841 | Tensor<[50, 1, 768]> self = ?,<br>List[int] size = [50, 768]                        | Unknown  |
| 842 | Tensor<[50, 1024]> self = ?,<br>List[int] size = [50, 1, 1024]                      | Unknown  |
| 843 | Tensor<[50, 2304]> self = ?,<br>List[int] size = [50, 1, 2304]                      | Unknown  |
| 844 | Tensor<[50, 3072]> self = ?,<br>List[int] size = [1, 50, 3072]                      | Unknown  |
| 845 | Tensor<[50, 3072]> self = ?,<br>List[int] size = [50, 1, 3072]                      | Unknown  |
| 846 | Tensor<[50, 4096]> self = ?,<br>List[int] size = [1, 50, 4096]                      | Unknown  |
| 847 | Tensor<[50, 768]> self = ?,<br>List[int] size = [1, 50, 768]                        | Unknown  |
| 848 | Tensor<[50, 768]> self = ?,<br>List[int] size = [50, 1, 768]                        | Unknown  |
| 849 | Tensor<[512]> self = ?,<br>List[int] size = [1, -1, 1, 1]                           | Unknown  |
| 850 | Tensor<[56, 56]> self = ?,<br>List[int] size = [8, 7, 8, 7]                         | Unknown  |
| 851 | Tensor<[6, 1, 100, 256]> self = ?,<br>List[int] size = [600, 256]                   | Unknown  |
| 852 | Tensor<[6, 1, 15]> self = ?,<br>List[int] size = [1, 6, 1, 15]                      | Unknown  |
| 853 | Tensor<[6, 1, 17]> self = ?,<br>List[int] size = [1, 6, 1, 17]                      | Unknown  |
| 854 | Tensor<[6, 1, 1]> self = ?,<br>List[int] size = [1, 6, 1, 1]                        | Unknown  |
| 855 | Tensor<[6, 1, 2]> self = ?,<br>List[int] size = [1, 6, 1, 2]                        | Unknown  |
| 856 | Tensor<[6, 1, 64]> self = ?,<br>List[int] size = [1, 6, 1, 64]                      | Unknown  |
| 857 | Tensor<[6, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 6, 1, sym_size_int]        | Unknown  |
| 858 | Tensor<[6, 15, 15]> self = ?,<br>List[int] size = [1, 6, 15, 15]                    | Unknown  |
| 859 | Tensor<[6, 15, 64]> self = ?,<br>List[int] size = [1, 6, 15, 64]                    | Unknown  |
| 860 | Tensor<[600, 256]> self = ?,<br>List[int] size = [6, 1, 100, 256]                   | Unknown  |
| 861 | Tensor<[600, 4]> self = ?,<br>List[int] size = [6, 1, 100, 4]                       | Unknown  |
| 862 | Tensor<[600, 92]> self = ?,<br>List[int] size = [6, 1, 100, 92]                     | Unknown  |
| 863 | Tensor<[64, 1024]> self = ?,<br>List[int] size = [1, 8, 8, 1024]                    | Unknown  |
| 864 | Tensor<[64, 2304]> self = ?,<br>List[int] size = [1, 64, 2304]                      | Unknown  |
| 865 | Tensor<[64, 3, 49, 49]> self = ?,<br>List[int] size = [192, 49, 49]                 | Unknown  |
| 866 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int] size = [192, 64, 64]                 | Unknown  |
| 867 | Tensor<[64, 3072]> self = ?,<br>List[int] size = [1, 64, 3072]                      | Unknown  |
| 868 | Tensor<[64, 3072]> self = ?,<br>List[int] size = [1, 8, 8, 3072]                    | Unknown  |
| 869 | Tensor<[64, 4, 49, 49]> self = ?,<br>List[int] size = [256, 49, 49]                 | Unknown  |
| 870 | Tensor<[64, 4, 64, 64]> self = ?,<br>List[int] size = [256, 64, 64]                 | Unknown  |
| 871 | Tensor<[64, 4096]> self = ?,<br>List[int] size = [1, 8, 8, 4096]                    | Unknown  |
| 872 | Tensor<[64, 49, 128]> self = ?,<br>List[int] size = [3136, 128]                     | Unknown  |
| 873 | Tensor<[64, 49, 288]> self = ?,<br>List[int] size = [64, 49, 3, 3, 32]              | Unknown  |
| 874 | Tensor<[64, 49, 32]> self = ?,<br>List[int] size = [4, 16, 49, 32]                  | Unknown  |
| 875 | Tensor<[64, 49, 384]> self = ?,<br>List[int] size = [64, 49, 3, 4, 32]              | Unknown  |
| 876 | Tensor<[64, 49, 49]> self = ?,<br>List[int] size = [4, 16, 49, 49]                  | Unknown  |
| 877 | Tensor<[64, 49, 96]> self = ?,<br>List[int] size = [3136, 96]                       | Unknown  |
| 878 | Tensor<[64, 64, 128]> self = ?,<br>List[int] size = [4096, 128]                     | Unknown  |
| 879 | Tensor<[64, 64, 288]> self = ?,<br>List[int] size = [64, 64, 3, 3, 32]              | Unknown  |
| 880 | Tensor<[64, 64, 32]> self = ?,<br>List[int] size = [4, 16, 64, 32]                  | Unknown  |
| 881 | Tensor<[64, 64, 384]> self = ?,<br>List[int] size = [64, 64, 3, 4, 32]              | Unknown  |
| 882 | Tensor<[64, 64, 64]> self = ?,<br>List[int] size = [4, 16, 64, 64]                  | Unknown  |
| 883 | Tensor<[64, 64, 96]> self = ?,<br>List[int] size = [4096, 96]                       | Unknown  |
| 884 | Tensor<[64, 64]> self = ?,<br>List[int] size = [8, 8, 8, 8]                         | Unknown  |
| 885 | Tensor<[64, 768]> self = ?,<br>List[int] size = [1, 8, 8, 768]                      | Unknown  |
| 886 | Tensor<[64, 9, 64]> self = ?,<br>List[int] size = [1, 64, 9, 64]                    | Unknown  |
| 887 | Tensor<[64, 9, 9]> self = ?,<br>List[int] size = [1, 64, 9, 9]                      | Unknown  |
| 888 | Tensor<[64]> self = ?,<br>List[int] size = [1, -1, 1, 1]                            | Unknown  |
| 889 | Tensor<[7, 18176]> self = ?,<br>List[int] size = [1, 7, 18176]                      | Unknown  |
| 890 | Tensor<[7, 2304]> self = ?,<br>List[int] size = [1, 7, 2304]                        | Unknown  |
| 891 | Tensor<[7, 2]> self = ?,<br>List[int] size = [1, 7, 2]                              | Unknown  |
| 892 | Tensor<[7, 3072]> self = ?,<br>List[int] size = [1, 7, 3072]                        | Unknown  |
| 893 | Tensor<[7, 4544]> self = ?,<br>List[int] size = [1, 7, 4544]                        | Unknown  |
| 894 | Tensor<[7, 4672]> self = ?,<br>List[int] size = [1, 7, 4672]                        | Unknown  |
| 895 | Tensor<[7, 65024]> self = ?,<br>List[int] size = [1, 7, 65024]                      | Unknown  |
| 896 | Tensor<[71, 7, 7]> self = ?,<br>List[int] size = [1, 71, 7, 7]                      | Unknown  |
| 897 | Tensor<[768, 384]> self = ?,<br>List[int] size = [1, 768, 384]                      | Unknown  |
| 898 | Tensor<[784, 1024]> self = ?,<br>List[int] size = [1, 28, 28, 1024]                 | Unknown  |
| 899 | Tensor<[784, 192]> self = ?,<br>List[int] size = [1, 28, 28, 192]                   | Unknown  |
| 900 | Tensor<[784, 256]> self = ?,<br>List[int] size = [1, 28, 28, 256]                   | Unknown  |
| 901 | Tensor<[784, 576]> self = ?,<br>List[int] size = [16, 49, 576]                      | Unknown  |
| 902 | Tensor<[784, 768]> self = ?,<br>List[int] size = [1, 28, 28, 768]                   | Unknown  |
| 903 | Tensor<[784, 768]> self = ?,<br>List[int] size = [16, 49, 768]                      | Unknown  |
| 904 | Tensor<[8, 1, 10]> self = ?,<br>List[int] size = [1, 8, 1, 10]                      | Unknown  |
| 905 | Tensor<[8, 1, 1]> self = ?,<br>List[int] size = [1, 8, 1, 1]                        | Unknown  |
| 906 | Tensor<[8, 1, 2]> self = ?,<br>List[int] size = [1, 8, 1, 2]                        | Unknown  |
| 907 | Tensor<[8, 1, 64]> self = ?,<br>List[int] size = [1, 8, 1, 64]                      | Unknown  |
| 908 | Tensor<[8, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 8, 1, sym_size_int]        | Unknown  |
| 909 | Tensor<[8, 10, 10]> self = ?,<br>List[int] size = [1, 8, 10, 10]                    | Unknown  |
| 910 | Tensor<[8, 10, 64]> self = ?,<br>List[int] size = [1, 8, 10, 64]                    | Unknown  |
| 911 | Tensor<[8, 2048, 256]> self = ?,<br>List[int] size = [1, 8, 2048, 256]              | Unknown  |
| 912 | Tensor<[8, 2048, 96]> self = ?,<br>List[int] size = [1, 8, 2048, 96]                | Unknown  |
| 913 | Tensor<[8, 256, 160]> self = ?,<br>List[int] size = [1, 8, 256, 160]                | Unknown  |
| 914 | Tensor<[8, 256, 2048]> self = ?,<br>List[int] size = [1, 8, 256, 2048]              | Unknown  |
| 915 | Tensor<[8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]                | Unknown  |
| 916 | Tensor<[8, 256, 32]> self = ?,<br>List[int] size = [1, 8, 256, 32]                  | Unknown  |
| 917 | Tensor<[8, 300, 300]> self = ?,<br>List[int] size = [1, 8, 300, 300]                | Unknown  |
| 918 | Tensor<[8, 300, 64]> self = ?,<br>List[int] size = [1, 8, 300, 64]                  | Unknown  |
| 919 | Tensor<[8732, 1, 4]> self = ?,<br>List[int] size = [8732, 4]                        | Unknown  |
| 920 | Tensor<[9, 1024]> self = ?,<br>List[int] size = [1, 9, 1024]                        | Unknown  |
| 921 | Tensor<[9, 128]> self = ?,<br>List[int] size = [1, 9, 128]                          | Unknown  |
| 922 | Tensor<[9, 16384]> self = ?,<br>List[int] size = [1, 9, 16384]                      | Unknown  |
| 923 | Tensor<[9, 2048]> self = ?,<br>List[int] size = [1, 9, 2048]                        | Unknown  |
| 924 | Tensor<[9, 30000]> self = ?,<br>List[int] size = [1, 9, 30000]                      | Unknown  |
| 925 | Tensor<[9, 3072]> self = ?,<br>List[int] size = [1, 9, 3072]                        | Unknown  |
| 926 | Tensor<[9, 4096]> self = ?,<br>List[int] size = [1, 9, 4096]                        | Unknown  |
| 927 | Tensor<[9, 4]> self = ?,<br>List[int] size = [1, -1, 4]                             | Unknown  |
| 928 | Tensor<[9, 768]> self = ?,<br>List[int] size = [1, 9, 768]                          | Unknown  |
| 929 | Tensor<[9, 8192]> self = ?,<br>List[int] size = [1, 9, 8192]                        | Unknown  |
| 930 | Tensor<[920, 1, 2048]> self = ?,<br>List[int] size = [920, 2048]                    | Unknown  |
| 931 | Tensor<[920, 1, 256]> self = ?,<br>List[int] size = [920, 256]                      | Unknown  |
| 932 | Tensor<[920, 2048]> self = ?,<br>List[int] size = [920, 1, 2048]                    | Unknown  |
| 933 | Tensor<[920, 256]> self = ?,<br>List[int] size = [920, 1, 256]                      | Unknown  |
| 934 | Tensor<[96, 49, 32]> self = ?,<br>List[int] size = [16, 6, 49, 32]                  | Unknown  |
| 935 | Tensor<[96, 49, 49]> self = ?,<br>List[int] size = [16, 6, 49, 49]                  | Unknown  |
| 936 | Tensor<[96, 64, 32]> self = ?,<br>List[int] size = [16, 6, 64, 32]                  | Unknown  |
| 937 | Tensor<[96, 64, 64]> self = ?,<br>List[int] size = [16, 6, 64, 64]                  | Unknown  |
| 938 | Tensor<[s0, 256]> self = ?,<br>List[int] size = [1, arg10_1, 256]                   | Unknown  |
| 939 | Tensor<[s0, 768]> self = ?,<br>List[int] size = [1, sym_size_int_1, 768]            | Unknown  |
### aten.where.self
|    | ATen Input Variations                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 256]> condition = ?,<br>Tensor<[1, 1, 256]> self = ?,<br>Tensor<[]> other = ?        | Unknown  |
|  1 | Tensor<[1, 1, 45, 45]> condition = ?,<br>Tensor<[1, 12, 45, 45]> self = ?,<br>Tensor<[]> other = ? | Unknown  |
|  2 | Tensor<[1, 1, 5, 5]> condition = ?,<br>Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[]> other = ?     | Unknown  |
|  3 | Tensor<[1, 1, 7, 7]> condition = ?,<br>Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[]> other = ?     | Unknown  |
|  4 | Tensor<[10, 10]> condition = ?,<br>Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?        | Unknown  |
|  5 | Tensor<[15, 15]> condition = ?,<br>Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?        | Unknown  |
### aten.zeros.default
|    | ATen Input Variations                                                                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int] size = [1, 12, 1, 10],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False    | Unknown  |
|  1 | List[int] size = [1, 16, 1, 10],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False    | Unknown  |
|  2 | List[int] size = [1, 3, 720, 1280],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
|  3 | List[int] size = [1, 6, 1, 15],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False     | Unknown  |
|  4 | List[int] size = [1, 8, 1, 10],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False     | Unknown  |
### aten.zeros_like.default
|    | ATen Input Variations                                                                                                                 | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1]> self = ?,<br>Optional[bool] pin_memory = False                                                                         | Unknown  |
|  1 | Tensor<[1, 8]> self = ?,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
|  2 | Tensor<[1, 920]> self = ?,<br>Optional[int] dtype = torch.float32,<br>Optional[bool] pin_memory = False                               | Unknown  |
|  3 | Tensor<[100, 1, 256]> self = ?,<br>Optional[bool] pin_memory = False                                                                  | Unknown  |
|  4 | Tensor<[13685]> self = ?,<br>Optional[int] dtype = torch.bool,<br>Optional[bool] pin_memory = False                                   | Unknown  |
|  5 | Tensor<[7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                      | Unknown  |

