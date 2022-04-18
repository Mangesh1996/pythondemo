import xml.etree.ElementTree as ET
import os

def generated(foldername,filename,pathname,objlist,folder_name):
    te=""
    for i in range(len(objlist)):
  
        
        w=f'''
            <object>
                <name>{objlist[i][4]}</name>
                <pose>Unspecified</pose>
                <truncated/>
                <difficult>0</difficult>
                <bndbox>
                    <xmin>{objlist[i][1]}</xmin>
                    <ymin>{objlist[i][0]}</ymin>
                    <xmax>{objlist[i][1] + objlist[i][2]}</xmax>
                    <ymax>{objlist[i][0] + objlist[i][3]}</ymax>
                </bndbox>
            </object>'''
        te+=w
    root = ET.fromstring(f'''<?xml version='1.0' encoding='utf-8'?>
        <annotation>
            <folder>{foldername}</folder>
            <filename>frame_{filename}.jpg</filename>
            <path>{pathname}/{folder_name}/{foldername}</path>
            <softinfo>vredefort</softinfo>
            <size>
                <width>1920</width>
                <height>1080</height>
                <depth>3</depth>
            </size>
            {te}

        </annotation>
        ''')
    tree = ET.ElementTree(root)
    tree.write(f"{os.getcwd()}/{folder_name}/stream_0/frame_{filename}.xml")
    objlist.clear()


print(os.getcwd())