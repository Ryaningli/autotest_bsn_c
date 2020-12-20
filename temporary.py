from time import sleep
from selenium.webdriver.common.by import By

import page
from base.get_driver import GetDriver
from base.base import Base


driver = GetDriver().get_driver()
driver = Base(driver)

driver.base_input((By.CSS_SELECTOR, '[placeholder="请输入账号"]'), '18815596963')
driver.base_input((By.CSS_SELECTOR, '[placeholder="请输入密码"]'), 'abc123')
driver.base_click((By.XPATH, '/html/body/div/div/div[2]/div/div/div/div[2]/form/div/button/span'))
sleep(3)

# driver.base_add_cookie({"name": "Admin-Token", "value": "574a4050535b5744575f5041505f5f56495e5045465b"})

driver.base_go_to_page('http://120.78.132.70/service/createservice')
sleep(3)

driver.base_dropdown_input_select(page.arrow_loc, page.option_loc)

# 获取当前选项
print(driver.base_dropdown_input_get_current_option(page.arrow_loc, page.options))
