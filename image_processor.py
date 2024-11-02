import cv2
import numpy as np

#input image path, outputs features of the image to make better inferences
def img_analyze(image_path):
    image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    brightness = np.mean(hsv[:,:,2])
    b, g, r = cv2.split(image)
    bg_ratio = np.mean(b)/np.mean(g)
    
    if bg_ratio > 1:
        temp = "cool"
    elif bg_ratio < 0.9:
        temp = "warm"
    else:
        temp = "neutral"
    return {
        "brightness": brightness,
        "temperature": temp
    }