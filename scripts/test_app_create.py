import unittest
from base.get_driver import GetDriver
from base.get_logger import GetLogger
from page.page_login import PageLogin
from page.page_app_create import PageAppCreate


log = GetLogger().get_logger()


class TestAppCreate(unittest.TestCase):

    def setUp(self):
        log.info('初始化测试程序...')
        self.driver = GetDriver().get_driver()
        self.app_create = PageAppCreate(self.driver)
        PageLogin(self.driver).page_login_success(username='18815596966', password='abc123')

    def tearDown(self):
        log.info('关闭驱动')
        GetDriver.quit_driver()

    def test_app_create(self):
        self.app_create.page_create_app('服务测试00016')
        try:
            self.assertIn(self.app_create.page_get_pay_result(), '支付成功')
            self.app_create.page_game_over()
        except Exception as e:
            raise e
