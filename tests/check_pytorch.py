import torch

# Check PyTorch version
print("PyTorch version: ", torch.__version__)

# Check for CUDA availability (returns True if CUDA is available and PyTorch can use GPUs)
print("CUDA available: ", torch.cuda.is_available())

# Get the CUDA device name
# This line will throw a meaningful error if no GPU is available, even if CUDA is available
if torch.cuda.is_available():
    print("CUDA device name: ", torch.cuda.get_device_name(0))

# Create a tensor and move it to GPU memory
if torch.cuda.is_available():
    tensor = torch.tensor([1.0, 2.0, 3.0]).cuda()
    print("Tensor on GPU: ", tensor)

