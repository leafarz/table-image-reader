import cv2 as cv
import pytesseract

def draw_letter_bounds(img):
    h, _, _ = img.shape
    boxes = pytesseract.image_to_boxes(img)

    for b in boxes.splitlines():
        b = b.split(' ')
        cv.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
