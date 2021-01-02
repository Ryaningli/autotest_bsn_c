from selenium.webdriver.common.by import By

# URL = 'http://192.168.0.158/login'
URL = 'http://www.fjbsn.com/login'


login_username = By.CSS_SELECTOR, '[name="phone "]'
login_password = By.CSS_SELECTOR, '[name="password"]'
login_login_button = By.CSS_SELECTOR, '.loginbtn'
login_if_success = By.CSS_SELECTOR, '.databox>span'
login_error_msg = By.CSS_SELECTOR, 'body > div:last-child.el-message.el-message--error'
login_logout = [(By.CSS_SELECTOR, '.el-icon-caret-bottom'), (By.CSS_SELECTOR, '[style="display: block;"]')]


'''登录日志'''
login_log = [(By.CSS_SELECTOR, 'ul>div:nth-child(7)>li>div>i'),
             (By.CSS_SELECTOR, 'ul>div:nth-child(7)>li>ul>div:nth-child(4)>a>li')]
login_log_count = By.CSS_SELECTOR, 'tbody>tr'
login_log_time = By.CSS_SELECTOR, 'tbody>tr:nth-child(1)>td:nth-child(1)>div'
login_log_ip = By.CSS_SELECTOR, 'tbody>tr:nth-child(1)>td:nth-child(2)>div'
login_log_address = By.CSS_SELECTOR, 'tbody>tr:nth-child(1)>td:nth-child(3)>div'

'''以下为创建服务模块的元素'''
release_create_app_button = By.CSS_SELECTOR, '.addbtn'
release_input_app_name = By.CSS_SELECTOR, '[placeholder="请填写您的服务名称"]'
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