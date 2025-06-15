import torch
from transformers import BertModel, BertTokenizer
from tools import torch_stat

# Load tokenizer and model
tokenizer = BertTokenizer.from_pretrained("bert-large-uncased")
model = BertModel.from_pretrained("bert-large-uncased", torch_dtype=torch.bfloat16).eval()

# Define tracing option
stat_option = torch_stat.TorchStatOption(model_name="bert-large-uncased")

# Compile model with torch_stat backend
compiled = torch.compile(model, backend=torch_stat.backend(stat_option))

# Create dummy input
inputs = tokenizer("The quick brown fox jumps over the lazy dog.", return_tensors="pt")

# Run forward pass to trace operations
with torch.no_grad():
    compiled(**inputs)
