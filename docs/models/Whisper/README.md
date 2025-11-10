# Whisper (distil-large-v3)

## Model Information

- **Model Name**: Whisper (distil-large-v3)
- **Source**: [distil-whisper/distil-large-v3](https://huggingface.co/distil-whisper/distil-large-v3)
- **Task**: Automatic Speech Recognition (ASR)
- **Model Type**: Encoder-Decoder Transformer
- **Batch Size**: 1 (as per issue #1044 requirements)
- **Hardware Target**: n150

## Status

**Current Status**: ❌ Traced

The model is currently in the "Traced" stage, meaning it runs on CPU to collect operation traces but does not yet compile through the TT-NN backend.

## Implementation Details

### Changes from Previous Version

- **Model Updated**: Changed from `openai/whisper-small` to `distil-whisper/distil-large-v3`
  - This aligns with the model version used in the [tt-metal Whisper demo](https://github.com/tenstorrent/tt-metal/tree/main/models/demos/whisper)
  - distil-large-v3 is a distilled version optimized for faster inference while maintaining accuracy

### Known Issues

The model currently fails compilation due to the following known issue:

```
torch._dynamo.exc.BackendCompilerFailed: backend='ttnn_backend' raised:
RuntimeError: aten::clone() Expected a value of type 'Tensor' for argument 'self' but instead found type 'SymInt'.
```

This is a **type casting issue** where the compiler cannot handle SymInt (symbolic integer) types in certain operations, particularly `aten::clone()`. This issue is documented in `torch_ttnn/passes/lowering/to_tt_guard.py`.

### Test Configuration

- **Test File**: `tests/models/whisper/test_whisper.py`
- **Mode**: Evaluation only
- **Input**: Audio samples from `hf-internal-testing/librispeech_asr_dummy` dataset
- **Data Type**: bfloat16

## Next Steps to Enable Compilation

To move this model from ❌ Traced to ✅ Compiled status, the following work is needed:

1. **Fix SymInt Handling**: 
   - Address the `aten::clone()` type casting issue for SymInt values
   - This may require updates to the TT-NN backend's type system or operation lowering

2. **Operation Fallback Configuration**:
   - Once the SymInt issue is resolved, identify operations that need fallback to PyTorch
   - Add appropriate blocklist entries in `to_tt_guard.py` for unsupported operation variants

3. **Performance Optimization**:
   - After compilation succeeds, measure performance on n150 hardware
   - Compare with tt-metal demo performance metrics
   - Target: 244 ms compile time, 54.7 inferences/second (as documented in issue #1044)

## References

- Issue: [#1044 - Add model: Whisper (distil-large-v3)](https://github.com/tenstorrent/pytorch2.0_ttnn/issues/1044)
- tt-metal demo: [models/demos/whisper](https://github.com/tenstorrent/tt-metal/tree/main/models/demos/whisper)
- Model card: [distil-whisper/distil-large-v3](https://huggingface.co/distil-whisper/distil-large-v3)

## Operation Trace

For detailed information about the operations used by this model, see [input_variations.md](./input_variations.md).
