from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

img = Image.new('1', (100, 50))
draw = ImageDraw.Draw(img)
txt = "Hello World"
fontsize = 1  # starting font size

# portion of image width you want text width to be
img_fraction = 0.50

font = ImageFont.truetype("arial.ttf", fontsize)
while font.getsize(txt)[0] < img_fraction*img.size[0]:
    fontsize += 1
    font = ImageFont.truetype("arial.ttf", fontsize)

# optionally de-increment to be sure it is less than criteria
fontsize -= 1
font = ImageFont.truetype("arial.ttf", fontsize)

print('final font size',fontsize)
draw.text((10, 25), txt, font=font) # put the text on the image
img.save('hsvwheel_txt.png') # save it