from time import sleep

import page
from base.base import Base


class PageLogin(Base):
    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_password(self, password):
        self.base_input(page.login_password, password)
        # self.base_loading()
        sleep(0.3)

    # 点击登录按钮
    def page_click_login_button(self):
        self.base_click(page.login_login_button)
        self.base_loading()

    # 判断登录是否成功
    def page_login_if_success(self, username):
        if self.base_get_text(page.login_if_success, timeout=3) == username[:3] + '****' + username[-4:]:
            return True
        else:
            return False

    # 点击退出登录
    def page_click_logout(self):
        self.base_click(page.login_logout[0])
        self.base_click(page.login_logout[1])

    # 获取登录失败提示框文本
    def page_get_error_msg(self):
        return self.base_get_text(page.login_error_msg)

    # 登录业务组合
    def page_login(self, username, password):
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_button()

    # 登录成功（依赖）
    def page_login_success(self, username='18815596963', password='abc123'):
        self.page_login(username, password)