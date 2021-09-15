# 任务1：
#     京东和淘宝登陆的脚本，并且搜索一个商品和添加购物车。


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
# driver.get("https://passport.jd.com/new/login.aspx")
# driver.maximize_window()
# driver.find_element_by_link_text("账户登录").click()
# driver.find_element_by_xpath("//input[@id='loginname']").send_keys("15530875829")
# driver.find_element_by_xpath("//input[@id='nloginpwd']").send_keys("121628ruan")
# driver.find_element_by_xpath("//div[@class='login-btn']").click()
# ac = ActionChains(driver)
# button = driver.find_element_by_xpath("//*[@class='JDJRV-slide-btn']")
# img = driver.find_element_by_xpath("//div[@class='JDJRV-smallimg']")
# #5.鼠标操作
# ac.click_and_hold(button).move_by_offset(100,0).perform()
# ac.click_and_hold(img).move_by_offset(100,0).perform()
driver.get("https://www.jd.com")
driver.find_element_by_xpath("//input[@id='key']").send_keys("华为手机")
driver.find_element_by_xpath("//button[@class='button']").click()
driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[1]/div/div[1]/a").click()
data=driver.window_handles
driver.switch_to_window(data[1])
driver.find_element_by_xpath("//a[@id='InitCartUrl']").click()
time.sleep(100)
driver.quit()

