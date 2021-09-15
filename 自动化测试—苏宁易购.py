# 任务2：
#     在苏宁的非登陆的情况，搜索一个商品，添加购物车。

from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.suning.com")
driver.find_element_by_xpath("//input[@id='searchKeywords']").send_keys("华为手机")
driver.find_element_by_xpath("//input[@id='searchSubmit']").click()
driver.find_element_by_xpath("//*[@id='0071225719-12137074678']/div/div/div[1]/div[1]/a").click()
data = driver.window_handles
driver.switch_to_window(data[1])
driver.find_element_by_xpath("//a[@id='addCart']").click()
time.sleep(100)
driver.quit()

