# Stable Diffusion 1.4 Reproducibility

## Install Requirements

```bash
pip install diffusers transformers accelerate scipy
```

## Verify Weights

```bash
python models/demos/stable_diffusion/verify_weights.py
```

## Run Pytest

```bash
pytest tests/models/stable_diffusion/test_stable_diffusion_14.py -v --tb=short
```

## Run Performance Report

```bash
python models/demos/stable_diffusion/perf_report.py
```
