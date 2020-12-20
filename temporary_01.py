from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()

driver.get('http://120.78.132.70/homepage/homepage')
sleep(1)
driver.find_element_by_css_selector('[placeholder="请输入账号"]').send_keys('18815596963')
sleep(1)
driver.find_element_by_css_selector('[placeholder="请输入密码"]').send_keys('abc123')
sleep(1)
driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[2]/form/div/button/span').click()
sleep(1)
# driver.add_cookie({"name": "Admin-Token", "value": "574a4050535b5744575f5041505f5f56495e5045465b"})
driver.get('http://120.78.132.70/service/createservice')

sleep(3)
# 点击箭头
driver.find_element_by_css_selector('.el-icon-arrow-up').click()

els = driver.find_elements_by_css_selector('.el-select-dropdown__item')

for el in els:
    print(el.get_attribute('class'))