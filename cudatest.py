import torch
print(torch.cuda.is_available())  # True면 정상!
print(torch.cuda.get_device_name(0))  # NVIDIA GeForce RTX 4060이 출력되면 성공!
import transformers
print(f"Torch version: {torch.__version__}")
print(f"Transformers version: {transformers.__version__}")
