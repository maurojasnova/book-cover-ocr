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


#Resize image to fit in the laptop windows
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
threshResized = cv2.resize(thresh, (540, 960)) 

#Show processed image
cv2.imshow("thresh Resized", threshResized)

#Config tesseract model
config = r'--oem 1 --psm 11'

# use Tesseract to OCR the image
text = pytesseract.image_to_string(thresh, config=config)
print(text)

cv2.waitKey(0)
