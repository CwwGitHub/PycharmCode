from selenium import webdriver
from selenium.webdriver.common.by import By
import time

nodeCondition = {
    "browserName":"chrome"
}

driver = webdriver.Remote("http://192.168.1.9:4444/wd/hub",desired_capabilities=nodeCondition)
driver.get("http://www.baidu.com")
driver.find_element(By.ID,"kw").send_keys("hello")
driver.find_element(By.ID,"su").click()
time.sleep(5)
#driver.quit()