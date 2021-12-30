driver.get(search_url.format(q="car"))

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(5)
imgresult=driver.find_elements_by_xpath("//img[contains(@class,'rg_i Q4LuWd')]")
totalresult=len(imgresult)
print(tot)