import cv2
import sys
import pytesseract
import numpy as np
import math

def nothing(x):
    return

def get_roi(gray):
    # check dominant color? check what thesholding we need to use?
    # _, thresh = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)
    thresh = gray

    contours, _ = cv2.findContours(255-thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    largest_box = ()
    largest_dim = 0

    # get largest rectangle
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        # cv2.drawContours(thresh, [approx], 0, (0,0,0), 3)

        # if rectangle
        if len(approx) == 4:
            pts = approx.ravel()
            ul = (pts[0], pts[1])
            ll = (pts[2], pts[3])
            lr = (pts[4], pts[5])
            ur = (pts[6], pts[7])

            ll_lr = (lr[0]-ll[0], lr[1]-ll[1])
            ll_ul = (ul[0]-ll[0], ul[1]-ll[1])
            width = math.sqrt(ll_lr[0]*ll_lr[0] + ll_lr[1]*ll_lr[1])
            height = math.sqrt(ll_ul[0]*ll_ul[0] + ll_ul[1]*ll_ul[1])

            # get the approx if dimension is larger
            curr_dim = width * height
            if curr_dim > largest_dim:
                largest_dim = curr_dim
                largest_box = approx

    if len(largest_box) != 0:
        pts = largest_box.ravel()
        region_of_interest_vertices = [
            (pts[0],pts[1]),
            (pts[2],pts[3]),
            (pts[4],pts[5]),
            (pts[6],pts[7])
        ]

        cv2.drawContours(img, [largest_box], 0, (0,255,0), 5)

        minx = min(pts[0],pts[2],pts[4],pts[6])
        maxx = max(pts[0],pts[2],pts[4],pts[6])
        miny = min(pts[1],pts[3],pts[5],pts[7])
        maxy = max(pts[1],pts[3],pts[5],pts[7])

        return thresh[miny:maxy,minx:maxx]
# END FUNCTIONS

# Use embedded tesseract
pytesseract.pytesseract.tesseract_cmd = r'./vendor/Tesseract-OCR/tesseract'

# for now we use a best-better case data
filepath = './data/table_02.png'

# Read image from disk
img = cv2.imread(filepath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Get region of interest
masked_image = get_roi(gray)

cv2.imshow('img',img)
cv2.imshow('gray',gray)
cv2.imshow('masked_img',masked_image)

# Run tesseract OCR on image
text = pytesseract.image_to_string(masked_image)
print(text)

cv2.waitKey(0)
cv2.destroyAllWindows()