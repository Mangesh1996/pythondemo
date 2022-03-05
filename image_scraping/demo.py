from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os as sys
import requests
import io
from PIL import Image


options=Options()
driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
q="kings"

driver.get(f"https://www.google.com/search?q={q}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjK8qC8nan2AhWryIsBHRvtCjkQ_AUoAXoECAEQAw&biw=1920&bih=907")
image_url=[]
count=0
missed_count=0
indx=1
time.sleep(3)

while 5 > count:
    try:
        imgurl=driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img'%(str(indx)))
        imgurl.click()
        missed_count=0
    except Exception:
        missed_count +=1
        if missed_count>10:
            print("missing")
            break
    try:
        time.sleep(1)
        class_names=["n3VNCb"]
        images=[]
        images = [driver.find_elements_by_class_name(class_name) for class_name in class_names if len(driver.find_elements_by_class_name(class_name)) != 0 ][0]
        
        for image in images:
            src_link=image.get_attribute("src")
            if (("http" in src_link) and (not "encrypted" in src_link)):
                print(src_link)
                image_url.append(src_link)
                count+=1       
                break
    except Exception as e:
        print("not get link")
    try:
        if(count%3==0):
            driver.execute_script("window.scrollTo(0,"+str(indx*60)+");")
        element=driver.find_element_by_class_name|("mye4qd")
        element.click()
        print("Load more photos")
        time.sleep(3)
    except Exception:
        time.sleep(1)
    indx +=1
    # driver.quit()
    # print(image_url)


