# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 13:14:45 2020

@author: renatons
"""

import pytesseract as ocr
from PIL import Image

phrase = ocr.image_to_string(Image.open(r'C:\Users\RenatoNS\Desktop\teste_ocr\phrase.jpeg'), lang='por')
print(phrase)
