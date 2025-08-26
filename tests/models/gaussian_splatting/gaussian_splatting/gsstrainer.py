import torch
import numpy as np
from . import utils
from .trainer import Trainer
from .utils import loss_utils
from .utils.camera_utils import to_viewpoint_camera

import contextlib


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
        camera = to_viewpoint_camera(camera)
        prof = contextlib.nullcontext()

        with prof:
            out = self.gaussRender(pc=self.model, camera=camera)

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
