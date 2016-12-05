
from PIL import Image 
'''to use tesserocr first do 
$ sudo apt-get install tesseract-ocr libtesseract-dev libleptonica-dev
$ sudo pip install Cython
$ sudo pip install tesserocr 
'''
#A simple, Pillow-friendly, wrapper around the tesseract-ocr API for Optical Character Recognition (OCR)
import tesserocr
image = Image.open('sample.jpg')
print tesserocr.image_to_text(image)  # print ocr text from image
# or
print tesserocr.file_to_text('sample.jpg')
