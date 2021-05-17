from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# 设置chrome为无界面浏览器
# options = Options()
# options.add_argument('--headless')

driver = webdriver.Firefox(executable_path=r"D:\geckodriver\geckodriver.exe")#,options=options
driver.get("http://www.pbc.gov.cn/")
elem=""
assert "中国人民银行" in driver.title
try:
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/table[2]/tbody/tr/td[3]/table[2]/tbody/tr[2]/td/div/div/div[2]/table/tbody/tr/td/a"))
    )
except:
    print("出错了！！")
assert "No results found." not in driver.page_source
title=elem.get_attribute("title")
print(title)
elem.click()
driver.save_screenshot('screenshot.png')
driver.close()