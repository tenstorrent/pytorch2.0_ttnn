from utils import *
from transformers import WhisperProcessor, WhisperForConditionalGeneration
from datasets import load_dataset
import torch
import time
import torch_ttnn
import ttnn
import numpy as np


@capture_output
def transcribe_audio(audio_sample=None, use_ttnn=True, iterations=1):
    model_name = "distil-whisper/distil-large-v3"
    processor = WhisperProcessor.from_pretrained(model_name, torch_dtype=torch.bfloat16)
    model = WhisperForConditionalGeneration.from_pretrained(model_name, torch_dtype=torch.bfloat16)
    model.config.forced_decoder_ids = None
    
    # Use default test audio if none provided
    if audio_sample is None:
        # Load dummy dataset for testing
        ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
        audio_sample = ds[0]["audio"]
    
    # Process audio input
    input_features = processor(
        audio_sample["array"], 
        sampling_rate=audio_sample["sampling_rate"], 
        return_tensors="pt"
    ).input_features.to(torch.bfloat16)
    
    if use_ttnn:
        device = compile_ttnn(model.generate, iterations, input_features)
    
    st.write("Running Whisper transcription (May take a few minutes)")
    start_time = time.time()
    
    # Generate transcription
    predicted_ids = model.generate(input_features, max_new_tokens=448)
    
    end_time = time.time()
    inference_time = end_time - start_time
    
    # Decode the transcription
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    
    # Calculate performance metrics
    num_tokens = len(predicted_ids[0])
    tokens_per_second = num_tokens / inference_time if inference_time > 0 else 0
    
    if use_ttnn:
        ttnn.close_device(device)
        
    return transcription, inference_time, num_tokens, tokens_per_second


def whisper_demo():
    st.header("Audio Transcription with Whisper (distil-large-v3)")
    
    # Audio input options
    st.subheader("Audio Input")
    audio_option = st.selectbox(
        "Choose audio source:",
        ["Use sample audio", "Upload audio file (experimental)"]
    )
    
    audio_sample = None
    if audio_option == "Upload audio file (experimental)":
        uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a", "flac"])
        if uploaded_file is not None:
            st.warning("Audio upload feature is experimental. Using sample audio for now.")
            audio_sample = None
    
    # Configuration
    st.subheader("Configuration")
    use_ttnn = st.checkbox("Use TTNN acceleration", value=True)
    iterations = st.number_input("Number of iterations for benchmarking", min_value=1, max_value=10, value=1)
    
    if st.button("Transcribe Audio"):
        with st.spinner("Processing audio..."):
            try:
                result, output = transcribe_audio(
                    audio_sample=audio_sample,
                    use_ttnn=use_ttnn,
                    iterations=iterations
                )
                
                transcription, inference_time, num_tokens, tokens_per_second = result
                
                st.subheader("Results")
                st.success("Transcription completed!")
                
                # Display transcription
                st.subheader("Transcription:")
                st.write(f"**Text:** {transcription}")
                
                # Performance metrics
                st.subheader("Performance Metrics")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Inference Time", f"{inference_time:.2f}s")
                
                with col2:
                    st.metric("Tokens Generated", num_tokens)
                
                with col3:
                    st.metric("Tokens/Second", f"{tokens_per_second:.1f}")
                
                # Show detailed output if available
                if output.strip():
                    with st.expander("Detailed Output"):
                        st.text(output)
                        
            except Exception as e:
                st.error(f"Error during transcription: {str(e)}")
                st.text(f"Full error: {e}")


if __name__ == "__main__":
    whisper_demo()