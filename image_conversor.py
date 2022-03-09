from PIL import Image
import glob

print(glob.glob("*.png"))

for file in glob.glob("*.png"):
    im = Image.open(file)
    rgb_im=im.convert('RGB')
    rgb_im.save(file.replace("png","jpg"), quality = 95)



#An option to convert to PNG and modify the size
""" for file in glob.glob("aboutme.jpg"):
    im = Image.open(file)
    width, height = im.size
   # print(width,height)
    im = im.resize((int(width/2), int(height/2)), Image.ANTIALIAS)
    rgb_im=im.convert('RGBA')
    rgb_im.save(file.replace("jpg","png"), quality = 100)
 """
