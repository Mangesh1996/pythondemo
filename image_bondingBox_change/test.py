"""
This python file are modify annouation value in the xml depend on image resoluation
if resoulation change xml annouation point are the change

Usage : images_shape.py

"""
# import libary
from fileinput import filename
import xml.etree.ElementTree as ET
from glob import glob
import os
import ffmpeg
import os
import cv2
import shutil
from datetime import datetime
# creat the method to modify the xml file 
def modify_xml(path,save,new_size):
    xmls=sorted(glob(f"{path}/*.xml"),key=os.path.basename)
    current_time=datetime.today().strftime("%d-%M-%Y-%H:%M:%S")
    i=0
    for e in xmls:
        xmlroot=ET.parse(e).getroot()
        name=e.split("/")[-1].split(".")[0]
        xmlroot.find("filename").text=str(current_time+name)
        
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
        i+=1
        tree.write(f"{save}/{current_time}"+name+"{i}.xml")
def image_convertion(paths,save,new_size):
    images=sorted(glob(paths+"/*"),key=os.path.basename)
    current_time=datetime.today().strftime("%d-%M-%Y-%H:%M:%S")
    exts=('.jpeg', '.JPEG', '.png', '.PNG', '.jpg', '.JPG')
    for path in images:
        if path.endswith(exts):
            
            name=path.split("/")[-1]
            try:
                process=(
                    ffmpeg
                    .input(path)
                    .filter("scale",width=new_size[0],height=new_size[1])
                    .output(f"{save}/{current_time}{name}")
                    .overwrite_output()
                    .run(quiet=True)
                    )
            except Exception as e:
                print(e,path)
                image=cv2.imread(path)
                size=(new_size[0],new_size[1])
                resize=cv2.resize(image,size)
                cv2.imwrite(f"{save}/cv_{name}",resize)  

def copy_pair(path,save):
    file=sorted(os.listdir(path))
    exts=(".png", ".jpg")
    xml=[i.replace(".xml","")for i in file if i.endswith(".xml")]
    img=[(i.split(".")[-2]) for i in file if i.endswith(exts)]
    # print(img)
    odd="odd"
    # for i in file:
    #     if i.endswith(exts):
    #         img.append(i.split(".")[-2])
    for i in xml:
        if i in img:
            shutil.copy(os.path.join(path,f"{i}.xml"),save)
        else:
            shutil.copy(os.path.join(path,f"{i}.xml"),odd)
    for f in file:
        if f.endswith(exts):
            shutil.copy(os.path.join(path,f),save)

            
    



if __name__ == "__main__":
    path=os.path.join(os.getcwd(),"save")
    # rename_files(path)
    images="/home/diycam/Desktop/work/image_bondingBox_change/images"
    save="temp"
    saves="save"
    size=[2020,920]
    modify_xml(images,save,size)
    image_convertion(images,save,size)
    # # filename=os.path.join(os.getcwd(),images)
    copy_pair(path,saves)
    
    

