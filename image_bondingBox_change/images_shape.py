"""
This python file are modify annouation value in the xml depend on image resoluation
if resoulation change xml annouation point are the change

Usage : images_shape.py

"""
# import libary
import xml.etree.ElementTree as ET
from glob import glob
import os
# creat the method to modify the xml file 
def modify_xml(path,save,new_size):
    xmls=sorted(glob(f"{path}/*.xml"),key=os.path.basename)
    
    for e in xmls:
        xmlroot=ET.parse(e).getroot()
        name=e.split("/")[-1].split(".")[0]
        size_node=xmlroot.find("size")
        width=size_node.find("width").text
        height=size_node.find("height").text
        scale_x=new_size[0]/int(width)
        scale_y=new_size[1]/int(height)
        size_node.find("width").text=str(new_size[0])
        size_node.find("height").text=str(new_size[1])
        for member in xmlroot.findall("object"):
            bndbox=member.find("bndbox")
            xmin=bndbox.find("xmin")
            ymin=bndbox.find("ymin")
            xmax=bndbox.find("xmax")
            ymax=bndbox.find("ymax")
            xmin.text=str(round(int(xmin.text)*scale_x))
            ymin.text=str(round(int(ymin.text)*scale_y))
            xmax.text=str(round(int(xmax.text)*scale_x))
            ymax.text=str(round(int(ymax.text)*scale_y))
        tree=ET.ElementTree(xmlroot)
        tree.write(f"{save}/"+name+".xml")

if __name__ == "__main__":
    images="/home/diycam/Downloads/fire_template/dataset/annotation_images"
    filename=os.path.join(os.getcwd(),images)
  
    save="save1"
    size=[2020,920]
    modify_xml(filename,save,size)