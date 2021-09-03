from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get(r"D:\python\autoweb01\练习的html\弹框的验证\dialogs.html")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='alert']").click()
# 切换至弹窗
al = driver.switch_to_alert()
time.sleep(6)
al.accept()
time.sleep(6)
driver.find_element_by_xpath("//*[@id='confirm']").click()
time.sleep(6)
al.accept()
time.sleep(6)
driver.find_element_by_xpath("//*[@id='confirm']").click()
time.sleep(6)
al.dismiss()
time.sleep(6)
driver.quit()
# accept - 点击【确认】按钮
# dismiss - 点击【取消】按钮（如有按钮）








