from PIL import Image

# 打开图像
image = Image.open("E:/我的实验记录/new_Drawing/R1.png")

# 调整图像尺寸
new_size = ((image.size[0]*4), (image.size[1]*4))
resized_image = image.resize(new_size)

# 保存调整后的图像
resized_image.save("R1.png")