from sys import platform
import sys
import urllib.request
import re
import os
import zipfile
import stat


def webdriver_executable():
    if platform == "linux" or platform =="linux2" or platform =="darwin":
        return "chromedriver"
    return "chromedriver.exe"
def get_version():
    ts=os.popen("google-chrome --version").read().split("\n")
    return ts[0].split(" ")[2]
    
def Chromedriver_install():
    current_chrome_version=get_version()
    def os_info():
        filename=""
        is_64bits=sys.maxsize>2**32
        if platform == "linux" or platform == "linux2":
            filename += "linux"
            filename += "64" if is_64bits else "32"
        elif platform == "darwin": filename += "mac64"
        elif platform == "win32":filename += "win32"
        filename += ".zip"
        return filename
    def webdriver_path(path):
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            print("webdriver are already exists")
    try:
        url="https://chromedriver.chromium.org/downloads"
        base_driver_url="https://chromedriver.storage.googleapis.com/"
        pattern="https://.*?path=(\d+\.\d+\.\d+\.\d+)"
        filename = "chromedriver_"+os_info()
        webdriver_path("webdriver")
        # Download of latesst driver
        stream=urllib.request.urlopen(url)
        content=stream.read().decode('utf-8')
        # #Parse the latest version
        all_match=re.findall(pattern,content)
        if all_match:
            #version of laters driver
            if (current_chrome_version !=""):
                print("[INFO] updating latest driver")
                all_match=list(set(re.findall(pattern,content)))
                current_chrome_version=".".join(current_chrome_version.split(".")[:-1])
                version_match=[i for i in all_match if re.search("^%s"%current_chrome_version,i)]
                version=version_match[0]
            else:
                print("Info installing new chromedriver")
                version=all_match[1]
                print(version)
            driver_url=base_driver_url+version+"/"+filename

            app_path=os.path.dirname(os.path.realpath(__file__))
            chromedriver_path=os.path.normpath(os.path.join(app_path,"webdriver",webdriver_executable()))
            print(driver_url)
            file_path=os.path.normpath(os.path.join(app_path,"webdriver",filename))
            urllib.request.urlretrieve(driver_url,file_path)

            #Unzip the file into directory
            with zipfile.ZipFile(file_path,'r') as zip_ref:
                zip_ref.extractall(os.path.normpath(os.path.join(app_path,"webdriver")))
            st=os.stat(chromedriver_path)
            os.chmod(chromedriver_path,st.st_mode | stat.S_IEXEC)
            print("INFO : latest chromediver download ")
            #cleanup
            os.remove(file_path)
            result =True
    except Exception as e:
        print(e)
    return 0


# Chromedriver_install()
# get_version()