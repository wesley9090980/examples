from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# 设置chrome为无界面浏览器
options = Options()
options.add_argument('--headless')
#使用selenium+firefox实现爬虫  抓取政策重要新闻  uu
#
driver = webdriver.Firefox(executable_path=r"D:\geckodriver\geckodriver.exe",options=options)#
driver.get("http://www.gov.cn/xinwen/index.htm")
elems=""
assert "新闻" in driver.title
try:
    elems = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[1]/div[1]/div[4]/div[1]/div[2]/dl/dd/h4/a"))
    )
except:
    print("出错了！！")
assert "No results found." not in driver.page_source
print("新闻标题为:  \t \n")
href=""
for elem in elems:
    title=elem.get_attribute("innerHTML")
    href=elem.get_attribute("href")
    print("{}，对应链接为>>>>{} \n".format(title,href))
driver.close()