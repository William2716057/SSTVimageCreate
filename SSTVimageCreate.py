from pysstv.color import Robot36
#from pysstv.wav import WavWriter
#from PIL import Image

from pysstv.color import Robot36
from PIL import Image

#load image 
img = Image.open('image.jpg')

sstv = Robot36(img, 44100, 16) #image file, sample rate, bit depth

with open('output.wav', 'wb') as f:
    sstv.write_wav(f)

#with open('output.wav', 'wb') as f:
 #   wav = WavWriter(f, sstv)
 #   sstv.write_wav(wav)
 #   wav.close()
    
print("wave file created successfully")
