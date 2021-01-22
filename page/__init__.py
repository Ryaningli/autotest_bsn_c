URL = 'http://192.168.0.158/login'
# URL = 'http://www.fjbsn.com/login'

'''登录'''
# 成功登录用的账号密码，供其他模块测试使用
username = '18815596960'
password = 'abc123'

login_username = '[name="phone "]'
login_password = '[name="password"]'
login_login_button = '.loginbtn'
login_if_success = '.databox>span'
login_error_msg = 'body > div:last-child.el-message.el-message--error'
login_logout = ['.el-icon-caret-bottom',
                '[style="display: block;"]']


'''登录日志'''
login_log = ['ul>div:nth-child(7)>li>div>i',
             'ul>div:nth-child(7)>li>ul>div:nth-child(4)>a>li']
login_log_count = 'tbody>tr'
login_log_time = 'tbody>tr:nth-child(1)>td:nth-child(1)>div'
login_log_ip = 'tbody>tr:nth-child(1)>td:nth-child(2)>div'
login_log_address = 'tbody>tr:nth-child(1)>td:nth-child(3)>div'

'''以下为创建服务模块的元素'''
release_myapp = ['ul>div:nth-child(4)>li>div>i',
                   'ul>div:nth-child(4)>li>ul>div:nth-child(1)>a>li']
release_app_name_search = '[placeholder="服务名称"]'
release_app_search_button = 'section>div>div>div:nth-child(2)>button:nth-child(1)'
release_release_app = 'div>table>tbody>tr>td:nth-child(10)>div>div>span:nth-child(2)'

release_create_app_button = '.addbtn'
release_app_upload = 'tbody>tr>td>div>div>span:nth-child(2)'
release_input_app_name = '[placeholder="请填写您的服务名称"]'
release_frame_type = ['.el-select__caret',
                      '[x-placement$="-start"]>div>div>ul>li:nth-child(1)']
release_step1_next = '.Btnbox button'
release_choice_tps = ['form>div:nth-child(1)>div>div>div>span>span>i',
                      '[x-placement$="-start"]>div>div>ul>li:nth-child(1)']
release_choice_capacity = [ 'form>div:nth-child(2)>div>div>div>span>span>i',
                            '[x-placement$="-start"]>div>div>ul>li:nth-child(1)']
release_step2_next = '.Btnbox button'
release_nodes = 'td>div>label>span'
release_pay_types = 'div.mt20.tab>span'
release_confirm_purchase = '.el-button.primary'
release_pay_now = '.el-button--primary.surebtn'
release_pay_now_enter = '[aria-label="订单支付"]>div:nth-child(3)>span>button:nth-child(2)'
release_pay_result = '[aria-label="订单支付"]>div:nth-child(2)>div>h2'
release_over_enter = ' section>div>div:nth-child(8)>div>div>span>button.el-button--primary'
release_create_app_now = '[aria-label="订单支付"]>div:nth-child(2)>div>button'
release_app_type = ['form>div:nth-child(2)>div>div>div>span>span>i',
                    '[x-placement$="-start"]>div>div>ul>li']
release_input_version = '[placeholder="请输入版本号"]'
release_input_introduction = '[placeholder="请输入服务简介"]'
release_input_desc = '#editor>div:nth-child(2)>div>p'
release_input_cover = 'form>div:nth-child(5)>div>div>div>input'
release_add_doc = 'section>div>div>div:nth-child(3)>div>button'
release_add_doc_path = '[aria-label="新增文档资料"]>div:nth-child(2)>form>div:nth-child(1)>div>div>div:nth-child(2)>div>input'
release_add_doc_name = '[aria-label="新增文档资料"]>div:nth-child(2)>form>div:nth-child(2)>div>div>input'
release_add_doc_type = ['[aria-label="新增文档资料"]>div:nth-child(2)>form>div:nth-child(3)>div>div>div>span>span>i',
                        '[x-placement$="-start"]>div>div>ul>li']
release_add_doc_enter = '[aria-label="新增文档资料"]>div:nth-child(3)>div>button:nth-child(2)>span'
release_upload_app_next = '[style="text-align: center;"]>button:nth-child(1)>span'

release_chain_code_link = 'section>div>div>div:nth-child(1)>div>div>button:nth-child(2)'
release_chain_code_select = '[aria-label="使用预置链码包"]>div:nth-child(2)>div>div:nth-child(3)>table>tbody>tr>td>div>label>span>span'
release_chain_code_enter = '[aria-label="使用预置链码包"]>div:nth-child(3)>span>button:nth-child(2)>span'

