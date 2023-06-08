from PIL import Image

img1 = Image.open('E:/我的实验记录/new_Drawing/B1.png')
img2 = Image.open('E:/我的实验记录/new_Drawing/B2.png')
img3 = Image.open('E:/我的实验记录/new_Drawing/B3.png')
img4 = Image.open('E:/我的实验记录/new_Drawing/B4.png')

width, height = img1.size

new_img = Image.new('RGB', (width*2, height*2))
# new_img = Image.new('RGB', (width, height*4))

new_img.paste(img1, (0, 0))
new_img.paste(img2, (width, 0))
new_img.paste(img3, (0, height))
new_img.paste(img4, (width, height))
# new_img.paste(img1, (0, 0))
# new_img.paste(img2, (0, height))
# new_img.paste(img3, (0, height*2))
# new_img.paste(img4, (0, height*3))

new_img.save('Confusion_merged_image.jpg')