
import cv2 as cv
from glob import glob
from bs4 import BeautifulSoup
import os


def resize(path,new_size):
    images=sorted(glob(path+"/*.png"),key=os.path.basename)
    xmls=sorted(glob(path+"/*.xml"),key=os.path.basename)
    bndbox=[]
    for img in images:
        img=cv.imread(img)
        scale_x=new_size[0]/img.shape[1]
        scale_y=new_size[1]/img.shape[0]
        for xml in xmls:
            with open(xml,"r")as data:
                read=data.read()
            bs_data=BeautifulSoup(read,'xml')
            obj=bs_data.find_all("object")
            x_min=bs_data.find_all("xmin")
            y_min=bs_data.find_all("ymin")
            x_max=bs_data.find_all("xmax")
            y_max=bs_data.find_all("ymax")
                
            for i in range(len(obj)):
                xmin=int(x_min[i].get_text())
                ymin=int(y_min[i].get_text())
                xmax=int(x_max[i].get_text())
                ymax=int(y_max[i].get_text())
                new_xmin=round(float(xmin) * scale_x)
                new_ymin=round(float(ymin) * scale_y)
                new_xmax=round(float(xmax) * scale_x)
                new_ymax=round(float(ymax) * scale_y)
                bndbox.append([new_xmin,new_ymin,new_xmax,new_ymax])
    return bndbox
                

            
        


if __name__=="__main__":
    images="images"
    new_res=[1280,720]

    print(resize(images,new_res))