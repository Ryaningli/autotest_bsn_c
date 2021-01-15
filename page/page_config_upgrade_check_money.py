import datetime
import math
import random
from time import sleep

import page
from base.base import Base


class PageConfigUpgradeCheckMoney(Base):

    def __init__(self, driver):
        super(PageConfigUpgradeCheckMoney, self).__init__(driver)
        self.tps_price = []
        self.capacity_price = []
        self.current_node = []
        self.add_node = []
        self.tps = 0
        self.capacity = 0
        self.pay_type = ''
        self.old_price = 0
        self.expired_time = ''
        self.page_pay_price = 0
        self.success = 0
        self.failure = 0

    # 点击我的发布
    def page_click_my_release(self):
        self.base_dropdown_select(page.config_up_myapp)
        self.base_loading()

    # 点击配置升级
    def page_click_config_upgrade(self):
        # 鼠标悬停至更多操作，然后再点击配置升级
        self.base_mouse_hover(page.config_up_button[0])
        self.base_click(page.config_up_button[1])
        self.base_loading()
        self.base_loading(css='[class="el-table__empty-text"]')
        self.base_loading()

    # 获取静态数据
    def page_get_static_data(self):
        self.tps = int(self.base_dropdown_get_current_option(page.config_up_tps))     # 当前tps选择
        self.capacity = int(self.base_dropdown_get_current_option(page.config_up_capacity))       # 当前容量选择
        self.pay_type = self.base_get_text(page.config_up_pay_type)     # 获取包含支付周期的文字
        self.old_price = float(self.base_get_text(page.config_up_old_price)[1:])    # 上个支付周期的总价格
        self.expired_time = self.base_get_text(page.config_up_expired_time)     # 到期时间

    # 更新数据，后面就可以运算了
    def page_update_data(self):
        els = self.base_find_elements(page.config_up_tps_price)
        for el in els:
            self.tps_price.append(float(el.text.split(' ')[1]))     # tps价格列表

        els = self.base_find_elements(page.config_up_capacity_price)
        for el in els:
            self.capacity_price.append(float(el.text.split(' ')[1]))    # 容量价格列表

        els = self.base_find_elements(page.config_up_current_node)
        for el in els:
            self.current_node.append(int(el.text))  # 当前节点数列表

        if len(self.add_node) == 0:
            for i in range(len(self.current_node)):
                self.add_node.append(0)

        self.page_pay_price = float(self.base_get_text(page.config_up_page_pay_price)[1:])      # 页面上的应付价格

    # 计算数据
    def page_get_calc_price(self):
        next_price = 0
        for tp, cp, cn, an in zip(self.tps_price, self.capacity_price, self.current_node, self.add_node):
            next_price = next_price + (tp + cp * self.capacity) * (cn + an)

        et = datetime.datetime.strptime(self.expired_time, '%Y-%m-%d %H:%M:%S')
        et_day = et.date()
        now = datetime.datetime.now()
        et_stamp = et.timestamp()
        now_stamp = now.timestamp()
        day = (et_stamp - now_stamp) / 86400
        remain_day = math.ceil(day)     # 剩余天数

        ct = None
        if '年' in self.pay_type:
            ct = datetime.date(et.year - 1, et.month, et.day)

        if '月' in self.pay_type:
            if et.month == 1:
                ct = datetime.date(et.year - 1, 12, et.day)
            else:
                ct = datetime.date(et.year, et.month - 1, et.day)

        all_day = (et_day - ct).days       # 支付周期总天数

        a = (next_price * 100 - self.old_price * 100) / all_day   # 日价格*100
        b = math.ceil(a * 100) / 100       # 向上保留两位小数
        calc_price = math.ceil(b * remain_day) / 100       # 应付价格（日价格乘以剩余天数）
        return calc_price

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
                self.add_node.append(int(op.text))
                op.click()
                self.base_loading()
            except:
                self.add_node.append(0)
                el.click()

        self.page_assert_equal()

    # 遍历新增城市（返回剩余城市数）
    def page_add_city(self):
        while True:
            self.base_click(page.config_up_add_city_button)
            self.base_loading()

            try:
                els = self.base_find_elements(page.config_up_add_city_select, timeout=2)
                self.base_click(page.config_up_add_city_select)
                self.base_click(page.config_up_add_city_enter)
                self.base_loading()
                self.page_change_nodes_count()
                if len(els) == 1:
                    break
            except:
                self.base_click(page.config_up_add_city_cancel)
                sleep(0.3)
                break

    # 遍历tps
    def page_change_tps(self):
        self.base_click(page.config_up_tps[0])
        sleep(0.3)
        tpses = self.base_find_elements(page.config_up_tps[1])
        max_tps = None
        for tps in tpses:
            if 'is-reverse' not in self.base_find(page.config_up_tps[0]).get_attribute('class'):
                self.base_click(page.config_up_tps[0])
                sleep(0.3)

            msg = tps.get_attribute('class')
            if 'is-disabled' in msg:
                continue
            if 'selected' in msg:
                max_tps = tps
                continue

            self.tps = int(tps.text)
            tps.click()
            self.base_loading()

            try:
                error = self.base_find(page.config_up_error, timeout=1, poll=0.2)
                assert 'tps数不可用' in error.text
                self.base_click(page.config_up_tps[0])
                sleep(0.3)
                max_tps.click()
                self.base_loading()
                break
            except:
                max_tps = tps

            self.page_change_nodes_count()

    # 遍历容量
    def page_change_capacity(self):
        self.base_click(page.config_up_capacity[0])
        sleep(0.3)
        capacities = self.base_find_elements(page.config_up_capacity[1])

        for capacity in capacities:
            if 'is-reverse' not in self.base_find(page.config_up_capacity[0]).get_attribute('class'):
                self.base_click(page.config_up_capacity[0])
                sleep(0.3)

            msg = capacity.get_attribute('class')
            if ('is-disabled' in msg) or ('selected' in msg):
                continue

            self.capacity = int(capacity.text)
            capacity.click()
            self.base_loading()
            self.page_change_nodes_count()

    # 断言相等
    def page_assert_equal(self):
        print('--------' * 20)
        self.page_update_data()
        calc_price = self.page_get_calc_price()
        pay_price = self.page_pay_price
        try:
            assert calc_price == pay_price
            self.success = self.success + 1
            print('断言成功\n'
                  '当前tps{}\n'
                  '当前容量{}\n'
                  'tps价格{}\n'
                  '容量价格{}\n'
                  '当前节点数{}\n'
                  '新增节点数{}\n'
                  '页面价格{}\n'
                  '我算的价格{}\n'
                  .format(self.tps, self.capacity, self.tps_price, self.capacity_price, self.current_node, self.add_node, pay_price, calc_price)
                  )
        except:
            self.base_get_image(name='我算的{}不等于{}'.format(calc_price, pay_price))
            self.failure = self.failure + 1
            print('断言失败啦啦啦啦啦啦啦\n'
                  '当前tps{}\n'
                  '当前容量{}\n'
                  'tps价格{}\n'
                  '容量价格{}\n'
                  '当前节点数{}\n'
                  '新增节点数{}\n'
                  '页面价格{}\n'
                  '我算的价格{}\n'
                  .format(self.tps, self.capacity, self.tps_price, self.capacity_price, self.current_node, self.add_node, pay_price, calc_price))
        self.tps_price = []
        self.capacity_price = []
        self.current_node = []
        self.add_node = []

    # 业务组合
    def page_config_up_check_money(self):

        self.page_click_my_release()
        self.page_click_config_upgrade()

        # 获取静态数据
        self.page_get_static_data()

        self.page_change_nodes_count()
        self.page_add_city()
        self.page_change_tps()
        self.page_change_capacity()

        print('共检查{}组，成功{}组，失败{}组'.format(self.success + self.failure, self.success, self.failure))




