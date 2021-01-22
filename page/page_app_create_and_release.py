import random
from time import sleep
import page
from base.base import Base
from page.page_app_create import PageAppCreate
from page.page_app_release import PageAppRelease


class PageAppCreateAndRelease(Base):

    # 创建服务并上传
    def page_app_create_and_release(self, app_name):
        PageAppCreate(self.driver).page_create_app_for(app_name)
        PageAppRelease(self.driver).page_app_release_for()

    # 回到个人主页
    def page_get_home_page(self):
        self.driver.get('http://192.168.0.158/homepage/homepage')
        self.base_loading()