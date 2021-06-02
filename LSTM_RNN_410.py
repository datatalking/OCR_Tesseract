# SOURCE(s) https://github.com/madmaze/pytesseract
# SOURCE(s) https://github.com/tesseract-ocr/tesseract
# SOURCE(s) https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/
# SOURCE(s) https://www.pyimagesearch.com/2020/09/14/getting-started-with-easyocr-for-optical-character-recognition/
# SOURCE(s) https://nanonets.com/blog/deep-learning-ocr/
# https://machinelearningmastery.com/simple-genetic-algorithm-from-scratch-in-python/
# https://colab.research.google.com/drive/1Kg6AvXKdSZXoqzSZ5BRHuewyHRMvrZs1#scrollTo=FR0xFmRapK-e
# FILENAME LSTM_RNN_410.py

import numpy as np
import cv2
from imutils.object_detection import non_max_suppression
import pytesseract
from matplotlib import pyplot

# create argument dictionary for arguments used
# TODO add function for local PATH of training on tagged photos
# TODO add output of saved files logged in csv
# TODO add wrappers for self-modifications will survive only if they are useful
#  according to a user-given fitness, error or reward function
# TODO msg Jurgen Schmidthuber for colab

args = {"image":"../input/text-detection/example-images/Example-images/ex24.jpg",
        "east":"../input/text-detection/east_text_detection.pb",
        "min_confidence":0.5, "width":320, "height":320}

"""
default arguments
:param: image as the location of input image(s) for ocr
:param: east as the location of input image having pretrained EAST model
:param: min-confidence minimum probability score for the confidence of geometric shape predicted at the location
:param: width as the literal width in multiples of 32 for the EAST model to work ~well
:param: height as the literal height in multiples of 32 for the EAST model to work ~well
:param: PATH as literal file RUNTIME PATH ing issues for runtime envs
:param: INPUTPATH as literal location for future training data
:param: OUTPUTPATH as literal location for where files are marked, organized and or user input is needed
:param:

:return 
"""

# give location of the image to be read.
# "Example-images/ex24.jpg"

args['image']="../input/text-detection/example-images/Example-images/ex24.jpg"
image = cv2.imread(args['image'])

# saving training data originals with shape vs recursive issues
orig = image.copy()
(origH, origW) = image.shape[:2]

# set new height and width to default 320 by using args dictionary
(args["width"], args["height"])

# ratio between original and new image for both height and weight.
(newW, NewH) = (args["width"], args["height"])

# Calculate the rstio between original and new image  for both height and weight
# This ratio will be used to translate buding box location on the orinal images
rW = origW / float(newW)
rH = origH / float(newH)

# resize the originl image to new dimensions
image = cv2 =
