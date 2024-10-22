from torchvision import models, transforms
from PIL import Image
import torch
import requests
import pytest
from tests.utils import ModelTester


class ThisTester(ModelTester):
    # pass model_info instead of model_name
    def __init__(self, model_info, mode):
        if mode not in ["train", "eval"]:
            raise ValueError(f"Current mode is not supported: {mode}")
        self.model_info = model_info
        self.mode = mode
        self.model = self._load_model()
        self.inputs = self._load_inputs()

    def _load_model(self):
        model_name, weights_name = self.model_info
        self.weights = getattr(models, weights_name).DEFAULT
        model = models.get_model(model_name, weights=self.weights)
        return model

    def _load_inputs(self):
        preprocess = self.weights.transforms()
        # Load and preprocess the image
        url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        image = Image.open(requests.get(url, stream=True).raw)
        img_t = preprocess(image)
        batch_t = torch.unsqueeze(img_t, 0)
        return batch_t


model_info_list = [
    ("googlenet", "GoogLeNet_Weights"),
    ("densenet121", "DenseNet121_Weights"),
    ("densenet161", "DenseNet161_Weights"),
    ("densenet169", "DenseNet169_Weights"),
    ("densenet201", "DenseNet201_Weights"),
    ("mobilenet_v2", "MobileNet_V2_Weights"),
    ("mobilenet_v3_small", "MobileNet_V3_Small_Weights"),
    ("mobilenet_v3_large", "MobileNet_V3_Large_Weights"),
    ("resnet18", "ResNet18_Weights"),
    ("resnet34", "ResNet34_Weights"),
    ("resnet50", "ResNet50_Weights"),
    ("resnet101", "ResNet101_Weights"),
    ("resnet152", "ResNet152_Weights"),
    ("resnext50_32x4d", "ResNeXt50_32X4D_Weights"),
    ("resnext101_32x8d", "ResNeXt101_32X8D_Weights"),
    ("resnext101_64x4d", "ResNeXt101_64X4D_Weights"),
    ("vgg11", "VGG11_Weights"),
    ("vgg11_bn", "VGG11_BN_Weights"),
    ("vgg13", "VGG13_Weights"),
    ("vgg13_bn", "VGG13_BN_Weights"),
    ("vgg16", "VGG16_Weights"),
    ("vgg16_bn", "VGG16_BN_Weights"),
    ("vgg19", "VGG19_Weights"),
    ("vgg19_bn", "VGG19_BN_Weights"),
    ("vit_b_16", "ViT_B_16_Weights"),
    ("vit_b_32", "ViT_B_32_Weights"),
    ("vit_l_16", "ViT_L_16_Weights"),
    ("vit_l_32", "ViT_L_32_Weights"),
    ("vit_h_14", "ViT_H_14_Weights"),
    ("wide_resnet50_2", "Wide_ResNet50_2_Weights"),
    ("wide_resnet101_2", "Wide_ResNet101_2_Weights"),
    ("regnet_y_400mf", "RegNet_Y_400MF_Weights"),
    ("regnet_y_800mf", "RegNet_Y_800MF_Weights"),
    ("regnet_y_1_6gf", "RegNet_Y_1_6GF_Weights"),
    ("regnet_y_3_2gf", "RegNet_Y_3_2GF_Weights"),
    ("regnet_y_8gf", "RegNet_Y_8GF_Weights"),
    ("regnet_y_16gf", "RegNet_Y_16GF_Weights"),
    ("regnet_y_32gf", "RegNet_Y_32GF_Weights"),
    ("regnet_y_128gf", "RegNet_Y_128GF_Weights"),
    ("regnet_x_400mf", "RegNet_X_400MF_Weights"),
    ("regnet_x_800mf", "RegNet_X_800MF_Weights"),
    ("regnet_x_1_6gf", "RegNet_X_1_6GF_Weights"),
    ("regnet_x_3_2gf", "RegNet_X_3_2GF_Weights"),
    ("regnet_x_8gf", "RegNet_X_8GF_Weights"),
    ("regnet_x_16gf", "RegNet_X_16GF_Weights"),
    ("regnet_x_32gf", "RegNet_X_32GF_Weights"),
    ("swin_t", "Swin_T_Weights"),
    ("swin_s", "Swin_S_Weights"),
    ("swin_b", "Swin_B_Weights"),
    ("swin_v2_t", "Swin_V2_T_Weights"),
    ("swin_v2_s", "Swin_V2_S_Weights"),
    ("swin_v2_b", "Swin_V2_B_Weights"),
]
mode_list = ["eval"]

model_info_and_mode_list = []

for model_info in model_info_list:
    for mode in mode_list:
        model_name = model_info[0]
        if (
            model_name == "vit_b_16"
            or model_name == "vit_b_32"
            or model_name == "vit_h_14"
            or model_name == "vit_l_16"
            or model_name == "vit_l_32"
        ):
            model_info_and_mode_list.append([model_info, mode])
        else:
            model_info_and_mode_list.append(pytest.param([model_info, mode], marks=pytest.mark.compilation_xfail))


@pytest.mark.parametrize("model_info_and_mode", model_info_and_mode_list)
def test_torchvision_image_classification(record_property, model_info_and_mode):
    model_info = model_info_and_mode[0]
    mode = model_info_and_mode[1]
    model_name, _ = model_info
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_info, mode)
    results = tester.test_model()
    if mode == "eval":
        # Print the top 5 predictions
        _, indices = torch.topk(results, 5)
        print(f"Model: {model_name} | Top 5 predictions: {indices[0].tolist()}")

    record_property("torch_ttnn", (tester, results))
