import torch
import torchvision
import os
import sys
import site

class Monodepth2_depth(torch.nn.Module):
    def __init__(self):
        super().__init__()
        home_dir = os.path.dirname(os.path.dirname(__file__))
        cache_dir = os.path.join(home_dir, ".cache")
        site.addsitedir(cache_dir)
        if not os.path.exists(cache_dir):
            os.mkdir(cache_dir)
        monodepth2_dir = os.path.join(cache_dir, "monodepth2")
        if not os.path.exists(monodepth2_dir):
            os.system(f"git clone https://github.com/nianticlabs/monodepth2.git {monodepth2_dir}")
            # Workaround: dynamo failed at these code in depth_decoder.py
            #     if i in self.scales:
            #         self.outputs[("disp", i)] = self.sigmoid(self.convs[("dispconv", i)](x))
            # disable it to pass the dynamo
            os.system(f"cp {home_dir}/tools/patches/depth_decoder.py {cache_dir}/monodepth2/networks/depth_decoder.py")
        site.addsitedir(monodepth2_dir)
        from monodepth2.utils import download_model_if_doesnt_exist
        from monodepth2 import networks
        download_model_if_doesnt_exist("mono+stereo_640x192")
        model_path = os.path.join("models", "mono+stereo_640x192")
        print("-> Loading model from ", model_path)
        encoder_path = os.path.join(model_path, "encoder.pth")
        depth_decoder_path = os.path.join(model_path, "depth.pth")
        # LOADING PRETRAINED MODEL
        print("   Loading pretrained encoder")
        encoder = networks.ResnetEncoder(18, False)
        device = torch.device("cpu")
        loaded_dict_enc = torch.load(encoder_path, map_location=device)
        # extract the height and width of image that this model was trained with
        feed_height = loaded_dict_enc['height']
        feed_width = loaded_dict_enc['width']
        filtered_dict_enc = {k: v for k, v in loaded_dict_enc.items() if k in encoder.state_dict()}
        encoder.load_state_dict(filtered_dict_enc)
        encoder.to(device)
        encoder.eval()
        self.encoder = encoder
        print("   Loading pretrained decoder")
        depth_decoder = networks.DepthDecoder(
            num_ch_enc=encoder.num_ch_enc, scales=range(4))

        loaded_dict = torch.load(depth_decoder_path, map_location=device)
        depth_decoder.load_state_dict(loaded_dict)

        depth_decoder.to(device)
        depth_decoder.eval()
        self.depth_decoder = depth_decoder

    def forward(self, input_image):
        features = self.encoder(input_image)
        outputs = self.depth_decoder(features)
        return outputs

def get_model_swimdi(model_name):
    if model_name == "monodepth2_depth":
        return Monodepth2_depth()
    if model_name == "deit":
        return torch.hub.load('facebookresearch/deit:main',
                              'deit_base_patch16_224',
                              pretrained=True)
    if model_name == "hardnet":
        print(f"If raise torch.cuda.is_available() is False \n\
Then you should edit the map_location: MAP_LOCATION = 'cpu' of load_state_dict_from_url in {torch.hub.__file__} \n\
def load_state_dict_from_url( \n\
    url: str,\n\
    model_dir: Optional[str] = None,\n\
    map_location: MAP_LOCATION = None <= change to 'cpu',\n\
    progress: bool = True,\n\
    check_hash: bool = False,\n\
    file_name: Optional[str] = None,\n\
    weights_only: bool = False,\n\
)")
        return torch.hub.load('PingoLH/Pytorch-HarDNet',
                              'hardnet68',
                               map_location=torch.device('cpu'),
                               pretrained=True)
    return None


def get_model_yoco(model_name):
    if model_name == "yolov8":
        from ultralytics import YOLO

        model = YOLO("yolov8n.pt")
        return model

    elif model_name == "yolov5":
        return torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)
    return None


def get_model(model_name):
    m = get_model_swimdi(model_name)
    if m is not None:
        return m
    m = get_model_yoco(model_name)
    if m is not None:
        return m

    if model_name == "dinov2_vits14":
        m = torch.hub.load("facebookresearch/dinov2", model_name)
    elif model_name == "detr_resnet50":
        m = torch.hub.load(
            "facebookresearch/detr:main", "detr_resnet50", pretrained=True
        )
    else:
        try:
            m = torchvision.models.get_model(model_name, pretrained=True)
        except Exception as e:
            print(e)
            try:
                m = torchvision.models.get_model(model_name, pretrained=False)
            except Exception as e:
                print(e)
                return None
    return m


def model_example_inputs_swimdi(model_name):
    return None


def model_example_inputs_yoco(model_name):
    if model_name == "yolov8":
        input_shapes = [1, 3, 224, 224]
        return [torch.rand(input_shapes)]
    elif model_name == "yolov5":
        input_shapes = [1, 3, 224, 224]
        return [torch.rand(input_shapes)]
    return None


