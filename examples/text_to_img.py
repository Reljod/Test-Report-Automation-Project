import PIL
import sys
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from shutil import copyfile

# width = 200
bgcolor = "#FA0" #RGB #CYM
color = "#FFF"
leftpadding = 3
rightpadding = 50
font_path = "../fonts/Hack-Regular.ttf"
font_size = 20
sample_line = \
"""Python script: Convert Text to Image
Author: Reljod Oreta
Assistant: Joshua Caleb
Test Report:

SPC-067
BLACK MAN

End line"""
sample_line_list = sample_line.split('\n')
num_lines = len(sample_line_list)

max_width_line = max(sample_line_list, key= lambda s: len(s))
print(max_width_line)

font = ImageFont.truetype(font_path, font_size)
line_height = font.getsize(sample_line)[1]

img_height = line_height * num_lines
img_width = font.getsize(max_width_line)[0] + rightpadding

print("line_height", line_height)
print("img_height", img_height)

img = Image.new("RGBA", (img_width, img_height), bgcolor)
draw = ImageDraw.Draw(img)

y = 0
for line in sample_line_list:
    draw.text((leftpadding, y), line, color, font=font)
    y += line_height

img.save("image.png")

copyfile("image.png", "/mnt/c/users/Reljod/Desktop/image.png")