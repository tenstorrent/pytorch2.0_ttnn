# Whisper (distil-large-v3)

## Model Information

- **Model Name**: Whisper (distil-large-v3)
- **Source**: [distil-whisper/distil-large-v3](https://huggingface.co/distil-whisper/distil-large-v3)
- **Task**: Automatic Speech Recognition (ASR)
- **Model Type**: Encoder-Decoder Transformer
- **Batch Size**: 1 (as per issue #1044 requirements)
- **Hardware Target**: n150

## Status

**Current Status**: 🔧 Compiling (SymInt guard implemented)

The model has been updated with a fix for the SymInt handling issue in `aten::clone()` operations. The compilation now proceeds past the previous blocker, though further testing on TT-NN hardware is required to verify full end-to-end functionality.

## Implementation Details

### Changes from Previous Version

- **Model Updated**: Changed from `openai/whisper-small` to `distil-whisper/distil-large-v3`
  - This aligns with the model version used in the [tt-metal Whisper demo](https://github.com/tenstorrent/tt-metal/tree/main/models/demos/whisper)
  - distil-large-v3 is a distilled version optimized for faster inference while maintaining accuracy

### Recent Fixes

**SymInt Handling for aten::clone() (Fixed)**

The model previously failed compilation due to:

```
torch._dynamo.exc.BackendCompilerFailed: backend='ttnn_backend' raised:
RuntimeError: aten::clone() Expected a value of type 'Tensor' for argument 'self' but instead found type 'SymInt'.
```

**Solution Implemented:**
- Added a custom guard function `guard_aten_clone()` in `torch_ttnn/passes/lowering/to_tt_guard.py`
- This guard prevents lowering `aten::clone()` operations to TTNN when they receive SymInt arguments
- SymInt values appear in generative models (Whisper, GPTNeo, OPT, etc.) due to dynamic sequence lengths during tracing
- The guard allows these operations to fall back to PyTorch native execution, avoiding the type mismatch error

### Test Configuration

- **Test File**: `tests/models/whisper/test_whisper.py`
- **Mode**: Evaluation only
- **Input**: Audio samples from `hf-internal-testing/librispeech_asr_dummy` dataset
- **Data Type**: bfloat16

## Next Steps

To move this model to ✅ Fully Working status, the following work remains:

1. **Test on TT-NN Hardware**:
   - Deploy to n150 hardware (via Koyeb or direct access)
   - Verify end-to-end compilation and execution
   - Identify any additional operation lowering issues that may arise

2. **Operation Fallback Tuning**:
   - Profile which operations are falling back to PyTorch vs running on TTNN
   - Optimize the balance between TTNN acceleration and PyTorch fallback
   - Add specific blocklist entries for operations that should always fall back

3. **Performance Measurement & Optimization**:
   - Measure actual performance metrics on n150 hardware:
     - ttft (time to first token): Target 244 ms
     - t/s/u (tokens/second/user): Target 54.7
     - t/s (tokens/second): Target 54.7
   - Compare against tt-metal demo baseline (TT-Metalium v0.58.0-rc22)
   - Identify and document performance gaps
   - Propose optimizations (kernel selection, layout choices, fusion opportunities)

4. **Model Reporting Integration**:
   - Ensure the model appears correctly in the main README model table
   - Update status from 🚧 to ✅ once all tests pass
   - Document final accuracy, throughput, and compilation metrics

## References

- Issue: [#1044 - Add model: Whisper (distil-large-v3)](https://github.com/tenstorrent/pytorch2.0_ttnn/issues/1044)
- tt-metal demo: [models/demos/whisper](https://github.com/tenstorrent/tt-metal/tree/main/models/demos/whisper)
- Model card: [distil-whisper/distil-large-v3](https://huggingface.co/distil-whisper/distil-large-v3)

## Operation Trace

For detailed information about the operations used by this model, see [input_variations.md](./input_variations.md).
