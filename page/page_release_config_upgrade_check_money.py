import datetime
import math
import random
from time import sleep

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
        self.base_loading(css='[class="el-table__empty-text"]')
        self.base_loading()

    # 随机改动新增节点数
    def page_change_nodes_count(self):
        arrow = page.config_up_new_nodes[0]
        options = page.config_up_new_nodes[1]
        els = self.base_find_elements(arrow)
        for el in els:
            el.click()
            sleep(0.3)
            try:
                ops = self.base_find_elements(options, timeout=1, poll=0.3)
                op = random.choice(ops)
                op.click()
                self.base_loading()
            except:
                el.click()

        self.page_assert_equal()

    # 新增一个城市（返回剩余城市数）
    def page_add_city(self):
        while True:
            self.base_click(page.config_up_add_city_button)
            self.base_loading()

            try:
                els = self.base_find_elements(page.config_up_add_city_select)
                self.base_click(page.config_up_add_city_select)
                self.base_click(page.config_up_add_city_enter)
                sleep(0.3)
                self.page_change_nodes_count()
                if len(els) == 1:
                    break
            except:
                self.base_click(page.config_up_add_city_enter)
                break

    # 改动tps
    def page_change_tps(self):
        self.base_click(page.config_up_get_tps[0])
        sleep(0.3)
        tpses = self.base_find_elements(page.config_up_get_tps[1])
        self.base_click(page.config_up_get_tps[0])

        for tps in tpses:
            self.base_click(page.config_up_get_tps[0])
            sleep(0.3)
            if 'is-disabled' in tps.get_attribute('class'):
                self.base_click(page.config_up_get_tps[0])
                continue

            if 'selected' in tps.get_attribute('class'):
                self.base_click(page.config_up_get_tps[0])
                continue

            tps.click()
            self.base_loading()
            self.page_change_nodes_count()

    # 获取当前tps
    def page_get_tps(self):
        return self.base_dropdown_input_get_current_option(page.config_up_get_tps)

    # 获取当前容量
    def page_get_capacity(self):
        capacity = int(self.base_dropdown_input_get_current_option(page.config_up_get_capacity, timeout=1))
        return capacity

    # 获取支付周期总天数和剩余天数（支付类型，1是年，0是月）
    def page_get_expired_time(self):
        msg = self.base_get_text(page.config_up_get_old_price)      # 获取含有支付周期文字的文本
        expired_time = self.base_get_text(page.config_up_expired_time)

        et = datetime.datetime.strptime(expired_time, '%Y-%m-%d %H:%M:%S')
        et_day = et.date()
        now = datetime.datetime.now()
        et_stamp = et.timestamp()
        now_stamp = now.timestamp()
        day = (et_stamp - now_stamp) / 86400
        remain_day = math.ceil(day)

        # et = datetime.datetime.strptime(expired_time, '%Y-%m-%d').date()
        # today = datetime.date.today()

        ct = None
        if '年' in msg:
            ct = datetime.date(et.year - 1, et.month, et.day)

        if '月' in msg:
            if et.month == 1:
                ct = datetime.date(et.year - 1, 12, et.day)
            else:
                ct = datetime.date(et.year, et.month - 1, et.day)

        # remain_day = (et - today).days      # 剩余天数
        all_day = (et_day - ct).days    # 支付周期天数
        return [all_day, remain_day]

    # 获取页面显示的应付价格
    def page_get_pay_price(self):
        pay_price = self.base_get_text(page.config_up_pay_price)
        return float(pay_price[1:])

    # 获取升级前价格
    def page_get_old_price(self):
        price = self.base_get_text(page.config_up_get_old_price)
        return float(price.split('\n')[1][1:])

    # 获取升级后配置价格
    def page_get_next_price(self):
        # 获取所有的节点元素和所有的新增节点下拉框的箭头元素
        cities = self.base_find_elements(page.config_up_city)
        arrows = self.base_find_elements(page.config_up_new_nodes[0])

        capacity = self.page_get_capacity()
        price = 0
        c = 1
        for city, arrow in zip(cities, arrows):
            msg = city.text   # 判断支付类型的msg

            tps_price = float(msg.split('\n')[2].split(' ')[1])     # tps价格
            capacity_price = float(msg.split('\n')[3].split(' ')[1])        # 容量单价
            current_nodes = int(msg.split('\n')[4])     # 已有节点数

            arrow.click()   #点击下箭头
            sleep(0.3)
            add_nodes = int(self.base_get_text_by_attribute(page.config_up_new_nodes[1]))        # 获取被选中的选项，即新增的节点数
            arrow.click()

            nodes = current_nodes + add_nodes
            price = price + (tps_price + capacity_price * capacity) * nodes

            c = c + 1
            # self.base_loading()

        return float('%.2f' % price)

    # 算出应付价格
    def page_price(self):
        next_price = self.page_get_next_price()
        old_price = self.page_get_old_price()
        days = self.page_get_expired_time()
        remain_days = days[1]

        a = (next_price * 100 - old_price * 100) / 31   # 日价格*100
        b = math.ceil(a * 100) / 100       # 向上保留两位小数
        c = math.ceil(b * remain_days) / 100       # 应付价格（日价格乘以剩余天数）

        return c

    # 断言相等
    def page_assert_equal(self):
        price = self.page_price()
        pay_price = self.page_get_pay_price()
        t = f = 0
        try:
            assert price == pay_price
            t = t + 1
        except:
            self.base_get_image(name='我算的{}'.format(price))
            f = f + 1
        return [t, f]

    # 业务组合
    def page_config_up_check_money(self):

        self.page_click_my_release()
        self.page_click_config_upgrade()

        self.page_change_nodes_count()
        self.page_add_city()
        self.page_change_tps()

