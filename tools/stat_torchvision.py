import os
import argparse
import torch
import torchvision
import torch_stat

def stat_model(model_name: str, input_shapes: list, out_path, source: str = "torchvision", backward = True):
    if source == "torchvision":
        try:
            m = torchvision.models.get_model(model_name, pretrained=True)
        except Exception as e:
            print(e)
            try:
                m = torchvision.models.get_model(model_name, pretrained=False)
            except Exception as e:
                print(e)
                print("Skip this model")
                return
    elif source == "torch.hub.dinov2":
        m = torch.hub.load('facebookresearch/dinov2', model_name)
    else:
        assert(0 and "unsupport source")
    if backward:
        m.train()
    else:
        m.eval()
    option = torch_stat.TorchStatOption(model_name = model_name, out = out_path, gen_graphviz=False)
    m = torch.compile(m, backend=torch_stat.backend(option, backward = backward))
    inputs = torch.rand(input_shapes)
    result = m(inputs)
    if backward:
        result.backward(torch.ones_like(result))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out_path", type = str, default = os.path.join(os.getcwd(),"stat"))
    parser.add_argument("--input_shapes", type = int, nargs='+', default = [1,3,224,224])
    args = parser.parse_args()
    out_path = args.out_path
    input_shapes = args.input_shapes

    stat_model("dinov2_vits14", input_shapes, out_path, "torch.hub.dinov2")
    for m in ["alexnet", "googlenet", "resnet18", "vgg11"]:
        stat_model(m, input_shapes, out_path, backward = True)
