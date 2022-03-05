'''
Image scrapping from google image 

usage:- python3 main.py -s {googleseacrh} -p {save_path} -n {number_of_image_downloads}


'''

import os
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from webdriver_manager import driver
import argparse
from webdriver_manager.chrome import ChromeDriverManager


opts=webdriver.ChromeOptions()
opts.headless=True
driver=webdriver.Chrome(ChromeDriverManager().install(),options=opts)


def scroll_to_end(driver):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(5)


def directory_create(folder_path):
    try:
        if os.path.exists(folder_path):
            print(f"This directoer already exits {folder_path}")
        else:
            os.mkdir(folder_path)
    except OSError:
        print("Some exception are occured check your permison")

def getImageUrls(name,totalimage,driver):
    search_url="https://www.google.com/search?q={q}&client=opera&hs=tDE&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiCnv-R_or1AhUNE4gKHaTLAVkQ_AUoAXoECAEQAw&biw=1813&bih=952&dpr=1"
    driver.get(search_url.format(q=name))
    img_urls=set()
    img_count=0
    result_start=0
    while(img_count<totalimage):# extract actual image
        scroll_to_end(driver)
        thumbnail_result=driver.find_elements_by_xpath("//img[contains(@class,'Q4LuWd')]")
        print("stst",thumbnail_result)
        totalresults=len(thumbnail_result)
        print(f"Found: {totalresults} search result , Extracting line from {result_start}:{totalresults}")
        for img in thumbnail_result[result_start:totalresults]:
            while True:
                try:
                    img.click()
                    break
                except Exception as e:
                    print(e)
                    time.sleep(5)
            time.sleep(2)
            actual_images=driver.find_elements_by_css_selector('img.Q4LuWd')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'https' in actual_image.get_attribute('src'):

                    img_urls.add(actual_image.get_attribute('src'))
        
            img_count=len(img_urls)
            if img_count >= totalimage:
                print(f"Found : {img_count} image links")
                break
            else:
                print("Found: ",img_count,"Looking for more image links ...")
                load_more_button=driver.find_element_by_css_selector(".mye4qd")
                driver.execute_script("document.querySelector('.mye4qd').click();")
        
                    
            result_start=len(thumbnail_result)
        temp=len(img_urls) - totalimage
        for i in range(temp):
            img_urls.pop()
        print(len(img_urls))
    return img_urls
# print(getImageUrls("dogs",100,driver))

def downloadImages(folder_path,file_name,url):
    try:
        image_content=requests.get(url).content
    except Exception as e:
        print(f"Error: Could not Download {url} - {e}")
    try:
        image_file=io.BytesIO(image_content)
        image=Image.open(image_file).convert('RGB')
        file_path=os.path.join(folder_path,file_name)
        with open(file_path,"wb")as w:
            image.save(w,"JPEG",quality=85)
        print(f"saved- {url} - AT: {file_path}")
    except Exception as e:
        print(f"ERROR - Could Not save {url} - {e}")

def saveInDestFolder(searchname,destdir,totalImage,driver):
    directory_create(destdir)
    for name in list(searchname):
        path=os.path.join(destdir,name)
        if not os.path.isdir(path):
            os.mkdir(path)
        print("Current path",path)
        totallinks=getImageUrls(name,totalImage,driver)
        print('totalLinks',totallinks)
        if totallinks is None:
            print("image not found :-",name)
            continue
        else:
            for i ,link in enumerate(totallinks):
                file_name=f"{i+1}.jpg"
                downloadImages(path,file_name,link)

def args_parse():
    parse=argparse.ArgumentParser()
    parse.add_argument("-s","--search",nargs="*",help="type the name of image you want to download",required=True)
    parse.add_argument("-p","--path",help="path the saving path",required=True)
    parse.add_argument("-n","--n_images",type=int,help="enter of number of images")
    argument=parse.parse_args()
    search=argument.search
    path=argument.path
    number=argument.n_images
    saveInDestFolder(search,path,number,driver)



if __name__=="__main__":
    args_parse()
    