release_add_functions_link = 'section>div>div>div:nth-child(3)>div>div>button>span'
release_add_functions_name = '[aria-label="新增链码包功能"]>div:nth-child(2)>form>div:nth-child(1)>div>div>input'
release_add_functions_select_chain_code = ['[aria-label="新增链码包功能"]>div:nth-child(2)>form>div:nth-child(2)>div>div>div>span>span>i',
                                           '[x-placement$="-start"]>div>div>ul>li']
release_add_functions_func_type = ['[aria-label="新增链码包功能"]>div:nth-child(2)>form>div:nth-child(3)>div>div>div>span>span>i',
                                   '[x-placement$="-start"]>div>div>ul>li']
release_add_functions_func = '[aria-label="新增链码包功能"]>div:nth-child(2)>form>div:nth-child(4)>div>div>input'
release_add_functions_enter = '[aria-label="新增链码包功能"]>div:nth-child(3)>span>button:nth-child(2)'

release_add_role_link = 'section>div>div>div:nth-child(5)>div>div>button>span'
release_add_role_name = '[aria-label="新增服务角色"]>div:nth-child(2)>form>div:nth-child(1)>div>div>input'
release_add_role_desc = '[aria-label="新增服务角色"]>div:nth-child(2)>form>div:nth-child(2)>div>div>input'
release_add_role_functions = '[aria-label="新增服务角色"]>div:nth-child(2)>div>div>label>span:nth-child(1)'
release_add_role_enter = '[aria-label="新增服务角色"]>div:nth-child(3)>span>button:nth-child(2)'

release_cert_type = 'div:nth-child(10)>label>span:nth-child(1).el-radio__input'
release_commit = 'section>div>div>div:nth-child(11)>button:nth-child(1)'

release_result_msg = 'section>div>div>div:nth-child(17)>div>div:nth-child(2)>div>h2'
release_commit_enter = 'section>div>div>div:nth-child(17)>div>div:nth-child(3)>span>button'


'''配置升级'''
# 个人主页我的发布按钮
config_up_myapp = ['ul>div:nth-child(4)>li>div>i',
                   'ul>div:nth-child(4)>li>ul>div:nth-child(1)>a>li']

# 我的发布服务的配置升级按钮（先悬停再点击）
config_up_button = ['.el-icon-arrow-down.el-icon--right',
                    '[x-placement$="-end"]>li:nth-child(5)']

# 新增城市节点按钮
config_up_add_city_button = 'section>div>div.flex>div.addBtn>button'

# 新增城市页面，城市多选框
config_up_add_city_select = '[aria-label="新增城市节点"]>div:nth-child(2)>div:nth-child(2)>div:nth-child(3)>table>tbody>tr>td>div>label>span>span'

# 新增城市页面，确定、取消按钮
config_up_add_city_enter = '.el-button.sureBtn'
config_up_add_city_cancel = '.cancelbtn'

# 配置升级前的价格
config_up_get_old_price = 'section>div>div.showBox>div:nth-child(1)'

# tps价格
config_up_tps_price = 'section>div>div:nth-child(3)>div>div.el-table__body-wrapper>table>tbody>tr>td:nth-child(3)'

# 容量价格
config_up_capacity_price = 'section>div>div:nth-child(3)>div>div.el-table__body-wrapper>table>tbody>tr>td:nth-child(4)'

# 当前节点数
config_up_current_node = 'section>div>div:nth-child(3)>div>div.el-table__body-wrapper>table>tbody>tr>td:nth-child(5)'

# 支付周期
config_up_pay_type = 'section>div>div.showBox>div:nth-child(1)>p'

# 上个支付周期总价格
config_up_old_price = 'section>div>div.showBox>div:nth-child(1)>span'

# 到期时间
config_up_expired_time = 'section>div>div.showBox>div:nth-child(3)>span'

# 获取页面上显示的应付价格
config_up_page_pay_price = 'section>div>div>div:nth-child(4)>span'

# tps下拉框
config_up_tps = ['div.adjust>div:nth-child(1)>div>div>div>span>span>i',
                 '[x-placement$="-start"]>div>div>ul>li']

# 容量下拉框
config_up_capacity = ['div.adjust>div:nth-child(2)>div>div>div>span>span>i',
                      '[x-placement$="-start"]>div>div>ul>li']

# 每个城市节点的新增节点数
config_up_new_nodes = ['tbody>tr>td>div>div>div>span>span>i',
                       '[x-placement$="-start"]>div>div:nth-child(1)>ul>li']

# 报错弹窗
config_up_error = 'body > div:last-child.el-message.el-message--error'
