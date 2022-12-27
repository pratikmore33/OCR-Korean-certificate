import cv2
import pytesseract
import os
from PIL import Image
import numpy as np
import skew



def parse_image(file):
    """
    Performs OCR on a single image
    :img_path: str, path to the image file
    :lang: str, language to be used while conversion (optional, default is english)
    Returns
    :text: str, converted text from image
    """
    nparr = np.fromstring(file, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # gray = cv2.medianBlur(gray, 3)
    filename = "{}.png".format("temp")
    cv2.imwrite(filename, gray)
    # detect language korean
    text = pytesseract.image_to_string(Image.open(filename), lang='kor',config='--psm 6')
    os.remove(filename)
    #img2 = skew.skew_correct(file)
    return text
