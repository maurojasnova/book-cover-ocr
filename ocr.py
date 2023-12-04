import pytesseract
import argparse
import imutils
import numpy as np
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image to be OCR'd")
args = vars(ap.parse_args())

# load the input image
image = cv2.imread(args["image"])

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



# Threshold the image using Otsu's thresholding method
thresh = cv2.threshold(gray, 0, 255,
                       cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

cv2.imshow("thresh", thresh)

# use Tesseract to OCR the image
text = pytesseract.image_to_string(thresh)
print(text)

cv2.waitKey(0)
