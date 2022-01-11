
import xml.etree.ElementTree as ET
import cv2 as cv
from glob import glob
import os

def modfiy_xml(path,save):
    output=sorted(glob(f"{path}/*.xml"))
    for i in output:
        xmlroot=ET.parse(i).getroot()
        images="images"
        name=i.split("/")[-1].split(".")[0]
        images=sorted(glob(images+f"/{name}.png"),key=os.path.basename)
        new_size=[1280,720]
        for imgs in images:
            img=cv.imread(imgs)
            scale_x=new_size[0]/img.shape[1]
            scale_y=new_size[1]/img.shape[0]
        sizes_node=xmlroot.find("size")
        sizes_node.find("width").text=str(new_size[0])
        sizes_node.find("height").text=str(new_size[1])
        for member in xmlroot.findall("object"):
            bndbox=member.find("bndbox")
            xmin=bndbox.find('xmin') 
            ymin = bndbox.find('ymin')
            xmax = bndbox.find('xmax')
            ymax = bndbox.find('ymax')
            xmin.text=str(round(int(xmin.text)*scale_x))
            ymin.text=str(round(int(ymin.text)*scale_y))
            xmax.text=str(round(int(xmax.text)*scale_x))
            ymax.text=str(round(int(ymax.text)*scale_y))

        tree=ET.ElementTree(xmlroot)

        tree.write(f"{save}/"+name+".xml")
if __name__ == "__main__":
    images="images"
    save="save"
    modfiy_xml(images,save)