def model_example_inputs(model_name, backward):
    torch.manual_seed(0)
    i = model_example_inputs_swimdi(model_name)
    if i is not None:
        return i
    i = model_example_inputs_yoco(model_name)
    if i is not None:
        return i

    if backward == False:
        if model_name in ["raft_small", "raft_large"]:
            input_shapes = [1, 3, 224, 224]
            return [torch.rand(input_shapes), torch.rand(input_shapes)]
        elif model_name in ["mvit_v1_b", "mvit_v2_s"]:
            input_shapes = [1, 3, 16, 224, 224]
        elif model_name in [
            "mc3_18",
            "r2plus1d_18",
            "r3d_18",
            "s3d",
            "swin3d_b",
            "swin3d_s",
            "swin3d_t",
        ]:
            input_shapes = [1, 3, 224, 224, 224]
        else:
            input_shapes = [1, 3, 224, 224]
        return [torch.rand(input_shapes)]
    else:
        if model_name in [
            "deeplabv3_mobilenet_v3_large",
            "deeplabv3_resnet101",
            "deeplabv3_resnet50",
        ]:
            # batch_size should > 1
            input_shapes = [2, 3, 224, 224]
        elif model_name in [
            "fasterrcnn_mobilenet_v3_large_320_fpn",
            "fasterrcnn_mobilenet_v3_large_fpn",
            "fasterrcnn_resnet50_fpn",
            "fasterrcnn_resnet50_fpn_v2",
            "fcos_resnet50_fpn",
            "keypointrcnn_resnet50_fpn",
            "maskrcnn_resnet50_fpn",
            "maskrcnn_resnet50_fpn_v2",
            "retinanet_resnet50_fpn",
            "retinanet_resnet50_fpn_v2",
            "ssd300_vgg16",
            "ssdlite320_mobilenet_v3_large",
        ]:
            batch_size = 2
            images, boxes = torch.rand(batch_size, 3, 224, 224), torch.rand(
                batch_size, 11, 4
            )
            boxes[:, :, 2:4] = boxes[:, :, 0:2] + boxes[:, :, 2:4]
            labels = torch.randint(1, 91, (batch_size, 11))
            images = list(image for image in images)
            if model_name in ["keypointrcnn_resnet50_fpn"]:
                labels = torch.randint(1, 2, (batch_size, 11))
            targets = []
            for i in range(len(images)):
                d = {}
                d["boxes"] = boxes[i]
                d["labels"] = labels[i]
                if model_name in ["keypointrcnn_resnet50_fpn"]:
                    d["keypoints"] = torch.zeros([11, 5, 3])
                if model_name in ["maskrcnn_resnet50_fpn", "maskrcnn_resnet50_fpn_v2"]:
                    d["masks"] = torch.zeros([11, 1, 1])
                targets.append(d)
            return [images, targets]
        elif model_name in ["inception_v3"]:
            input_shapes = [1, 3, 448, 448]
        elif model_name in ["raft_small", "raft_large"]:
            input_shapes = [1, 3, 224, 224]
            return [torch.rand(input_shapes), torch.rand(input_shapes)]
        elif model_name in ["mvit_v1_b", "mvit_v2_s"]:
            input_shapes = [1, 3, 16, 224, 224]
        elif model_name in [
            "mc3_18",
            "r2plus1d_18",
            "r3d_18",
            "s3d",
            "swin3d_b",
            "swin3d_s",
            "swin3d_t",
        ]:
            input_shapes = [1, 3, 224, 224, 224]
        else:
            input_shapes = [1, 3, 224, 224]
        return [torch.rand(input_shapes)]


def do_model_backward(model_name, result):
    if model_name in ["inception_v3"]:
        result.logits.backward(torch.ones_like(result.logits), retain_graph=True)
        result.aux_logits.backward(
            torch.ones_like(result.aux_logits), retain_graph=True
        )
    elif isinstance(result, dict):
        for k in result.keys():
            if model_name in [
                "detr_resnet50",
                "deeplabv3_mobilenet_v3_large",
                "deeplabv3_resnet101",
                "deeplabv3_resnet50",
                "fasterrcnn_mobilenet_v3_large_320_fpn",
                "fasterrcnn_mobilenet_v3_large_fpn",
                "fasterrcnn_resnet50_fpn",
                "fasterrcnn_resnet50_fpn_v2",
                "fcn_resnet101",
                "fcn_resnet50",
                "fcos_resnet50_fpn",
                "keypointrcnn_resnet50_fpn",
                "maskrcnn_resnet50_fpn",
                "maskrcnn_resnet50_fpn_v2",
                "retinanet_resnet50_fpn",
                "retinanet_resnet50_fpn_v2",
                "ssd300_vgg16",
                "ssdlite320_mobilenet_v3_large",
            ]:
                result[k].backward(torch.ones_like(result[k]), retain_graph=True)
            else:
                result[k].backward(torch.ones_like(result[k]))
    elif isinstance(result, list):
        for r in result:
            if model_name in ["raft_large", "raft_small"]:
                r.backward(torch.ones_like(r), retain_graph=True)
            else:
                r.backward(torch.ones_like(r))
    else:
        result.backward(torch.ones_like(result))
