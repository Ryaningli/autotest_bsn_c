from selenium.webdriver.common.by import By

URL = 'http://192.168.0.158/login'
# URL = 'http://www.fjbsn.com/login'

'''登录'''
# 成功登录用的账号密码，供其他模块测试使用
username = '18815596964'
password = 'abc123'

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

'''配置升级'''
# 个人主页我的发布按钮
config_up_myapp = [(By.CSS_SELECTOR, 'ul>div:nth-child(4)>li>div>i'),
                   (By.CSS_SELECTOR, 'ul>div:nth-child(4)>li>ul>div:nth-child(1)>a>li')]

# 我的发布服务的配置升级按钮（先悬停再点击）
config_up_button = [(By.CSS_SELECTOR, '.el-icon-arrow-down.el-icon--right'),
                    (By.CSS_SELECTOR, 'body>ul>li:nth-child(5)')]

# 新增城市节点按钮
config_up_add_city_button = By.CSS_SELECTOR, 'section>div>div.flex>div.addBtn>button'

# 新增城市页面，城市多选框
config_up_add_city_select = By.CSS_SELECTOR, '[aria-label="新增城市节点"]>div:nth-child(2)>div:nth-child(2)>div:nth-child(3)>table>tbody>tr>td>div>label>span>span'

# 新增城市页面，确定按钮
config_up_add_city_enter = By.CSS_SELECTOR, '.el-button.sureBtn'

# 配置升级前的价格
config_up_get_old_price = By.CSS_SELECTOR, 'section>div>div.showBox>div:nth-child(1)'

# tps价格
config_up_tps_price = By.CSS_SELECTOR, 'section>div>div:nth-child(3)>div>div.el-table__body-wrapper>table>tbody>tr>td:nth-child(3)'

# 容量价格
config_up_capacity_price = By.CSS_SELECTOR, 'section>div>div:nth-child(3)>div>div.el-table__body-wrapper>table>tbody>tr>td:nth-child(4)'

# 当前节点数
config_up_current_node = By.CSS_SELECTOR, 'section>div>div:nth-child(3)>div>div.el-table__body-wrapper>table>tbody>tr>td:nth-child(5)'

# 支付周期
config_up_pay_type = By.CSS_SELECTOR, 'section>div>div.showBox>div:nth-child(1)>p'

# 上个支付周期总价格
config_up_old_price = By.CSS_SELECTOR, 'section>div>div.showBox>div:nth-child(1)>span'

# 到期时间
config_up_expired_time = By.CSS_SELECTOR, 'section>div>div.showBox>div:nth-child(3)>span'

# 获取页面上显示的应付价格
config_up_page_pay_price = By.CSS_SELECTOR, 'section>div>div>div:nth-child(4)>span'

# tps下拉框
config_up_tps = [(By.CSS_SELECTOR, 'div.adjust>div:nth-child(1)>div>div>div>span>span>i'),
                     (By.CSS_SELECTOR, '[x-placement$="-start"]>div>div>ul>li')]

# 容量下拉框
config_up_capacity = [(By.CSS_SELECTOR, 'div.adjust > div:nth-child(2) > div > div > div > span > span > i'),
                          (By.CSS_SELECTOR, '[x-placement$="-start"]>div>div>ul>li')]

# 每个城市节点的新增节点数
config_up_new_nodes = [(By.CSS_SELECTOR, 'tbody>tr>td>div>div>div>span>span>i'),
                       (By.CSS_SELECTOR, '[x-placement$="-start"]>div>div:nth-child(1)>ul>li')]