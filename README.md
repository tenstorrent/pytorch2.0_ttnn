[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/tenstorrent/pytorch2.0_ttnn)

# PyTorch 2.0 TTNN Compiler
The PyTorch 2.0 TT-NN Compiler enables seamless execution of PyTorch models on [Tenstorrent](https://tenstorrent.com/) AI accelerators. 
By leveraging the TT-NN backend, you can achieve significant performance improvements while maintaining PyTorch's familiar API.

## 🚀 Quick Start

### Installation

Install from repo:
```bash
pip install git+https://bitbucket.org/tenstorrent/pytorch2.0_ttnn
```
or as editable package from source:
```bash
git clone https://github.com/tenstorrent/pytorch2.0_ttnn.git
cd pytorch2.0_ttnn
pip install -e .
```

### ✨ Basic Usage

**Option 1: Eager Mode:** get your model running by switching to TT device
```python
import torch
import torch_ttnn

model = YourModel()

device = ttnn.open_device(device_id=0)
model.to(torch_ttnn.ttnn_device_as_torch_device(device))

output = model(input_data)
```

**Option 2: Compilation Mode (Recommended):** get more perf with JIT compiler
```python
import torch
import torch_ttnn

model = YourModel()

device = ttnn.open_mesh_device(ttnn.MeshShape(1, 2))  # 1x2 device grid
option = torch_ttnn.TorchTtnnOption(device=device, data_parallel=2)

model = torch.compile(model, backend=torch_ttnn.backend, options=option)
output = model(input_data)
```

## 📊 Model Support

We've extensively tested the compiler across a diverse range of model architectures. Here's a summary of our validation results:


| Model                                                                                                | Status   | Torch Ops Before (Unique Ops)   | Torch Ops Remain (Unique Ops)   | To/From Device Ops   |   Original Run Time (ms) | Compiled Run Time for 5th Iteration (ms)   | Accuracy (%)   |
|:-----------------------------------------------------------------------------------------------------|:---------|:--------------------------------|:--------------------------------|:---------------------|-------------------------:|:-------------------------------------------|:---------------|
| [Autoencoder (linear)](<docs/models/Autoencoder (linear)>)                                           | ✅       | 22 (3)                          | 0 (0)                           | 0                    |           1336.64        | 1.7                                        | 100.0          |
| [BERT](<docs/models/BERT>)                                                                           | ✅       | 1393 (21)                       | 0 (0)                           | 0                    |          99721.4         | 52.06                                      | 99.53          |
| [DPR](<docs/models/DPR>)                                                                             | ✅       | 720 (22)                        | 0 (0)                           | 1                    |           2784.91        | 11.85                                      | 99.38          |
| [HardNet](<docs/models/HardNet>)                                                                     | ✅       | 245 (10)                        | 0 (0)                           | 124                  |           5159.7         | 32.36                                      | 98.41          |
| [Llama](<docs/models/Llama>)                                                                         | ✅       | 40 (11)                         | 0 (0)                           | 2                    |         168416           | 131290.23                                  | 100.0          |
| [MLPMixer](<docs/models/MLPMixer>)                                                                   | ✅       | 253 (11)                        | 0 (0)                           | 0                    |           6256.99        | 13.07                                      | 99.99          |
| [Mnist](<docs/models/Mnist>)                                                                         | ✅       | 14 (8)                          | 0 (0)                           | 1                    |             28.87        | 2.41                                       | 99.42          |
| [MobileNetV2](<docs/models/MobileNetV2>)                                                             | ✅       | 154 (9)                         | 0 (0)                           | 0                    |           1395.96        | 23.88                                      | 99.09          |
| [OpenPose V2](<docs/models/OpenPose V2>)                                                             | ✅       | 155 (7)                         | 0 (0)                           | 6                    |           3039.35        | 31.58                                      | 91.49          |
| [Perceiver IO](<docs/models/Perceiver IO>)                                                           | ✅       | 1531 (20)                       | 0 (0)                           | 1                    |          42429.7         | 49.85                                      | 99.95          |
| [ResNet18](<docs/models/ResNet18>)                                                                   | ✅       | 70 (9)                          | 0 (0)                           | 1                    |           2274.26        | 10.24                                      | 98.88          |
| [ResNet50](<docs/models/ResNet50>)                                                                   | ✅       | 176 (9)                         | 0 (0)                           | 1                    |           4290.54        | 24.41                                      | 98.61          |
| [RoBERTa](<docs/models/RoBERTa>)                                                                     | ✅       | 719 (21)                        | 0 (0)                           | 3                    |          12311.8         | 50.27                                      | 7.19           |
| [SqueezeBERT](<docs/models/SqueezeBERT>)                                                             | ✅       | 16 (9)                          | 0 (0)                           | 3                    |           1031.12        | 263.96                                     | 100.0          |
| [U-Net](<docs/models/U-Net>)                                                                         | ✅       | 68 (6)                          | 0 (0)                           | 12                   |          65136.5         | 13.69                                      | 100.0          |
| [Unet-brain](<docs/models/Unet-brain>)                                                               | ✅       | 68 (6)                          | 0 (0)                           | 12                   |          68679.2         | 12.59                                      | N/A            |
| [Unet-carvana](<docs/models/Unet-carvana>)                                                           | ✅       | 67 (5)                          | 0 (0)                           | 12                   |          84355.7         | 38.3                                       | 99.69          |
| [YOLOv5](<docs/models/YOLOv5>)                                                                       | ✅       | 3 (3)                           | 0 (0)                           | 0                    |          14127.1         | 11520.33                                   | 99.98          |
| [albert/albert-base-v2](<docs/models/albert/albert-base-v2>)                                         | ✅       | 791 (21)                        | 0 (0)                           | 3                    |           1066.42        | 17.64                                      | 98.82          |
| [albert/albert-base-v2-classification](<docs/models/albert/albert-base-v2-classification>)           | ✅       | 779 (21)                        | 0 (0)                           | 2                    |           1232.89        | 14.61                                      | 99.97          |
| [albert/albert-large-v2](<docs/models/albert/albert-large-v2>)                                       | ✅       | 1547 (21)                       | 0 (0)                           | 3                    |           2716.11        | 32.75                                      | 98.95          |
| [albert/albert-xlarge-v2](<docs/models/albert/albert-xlarge-v2>)                                     | ✅       | 1547 (21)                       | 0 (0)                           | 3                    |           7853.48        | 77.57                                      | 97.36          |
| [densenet121](<docs/models/densenet121>)                                                             | ✅       | 432 (10)                        | 0 (0)                           | 597                  |           2865.48        | 55.96                                      | 99.74          |
| [densenet161](<docs/models/densenet161>)                                                             | ✅       | 572 (10)                        | 0 (0)                           | 1147                 |           7734.74        | 73.11                                      | 99.49          |
| [densenet169](<docs/models/densenet169>)                                                             | ✅       | 600 (10)                        | 0 (0)                           | 1241                 |           3855.75        | 81.79                                      | 99.59          |
| [distilbert-base-uncased](<docs/models/distilbert-base-uncased>)                                     | ✅       | 361 (16)                        | 0 (0)                           | 1                    |           1528.61        | 9.02                                       | 99.9           |
| [dla34.in1k](<docs/models/dla34.in1k>)                                                               | ✅       | 135 (9)                         | 0 (0)                           | 23                   |           3470.81        | 18.62                                      | 99.5           |
| [ese_vovnet19b_dw.ra_in1k](<docs/models/ese_vovnet19b_dw.ra_in1k>)                                   | ✅       | 111 (12)                        | 0 (0)                           | 19                   |           1711.81        | 17.52                                      | 99.44          |
| [ghostnet_100.in1k](<docs/models/ghostnet_100.in1k>)                                                 | ✅       | 515 (14)                        | 0 (0)                           | 64                   |           1092.8         | 41.86                                      | 99.6           |
| [mobilenet_v2](<docs/models/mobilenet_v2>)                                                           | ✅       | 154 (9)                         | 0 (0)                           | 0                    |            762.64        | 22.37                                      | 99.09          |
| [mobilenet_v3_large](<docs/models/mobilenet_v3_large>)                                               | ✅       | 188 (11)                        | 0 (0)                           | 0                    |            756.05        | 25.58                                      | 99.15          |
| [mobilenet_v3_small](<docs/models/mobilenet_v3_small>)                                               | ✅       | 158 (11)                        | 0 (0)                           | 0                    |            873.22        | 19.35                                      | 99.09          |
| [mobilenetv1_100.ra4_e3600_r224_in1k](<docs/models/mobilenetv1_100.ra4_e3600_r224_in1k>)             | ✅       | 85 (7)                          | 0 (0)                           | 0                    |            928.95        | 15.3                                       | 96.04          |
| [regnet_x_16gf](<docs/models/regnet_x_16gf>)                                                         | ✅       | 235 (8)                         | 0 (0)                           | 0                    |          14877.7         | 75.02                                      | 99.59          |
| [regnet_x_1_6gf](<docs/models/regnet_x_1_6gf>)                                                       | ✅       | 195 (8)                         | 0 (0)                           | 0                    |           2724.59        | 24.47                                      | 99.47          |
| [regnet_x_32gf](<docs/models/regnet_x_32gf>)                                                         | ✅       | 245 (8)                         | 0 (0)                           | 0                    |          28350.4         | 123.84                                     | 99.27          |
| [regnet_x_3_2gf](<docs/models/regnet_x_3_2gf>)                                                       | ✅       | 265 (8)                         | 0 (0)                           | 0                    |           3631.42        | 35.58                                      | 99.5           |
| [regnet_x_400mf](<docs/models/regnet_x_400mf>)                                                       | ✅       | 235 (8)                         | 0 (0)                           | 0                    |           1179.5         | 24.15                                      | 99.66          |
| [regnet_x_800mf](<docs/models/regnet_x_800mf>)                                                       | ✅       | 175 (8)                         | 0 (0)                           | 0                    |           1125.32        | 19.91                                      | 99.44          |
| [regnet_x_8gf](<docs/models/regnet_x_8gf>)                                                           | ✅       | 245 (8)                         | 0 (0)                           | 0                    |           7730.42        | 51.33                                      | 98.99          |
| [regnet_y_16gf](<docs/models/regnet_y_16gf>)                                                         | ✅       | 303 (10)                        | 0 (0)                           | 0                    |          15705.6         | 87.87                                      | 99.66          |
| [regnet_y_1_6gf](<docs/models/regnet_y_1_6gf>)                                                       | ✅       | 447 (10)                        | 0 (0)                           | 0                    |           2186.49        | 44.33                                      | 99.69          |
| [regnet_y_32gf](<docs/models/regnet_y_32gf>)                                                         | ✅       | 335 (10)                        | 0 (0)                           | 0                    |          32273.3         | 128.02                                     | 99.72          |
| [regnet_y_3_2gf](<docs/models/regnet_y_3_2gf>)                                                       | ✅       | 351 (10)                        | 0 (0)                           | 0                    |           3121.33        | 41.06                                      | 99.82          |
| [regnet_y_400mf](<docs/models/regnet_y_400mf>)                                                       | ✅       | 271 (10)                        | 0 (0)                           | 0                    |            815.77        | 26.15                                      | 99.64          |
| [regnet_y_800mf](<docs/models/regnet_y_800mf>)                                                       | ✅       | 239 (10)                        | 0 (0)                           | 0                    |           1111.83        | 25.24                                      | 99.59          |
| [regnet_y_8gf](<docs/models/regnet_y_8gf>)                                                           | ✅       | 287 (10)                        | 0 (0)                           | 0                    |           7839.36        | 57.33                                      | 99.83          |
| [resnet101](<docs/models/resnet101>)                                                                 | ✅       | 346 (9)                         | 0 (0)                           | 1                    |           7479.01        | 37.91                                      | 99.25          |
| [resnet152](<docs/models/resnet152>)                                                                 | ✅       | 516 (9)                         | 0 (0)                           | 1                    |          11338.5         | 67.09                                      | 99.09          |
| [resnet18](<docs/models/resnet18>)                                                                   | ✅       | 70 (9)                          | 0 (0)                           | 1                    |           2270.94        | 9.28                                       | 99.61          |
| [resnet34](<docs/models/resnet34>)                                                                   | ✅       | 126 (9)                         | 0 (0)                           | 1                    |           4593.89        | 16.09                                      | 99.07          |
| [resnet50](<docs/models/resnet50>)                                                                   | ✅       | 176 (9)                         | 0 (0)                           | 1                    |           4273.99        | 20.02                                      | 98.61          |
| [resnext101_32x8d](<docs/models/resnext101_32x8d>)                                                   | ✅       | 346 (9)                         | 0 (0)                           | 1                    |          15796.1         | 120.17                                     | 99.57          |
| [resnext101_64x4d](<docs/models/resnext101_64x4d>)                                                   | ✅       | 346 (9)                         | 0 (0)                           | 1                    |          15101.6         | 112.5                                      | 99.65          |
| [resnext50_32x4d](<docs/models/resnext50_32x4d>)                                                     | ✅       | 176 (9)                         | 0 (0)                           | 1                    |           4504.99        | 28.52                                      | 99.44          |
| [textattack/albert-base-v2-imdb](<docs/models/textattack/albert-base-v2-imdb>)                       | ✅       | 782 (22)                        | 0 (0)                           | 2                    |           1116.61        | 13.7                                       | 100.0          |
| [tf_efficientnet_lite0.in1k](<docs/models/tf_efficientnet_lite0.in1k>)                               | ✅       | 149 (9)                         | 0 (0)                           | 5                    |            912.22        | 34.02                                      | 99.3           |
| [tf_efficientnet_lite1.in1k](<docs/models/tf_efficientnet_lite1.in1k>)                               | ✅       | 194 (9)                         | 0 (0)                           | 5                    |           1207.83        | 46.04                                      | 99.56          |
| [tf_efficientnet_lite2.in1k](<docs/models/tf_efficientnet_lite2.in1k>)                               | ✅       | 194 (9)                         | 0 (0)                           | 5                    |           1967.21        | 76.78                                      | 99.21          |
| [twmkn9/albert-base-v2-squad2](<docs/models/twmkn9/albert-base-v2-squad2>)                           | ✅       | 783 (23)                        | 0 (0)                           | 2                    |           1332.62        | 15.31                                      | 99.86          |
| [vgg11](<docs/models/vgg11>)                                                                         | ✅       | 33 (8)                          | 0 (0)                           | 5                    |          11570.4         | 13.32                                      | 99.65          |
| [vgg11_bn](<docs/models/vgg11_bn>)                                                                   | ✅       | 41 (9)                          | 0 (0)                           | 5                    |          12294.8         | 14.31                                      | 98.99          |
| [vgg13](<docs/models/vgg13>)                                                                         | ✅       | 37 (8)                          | 0 (0)                           | 5                    |          18909.4         | 16.32                                      | 99.38          |
| [vgg13_bn](<docs/models/vgg13_bn>)                                                                   | ✅       | 47 (9)                          | 0 (0)                           | 5                    |          16392.8         | 16.57                                      | 97.35          |
| [vgg16](<docs/models/vgg16>)                                                                         | ✅       | 43 (8)                          | 0 (0)                           | 5                    |          25390.3         | 19.41                                      | 99.44          |
| [vgg16_bn](<docs/models/vgg16_bn>)                                                                   | ✅       | 56 (9)                          | 0 (0)                           | 5                    |          22065.8         | 20.9                                       | 98.38          |
| [vgg19](<docs/models/vgg19>)                                                                         | ✅       | 49 (8)                          | 0 (0)                           | 5                    |          26182.7         | 23.51                                      | 99.27          |
| [vgg19_bn](<docs/models/vgg19_bn>)                                                                   | ✅       | 65 (9)                          | 0 (0)                           | 5                    |          23790.4         | 25.37                                      | 96.97          |
| [wide_resnet101_2](<docs/models/wide_resnet101_2>)                                                   | ✅       | 346 (9)                         | 0 (0)                           | 1                    |          22229.7         | 54.31                                      | 99.2           |
| [wide_resnet50_2](<docs/models/wide_resnet50_2>)                                                     | ✅       | 176 (9)                         | 0 (0)                           | 1                    |          12618           | 29.78                                      | 98.8           |
| [xception71.tf_in1k](<docs/models/xception71.tf_in1k>)                                               | ✅       | 393 (9)                         | 0 (0)                           | 0                    |          18032.5         | 241.53                                     | 99.21          |
| [Autoencoder (conv)](<docs/models/Autoencoder (conv)>)                                               | 🚧       | 9 (3)                           | 1 (1)                           | 1                    |           1321.18        | 2.82                                       | 100.0          |
| [Autoencoder (conv)-train](<docs/models/Autoencoder (conv)-train>)                                   | 🚧       | 24 (7)                          | 11 (4)                          | 0                    |           2350.66        | 6.32                                       | 100.0          |
| [Autoencoder (linear)-train](<docs/models/Autoencoder (linear)-train>)                               | 🚧       | 104 (8)                         | 14 (2)                          | 0                    |           2797.37        | 15.75                                      | 100.0          |
| [Bloom](<docs/models/Bloom>)                                                                         | 🚧       | 1405 (27)                       | 2 (2)                           | 0                    |          29591           | 1139.22                                    | 98.86          |
| [CLIP](<docs/models/CLIP>)                                                                           | 🚧       | 1397 (30)                       | 7 (6)                           | 2                    |           5578.87        | 140.03                                     | 99.56          |
| [CLIP-train](<docs/models/CLIP-train>)                                                               | 🚧       | 3944 (44)                       | 265 (16)                        | 5                    |          22379.5         | 1856.09                                    | 100.0          |
| [DETR](<docs/models/DETR>)                                                                           | 🚧       | 1663 (42)                       | 9 (6)                           | 3                    |          92799.2         | 4806.6                                     | 41.86          |
| [DINOv2](<docs/models/DINOv2>)                                                                       | 🚧       | 928 (25)                        | 16 (1)                          | 2                    |          16363.8         | 78.62                                      | 98.99          |
| [Falcon](<docs/models/Falcon>)                                                                       | 🚧       | 94 (15)                         | 5 (5)                           | 3                    |          72186.2         | 35800.07                                   | 100.0          |
| [GLPN-KITTI](<docs/models/GLPN-KITTI>)                                                               | 🚧       | 2959 (26)                       | 22 (2)                          | 6                    |         121875           | 59246.22                                   | 99.75          |
| [GPT-2](<docs/models/GPT-2>)                                                                         | 🚧       | 745 (29)                        | 2 (2)                           | 2                    |           2530.42        | 27.6                                       | 99.98          |
| [HardNet-train](<docs/models/HardNet-train>)                                                         | 🚧       | 867 (21)                        | 412 (9)                         | 120                  |          15664.5         | 10898.06                                   | 100.0          |
| [MLPMixer-train](<docs/models/MLPMixer-train>)                                                       | 🚧       | 616 (19)                        | 100 (5)                         | 0                    |          16977.5         | 8215.47                                    | 100.0          |
| [Mnist-train](<docs/models/Mnist-train>)                                                             | 🚧       | 46 (15)                         | 10 (6)                          | 0                    |           2872.17        | 45.38                                      | 100.0          |
| [MobileNetSSD](<docs/models/MobileNetSSD>)                                                           | 🚧       | 447 (28)                        | 5 (2)                           | 32                   |            870.9         | 2309.94                                    | 38.39          |
| [OpenPose V2-train](<docs/models/OpenPose V2-train>)                                                 | 🚧       | 523 (14)                        | 246 (7)                         | 6                    |          10749.6         | 8063.89                                    | 100.0          |
| [ResNet18-train](<docs/models/ResNet18-train>)                                                       | 🚧       | 241 (19)                        | 121 (9)                         | 0                    |           5241.88        | 3720.44                                    | 100.0          |
| [ResNet50-train](<docs/models/ResNet50-train>)                                                       | 🚧       | 616 (19)                        | 318 (9)                         | 0                    |          14362           | 11212.6                                    | 100.0          |
| [SegFormer](<docs/models/SegFormer>)                                                                 | 🚧       | 676 (22)                        | 16 (1)                          | 4                    |          40369           | 367.61                                     | 99.85          |
| [SegFormer-train](<docs/models/SegFormer-train>)                                                     | 🚧       | 1794 (36)                       | 156 (12)                        | 4                    |          78032.1         | 34308.44                                   | 100.0          |
| [Stable Diffusion V2](<docs/models/Stable Diffusion V2>)                                             | 🚧       | 29 (14)                         | 11 (5)                          | 4                    |              1.85046e+06 | 1835719.59                                 | 99.97          |
| [U-Net-train](<docs/models/U-Net-train>)                                                             | 🚧       | 236 (15)                        | 122 (8)                         | 8                    |         113635           | 48359.31                                   | 100.0          |
| [Unet-brain-train](<docs/models/Unet-brain-train>)                                                   | 🚧       | 236 (15)                        | 122 (8)                         | 8                    |         108974           | 48786.05                                   | 100.0          |
| [Unet-carvana-train](<docs/models/Unet-carvana-train>)                                               | 🚧       | 232 (13)                        | 121 (7)                         | 8                    |         172538           | 89658.62                                   | 100.0          |
| [ViLT](<docs/models/ViLT>)                                                                           | 🚧       | 42 (16)                         | 5 (4)                           | 3                    |          16004.5         | 14065.2                                    | 87.94          |
| [YOLOS](<docs/models/YOLOS>)                                                                         | 🚧       | 952 (27)                        | 17 (2)                          | 2                    |          12579.8         | 249.95                                     | 98.6           |
| [YOLOv3](<docs/models/YOLOv3>)                                                                       | 🚧       | 250 (7)                         | 2 (1)                           | 4                    |         162687           | 62.0                                       | 98.63          |
| [albert/albert-xxlarge-v2](<docs/models/albert/albert-xxlarge-v2>)                                   | 🚧       | 791 (21)                        | 24 (1)                          | 3                    |          15803.3         | 151.31                                     | 98.54          |
| [dla34.in1k-train](<docs/models/dla34.in1k-train>)                                                   | 🚧       | 469 (18)                        | 230 (8)                         | 17                   |           9795.35        | 7048.7                                     | 100.0          |
| [ese_vovnet19b_dw.ra_in1k-train](<docs/models/ese_vovnet19b_dw.ra_in1k-train>)                       | 🚧       | 383 (25)                        | 176 (10)                        | 16                   |           5351.33        | 3481.36                                    | 100.0          |
| [facebook/deit-base-patch16-224](<docs/models/facebook/deit-base-patch16-224>)                       | 🚧       | 685 (17)                        | 1 (1)                           | 1                    |          13002           | 118.41                                     | 98.34          |
| [facebook/deit-base-patch16-224-train](<docs/models/facebook/deit-base-patch16-224-train>)           | 🚧       | 1854 (27)                       | 127 (8)                         | 2                    |          74542.7         | 1614.34                                    | 100.0          |
| [ghostnet_100.in1k-train](<docs/models/ghostnet_100.in1k-train>)                                     | 🚧       | 1469 (33)                       | 562 (12)                        | 64                   |           1187.73        | 1971.57                                    | 100.0          |
| [ghostnetv2_100.in1k](<docs/models/ghostnetv2_100.in1k>)                                             | 🚧       | 683 (18)                        | 24 (2)                          | 68                   |            994.86        | 124.97                                     | 99.65          |
| [ghostnetv2_100.in1k-train](<docs/models/ghostnetv2_100.in1k-train>)                                 | 🚧       | 2001 (39)                       | 852 (17)                        | 68                   |           1837.57        | 4012.56                                    | 100.0          |
| [googlenet](<docs/models/googlenet>)                                                                 | 🚧       | 214 (15)                        | 1 (1)                           | 51                   |           2017.89        | 30.35                                      | 99.67          |
| [hrnet_w18.ms_aug_in1k](<docs/models/hrnet_w18.ms_aug_in1k>)                                         | 🚧       | 1209 (11)                       | 31 (1)                          | 0                    |           5194.37        | 180.31                                     | 99.62          |
| [hrnet_w18.ms_aug_in1k-train](<docs/models/hrnet_w18.ms_aug_in1k-train>)                             | 🚧       | 3998 (21)                       | 1973 (9)                        | 0                    |          12519.5         | 9052.43                                    | 100.0          |
| [inception_v4.tf_in1k](<docs/models/inception_v4.tf_in1k>)                                           | 🚧       | 495 (11)                        | 14 (1)                          | 84                   |          11986.3         | 175.14                                     | 99.11          |
| [inception_v4.tf_in1k-train](<docs/models/inception_v4.tf_in1k-train>)                               | 🚧       | 1851 (24)                       | 932 (11)                        | 80                   |          32510.2         | 22379.87                                   | 100.0          |
| [mixer_b16_224.goog_in21k](<docs/models/mixer_b16_224.goog_in21k>)                                   | 🚧       | 356 (11)                        | 1 (1)                           | 0                    |          11903.2         | 104.85                                     | 3.65           |
| [mixer_b16_224.goog_in21k-train](<docs/models/mixer_b16_224.goog_in21k-train>)                       | 🚧       | 959 (18)                        | 101 (6)                         | 0                    |          54735.7         | 1489.7                                     | 100.0          |
| [mobilenetv1_100.ra4_e3600_r224_in1k-train](<docs/models/mobilenetv1_100.ra4_e3600_r224_in1k-train>) | 🚧       | 258 (16)                        | 164 (7)                         | 0                    |           2574.36        | 2236.05                                    | 100.0          |
| [regnet_y_128gf](<docs/models/regnet_y_128gf>)                                                       | 🚧       | 447 (10)                        | 3 (1)                           | 0                    |         507626           | 61594.77                                   | 98.91          |
| [ssd300_vgg16](<docs/models/ssd300_vgg16>)                                                           | 🚧       | 251 (26)                        | 6 (3)                           | 37                   |           3254.4         | 1129.81                                    | N/A            |
| [ssdlite320_mobilenet_v3_large](<docs/models/ssdlite320_mobilenet_v3_large>)                         | 🚧       | 447 (28)                        | 5 (2)                           | 32                   |            610.53        | 1687.32                                    | 46.25          |
| [swin_b](<docs/models/swin_b>)                                                                       | 🚧       | 2492 (32)                       | 110 (2)                         | 479                  |          12677.8         | 234.5                                      | 92.77          |
| [swin_s](<docs/models/swin_s>)                                                                       | 🚧       | 2492 (32)                       | 110 (2)                         | 479                  |           7329.24        | 215.82                                     | 91.71          |
| [swin_t](<docs/models/swin_t>)                                                                       | 🚧       | 1238 (32)                       | 50 (2)                          | 227                  |           3948           | 123.49                                     | 96.62          |
| [swin_v2_b](<docs/models/swin_v2_b>)                                                                 | 🚧       | 3140 (40)                       | 158 (3)                         | 473                  |          15806.9         | 327.93                                     | 10.81          |
| [swin_v2_s](<docs/models/swin_v2_s>)                                                                 | 🚧       | 3140 (40)                       | 158 (3)                         | 473                  |           9167.18        | 308.14                                     | 31.41          |
| [swin_v2_t](<docs/models/swin_v2_t>)                                                                 | 🚧       | 1562 (40)                       | 74 (3)                          | 221                  |           5044.32        | 174.77                                     | 44.1           |
| [tf_efficientnet_lite0.in1k-train](<docs/models/tf_efficientnet_lite0.in1k-train>)                   | 🚧       | 452 (17)                        | 285 (8)                         | 5                    |           2577.18        | 8244.54                                    | 100.0          |
| [tf_efficientnet_lite1.in1k-train](<docs/models/tf_efficientnet_lite1.in1k-train>)                   | 🚧       | 587 (17)                        | 370 (8)                         | 5                    |           3617.92        | 7678.4                                     | 100.0          |
| [tf_efficientnet_lite2.in1k-train](<docs/models/tf_efficientnet_lite2.in1k-train>)                   | 🚧       | 587 (17)                        | 370 (8)                         | 5                    |           3727.14        | 10083.2                                    | 100.0          |
| [tf_efficientnet_lite3.in1k](<docs/models/tf_efficientnet_lite3.in1k>)                               | 🚧       | 221 (9)                         | 5 (1)                           | 5                    |           2429.91        | 282.23                                     | 99.15          |
| [tf_efficientnet_lite3.in1k-train](<docs/models/tf_efficientnet_lite3.in1k-train>)                   | 🚧       | 668 (17)                        | 426 (9)                         | 5                    |           6132.59        | 14446.03                                   | 100.0          |
| [tf_efficientnet_lite4.in1k](<docs/models/tf_efficientnet_lite4.in1k>)                               | 🚧       | 275 (9)                         | 6 (1)                           | 5                    |           5058.67        | 475.87                                     | 99.21          |
| [tf_efficientnet_lite4.in1k-train](<docs/models/tf_efficientnet_lite4.in1k-train>)                   | 🚧       | 830 (17)                        | 529 (9)                         | 5                    |          14761.5         | 26256.86                                   | 100.0          |
| [vit_b_16](<docs/models/vit_b_16>)                                                                   | 🚧       | 552 (17)                        | 1 (1)                           | 1                    |          12867.1         | 154.04                                     | 99.54          |
| [vit_b_32](<docs/models/vit_b_32>)                                                                   | 🚧       | 552 (17)                        | 1 (1)                           | 1                    |           4687.08        | 137.01                                     | 98.68          |
| [vit_h_14](<docs/models/vit_h_14>)                                                                   | 🚧       | 1452 (17)                       | 1 (1)                           | 1                    |         777760           | 2703.45                                    | 98.59          |
| [vit_l_16](<docs/models/vit_l_16>)                                                                   | 🚧       | 1092 (17)                       | 1 (1)                           | 1                    |          43692.2         | 271.29                                     | 99.74          |
| [vit_l_32](<docs/models/vit_l_32>)                                                                   | 🚧       | 1092 (17)                       | 1 (1)                           | 1                    |          18575           | 241.75                                     | 98.97          |
| [xception71.tf_in1k-train](<docs/models/xception71.tf_in1k-train>)                                   | 🚧       | 1378 (18)                       | 806 (7)                         | 0                    |          57994.1         | 58516.46                                   | 100.0          |
| [FLAN-T5](<docs/models/FLAN-T5>)                                                                     | ❌       | 20020 (38)                      | N/A                             | N/A                  |           3565.74        | N/A                                        | N/A            |
| [GPTNeo](<docs/models/GPTNeo>)                                                                       | ❌       | 2733 (35)                       | N/A                             | N/A                  |          15124.4         | N/A                                        | N/A            |
| [OPT](<docs/models/OPT>)                                                                             | ❌       | 4003 (32)                       | N/A                             | N/A                  |          21135.5         | N/A                                        | N/A            |
| [Whisper](<docs/models/Whisper>)                                                                     | ❌       | 4310 (21)                       | N/A                             | N/A                  |         199347           | N/A                                        | N/A            |
| [codegen](<docs/models/codegen>)                                                                     | ❌       | 9183 (37)                       | N/A                             | N/A                  |           6372.68        | N/A                                        | N/A            |
| [densenet201](<docs/models/densenet201>)                                                             | ❌       | 712 (10)                        | N/A                             | N/A                  |           4337.26        | N/A                                        | N/A            |
| [speecht5-tts](<docs/models/speecht5-tts>)                                                           | ❌       | 6942 (40)                       | N/A                             | N/A                  |          49254.3         | N/A                                        | N/A            |
| [t5-base](<docs/models/t5-base>)                                                                     | ❌       | 14681 (38)                      | N/A                             | N/A                  |           5568.21        | N/A                                        | N/A            |
| [t5-large](<docs/models/t5-large>)                                                                   | ❌       | 22696 (38)                      | N/A                             | N/A                  |          13454.6         | N/A                                        | N/A            |
| [t5-small](<docs/models/t5-small>)                                                                   | ❌       | 6118 (38)                       | N/A                             | N/A                  |           2774.1         | N/A                                        | N/A            |

### Explanation of Metrics

**Model**: Name of the model.  
**Status**: Indicates whether the model is ❌ traced / 🚧 compiled / ✅ E2E on device.  
**Torch Ops Before (Unique Ops)**: The total number of operations used by the model in the original Torch implementation. The number in parenthesis represents the total unique ops.  
**Torch Ops Remain (Unique Ops)**: The total number of operations used after conversion to TTNN. The number in parenthesis represents the total unique ops.  
**To/From Device Ops**: The number of `to/from_device` operations (data transfer to/from the device).  
**Original Run Time (ms)**: Execution time (in seconds) of the model before conversion.  
**Compiled Run Time for 5th Iteration (ms)**: Execution time (in seconds) of the model after conversion for the 5th iteration.  
**Accuracy (%)**: Model accuracy on a predefined test dataset after conversion.  

***

# Contributing

Whether you are new to Tenstorrent hardware or an experienced developer, there are many ways to contribute.

## Getting Started

Start with our high level [Contribution guide](docs/Contributing.md).
You can find more information here:
* [Discussions](https://github.com/tenstorrent/pytorch2.0_ttnn/discussions)
* [Operations Report](docs/OperationsReport.md)
* [Lowering TT-NN Operation to PyTorch](docs/AddNewOperationLowering.md)
* [Native Device Integration Extesion](docs/OpenRegistrationAPI.md)
* [Build with Metal from Sources](docs/DevelopWithMetalFromSources.md)
* [Known Issues](docs/KnownIssues.md)
* [Problem Solving](docs/ProblemSolving.md)

We encourage contributions and offer [🤑 Bounties](https://github.com/tenstorrent/pytorch2.0_ttnn/issues?q=is%3Aissue%20state%3Aopen%20label%3Abounty) for some issues.

## Development Environment

To get started with development, you'll need Wormhole or Blackhole Tenstorrent accelerator card
* can be ordered on [Tenstorrent website](https://tenstorrent.com/) 
* can be requested on [Koyeb](https://www.koyeb.com/blog/tenstorrent-cloud-instances-unveiling-next-gen-ai-accelerators)

Install the development dependencies:
```shell
pip install -r requirements-dev.txt
pip install -e .
```

You can build the wheel file with
```shell
python -m build
```

## Project Structure

- `torch_ttnn/`: Main package directory containing the core implementation
- `tests/`: Test files for the project including models suits. We use `pytest` as our testing framework.
- `tools/`: Development and utility scripts
- `docs/`: Project documentation and reports
- `demo/`: Example code and usage demonstrations

## Questions and Support

If you have questions or need help getting started, please:
1. Review the existing documentation
2. Ask [PyTorch TT-NN DeepWiki](https://deepwiki.com/tenstorrent/pytorch2.0_ttnn) or [TT-Metal DeepWiki](https://deepwiki.com/tenstorrent/tt_metal)
3. Ask on [Discord](https://discord.gg/tenstorrent)
4. Open an issue on GitHub