import time
from threading import Thread

from selenium import webdriver
#DistributedParallelTest:分布式并行测试
from selenium.webdriver.common.by import By


def baiduSearch(hubUrl, capabilities):
    driver = webdriver.Remote(hubUrl,desired_capabilities=capabilities)
    driver.get("http://www.baidu.com")
    driver.find_element(By.ID, "kw").send_keys("hello")
    driver.find_element(By.ID, "su").click()
    time.sleep(5)
    print("测试成功，浏览器以及平台为：",capabilities)
    # driver.quit()

listOfConditions = [
    {"browserName":"chrome","platform":"windows"},
    {"browserName":"firefox","platform":"windows"}
]

# listOfConditions = [
#     {"browserName":"chrome","platform":"windows"}
# ]
hubUrl = "http://192.168.1.9:4444/wd/hub"

threads = []
for condition in listOfConditions:
    t = Thread(target=baiduSearch, args=(hubUrl, condition))
    threads.append(t)
    t.start()

#等待所有线程执行完毕
for t in threads:
    t.join()