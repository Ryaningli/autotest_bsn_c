from selenium.webdriver.common.by import By

URL = 'http://120.78.132.70/homepage/homepage'

news = By.LINK_TEXT, '新闻'
hao = By.LINK_TEXT, 'hao123'
baidu_map = By.LINK_TEXT, '地图'
vid = By.LINK_TEXT, '视频'

dropdown = By.CSS_SELECTOR, '#select'

arrow_loc = By.CSS_SELECTOR, '.el-icon-arrow-up'
option_loc = By.CSS_SELECTOR, '.el-select-dropdown__list>li:nth-child(1)'

# options = By.CSS_SELECTOR, '.el-select-dropdown__item'
options = By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li'

new_op = By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[3]'