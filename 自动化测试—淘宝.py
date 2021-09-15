# 任务1：
#     淘宝登陆的脚本，并且搜索一个商品和添加购物车。

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains # actionchains 事件链
import time

driver = webdriver.Chrome()#使用谷歌浏览器

driver.get("https://www.taobao.com/")#打开淘宝网页链接

driver.maximize_window()#窗口最大化

driver.find_element_by_link_text("亲，请登录").click()#点击登录

driver.find_element_by_xpath("//*[@aria-label='会员名/邮箱/手机号']").send_keys("#账号")#输入账号

# driver.find_element_by_xpath("//*[@placeholder=请输入登录密码]").send_keys("#密码")输入密码

driver.find_element_by_id("fm-login-password").send_keys('lj200058')#输入密码

driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
time.sleep(3)
a = driver.find_element_by_xpath('//*[@id="baxia-dialog-content"]')
driver.switch_to.frame(a)
time.sleep(5)
ele = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')

ac = ActionChains(driver)
time.sleep(2)
ac.click_and_hold(ele).move_by_offset(200,0).perform()
ac.release() # 释放


time.sleep(2)

driver.quit()
