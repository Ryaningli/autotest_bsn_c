import page
from base.base import Base


class PageLoginLog(Base):
    # 点击登录日志
    def page_click_login_log(self):
        self.base_dropdown_select(page.login_log)

    # # 获取参考地址文字信息
    # def page_get_address(self):
    #     return self.base_get_text(page.login_log_address)

    # 统计条数
    def page_all(self):
        count = len(self.base_find_elements(page.login_log_count))
        for info in range(1, count + 1):
            login_log_time = (
                page.login_log_time[0], page.login_log_time[1][:19] + str(info) + page.login_log_time[1][20:])
            login_log_ip = (
                page.login_log_ip[0], page.login_log_ip[1][:19] + str(info) + page.login_log_ip[1][20:])
            login_log_address = (
                page.login_log_address[0], page.login_log_address[1][:19] + str(info) + page.login_log_address[1][20:])

            msg_time = self.base_get_text(login_log_time)
            msg_ip = self.base_get_text(login_log_ip)
            msg_address = self.base_get_text(login_log_address)

            print('本账号于 {} 在IP {} 登录，参考地址为 {}'.format(msg_time, msg_ip, msg_address))

    def page_all2(self):
        els = self.base_find_elements(page.login_log_count)
        for el in els:
            info = el.text.split('\n')
            print('本账号于 {} 在IP {} 登录，参考地址为 {}'.format(info[0], info[1], info[2]))