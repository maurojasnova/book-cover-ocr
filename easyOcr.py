import easyocr
import cv2

img = cv2.imread('./images/test3.jpg')
reader = easyocr.Reader(['en', 'es']) # this needs to run only once to load the model into memory
result = reader.readtext(img, detail= 0)
print(result)