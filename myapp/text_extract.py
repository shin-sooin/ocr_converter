import cv2
import pytesseract

#pytesseract.pytesseract.tesseract_cmd

img=cv2.imread('Capture.png')
text=pytesseract.image_to_string(img)
print(text)