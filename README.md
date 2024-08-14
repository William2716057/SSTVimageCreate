# Image to SSTV Wave File Converter
This Python script converts an image into an SSTV (Slow Scan Television) wave file using the pysstv library. The resulting .wav file can be transmitted and received using SSTV software or equipment.

## Features
- Converts images to SSTV wave files using the Robot36 color mode.
- Outputs a .wav file that can be used for SSTV transmissions.
- Supports customization of sample rate and bit depth.

## Requirements
- Python 3.x
- pysstv library
- PIL (Pillow) library

## Installation
1. Clone the repository:
```
https://github.com/William2716057/SSTVimageCreate.git
```
2. Install the required Python packages:
```
pip install pysstv Pillow
```

### Usage
1. Place the image you want to convert in the same directory as the script and rename it to image.jpg (or update the filename in the script).

2. Run the script:
```
python3 SSTVimageCreate.py
```
3. After running the script, an output.wav file will be created in the same directory.

### Customization
- Image File: Change 'image.jpg' to the path of your desired image.
- Sample Rate: Adjust the sample rate by modifying 44100 to another value.
- Bit Depth: Modify the bit depth by changing 16 to another supported value.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
pysstv - The library used to generate SSTV wave files.
Pillow - The Python Imaging Library used to load and manipulate images.
