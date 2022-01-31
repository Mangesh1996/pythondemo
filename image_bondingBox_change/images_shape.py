"""
This python file are modify annouation value in the xml depend on image resoluation
if resoulation change xml annouation point are the change

Usage : images_shape.py

"""
# import libary
import xml.etree.ElementTree as ET
import cv2 as cv
from glob import glob
import os
# creat the method to modify the xml file 
def modifiy_xml(path,save,new_size):
    output=sorted(glob(f"{path}/*.xml"))
    for i in output:
        xmlroot=ET.parse(i).getroot()
        images="images"
        name=i.split("/")[-1].split(".")[0]
        print(name)
        images=sorted(glob(images+f"/{name}.png"),key=os.path.basename)
        # extract the old image resolution using opencv
        for imgs in images:
            img=cv.imread(imgs)
            scale_x=new_size[0]/img.shape[1]
            scale_y=new_size[1]/img.shape[0]
            print(scale_x,"fro png")
        sizes_node=xmlroot.find("size")
        sizes_node.find("width").text=str(new_size[0])
        sizes_node.find("height").text=str(new_size[1])
        for member in xmlroot.findall("object"):
            bndbox=member.find("bndbox")
            xmin=bndbox.find('xmin') 
            ymin = bndbox.find('ymin')
            xmax = bndbox.find('xmax')
            ymax = bndbox.find('ymax')
            #calcuate the new coordinate of annouation point
            xmin.text=str(round(int(xmin.text)*scale_x))
            ymin.text=str(round(int(ymin.text)*scale_y))
            xmax.text=str(round(int(xmax.text)*scale_x))
            ymax.text=str(round(int(ymax.text)*scale_y))

        tree=ET.ElementTree(xmlroot)
        #save to xml
        tree.write(f"{save}/"+name+".xml")
if __name__ == "__main__":
    images="images"
    filename=os.path.join(os.getcwd(),images)
  
    save="save"
    size=[1280,720]
    modifiy_xml(filename,save,size)