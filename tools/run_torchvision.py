import os
import argparse
import torch
import torchvision

def get_ttnn_backend(model_name, trace_orig, trace_modi, backward, out_folder, graphviz, device):
    use_tracer = (trace_orig or trace_modi)
    if use_tracer:
        tracer_option = {
            "model_name": model_name,
            "out_folder": out_folder,
            "trace_orig": trace_orig,
            "trace_modi": trace_modi
        }
    else:
        tracer_option = None
    option = torch_ttnn.TorchTtnnOption(device=device, tracer_option = tracer_option)
    return torch_ttnn.backend(option)

def get_dummy_backend(model_name, trace_orig, trace_modi, backward, out_folder):
    from torch._dynamo.backends.common import aot_autograd
    def dummy_backend(gm, example_inputs):
        return gm
    def dummy_backend_with_tracer(out_prefix):
        from torch_ttnn.tracer import Tracer
        return Tracer(dummy_backend, out_prefix = out_prefix, out_folder = out_folder, \
                      trace_orig = trace_orig, trace_modi = trace_modi)
    use_tracer = (trace_orig or trace_modi)
    if not use_tracer and not backward:
        return aot_autograd(fw_compiler = dummy_backend)
    elif not use_tracer and backward:
        return aot_autograd(fw_compiler = dummy_backend, bw_compiler = dummy_backend)
    elif use_tracer and not backward:
        return aot_autograd(fw_compiler = dummy_backend_with_tracer(f"fw_{model_name}"))
    elif use_tracer and backward:
        return aot_autograd(fw_compiler = dummy_backend_with_tracer(f"fw_{model_name}"),
                            bw_compiler = dummy_backend_with_tracer(f"bw_{model_name}"))


def run_model(model_name: str, do_compile: bool, trace_orig: bool, trace_modi, \
              backward: bool, out_folder: str, graphviz: bool, to_profile: bool, device = None):
    if model_name == "dinov2_vits14":
        m = torch.hub.load('facebookresearch/dinov2', model_name)
    else:
        try:
            m = torchvision.models.get_model(model_name, pretrained=True)
        except Exception as e:
            print(e)
            try:
                m = torchvision.models.get_model(model_name, pretrained=False)
            except Exception as e:
                print(e)
                print(f"Skip this model: {model_name}")
                return
    if backward:
        try:
            m.train()
        except:
            print(f"{model_name} Cannot to the training mode, use just eval mode")
            m.eval()
            backward = False
    else:
        m.eval()

    if do_compile:
        backend = get_ttnn_backend(model_name, trace_orig, trace_modi, backward, out_folder, graphviz, device)
    else:
        backend = get_dummy_backend(model_name, trace_orig, trace_modi, backward, out_folder)
    m = torch.compile(m, backend = backend)

    inputs = [torch.randn([1, 3, 224, 224])]

    if to_profile:
        from torch.profiler import profile, record_function, ProfilerActivity
        trace_file = os.path.join(out_folder, "profile", model_name)
        os.makedirs(os.path.dirname(trace_file), exist_ok=True)
        activities = [ProfilerActivity.CPU]
        if torch.cuda.is_available():
            activities.append(ProfilerActivity.CUDA)
        with profile(activities=activities, record_shapes=True) as prof:
            result = m(*inputs)
            if backward:
                result.backward(torch.ones_like(result))
        prof.export_chrome_trace(trace_file)
    else:
        result = m(*inputs)
        if backward:
            result.backward(torch.ones_like(result))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out_folder", "-o", type = str, default = os.path.join(os.getcwd(),"stat"))
    parser.add_argument("--do_compile", action="store_true")
    parser.add_argument("--trace_orig", action="store_true")
    parser.add_argument("--trace_modi", action="store_true")
    parser.add_argument("--backward", action="store_true")
    parser.add_argument("--graphviz", action="store_true")
    parser.add_argument("--profile", action="store_true")
    args = parser.parse_args()
    if args.do_compile and args.backward:
        assert(0 and "torch_ttnn not yet support backward")
    if not args.do_compile and args.graphviz:
        assert(0 and "graphviz is in ttnn")

    if args.do_compile:
        import torch_ttnn

    models = ["dinov2_vits14", "alexnet", "googlenet", "resnet18", "vgg11"]

    device = torch_ttnn.ttnn.open(0) if args.do_compile else None
    for m in models:
        try:
            run_model(m, args.do_compile, args.trace_orig, args.trace_modi, args.backward, args.out_folder, args.graphviz, args.profile, device)
        except:
            print(f"{m} FAIL")
    if args.do_compile:
        torch_ttnn.ttnn.close(device)