import wandb

wandb.init(project="test_wandb_cpp", name="")

for i in range(100):
    wandb.log({"x": 1.0, "mode": "abc"}, step=i)

wandb.summary.a = 1

wandb.config.update({"a": 1, "b": 2})