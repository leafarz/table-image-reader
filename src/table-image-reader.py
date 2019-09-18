import cv2 as cv
import sys
import pytesseract

# Use embedded tesseract
pytesseract.pytesseract.tesseract_cmd = r'./vendor/Tesseract-OCR/tesseract'

filepath = './data/test.png'

# Read image from disk
im = cv.imread(filepath, cv.IMREAD_COLOR)

# Run tesseract OCR on image
text = pytesseract.image_to_string(filepath)

# Print recognized text
print(text)

cv.imshow('im',im)
cv.waitKey(0)
cv.destroyAllWindows()