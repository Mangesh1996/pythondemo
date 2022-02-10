import glob
import os


def check_format(path):
    format=sorted(glob.glob(f"{path}/*"),key=os.path.basename)
    uni=set()
    for i in format:
        st=i.split("/")[-1].split(".")[1]
        uni.add(st)
    print(uni)
check_format("/home/diycam/Desktop/work/image_bondingBox_change/save")