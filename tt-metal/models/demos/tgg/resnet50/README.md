---

# ResNet50 Demo

## Introduction
ResNet50 is a deep convolutional neural network architecture with 50 layers, designed to enable training of very deep networks by using residual learning to mitigate the vanishing gradient problem.

## Details

+ The entry point to the Metal ResNet model is `ResNet` in `ttnn_functional_resnet50.py`.
+ The model picks up certain configs and weights from TorchVision pretrained model. We have used `torchvision.models.ResNet50_Weights.IMAGENET1K_V1` version from TorchVision as our reference.
+ Our ImageProcessor on the other hand is based on `microsoft/resnet-50` from huggingface.

## Performance

### TGG
#### End-to-End Performance
+ For end-to-end performance, run
```python
  pytest models/demos/tgg/resnet50/tests/test_perf_e2e_resnet.py::test_perf_trace`
```
+ This will generate a CSV with the timings and throughputs.
+ **Expected end-to-end perf**: For batch = 16 per device, or batch 1024 in total, it is about `145,000 fps` currently. This may vary machine to machine.
