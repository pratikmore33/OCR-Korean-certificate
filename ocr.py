import pytesseract
import os
import sys


def read_image(img_path):
    import re
    import cv2
    import numpy as np
    #img = cv2.imread(img_path)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    #kernel = np.ones((5, 5), np.uint8)
    #img = cv2.dilate(img, kernel, iterations=1)
    #img = cv2.erode(img, kernel, iterations=1)
    #img = cv2.Canny(img,100,200)

    
    """
    Performs OCR on a single image

    :img_path: str, path to the image file
    :lang: str, language to be used while conversion (optional, default is english)

    Returns
    :text: str, converted text from image
    """

    try:
        pattern = '.pdf'
        if bool(re.search(pattern,img_path)):
            return 'pdf file please upload in png or jpg format '
        #return pytesseract.image_to_string(img)
        else:
            img = cv2.imread(img_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            return pytesseract.image_to_string(img)
        
    except:
        
        return "[ERROR] Unable to process file: {0}".format(img_path)