from PIL import Image
from reportlab.pdfgen import canvas

# 打开 TIFF 图像
image = Image.open('E:/我的实验记录/Origin作图/双相电流矢量运算准确率曲线.tif')

# 将tif文件保存为png格式
image.save('E:/我的实验记录/Origin作图/双相电流矢量运算准确率曲线.png')