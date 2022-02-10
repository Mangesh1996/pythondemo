import cv2 as cv
import numpy as np


def crop_img(img):
    im=cv.imread(img)
    for i in range(5):

        r=cv.selectROI("Image",im,fromCenter=False,showCrosshair=False)
        imCrop=im[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]
        cv.imshow(f"Image{i}",imCrop)
    cv.waitKey(0)


if __name__=="__main__":
    img="image.jpg"
    crop_img(img)