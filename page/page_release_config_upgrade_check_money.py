import datetime
from time import sleep

from selenium.webdriver.common.by import By

import page
from base.base import Base


class PageReleaseConfigUpgradeCheckMoney(Base):
    # 点击我的发布
    def page_click_my_release(self):
        self.base_dropdown_input_select(page.config_up_myapp)
        self.base_loading()

    # 点击配置升级
    def page_click_config_upgrade(self):
        # 鼠标悬停至更多操作，然后再点击配置升级
        self.base_mouse_hover(page.config_up_button[0])
        self.base_click(page.config_up_button[1])
        self.base_loading()

    # 改动配置
    def page_change_config(self):
        self.base_dropdown_input_random_select(page.config_up_test)

    # 获取当前tps
    def page_get_tps(self):
        return self.base_dropdown_input_get_current_option(page.config_up_get_tps)

    # 获取当前容量
    def page_get_capacity(self):
        capacity = int(self.base_dropdown_input_get_current_option(page.config_up_get_capacity, timeout=1))
        return capacity

    # 获取支付周期总天数和剩余天数（支付类型，1是年，0是月）
    def page_get_expired_time(self, pay_type):
        msg = self.base_get_text(page.config_up_get_old_price)      # 获取含有支付周期文字的文本
        expired_time = self.base_get_text(page.config_up_expired_time)[:10]

        et = datetime.datetime.strptime(expired_time, '%Y-%m-%d').date()
        today = datetime.date.today()

        ct = None
        if '年' in msg:
            ct = datetime.date(et.year - 1, et.month, et.day)

        if '月' in msg:
            if et.month == 1:
                ct = datetime.date(et.year - 1, 12, et.day)
            else:
                ct = datetime.date(et.year, et.month - 1, et.day)

        remain_day = (et - today).days      # 剩余天数
        all_day = (et - ct).days    # 支付周期天数

    # 获取升级前价格
    def page_get_old_price(self):
        price = self.base_get_text(page.config_up_get_old_price)
        return float(price.split('\n')[1][1:])

    # 获取升级后配置价格
    def page_get_price(self, capacity):
        # 获取所有的节点元素
        els = self.base_find_elements(page.config_up_city)
        price = 0
        c = 1
        for el in els:
            msg = el.text
            tps_price = float(msg.split('\n')[2].split(' ')[1])
            capacity_price = float(msg.split('\n')[3].split(' ')[1])
            current_nodes = int(msg.split('\n')[4])

            i = page.config_up_new_nodes
            new_css = i[0][1][:19] + str(c) + i[0][1][20:]
            new_nodes = [(i[0][0], new_css), i[1]]
            add_nodes = int(self.base_dropdown_input_get_current_option(new_nodes, timeout=0.5))
            nodes = current_nodes + add_nodes
            price = price + (tps_price + capacity_price * capacity) * nodes

            c = c + 1
            # sleep(1)
            self.base_loading()

        return float('%.2f' % price)

    # 业务组合
    def page_config_up_check_money(self):

        self.page_click_my_release()
        self.page_click_config_upgrade()

        self.page_change_config()

        capacity = self.page_get_capacity()
        new_price = self.page_get_price(capacity)
        old_price = self.page_get_old_price()
        self.page_get_expired_time(1)

        return [new_price, old_price]
