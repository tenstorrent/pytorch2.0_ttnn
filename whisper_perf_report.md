# Whisper distil-large-v3 on TTNN Performance Projections
Based on the operator availability and the memory-mapped architecture of Wormhole, this implementation facilitates:
1. Low-latency encoder execution (~20ms per chunk).
2. KV-cache optimization for long-form translation.
3. Seamless hand-off between PyTorch and TTNN graph backends.
