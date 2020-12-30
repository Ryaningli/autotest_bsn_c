from selenium.webdriver.common.by import By

URL = 'http://192.168.0.158/login'

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

login_username = By.CSS_SELECTOR, '[name="phone "]'
login_password = By.CSS_SELECTOR, '[name="password"]'
login_login_button = By.CSS_SELECTOR, '.loginbtn'


'''以下为创建服务模块的元素'''
release_create_service_button = By.CSS_SELECTOR, '.addbtn'
release_input_service_name = By.CSS_SELECTOR, '[placeholder="请填写您的服务名称"]'
release_frame_type = [(By.CSS_SELECTOR, '.el-select__caret'),
                      (By.CSS_SELECTOR, '.el-select-dropdown__wrap>ul>li')]
release_step1_next = By.CSS_SELECTOR, '.Btnbox button'
release_choice_tps = [(By.CSS_SELECTOR, '.el-form--label-top>div>div>div>div>span>span>i'),
                      (By.CSS_SELECTOR, '[x-placement="bottom-start"]>div>div>ul>li:nth-child(1)')]
release_choice_capacity = [(By.CSS_SELECTOR, '.el-form--label-top>div:nth-child(2)>div>div>div>span>span>i'),
                           (By.CSS_SELECTOR, '[x-placement="bottom-start"]>div>div>ul>li:nth-child(1)')]
release_step2_next = By.CSS_SELECTOR, '.Btnbox button'
release_node1 = By.CSS_SELECTOR, 'tr:nth-child(1)>td>div>label>span>span'
release_node2 = By.CSS_SELECTOR, 'tr:nth-child(2)>td>div>label>span>span'
release_node3 = By.CSS_SELECTOR, 'tr:nth-child(3)>td>div>label>span>span'
release_pay_type = By.CSS_SELECTOR, 'div.mt20.tab :nth-child(2)'
release_confirm_purchase = By.CSS_SELECTOR, '.el-button.primary'
release_pay_now = By.CSS_SELECTOR, '.el-button--primary.surebtn'