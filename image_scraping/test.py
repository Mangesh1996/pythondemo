
from selenium import webdriver
import time
import io
from PIL import Image
import requests
import os
from PIL import Image
from driver_install import Chromedriver_install
import argparse
from selenium.webdriver.chrome.options import Options

opts=Options()
opts.add_argument("--headless")
def directory_create(folder_path):
    try:
        if os.path.exists(os.path.join(os.getcwd(),folder_path)):
            print(f"This directory already exist {folder_path}")
        else:
            os.mkdir(folder_path)
    except OSError:
        print("some exception are occured check your permissions")
    
def get_url(name,num_img):
    seach_url=f"https://www.google.com/search?q={name}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjK8qC8nan2AhWryIsBHRvtCjkQ_AUoAXoECAEQAw&biw=1920&bih=907"
    
    #check the driver and install
    if not os.path.exists(os.path.join(os.getcwd(),"webdriver")):
        print("enter the block")
        Chromedriver_install()
        driver=webdriver.Chrome(executable_path=os.path.join(os.getcwd(),"webdriver/chromedriver"),options=opts)
    else:
        driver=webdriver.Chrome(executable_path=os.path.join(os.getcwd(),"webdriver/chromedriver"),options=opts)    
    driver.get(seach_url)
    image_url=list()
    img_count=1
    missed_count=0
    indx=1  
    print("Please wait geting url from google search page")    
    while num_img >= img_count:
        try:
            imgurl=driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img'%(str(indx)))
            imgurl.click()
            time.sleep(3)
            missed_count=0
        except Exception:
            missed_count +=1
            if missed_count>10:
                print("missing")
                break
        try:
            time.sleep(2)
            class_names=["n3VNCb"]
            images = [driver.find_elements_by_class_name(class_name) for class_name in class_names if len(driver.find_elements_by_class_name(class_name)) != 0 ][0]
            for image in images:
                src_link=image.get_attribute("src")
                if (("http" in src_link) and (not "encrypted" in src_link)):
                    image_url.append(src_link)
                    print( img_count,src_link)
                    img_count+=1     
                    break
        except Exception as e:
            print(e,"not get link")
        #scroll the page
        try:
            if(img_count%3==0):
                driver.execute_script("window.scrollTo(0,"+str(indx*60)+");")
            element=driver.find_element_by_class_name|("mye4qd")
            element.click()
            print("Load more photos")
            time.sleep(3)
        except Exception:
            time.sleep(1)
        indx +=1
    driver.quit()

    return image_url
    # print(image_url)

# get_url("cat",5)

def DownloadImage(folderpath,file_name,url):
    try:   

        image_content=requests.get(url,stream=True,headers={'User-Agent':'Mozilla/5.0'})
        if image_content.status_code==200:
            image_file=io.BytesIO(image_content.content)
            image=Image.open(image_file).convert('RGB')
            file_path=os.path.join(folderpath,file_name)
            with open(file_path,"wb") as w:
                image.save(w,"JPEG",quality=85)
            print(f"saved- {url} - AT : {file_path}")
        
    except Exception as e:
        print(f"Error : could not download{url}-{e}")

def saveInDestFolder(searchname,destdir,totalImage):
    directory_create(destdir)
    for name in list(searchname):
        path=os.path.join(destdir,name)
        if not os.path.isdir(path):
            os.mkdir(path)
        print("Current path",path)
        totallinks=get_url(name,totalImage)
        if totallinks is None:
            print("image not found :- ",name)
            continue
        else:
            for i,link in enumerate(totallinks):
                file_name=f"{name}_{i+1}.jpg"
                DownloadImage(path,file_name,link)

def args_parse():
    parse=argparse.ArgumentParser()
    parse.add_argument("-s","--search",nargs="*",help="type the name of image want to download",required=True)
    parse.add_argument("-p","--path",help="path the saving path",required=True)
    parse.add_argument("-n","--nimages",type=int,help="enter of numerb of images",required=True)
    argument=parse.parse_args()
    search=argument.search
    path=argument.path
    n_img=argument.nimages
    saveInDestFolder(search,path,n_img)



if __name__=="__main__":
    # search=["test"]
    # path="save"
    # n_img=10
    # saveInDestFolder(search,path,n_img)

    args_parse()
