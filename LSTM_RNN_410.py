# SOURCE(s) https://github.com/madmaze/pytesseract
# SOURCE(s) https://github.com/tesseract-ocr/tesseract
# SOURCE(s) https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/
# SOURCE(s) https://www.pyimagesearch.com/2020/09/14/getting-started-with-easyocr-for-optical-character-recognition/
# SOURCE(s) https://nanonets.com/blog/deep-learning-ocr/
# FILENAME LSTM_RNN_410.py

import numpy as np
import cv2
from imutils.object_detection import non_max_suppression
import pytesseract
from matplotlib import pyplot

# create argument dictionary for arguments used
args = {"image":"../input/text-detection/example-images/Example-images/ex24.jpg",
        "east":"../input/text-detection/east_text_detection.pb",
        "min_confidence":0.5, "width":320, "height":320}

"""
default arguments
:param: image as the location of input image(s) for ocr
:param: east as the location of input image having pretrained EAST model
:param: min-confidence minimum probability score for the confidence of geometric shape predicted at the location
:param: width as the litteral width in multiples of 32 for the EAST model to work ~well
:param: height as the litteral height in multiples of 32 for the EAST model to work ~well

:return 
"""

# give location of the image to be read.