import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
import random
# 设置chrome为无界面浏览器
options = Options()
options.add_argument('--headless')
headers = {"User-Agent":
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
# 使用selenium+firefox实现爬虫  抓取政策重要新闻  uu
driver = webdriver.Firefox(
    executable_path=r"D:\geckodriver\geckodriver.exe", options=options)
driver.get("https://cn.bing.com/images/search?q=%e6%80%a7%e6%84%9f%e7%be%8e%e5%a5%b3&qs=n&form=QBILPG&sp=-1&pq=%e6%80%a7%e6%84%9f%e7%be%8e%e5%a5%b3&sc=1-4&cvid=A755D80EF5084882B031DEEADA627594&first=1&tsc=ImageBasicHover")
elems = ""
assert "性感" in driver.title

elems = WebDriverWait(driver, 1000).until(
     EC.presence_of_all_elements_located((By.CLASS_NAME, "mimg"))
     )

assert "No results found." not in driver.page_source
href = ""
def run(elems):
    elemslen=0
    for elem in elems:
        src = elem.get_attribute("src")
        if str(src).startswith("http"):
            elemslen +=1
    
    print("长度为------"+str(elemslen))
    for elem in elems:
        src = elem.get_attribute("src")
        if str(src).startswith("http"):
            r = requests.get(src, headers=headers)
            # driver.back()
            f = open("imgs/{}.jpg".format(random.random()), "wb")
            f.write(r.content)
            elemslen-=1
            time.sleep(1)
            if elemslen<=0:
                driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

                elems = WebDriverWait(driver, 1000).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "mimg"))
        )   
                time.sleep(5)
                run(elems)
    

run(elems)   
driver.close()
