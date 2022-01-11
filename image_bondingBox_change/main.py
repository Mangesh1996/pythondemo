"""
main.py It converted Image resoluation and also change annotation  point in xml file

usage : main.py

"""
# import libarayr and create python module
from image import image_convertion
from images_shape import modfiy_xml
import os

# create the method to check output file are preset 
# and run the image convetion and xml modificatiion module
def run(path,save,res):
    try:
        if not os.path.exists(save):
            os.mkdir(save)
        else:
            print("Already exists")
    except Exception as e:
        print(e)
    image_convertion(path,res,save)
    modfiy_xml(path,save,res)

if __name__=="__main__":
    path="images"
    save="save"
    res=[1280,720]
    run(path,save,res)
