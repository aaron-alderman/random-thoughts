"""Run this first to find out whether your GPU is usable."""
import subprocess, sys

print("Python:", sys.version)

try:
    import torch
    print(f"PyTorch {torch.__version__}")
    print(f"CUDA available : {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"GPU name       : {torch.cuda.get_device_name(0)}")
        print(f"CUDA version   : {torch.version.cuda}")
        t = torch.rand(1000, 1000, device='cuda')
        print(f"Smoke test     : tensor on GPU OK  (shape {list(t.shape)})")
    else:
        print("No CUDA GPU detected — run.py will use CPU (still works, just slower).")
        print()
        print("To install PyTorch with CUDA support (NVIDIA GPU required):")
        print("  1. Run:  nvidia-smi   — top-right corner shows your CUDA version")
        print("  2. Then: pip install torch --index-url https://download.pytorch.org/whl/cu124")
        print("     (replace cu124 with cu118 if your CUDA is 11.8)")
except ImportError:
    print("PyTorch not installed.")
    print("Install it first — see requirements.txt for instructions.")
