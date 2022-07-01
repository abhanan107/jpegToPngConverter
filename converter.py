from email.mime import image
import os
import sys
from PIL import Image 

jpg_image_folder=sys.argv[1]
png_image_folder=sys.argv[2]

if not os.path.exists(png_image_folder):
    os.mkdir(png_image_folder)

for file in os.listdir(jpg_image_folder):
    img=Image.open(f"{jpg_image_folder}/{file}")
    new_name=os.path.splitext(file)[0]
    img.save(f'{png_image_folder}/{file}.png','png')
