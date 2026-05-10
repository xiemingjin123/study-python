# 兼容 Python 3.12+ 的 distutils 替代方案
try:
    import distutils.version
except (ModuleNotFoundError, AttributeError):
    import setuptools._distutils.version as distutils_version
    import sys
    sys.modules['distutils.version'] = distutils_version

from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

# Pillow 10+ 不再支持 Image.ANTIALIAS，兼容写法
if hasattr(Image, "Resampling"):
    RESAMPLING_MODE = Image.Resampling.LANCZOS  # Pillow 10+
else:
    RESAMPLING_MODE = Image.ANTIALIAS  # Pillow <10

# 创建 SummaryWriter
writer = SummaryWriter("logs")

# 读取图片
img_path = "images/院徽2.jpg"
img = Image.open(img_path)
print(f"图片信息: {img}")

# 转为 tensor
totensor = transforms.ToTensor()
image_totensor = totensor(img)

# 添加图片到 TensorBoard
# dataformats="CHW" 告诉 TensorBoard 通道-高-宽格式
writer.add_image("Totensor", image_totensor, dataformats="CHW")

writer.close()
print("TensorBoard 日志已生成，路径: logs")