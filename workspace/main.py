# copy from https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2
import torch
from transformers import pipeline

# config
model_id = "kotoba-tech/kotoba-whisper-v2.2"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
device = "cuda:0" if torch.cuda.is_available() else "cpu"
model_kwargs = {"attn_implementation": "sdpa"} if torch.cuda.is_available() else {}


# load model
pipe = pipeline(
    model=model_id,
    torch_dtype=torch_dtype,
    device=device,
    model_kwargs=model_kwargs,
    batch_size=8,
    trust_remote_code=True,
)

# run inference
result = pipe("sample_diarization_japanese.mp3", chunk_length_s=15)
print(result)

