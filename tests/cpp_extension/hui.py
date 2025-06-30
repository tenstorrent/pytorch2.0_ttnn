from transformers import BertModel, BertTokenizer
import torch

model = BertModel.from_pretrained("bert-large-uncased")
tokenizer = BertTokenizer.from_pretrained("bert-large-uncased")
model.eval()

sentence = "Tenstorrent powers the future of AI."
inputs = tokenizer(sentence, return_tensors="pt", padding="max_length", max_length=16)

# Test on CPU
with torch.no_grad():
    out_cpu = model(**inputs).last_hidden_state

# Move to TTNN
model.to("ttnn:0")
inputs = {k: v.to("ttnn:0") for k, v in inputs.items()}
with torch.no_grad():
    out_tt = model(**inputs).last_hidden_state

# Compare outputs
diff = (out_tt[0, 0].cpu() - out_cpu[0, 0]).abs().max()
print(f"Max abs difference at first token: {diff}")
