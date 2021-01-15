import random
from time import sleep
import page
from base.base import Base


class PageAppCreate(Base):

    # 点击创建服务按钮
    def page_click_create_service_button(self):
        self.base_click(page.release_create_app_button)

    # 输入服务名称
    def page_input_service_name(self, app_name):
        self.base_input(page.release_input_app_name, app_name)
        self.base_loading()

    # 选择框架类型
    def page_choice_frame_type(self):
        self.base_dropdown_select(page.release_frame_type)

    # 点击下一步
    def page_click_step1_next(self):
        self.base_click(page.release_step1_next)
        self.base_loading()

    # 选择计算资源
    def page_choice_tps(self):
        self.base_dropdown_select(page.release_choice_tps)

    # 选择存储容量
    def page_choice_capacity(self):
        self.base_dropdown_select(page.release_choice_capacity)

    # 点击下一步
    def page_click_step2_next(self):
        self.base_click(page.release_step2_next)
        self.base_loading()

    # 随机选择三个城市节点
    def page_choice_node(self):
        all_cities = self.base_find_elements(page.release_nodes)
        cities = random.sample(all_cities, 3)
        for city in cities:
            city.click()
            self.base_loading()

    # 选择支付方式
    def page_choice_pay_mode(self):
        pay_types = self.base_find_elements(page.release_pay_types)
        pay_type = random.choice(pay_types)
        pay_type.click()
        self.base_loading()

    # 点击确认购买
    def page_click_confirm_purchase_button(self):
        self.base_click(page.release_confirm_purchase)
        self.base_loading()

    # 点击立即支付并确定
    def page_click_pay_now(self):
        self.base_click(page.release_pay_now)
        sleep(0.3)
        self.base_click(page.release_pay_now_enter)
        self.base_loading()

    # 点击立即创建服务
    def page_click_create_app_now(self):
        self.base_click(page.release_create_app_now)
        self.base_loading()

    # 随机选择服务类型，输入版本号、简介、描述，添加服务封面，点击下一步
    def page_input_data(self):
        self.base_click(page.release_app_type[0])
        sleep(0.3)
        app_types = self.base_find_elements(page.release_app_type[1])
        app_type = random.choice(app_types)
        app_type.click()
        sleep(0.3)

        self.base_input(page.release_input_version, '1.1.1')
        self.base_input(page.release_input_introduction, '这是服务的简介-autotest')
        self.base_find(page.release_input_cover).send_keys(r'C:\Users\shangchain\Desktop\Ryan\autotest_bsn_c\data\document\cover.jpg')

        js = 'document.querySelector("{}").innerText="{}"'.format(page.release_input_desc[1], '这是服务的描述-autotest')
        self.driver.execute_script(js)

        self.base_click(page.release_add_doc)
        sleep(0.3)
        self.base_find(page.release_add_doc_path).send_keys(r'C:\Users\shangchain\Desktop\Ryan\autotest_bsn_c\data\document\服务的文档资料.txt')
        self.base_input(page.release_add_doc_name, '文档资料名称-autotest')
        self.base_click(page.release_add_doc_type[0])
        sleep(0.3)
        random.choice(self.base_find_elements(page.release_add_doc_type[1])).click()
        self.base_click(page.release_add_doc_enter)
        sleep(0.3)
        self.base_click(page.release_upload_app_next)
        self.base_loading()

    # 使用预置链码包
    def page_use_preset_chain_code(self):
        self.base_click(page.release_chain_code_link)
        sleep(0.3)
        self.base_click(page.release_chain_code_select)
        self.base_click(page.release_chain_code_enter)
        self.base_loading()

    # 增加功能
    def page_add_functions(self, value=3):
        for i in range(value):
            self.base_click(page.release_add_functions_link)
            sleep(0.3)
            self.base_input(page.release_add_functions_name, '新增功能{}'.format(str(i + 1)))
            self.base_dropdown_select(page.release_add_functions_select_chain_code)
            self.base_dropdown_random_select(page.release_add_functions_func_type)
            self.base_input(page.release_add_functions_func, 'new_feature_{}'.format(str(i + 1)))
            self.base_click(page.release_add_functions_enter)
            sleep(0.3)

    # 增加角色
    def page_add_roles(self, value=3):
        for i in range(value):
            self.base_click(page.release_add_role_link)
            sleep(0.3)
            self.base_input(page.release_add_role_name, '角色{}'.format(str(i + 1)))
            self.base_input(page.release_add_role_desc, '这是角色{}的描述-autotest'.format(str(i + 1)))
            functions = self.base_find_elements(page.release_add_role_functions)
            select_functions = random.sample(functions, random.randint(1, len(functions)))
            for func in select_functions:
                func.click()

            self.base_click(page.release_add_role_enter)
            sleep(0.3)

    # 选择参与者证书模式并提交
    def page_release_commit(self):
        random.choice(self.base_find_elements(page.release_cert_type)).click()
        self.base_click(page.release_commit)
        self.base_loading()

    # 获取提交结果
    def page_get_commit_msg(self):
        msg = self.base_get_text(page.release_result_msg)
        return msg

    # 点击确定
    def page_click_commit_enter(self):
        self.base_click(page.release_commit_enter)
        self.base_loading()

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
        self.page_click_pay_now()

        self.page_click_create_app_now()
        self.page_input_data()

    def page_tem(self):
        self.driver.get('http://192.168.0.158/service/uploadservice?type=1&appTypeName=Fabric-secp256r1-1.4.3&appInfoId=12327&frameType=fabric&payType=1')
        self.driver.refresh()
        sleep(2)
        self.page_input_data()
        self.page_use_preset_chain_code()
        self.page_add_functions(3)
        self.page_add_roles(3)
        self.page_release_commit()
        print(self.page_get_commit_msg())
        self.page_click_commit_enter()