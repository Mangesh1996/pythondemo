import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)
if not cap.isOpened():
    print("error")
while True:
    res,frame=cap.read()
    cv.imshow('frame',frame)
    if cv.waitkey(1)& 0xFF ==ord('q'):
        break

cap.release()
cv.destroyAllwindows()