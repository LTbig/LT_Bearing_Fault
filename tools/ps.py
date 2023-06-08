from PIL import Image

# 打开图片
img = Image.open('E:/我的实验记录/new_Drawing/Q2.png')
# 获取图片的宽度和高度
width, height = img.size

# 定义要替换的颜色（这里假设要替换为红色）
target_color = (255, 0, 0)

# 遍历图片的每个像素，将蓝色像素替换为目标颜色
for x in range(width):
    for y in range(height):
        # 获取当前像素的颜色
        current_color = img.getpixel((x, y))
        # 如果当前像素颜色为蓝色，则将其替换为目标颜色
        if current_color == (0, 0, 255):
            img.putpixel((x, y), target_color)
# 保存修改后的图像
img.save('final_image.png')