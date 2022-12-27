
import math
from typing import Tuple, Union

import cv2
import numpy as np

from deskew import determine_skew

#img = cv2.imread('skew.jpg')
def rotate(
        image: np.ndarray, angle: float, background: Union[int, Tuple[int, int, int]]
) -> np.ndarray:
    old_width, old_height = image.shape[:2]
    angle_radian = math.radians(angle)
    width = abs(np.sin(angle_radian) * old_height) + abs(np.cos(angle_radian) * old_width)
    height = abs(np.sin(angle_radian) * old_width) + abs(np.cos(angle_radian) * old_height)

    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    rot_mat[1, 2] += (width - old_width) / 2
    rot_mat[0, 2] += (height - old_height) / 2
    return cv2.warpAffine(image, rot_mat, (int(round(height)), int(round(width))), borderValue=background)


#grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#angle = determine_skew(grayscale)
#rotated = rotate(img, angle, (0, 0, 0))
#cv2.imwrite('output.png', rotated)

#img2 = cv2.imread('output.png')
#print(pytesseract.image_to_string(img2))

def skew_correct(image):
        img = cv2.imread(image)
        grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        angle = determine_skew(grayscale)
        rotated = rotate(img, angle, (0, 0, 0))
        cv2.imwrite('output.png', rotated)
        return 'output.png'