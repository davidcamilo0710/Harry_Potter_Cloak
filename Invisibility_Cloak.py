import cv2 as cv
import time
import numpy as np


print("Lets see you in pieces")


cap = cv.VideoCapture(0)
time.sleep(3)
background = 0

for i in range(40):
    ret, background = cap.read()

background = np.flip(background, axis=1)

while cap.isOpened():
    ret, img = cap.read()

    img = np.flip(img, axis=1)

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    value = (35, 35)

    blurred = cv.GaussianBlur(hsv, value, 0)

    # lower and upper ranges of blue

    lower_blue = np.array([25, 50, 50])
    upper_blue = np.array([32, 255, 255])
    mask1 = cv.inRange(hsv, lower_blue, upper_blue)

    lower_blue = np.array([101, 50, 38])
    upper_blue = np.array([110, 255, 255])
    mask2 = cv.inRange(hsv, lower_blue, upper_blue)

    mask = mask1 + mask2
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, np.ones((5, 5), np.uint8))

    # Replace cloack values of pixels with background

    img[np.where(mask == 255)] = background[np.where(mask == 255)]
    cv.imshow('Display', img)
    k = cv.waitKey(100)
    if k == 27:
        break
