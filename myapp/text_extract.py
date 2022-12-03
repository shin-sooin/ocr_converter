import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/Users/shinsooin/opt/anaconda3/envs/ocr_tesseract/bin/pytesseract'

img=cv2.imread('Capture.png')
text=pytesseract.image_to_string(img)
print(text)