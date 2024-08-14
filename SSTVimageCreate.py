from pysstv.color import Robot36
from PIL import Image

#load image 
img = Image.open('image.jpg')

sstv = Robot36(img, 44100, 16) #image file, sample rate, bit depth

with open('output.wav', 'wb') as f:
    sstv.write_wav(f)
    
print("wave file created successfully")
