import os
import selenium
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from webdriver_manager import driver
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException


# install chrome drive  and luanch the chrome browser
driver=webdriver.Chrome(ChromeDriverManager().install())

#url for google image section
search_url="https://www.google.com/search?q={q}&client=opera&hs=y9r&source=lnms&tbm=isch&sa=X&ved=2ahUKEwit3ceT6or1AhVHFogKHfKvC0gQ_AUoAXoECAEQAw&biw=1813&bih=952&dpr=1"

#query for user define
# query=input("Enter the search keworkd")
#get query of google page
driver.get(search_url.format(q='car'))

# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# time.sleep(5)

imgresult=driver.find_elements_by_xpath("//img[contains(@class,'Q4LuWd')]")
totalresult=len(imgresult)
img_url=set()
for i in range(0,len(imgresult)):
    img=imgresult[i]
    try:
        img.click()
        time.sleep(2)
        actual_img=driver.find_elements_by_css_selector('img.Q4LuWd')
        for actual in actual_img:
            if actual.get_attribute('src')and 'https' in actual.get_attribute('src'):
                img_url.add(actual.get_attribute('src'))
    except ElementClickInterceptedException or ElementNotInteractableException as err:
        print(err)
os.chdir("save")
baseDir=os.getcwd()

for i ,url in enumerate(img_url):
    file_name=f"{i}.jpg"
    try:
        image_conten=requests.get(url).content
    except Exception as e:
        print(f"Error - Could Not download {url} - {e}")
    try:
        image_file=io.BytesIO(image_conten)
        image=Image.open(image_file).convert('RGB')
        file_path=os.path.join(baseDir,file_name)
        with open(file_path,'wb')as f:
            image.save(f,"JPEG",quality=85)
        print(f"Saved - {url} - AT: {file_path}")
    except Exception as e:
        print(f"ERROR - COULD NOT SAVE {url} - {e}")
        