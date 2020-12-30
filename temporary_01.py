from selenium import webdriver


from base.wait_loading import WaitLoading


def wait_loading():
    WaitLoading(driver, timeout=20).until_not(lambda x: x.find_element_by_css_selector('.el-loading-text'))


driver = webdriver.Firefox()
driver.maximize_window()

driver.get('http://192.168.0.158/login')
driver.find_element_by_css_selector('[name="phone "]').send_keys('18815596964')
driver.find_element_by_css_selector('[name="password"]').send_keys('abc123')

wait_loading()
# loading(driver)
driver.find_element_by_css_selector('#app > div > div.main.el-row > div > div > div > div.clearfix.el-col.el-col-24.el-col-xs-24.el-col-sm-24.el-col-md-9 > form > div > button').click()

wait_loading()
# loading(driver)
driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.serverbox > div:nth-child(1) > div.text-center.mt10 > button').click()
driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.oneStep > form > div:nth-child(1) > div > div > input').send_keys('asfsafsafsa')

wait_loading()
# loading(driver)
driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.oneStep > form > div:nth-child(2) > div > div > div > span > span > i').click()

wait_loading()
# loading(driver)
driver.find_element_by_css_selector('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1) > span').click()