import cv2
import pytesseract
import numpy as np

def draw_letter_bounds(img):
    h = img.shape[0]
    boxes = pytesseract.image_to_boxes(img)

    for b in boxes.splitlines():
        b = b.split(' ')
        cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    channel_count = img.shape[2] if len(img.shape) > 2 else 1
    match_mask_color = (255,) * channel_count
    cv2.fillPoly(mask, vertices, match_mask_color)
    # masked_image = cv2.bitwise_and(img, mask)
    return mask