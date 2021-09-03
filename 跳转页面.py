from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get(r"D:\python\autoweb01\练习的html\跳转页面\pop.html")#打开指定网页

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='goo']").click()

time.sleep(30)
driver.quit()