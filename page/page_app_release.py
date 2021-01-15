import random
from time import sleep

import page
from base.base import Base


class PageAppRelease(Base):

    # 进入我的服务页面
    def page_get_to_app_page(self):
        self.base_dropdown_select(page.release_myapp)
        self.base_loading()

    # 搜索指定服务
    def page_get_app(self, app_name):
        self.base_input(page.release_app_name_search, app_name)
        self.base_click(page.release_app_search_button)
        self.base_loading()

    # 点击上传
    def page_click_release(self):
        self.base_click(page.release_release_app)
        self.base_loading()

    # 随机选择服务类型，输入版本号、简介、描述，添加服务封面，点击下一步
    def page_input_data(self):
        self.base_click(page.release_app_type[0])
        sleep(0.3)
        app_types = self.base_find_elements(page.release_app_type[1])
        app_type = random.choice(app_types)
        app_type.click()
        sleep(0.3)

        self.base_input(page.release_input_version, '1.1.2')
        self.base_input(page.release_input_introduction, '这是服务的简介-autotest')
        self.base_find(page.release_input_cover).send_keys(r'C:\Users\shangchain\Desktop\Ryan\autotest_bsn_c\data\document\cover.jpg')

        js = 'document.querySelector("{}").innerText="{}"'.format(page.release_input_desc, '这是服务的描述-autotest')
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
    def page_app_release(self, app_name):
        self.page_get_to_app_page()
        self.page_get_app(app_name)
        self.page_click_release()
        self.page_input_data()
        self.page_use_preset_chain_code()
        self.page_add_functions(3)
        self.page_add_roles(3)
        self.page_release_commit()
