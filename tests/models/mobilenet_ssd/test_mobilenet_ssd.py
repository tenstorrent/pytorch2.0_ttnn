# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
# Reference: https://pytorch.org/vision/stable/models/generated/torchvision.models.detection.ssdlite320_mobilenet_v3_large.html
# Image URL from: https://github.com/tenstorrent/tt-buda-demos/blob/main/model_demos/cv_demos/mobilenet_ssd/tflite_mobilenet_v2_ssd_1x1.py

import torchvision
import torch
from PIL import Image
from torchvision import transforms
import requests
import pytest
from tests.utils import ModelTester
from collections import OrderedDict
import ttnn
import torch_ttnn


class BaseModel(torch.nn.Module):
    def __init__(self, backbone, head, anchor_generator=None, postprocess=None):
        super().__init__()
        self.backbone = backbone
        self.head = head
        self.anchor_generator = anchor_generator
        self.postprocess = postprocess

    def forward(self, inputs):
        features = self.backbone(inputs.tensors)
        if isinstance(features, torch.Tensor):
            features = OrderedDict([("0", features)])
        features = list(features.values())
        head_outputs = self.head(features)
        anchors = self.anchor_generator(inputs, features)
        # detections = self.postprocess(head_outputs, anchors, inputs.image_sizes)
        return head_outputs, anchors


# TODO: RuntimeError: "nms_kernel" not implemented for 'BFloat16'
class ThisTester(ModelTester):
    def _load_model(self):
        self.full_model = torchvision.models.detection.ssdlite320_mobilenet_v3_large(
            weights=torchvision.models.detection.SSDLite320_MobileNet_V3_Large_Weights.DEFAULT
        )
        
        backbone = self.full_model.backbone
        head = self.full_model.head
        anchor_generator = self.full_model.anchor_generator
        # postprocess = self.full_model.postprocess_detections
        
        # model = BaseModel(backbone, head, anchor_generator) #, postprocess)
        
        return self.full_model  # .to(torch.bfloat16)

    def _load_inputs(self):
        # Image preprocessing
        image_url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        image = Image.open(requests.get(image_url, stream=True).raw)
        transform = transforms.Compose([transforms.Resize((320, 320)), transforms.ToTensor()])
        img_tensor = [transform(image).unsqueeze(0)]
        batch_tensor = torch.cat(img_tensor, dim=0)
        # model_transform = self.full_model.transform
        # batch_tensor, _ = model_transform(batch_tensor)
        # batch_tensor = batch_tensor
        return batch_tensor  # .to(torch.bfloat16)
    
    def set_postprocessing_steps(self, mode, outputs): 
        if mode != "eval":
            return
        batched_nms = torchvision.ops.boxes.batched_nms
        postprocessed_outputs = batched_nms(*outputs, self.model.nms_thresh)
        keep = keep[: self.detections_per_img]
        return keep
        
@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
def test_mobilenet_ssd(record_property, mode):
    model_name = "MobileNetSSD"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    record_property("torch_ttnn", (tester, results))
    
    
def trace_mobilenet_ssd():
    model_name = "MobileNetSSD"
    mode = "eval"
    tester = ThisTester(model_name, mode)
    model = tester.model.eval()
    inputs = tester.inputs
    
    from typing import List
    def custom_backend(gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor]):
        # print("custom backend called with FX graph:")
        # gm.graph.print_tabular()
        return gm.forward    
    
    torch._dynamo.reset()
    
    with torch.no_grad():
        opt_model = torch.compile(model)
        outputs = opt_model(inputs)[0]
    

def run_mobilenet_ssd():
    model_name = "MobileNetSSD"
    mode = "eval"
    
    image_url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    image = Image.open(requests.get(image_url, stream=True).raw)
    transform = transforms.Compose([transforms.Resize((320, 320)), transforms.ToTensor()])
    img_tensor = [transform(image).unsqueeze(0)]
    batch_tensor = torch.cat(img_tensor, dim=0)
    
    tester = ThisTester(model_name, mode)
    if mode == "eval":
        tester.set_model_eval(tester.model)
    with torch.no_grad():
        outputs = tester.run_model(tester.model, tester.inputs)
        
    print(outputs)
    
    
def compile_mobilenet_ssd():
    model_name = "MobileNetSSD"
    mode = "eval"
    tester = ThisTester(model_name, mode)
    model = tester.model.eval()
    inputs = tester.inputs
    
    from typing import List
    def custom_backend(gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor]):
        # print("custom backend called with FX graph:")
        # gm.graph.print_tabular()
        return gm.forward    
    
    torch._dynamo.reset()
    
    device = ttnn.open_device(device_id=0, l1_small_size=16384)
    option = torch_ttnn.TorchTtnnOption(device=device)
    
    with torch.no_grad():
        opt_model = torch.compile(model, backend=torch_ttnn.backend, options=option)
        outputs = opt_model(inputs)[0]
    
    ttnn.close_device(device)
    
if __name__ == "__main__":
    compile_mobilenet_ssd()

