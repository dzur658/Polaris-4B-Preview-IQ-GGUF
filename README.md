# Polaris-4B-Preview-IQ-GGUF
Repository for associated scripts and files used to make my GGUF quantizations. Check out the associated [hugging face 🤗](https://huggingface.co/dzur658/Polaris-4B-Preview-IQ-GGUF) repository to downloads the quantizations!

# Modelfile Settings
*Note it is incredibly important to use these modelfile settings when running in Olama to preserve the unique characteristics of the Polaris model.*

### Modelfile
```
# This Modelfile is for the Polaris model, quantized into GGUF format.
# It sets the base model, license, and the correct chat template.

# --- IMPORTANT ---
# Replace with the path to your script
FROM ./[PATH TO YOUR GGUF]

# Sets the model's license.
LICENSE "Apache-2.0"

# Defines the chat template.
TEMPLATE """<|im_start|>system
{{ .System }}<|im_end|>
<|im_start|>user
{{ .Prompt }}<|im_end|>
<|im_start|>assistant
"""

# --- Stopping Parameters ---
PARAMETER stop "<|im_end|>"

# --- Sytem Prompt ---
SYSTEM """You are Polaris, an impartial and reliable AI assistant."""

# --- Hardware & Performance Parameters ---
# Tells Ollama to offload all possible layers to the GPU for maximum performance.
PARAMETER num_gpu 99
# Explicitly sets the context window size. This prevents context from "leaking" between chats.
PARAMETER num_ctx 32768

# POLARIS reccomended sampling parameters
PARAMETER temperature 1.4
PARAMETER top_k 20
PARAMETER num_predict 90000
```

# Accredation
All credit for the original model belongs to the Polaris team and their affiliated organizations.
```
@misc{Polaris2025,
    title = {POLARIS: A Post-Training Recipe for Scaling Reinforcement Learning on Advanced Reasoning Models},
    url = {https://hkunlp.github.io/blog/2025/Polaris},
    author = {An, Chenxin and Xie, Zhihui and Li, Xiaonan and Li, Lei and Zhang, Jun and Gong, Shansan and Zhong, Ming and Xu, Jingjing and Qiu, Xipeng and Wang, Mingxuan and Kong, Lingpeng}
    year = {2025}
}
```
