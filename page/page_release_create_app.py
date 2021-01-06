import page
from base.base import Base


class PageRelease(Base):
    # 输入用户名
    def page_input_username(self):
        self.base_input(page.login_username, '18815596963')

    # 输入密码
    def page_input_password(self):
        self.base_input(page.login_password, 'abc123')
        self.base_loading()

    # 点击登录按钮
    def page_click_login_button(self):
        self.base_click(page.login_login_button)
        self.base_loading()

    # 点击创建服务按钮
    def page_click_create_service_button(self):
        self.base_click(page.release_create_app_button)

    # 输入服务名称
    def page_input_service_name(self, app_name):
        self.base_input(page.release_input_app_name, app_name)
        self.base_loading()

    # 选择框架类型
    def page_choice_frame_type(self):
        self.base_dropdown_input_select(page.release_frame_type)

    # 点击下一步
    def page_click_step1_next(self):
        self.base_click(page.release_step1_next)
        self.base_loading()

    # 选择计算资源
    def page_choice_tps(self):
        self.base_dropdown_input_select(page.release_choice_tps)

    # 选择存储容量
    def page_choice_capacity(self):
        self.base_dropdown_input_select(page.release_choice_capacity)

    # 点击下一步
    def page_click_step2_next(self):
        self.base_click(page.release_step2_next)
        self.base_loading()

    # 选择城市节点
    def page_choice_node(self):
        self.base_click(page.release_node1)
        self.base_loading()
        self.base_click(page.release_node2)
        self.base_loading()
        self.base_click(page.release_node3)
        self.base_loading()

    # 选择支付方式
    def page_choice_pay_mode(self):
        self.base_click(page.release_pay_type)
        self.base_loading()

    # 点击确认购买
    def page_click_confirm_purchase_button(self):
        self.base_click(page.release_confirm_purchase)

    # 业务组合
    def page_create_app(self, service_name):
        self.page_click_create_service_button()
        self.page_input_service_name(service_name)
        self.page_choice_frame_type()
        self.page_click_step1_next()
        self.page_choice_tps()
        self.page_choice_capacity()
        self.page_click_step2_next()
        self.page_choice_node()
        self.page_choice_pay_mode()
        self.page_click_confirm_purchase_button()
