[comment]: <> (This README.md was generated by tools/collect_metrics.py.)
[comment]: <> (Please modify docs/README.md.in and/or collect_metrics.py to make permanent changes.)

# PyTorch 2.0 TTNN Compiler
This project allows to run PyTorch code on [Tenstorrent](https://tenstorrent.com/) hardware.

## Supported Models

The table below summarizes the results of running various ML models through our TTNN compiler. For each model, we track whether the run was successful, the number of operations before and after conversion, the number of `to_device` and `from_device` operations, performance metrics, and accuracy.

| Model                                                                                    | Run Success   | Torch Ops Before (Unique Ops)   | Torch Ops Remain (Unique Ops)   | To/From Device Ops   |   Original Run Time (ms) | Compiled Run Time (ms)   | Accuracy (%)   |
|:-----------------------------------------------------------------------------------------|:--------------|:--------------------------------|:--------------------------------|:---------------------|-------------------------:|:-------------------------|:---------------|
| [Autoencoder (conv)](<docs/models/Autoencoder (conv)>)                                   | ✘             | 9 (3)                           | N/A                             | N/A                  |                  2142.78 | N/A                      | N/A            |
| [Autoencoder (linear)](<docs/models/Autoencoder (linear)>)                               | ✘             | 22 (3)                          | N/A                             | N/A                  |                  1504.47 | N/A                      | N/A            |
| [BERT](<docs/models/BERT>)                                                               | ✅            | 1393 (21)                       | 0 (0)                           | 513                  |                 72690.7  | 69480.14                 | 98.88          |
| [Bloom](<docs/models/Bloom>)                                                             | ✅            | 1407 (29)                       | 106 (8)                         | 657                  |                110322    | 77957.35                 | 41.09          |
| [CLIP](<docs/models/CLIP>)                                                               | ✘             | 1397 (30)                       | N/A                             | N/A                  |                 12861.4  | N/A                      | N/A            |
| [DETR](<docs/models/DETR>)                                                               | ✘             | 1685 (42)                       | N/A                             | N/A                  |                  3676.79 | N/A                      | N/A            |
| [DPR](<docs/models/DPR>)                                                                 | ✘             | 720 (22)                        | N/A                             | N/A                  |                  5004.51 | N/A                      | N/A            |
| [FLAN-T5](<docs/models/FLAN-T5>)                                                         | ✘             | 19680 (38)                      | N/A                             | N/A                  |                  4369.42 | N/A                      | N/A            |
| [Falcon](<docs/models/Falcon>)                                                           | ✘             | 2698 (30)                       | N/A                             | N/A                  |                165949    | N/A                      | N/A            |
| [GLPN-KITTI](<docs/models/GLPN-KITTI>)                                                   | ✘             | 3064 (30)                       | N/A                             | N/A                  |                  5450.72 | N/A                      | N/A            |
| [GPT-2](<docs/models/GPT-2>)                                                             | ✘             | 748 (31)                        | N/A                             | N/A                  |                  6581.17 | N/A                      | N/A            |
| [GPTNeo](<docs/models/GPTNeo>)                                                           | ✘             | 2652 (36)                       | N/A                             | N/A                  |                  9886.38 | N/A                      | N/A            |
| [Hand Landmark](<docs/models/Hand Landmark>)                                             | ✘             | N/A                             | N/A                             | N/A                  |                  8403.38 | N/A                      | N/A            |
| [HardNet](<docs/models/HardNet>)                                                         | ✅            | 245 (10)                        | 240 (5)                         | 3                    |                   984.43 | 21812.93                 | 99.99          |
| [Llama](<docs/models/Llama>)                                                             | ✅            | 104 (5)                         | 33 (2)                          | 35                   |                437990    | 166977.79                | 100.0          |
| [MLPMixer](<docs/models/MLPMixer>)                                                       | ✘             | 253 (11)                        | N/A                             | N/A                  |                   208.49 | N/A                      | N/A            |
| [Mnist (eval)](<docs/models/Mnist (eval)>)                                               | ✅            | 14 (8)                          | 3 (2)                           | 3                    |                    26.69 | 431.76                   | 99.42          |
| [Mnist (train)](<docs/models/Mnist (train)>)                                             | ✅            | 46 (15)                         | 20 (8)                          | 14                   |                  5919.84 | 10719.76                 | 91.62          |
| [MobileNetSSD](<docs/models/MobileNetSSD>)                                               | ✘             | 575 (34)                        | N/A                             | N/A                  |                   538.94 | N/A                      | N/A            |
| [MobileNetV2](<docs/models/MobileNetV2>)                                                 | ✘             | 154 (9)                         | N/A                             | N/A                  |                   594.79 | N/A                      | N/A            |
| [OPT](<docs/models/OPT>)                                                                 | ✘             | 4072 (32)                       | N/A                             | N/A                  |                 12108.5  | N/A                      | N/A            |
| [OpenPose](<docs/models/OpenPose>)                                                       | ✘             | 155 (7)                         | N/A                             | N/A                  |                  1210.26 | N/A                      | N/A            |
| [Perceiver IO](<docs/models/Perceiver IO>)                                               | ✘             | 1532 (21)                       | N/A                             | N/A                  |                  8814.58 | N/A                      | N/A            |
| [ResNet18](<docs/models/ResNet18>)                                                       | ✅            | 70 (9)                          | 41 (3)                          | 20                   |                  1967.27 | 12774.81                 | 99.99          |
| [ResNet50](<docs/models/ResNet50>)                                                       | ✅            | 176 (9)                         | 107 (3)                         | 52                   |                  4500.02 | 19619.02                 | 99.98          |
| [RoBERTa](<docs/models/RoBERTa>)                                                         | ✘             | 719 (21)                        | N/A                             | N/A                  |                 12970.3  | N/A                      | N/A            |
| [SegFormer](<docs/models/SegFormer>)                                                     | ✘             | 760 (27)                        | N/A                             | N/A                  |                  1883.07 | N/A                      | N/A            |
| [SqueezeBERT](<docs/models/SqueezeBERT>)                                                 | ✅            | 16 (9)                          | 4 (2)                           | 6                    |                  3259.59 | 9833.41                  | 100.0          |
| [Stable Diffusion](<docs/models/Stable Diffusion>)                                       | ✘             | 1762 (29)                       | N/A                             | N/A                  |                 49259.7  | N/A                      | N/A            |
| [U-Net](<docs/models/U-Net>)                                                             | ✘             | 86 (7)                          | N/A                             | N/A                  |                   881.39 | N/A                      | N/A            |
| [Unet-brain](<docs/models/Unet-brain>)                                                   | ✘             | 86 (7)                          | N/A                             | N/A                  |                   702.31 | N/A                      | N/A            |
| [Unet-carvana](<docs/models/Unet-carvana>)                                               | ✘             | 85 (6)                          | N/A                             | N/A                  |                   644.53 | N/A                      | N/A            |
| [ViLT](<docs/models/ViLT>)                                                               | ✘             | 781 (30)                        | N/A                             | N/A                  |                 17381.1  | N/A                      | N/A            |
| [Whisper](<docs/models/Whisper>)                                                         | ✘             | 4294 (19)                       | N/A                             | N/A                  |                 19325.4  | N/A                      | N/A            |
| [XGLM](<docs/models/XGLM>)                                                               | ✘             | 1458 (30)                       | N/A                             | N/A                  |                 14559.7  | N/A                      | N/A            |
| [YOLOS](<docs/models/YOLOS>)                                                             | ✅            | 964 (28)                        | 50 (8)                          | 328                  |                  1645.67 | 66643.93                 | 42.2           |
| [YOLOv3](<docs/models/YOLOv3>)                                                           | ✘             | 264 (10)                        | N/A                             | N/A                  |                 28767.5  | N/A                      | N/A            |
| [YOLOv5](<docs/models/YOLOv5>)                                                           | ✘             | 236 (13)                        | N/A                             | N/A                  |                 10733.3  | N/A                      | N/A            |
| [albert/albert-base-v2](<docs/models/albert/albert-base-v2>)                             | ✘             | 791 (21)                        | N/A                             | N/A                  |                  1999.25 | N/A                      | N/A            |
| [albert/albert-large-v2](<docs/models/albert/albert-large-v2>)                           | ✘             | 1547 (21)                       | N/A                             | N/A                  |                  2105.95 | N/A                      | N/A            |
| [albert/albert-xlarge-v2](<docs/models/albert/albert-xlarge-v2>)                         | ✘             | 1547 (21)                       | N/A                             | N/A                  |                  3917.06 | N/A                      | N/A            |
| [albert/albert-xxlarge-v2](<docs/models/albert/albert-xxlarge-v2>)                       | ✘             | 791 (21)                        | N/A                             | N/A                  |                  8753.58 | N/A                      | N/A            |
| [codegen](<docs/models/codegen>)                                                         | ✘             | 9114 (37)                       | N/A                             | N/A                  |                  9809.68 | N/A                      | N/A            |
| [densenet121](<docs/models/densenet121>)                                                 | ✘             | 432 (10)                        | N/A                             | N/A                  |                   581.17 | N/A                      | N/A            |
| [densenet161](<docs/models/densenet161>)                                                 | ✘             | 572 (10)                        | N/A                             | N/A                  |                  1208.75 | N/A                      | N/A            |
| [densenet169](<docs/models/densenet169>)                                                 | ✘             | 600 (10)                        | N/A                             | N/A                  |                   817.23 | N/A                      | N/A            |
| [densenet201](<docs/models/densenet201>)                                                 | ✘             | 712 (10)                        | N/A                             | N/A                  |                   947.82 | N/A                      | N/A            |
| [distilbert-base-uncased](<docs/models/distilbert-base-uncased>)                         | ✘             | 367 (17)                        | N/A                             | N/A                  |                  3155.62 | N/A                      | N/A            |
| [dla34.in1k](<docs/models/dla34.in1k>)                                                   | ✘             | 135 (9)                         | N/A                             | N/A                  |                  1239.98 | N/A                      | N/A            |
| [ese_vovnet19b_dw.ra_in1k](<docs/models/ese_vovnet19b_dw.ra_in1k>)                       | ✘             | 111 (12)                        | N/A                             | N/A                  |                  1159.23 | N/A                      | N/A            |
| [facebook/deit-base-patch16-224](<docs/models/facebook/deit-base-patch16-224>)           | ✅            | 685 (17)                        | 15 (4)                          | 282                  |                  3878.09 | 42943.87                 | 96.77          |
| [ghostnet_100.in1k](<docs/models/ghostnet_100.in1k>)                                     | ✘             | 515 (14)                        | N/A                             | N/A                  |                  1153.31 | N/A                      | N/A            |
| [ghostnetv2_100.in1k](<docs/models/ghostnetv2_100.in1k>)                                 | ✘             | 781 (20)                        | N/A                             | N/A                  |                  2542.39 | N/A                      | N/A            |
| [googlenet](<docs/models/googlenet>)                                                     | ✘             | 214 (15)                        | N/A                             | N/A                  |                   507.47 | N/A                      | N/A            |
| [hrnet_w18.ms_aug_in1k](<docs/models/hrnet_w18.ms_aug_in1k>)                             | ✘             | 1426 (14)                       | N/A                             | N/A                  |                  1603.43 | N/A                      | N/A            |
| [inception_v4.tf_in1k](<docs/models/inception_v4.tf_in1k>)                               | ✘             | 495 (11)                        | N/A                             | N/A                  |                  5342    | N/A                      | N/A            |
| [microsoft/beit-base-patch16-224](<docs/models/microsoft/beit-base-patch16-224>)         | ✘             | 793 (21)                        | N/A                             | N/A                  |                  3740.61 | N/A                      | N/A            |
| [microsoft/beit-large-patch16-224](<docs/models/microsoft/beit-large-patch16-224>)       | ✘             | 1573 (21)                       | N/A                             | N/A                  |                 45198.7  | N/A                      | N/A            |
| [mixer_b16_224.goog_in21k](<docs/models/mixer_b16_224.goog_in21k>)                       | ✅            | 356 (11)                        | 1 (1)                           | 198                  |                  3670.79 | 31897.24                 | 53.1           |
| [mobilenet_v2](<docs/models/mobilenet_v2>)                                               | ✘             | 154 (9)                         | N/A                             | N/A                  |                   409.57 | N/A                      | N/A            |
| [mobilenet_v3_large](<docs/models/mobilenet_v3_large>)                                   | ✘             | 188 (11)                        | N/A                             | N/A                  |                   436.14 | N/A                      | N/A            |
| [mobilenet_v3_small](<docs/models/mobilenet_v3_small>)                                   | ✘             | 158 (11)                        | N/A                             | N/A                  |                   362.97 | N/A                      | N/A            |
| [mobilenetv1_100.ra4_e3600_r224_in1k](<docs/models/mobilenetv1_100.ra4_e3600_r224_in1k>) | ✅            | 85 (7)                          | 81 (3)                          | 3                    |                   672.21 | 9043.34                  | 99.14          |
| [regnet_x_16gf](<docs/models/regnet_x_16gf>)                                             | ✘             | 235 (8)                         | N/A                             | N/A                  |                  1555.19 | N/A                      | N/A            |
| [regnet_x_1_6gf](<docs/models/regnet_x_1_6gf>)                                           | ✘             | 195 (8)                         | N/A                             | N/A                  |                   552.07 | N/A                      | N/A            |
| [regnet_x_32gf](<docs/models/regnet_x_32gf>)                                             | ✘             | 245 (8)                         | N/A                             | N/A                  |                  2527.94 | N/A                      | N/A            |
| [regnet_x_3_2gf](<docs/models/regnet_x_3_2gf>)                                           | ✘             | 265 (8)                         | N/A                             | N/A                  |                   695.91 | N/A                      | N/A            |
| [regnet_x_400mf](<docs/models/regnet_x_400mf>)                                           | ✘             | 235 (8)                         | N/A                             | N/A                  |                   720.08 | N/A                      | N/A            |
| [regnet_x_800mf](<docs/models/regnet_x_800mf>)                                           | ✘             | 175 (8)                         | N/A                             | N/A                  |                   473.95 | N/A                      | N/A            |
| [regnet_x_8gf](<docs/models/regnet_x_8gf>)                                               | ✘             | 245 (8)                         | N/A                             | N/A                  |                  1136.19 | N/A                      | N/A            |
| [regnet_y_128gf](<docs/models/regnet_y_128gf>)                                           | ✘             | 447 (10)                        | N/A                             | N/A                  |                 14999.3  | N/A                      | N/A            |
| [regnet_y_16gf](<docs/models/regnet_y_16gf>)                                             | ✘             | 303 (10)                        | N/A                             | N/A                  |                  2052.39 | N/A                      | N/A            |
| [regnet_y_1_6gf](<docs/models/regnet_y_1_6gf>)                                           | ✘             | 447 (10)                        | N/A                             | N/A                  |                   622.04 | N/A                      | N/A            |
| [regnet_y_32gf](<docs/models/regnet_y_32gf>)                                             | ✘             | 335 (10)                        | N/A                             | N/A                  |                  3812.85 | N/A                      | N/A            |
| [regnet_y_3_2gf](<docs/models/regnet_y_3_2gf>)                                           | ✘             | 351 (10)                        | N/A                             | N/A                  |                   748.51 | N/A                      | N/A            |
| [regnet_y_400mf](<docs/models/regnet_y_400mf>)                                           | ✘             | 271 (10)                        | N/A                             | N/A                  |                   417.59 | N/A                      | N/A            |
| [regnet_y_800mf](<docs/models/regnet_y_800mf>)                                           | ✘             | 239 (10)                        | N/A                             | N/A                  |                   476.41 | N/A                      | N/A            |
| [regnet_y_8gf](<docs/models/regnet_y_8gf>)                                               | ✘             | 287 (10)                        | N/A                             | N/A                  |                  1135.48 | N/A                      | N/A            |
| [resnet101](<docs/models/resnet101>)                                                     | ✘             | 346 (9)                         | N/A                             | N/A                  |                  1269.08 | N/A                      | N/A            |
| [resnet152](<docs/models/resnet152>)                                                     | ✘             | 516 (9)                         | N/A                             | N/A                  |                  1718.21 | N/A                      | N/A            |
| [resnet18](<docs/models/resnet18>)                                                       | ✘             | 70 (9)                          | N/A                             | N/A                  |                   554.24 | N/A                      | N/A            |
| [resnet34](<docs/models/resnet34>)                                                       | ✘             | 126 (9)                         | N/A                             | N/A                  |                   701.65 | N/A                      | N/A            |
| [resnet50](<docs/models/resnet50>)                                                       | ✘             | 176 (9)                         | N/A                             | N/A                  |                   832.92 | N/A                      | N/A            |
| [resnext101_32x8d](<docs/models/resnext101_32x8d>)                                       | ✘             | 346 (9)                         | N/A                             | N/A                  |                  2166.94 | N/A                      | N/A            |
| [resnext101_64x4d](<docs/models/resnext101_64x4d>)                                       | ✘             | 346 (9)                         | N/A                             | N/A                  |                  2051.97 | N/A                      | N/A            |
| [resnext50_32x4d](<docs/models/resnext50_32x4d>)                                         | ✘             | 176 (9)                         | N/A                             | N/A                  |                   840.9  | N/A                      | N/A            |
| [retinanet_resnet50_fpn](<docs/models/retinanet_resnet50_fpn>)                           | ✘             | 1107 (32)                       | N/A                             | N/A                  |                  2320.81 | N/A                      | N/A            |
| [retinanet_resnet50_fpn_v2](<docs/models/retinanet_resnet50_fpn_v2>)                     | ✘             | 617 (33)                        | N/A                             | N/A                  |                  1858.07 | N/A                      | N/A            |
| [speecht5-tts](<docs/models/speecht5-tts>)                                               | ✘             | 6940 (38)                       | N/A                             | N/A                  |                  9623.78 | N/A                      | N/A            |
| [ssd300_vgg16](<docs/models/ssd300_vgg16>)                                               | ✘             | 387 (32)                        | N/A                             | N/A                  |                  3194.93 | N/A                      | N/A            |
| [ssdlite320_mobilenet_v3_large](<docs/models/ssdlite320_mobilenet_v3_large>)             | ✘             | 575 (34)                        | N/A                             | N/A                  |                   609.96 | N/A                      | N/A            |
| [swin_b](<docs/models/swin_b>)                                                           | ✘             | 1898 (30)                       | N/A                             | N/A                  |                  2540.88 | N/A                      | N/A            |
| [swin_s](<docs/models/swin_s>)                                                           | ✘             | 1898 (30)                       | N/A                             | N/A                  |                  1580.92 | N/A                      | N/A            |
| [swin_t](<docs/models/swin_t>)                                                           | ✘             | 968 (30)                        | N/A                             | N/A                  |                  1022.99 | N/A                      | N/A            |
| [swin_v2_b](<docs/models/swin_v2_b>)                                                     | ✘             | 2474 (37)                       | N/A                             | N/A                  |                  2611.14 | N/A                      | N/A            |
| [swin_v2_s](<docs/models/swin_v2_s>)                                                     | ✘             | 2474 (37)                       | N/A                             | N/A                  |                  1759.15 | N/A                      | N/A            |
| [swin_v2_t](<docs/models/swin_v2_t>)                                                     | ✘             | 1256 (37)                       | N/A                             | N/A                  |                  1003.64 | N/A                      | N/A            |
| [t5-base](<docs/models/t5-base>)                                                         | ✘             | 13550 (38)                      | N/A                             | N/A                  |                  9187.18 | N/A                      | N/A            |
| [t5-large](<docs/models/t5-large>)                                                       | ✘             | 20891 (38)                      | N/A                             | N/A                  |                 26010.5  | N/A                      | N/A            |
| [t5-small](<docs/models/t5-small>)                                                       | ✘             | 5681 (38)                       | N/A                             | N/A                  |                  3642.91 | N/A                      | N/A            |
| [textattack/albert-base-v2-imdb](<docs/models/textattack/albert-base-v2-imdb>)           | ✘             | 782 (22)                        | N/A                             | N/A                  |                  3599.95 | N/A                      | N/A            |
| [tf_efficientnet_lite0.in1k](<docs/models/tf_efficientnet_lite0.in1k>)                   | ✘             | 149 (9)                         | N/A                             | N/A                  |                  1695.9  | N/A                      | N/A            |
| [tf_efficientnet_lite1.in1k](<docs/models/tf_efficientnet_lite1.in1k>)                   | ✘             | 194 (9)                         | N/A                             | N/A                  |                  1497.96 | N/A                      | N/A            |
| [tf_efficientnet_lite2.in1k](<docs/models/tf_efficientnet_lite2.in1k>)                   | ✘             | 194 (9)                         | N/A                             | N/A                  |                  2186.19 | N/A                      | N/A            |
| [tf_efficientnet_lite3.in1k](<docs/models/tf_efficientnet_lite3.in1k>)                   | ✘             | 221 (9)                         | N/A                             | N/A                  |                  2137.02 | N/A                      | N/A            |
| [tf_efficientnet_lite4.in1k](<docs/models/tf_efficientnet_lite4.in1k>)                   | ✘             | 275 (9)                         | N/A                             | N/A                  |                  3122.96 | N/A                      | N/A            |
| [twmkn9/albert-base-v2-squad2](<docs/models/twmkn9/albert-base-v2-squad2>)               | ✘             | 783 (23)                        | N/A                             | N/A                  |                  3124.04 | N/A                      | N/A            |
| [vgg11](<docs/models/vgg11>)                                                             | ✘             | 33 (8)                          | N/A                             | N/A                  |                  1767.72 | N/A                      | N/A            |
| [vgg11_bn](<docs/models/vgg11_bn>)                                                       | ✘             | 41 (9)                          | N/A                             | N/A                  |                  1815.12 | N/A                      | N/A            |
| [vgg13](<docs/models/vgg13>)                                                             | ✘             | 37 (8)                          | N/A                             | N/A                  |                  1834.45 | N/A                      | N/A            |
| [vgg13_bn](<docs/models/vgg13_bn>)                                                       | ✘             | 47 (9)                          | N/A                             | N/A                  |                  1714.86 | N/A                      | N/A            |
| [vgg16](<docs/models/vgg16>)                                                             | ✘             | 43 (8)                          | N/A                             | N/A                  |                  1897.49 | N/A                      | N/A            |
| [vgg16_bn](<docs/models/vgg16_bn>)                                                       | ✘             | 56 (9)                          | N/A                             | N/A                  |                  1922.27 | N/A                      | N/A            |
| [vgg19](<docs/models/vgg19>)                                                             | ✘             | 49 (8)                          | N/A                             | N/A                  |                  1968.67 | N/A                      | N/A            |
| [vgg19_bn](<docs/models/vgg19_bn>)                                                       | ✘             | 65 (9)                          | N/A                             | N/A                  |                  1970.22 | N/A                      | N/A            |
| [vit_b_16](<docs/models/vit_b_16>)                                                       | ✘             | 552 (17)                        | N/A                             | N/A                  |                  1925.7  | N/A                      | N/A            |
| [vit_b_32](<docs/models/vit_b_32>)                                                       | ✘             | 552 (17)                        | N/A                             | N/A                  |                  1810.93 | N/A                      | N/A            |
| [vit_h_14](<docs/models/vit_h_14>)                                                       | ✘             | 1452 (17)                       | N/A                             | N/A                  |                 15906.5  | N/A                      | N/A            |
| [vit_l_16](<docs/models/vit_l_16>)                                                       | ✘             | 1092 (17)                       | N/A                             | N/A                  |                  5647.89 | N/A                      | N/A            |
| [vit_l_32](<docs/models/vit_l_32>)                                                       | ✘             | 1092 (17)                       | N/A                             | N/A                  |                  5335.22 | N/A                      | N/A            |
| [wide_resnet101_2](<docs/models/wide_resnet101_2>)                                       | ✘             | 346 (9)                         | N/A                             | N/A                  |                  2736.89 | N/A                      | N/A            |
| [wide_resnet50_2](<docs/models/wide_resnet50_2>)                                         | ✘             | 176 (9)                         | N/A                             | N/A                  |                  1565.16 | N/A                      | N/A            |
| [xception71.tf_in1k](<docs/models/xception71.tf_in1k>)                                   | ✘             | 393 (9)                         | N/A                             | N/A                  |                  2451.16 | N/A                      | N/A            |

### Explanation of Metrics

**Model**: Name of the model.  
**Run Success**: Indicates whether the model runs successfully after conversion.  
**Torch Ops Before (Unique Ops)**: The total number of operations used by the model in the original Torch implementation. The number in parenthesis represents the total unique ops.  
**Torch Ops Remain (Unique Ops)**: The total number of operations used after conversion to TTNN. The number in parenthesis represents the total unique ops.  
**To/From Device Ops**: The number of `to/from_device` operations (data transfer to/from the device).  
**Original Run Time (ms)**: Execution time (in seconds) of the model before conversion.  
**Compiled Run Time (ms)**: Execution time (in seconds) of the model after conversion.  
**Accuracy (%)**: Model accuracy on a predefined test dataset after conversion.  

***

## Quickstart

The `torch_ttnn` module has a `backend` function, which can be used with the `torch.compile()`.

```python
import torch
import torch_ttnn

# A torch Module
class FooModule(torch.nn.Module):
    ...
# Create a module
module = FooModule()

# Compile the module, with ttnn backend
device = ttnn.open_device(device_id=0)
option = torch_ttnn.TorchTtnnOption(device=self.device)
ttnn_module = torch.compile(module, backend=torch_ttnn.backend, options=option)

# Running inference / training
ttnn_module(input_data)
```

## Tracer
The tracer dump the information of fx graph such as node's op_name and shape.

For example, you can run this script to parse the information
```
PYTHONPATH=$(pwd) python3 tools/stat_models.py --trace_orig --backward --profile
ls stat/raw
```

By default, the raw result will be stored at `stat/raw`, and you can run this script to generate the report
```
python3 tools/generate_report.py
ls stat/
```
Now the `stat/` folder have these report
 - `fw_node_count.csv`
 - `bw_node_count.csv`
 - `fw_total_input_size_dist/`
 - `bw_total_input_size_dist/`
 - `fw_total_output_size_dist/`
 - `bw_total_output_size_dist/`
 - `profile/`

The `node_count.csv` show the node with `op_type` appear in the fx graph. This report can help analyze the frequency of op type appear in the graph.

The `*_total_*_size_dist/` statistics the `op_type`'s input/output_size distribution from all fx graph recored in `stat/raw`. This report can help analyze the memory footprint durning the calculation of `op_type`.

 - Notice: the default `input_shapes` in `tools/stat_torchvision.py` is `[1,3,224,224]`, which has dependency with `*_total_*_size_dist/` report.

 - Notice: the [aten ir interface is in there](https://pytorch.org/docs/stable/torch.compiler_ir.html)

[The `profile/` is the tools provided by pytorch](https://pytorch.org/tutorials/recipes/recipes/profiler_recipe.html), you can open it by the url: chrome://tracing


# For developers

## Install torch-ttnn with editable mode

During development, you may want to use the torch-ttnn package for testing.
In order to do that, you can install the torch-ttnn package in "editable"
mode with

```shell
pip install -e .
```

Now, you can utilize `torch_ttnn` in your Python code. Any modifications you make to the `torch_ttnn` package will take effect immediately, eliminating the need for constant reinstallation via pip.

## Build wheel file

For developers want to deploy the wheel, you can build the wheel file with

```shell
python -m build
```

Then you can upload the `.whl` file to the PyPI (Python Package Index).

## Run transformer models
To run transformer model with ttnn backend, run:
```
PYTHONPATH="$TT_METAL_HOME:$(pwd)" python3 tools/run_transformers.py --model "phiyodr/bert-large-finetuned-squad2" --backend torch_ttnn
```

You can also substitute the backend with `torch_stat` to run a reference comparison.

# Add a model test
If you want to record run time metrics for a model or test, include a Pytest fixture named `record_property` as a parameter and set the "model_name" key.  
If you also want to compile the model with torch_ttnn backend, set the "torch_ttnn" key to a tuple in this order `(model, test_inputs, outputs)`. "model_name" still needs to be set. See the example code snippet below. `torch.nn.Module` models with `generate` method is supported.
```python
def Model(torch.nn.Module):
    def forward(self, x):
        # ...
        return outputs

# Add compilation_xfail marker if torch/CPU runs, but compiled version is xfail
@pytest.mark.compilation_xfail
# Add "record_property" parameter
def test_model_name(record_property):
    # Should be set as early as possible
    record_property("model_name", "Model Name")

    model = Model()
    # ...
    outputs = model(test_input)
    # outputs = model(**test_inputs) # dictionary inputs are also supported
    # ...

    # Can be set once all three objects for the tuple are defined
    record_property("torch_ttnn", (model, test_input(s), outputs))
```

If `model.generate(inputs)` is used, pass in `model.generate` instead of `model` to `record_property`.

