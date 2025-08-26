import torch
import numpy as np
import gaussian_splatting.utils as utils
from gaussian_splatting.trainer import Trainer
import gaussian_splatting.utils.loss_utils as loss_utils
from gaussian_splatting.utils.data_utils import read_all
from gaussian_splatting.utils.camera_utils import to_viewpoint_camera
from gaussian_splatting.utils.point_utils import get_point_clouds
from gaussian_splatting.gauss_model import GaussModel
from gaussian_splatting.gauss_render import GaussRenderer

import contextlib

from torch.profiler import profile as torch_profile
from torch.profiler import ProfilerActivity

USE_GPU_PYTORCH = True
USE_PROFILE = False


class GSSTrainer(Trainer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = kwargs.get("data")
        self.gaussRender = kwargs.get("gauss_render_model")
        self.model = kwargs.get("model")
        self.lambda_dssim = 0.2
        self.lambda_depth = 0.0

        if kwargs.get("fp16"):
            torch.set_default_dtype(torch.float16)

    def on_train_step(self):
        ind = np.random.choice(len(self.data["camera"]))
        camera = self.data["camera"][ind]
        rgb = self.data["rgb"][ind]
        depth = self.data["depth"][ind]
        mask = self.data["alpha"][ind] > 0.5
        if USE_GPU_PYTORCH:
            camera = to_viewpoint_camera(camera)

        if USE_PROFILE:
            prof = torch_profile(activities=[ProfilerActivity.CUDA], with_stack=True)
        else:
            prof = contextlib.nullcontext()

        with prof:
            out = self.gaussRender(pc=self.model, camera=camera)

        if USE_PROFILE:
            print(prof.key_averages(group_by_stack_n=True).table(sort_by="self_cuda_time_total", row_limit=20))

        l1_loss = loss_utils.l1_loss(out["render"], rgb)
        depth_loss = loss_utils.l1_loss(out["depth"][..., 0][mask], depth[mask])
        ssim_loss = 1.0 - loss_utils.ssim(out["render"], rgb)

        total_loss = (1 - self.lambda_dssim) * l1_loss + self.lambda_dssim * ssim_loss + depth_loss * self.lambda_depth
        psnr = utils.img2psnr(out["render"], rgb)
        log_dict = {"total": total_loss, "l1": l1_loss, "ssim": ssim_loss, "depth": depth_loss, "psnr": psnr}

        self.train_results = out
        return total_loss, log_dict

    @torch.no_grad()
    def on_evaluate_step(self, **kwargs):
        import matplotlib.pyplot as plt

        ind = np.random.choice(len(self.data["camera"]))
        camera = self.data["camera"][ind]
        if USE_GPU_PYTORCH:
            camera = to_viewpoint_camera(camera)

        rgb = self.data["rgb"][ind].detach().cpu().numpy()
        out = self.gaussRender(pc=self.model, camera=camera)
        self.eval_results = out
        rgb_pd = out["render"].detach().cpu().numpy()
        depth_pd = out["depth"].detach().cpu().numpy()[..., 0]
        depth = self.data["depth"][ind].detach().cpu().numpy()
        depth = np.concatenate([depth, depth_pd], axis=1)
        depth = 1 - depth / depth.max()
        depth = plt.get_cmap("jet")(depth)[..., :3]
        image = np.concatenate([rgb, rgb_pd], axis=1)
        image = np.concatenate([image, depth], axis=0)
        utils.imwrite(str(self.results_folder / f"image-{self.step}.png"), image)


import ttnn
import torch_ttnn


def get_dispatch_core_type():
    # Instead of conditionally returning WORKER or ETH, here we always return ETH
    # Without setting this property, we get less cores availble on N300 than on N150, which might lead to inconsistent and sub-sufficient results
    return ttnn.device.DispatchCoreType.ETH


def get_dispatch_core_axis():
    # Should be ttnn.DispatchCoreAxis.COL for Blackhole
    return ttnn.DispatchCoreAxis.ROW


def get_dispatch_core_config():
    dispatch_core_type = get_dispatch_core_type()
    dispatch_core_axis = get_dispatch_core_axis()
    dispatch_core_config = ttnn.DispatchCoreConfig(dispatch_core_type, dispatch_core_axis)
    return dispatch_core_config


def run_train():
    use_fp16 = True
    to_dtype = torch.float16 if use_fp16 else torch.float
    device = "cpu"
    folder = "./B075X65R3X"
    data = read_all(folder, resize_factor=0.5)
    data = {k: v.to(to_dtype) for k, v in data.items()}
    data["depth_range"] = torch.Tensor([[1, 3]] * len(data["rgb"])).to(to_dtype)

    points = get_point_clouds(data["camera"], data["depth"], data["alpha"], data["rgb"])
    raw_points = points.random_sample(2**14)
    # raw_points.write_ply(open('points.ply', 'wb'))

    device_id = 0
    l1_small_size = 16384
    dispatch_core_config = get_dispatch_core_config()
    print("Opening device")
    device = ttnn.open_device(
        device_id=device_id, dispatch_core_config=dispatch_core_config, l1_small_size=l1_small_size
    )
    print("Device Opened")
    device.enable_program_cache()
    # Compile the model for TTNN
    option = torch_ttnn.TorchTtnnOption(
        device=device,
        verbose=False,
        gen_graphviz=False,
        export_code="accuracy",
        metrics_path="gaussian_splatting_profile",
    )
    option._is_end_to_end = False
    print("Device Compiled")
    # option.bypass_compile = True

    render_kwargs = {
        "white_bkgd": True,
    }

    gaussModel = GaussModel(
        sh_degree=4,
        debug=False,
    )
    gaussModel.create_from_pcd(pcd=raw_points)
    gaussRenderer = GaussRenderer(**render_kwargs)
    # gaussRenderer = torch.compile(gaussRenderer, backend=torch_ttnn.backend, options=option)

    trainer = GSSTrainer(
        model=gaussModel,
        data=data,
        train_batch_size=1,
        train_num_steps=1,
        i_image=100,
        train_lr=1e-3,
        amp=False,
        fp16=use_fp16,
        results_folder="result/test",
        gauss_render_model=gaussRenderer,
        render_kwargs=render_kwargs,
    )

    trainer.on_evaluate_step()
    trainer.train()


if __name__ == "__main__":
    run_train()
