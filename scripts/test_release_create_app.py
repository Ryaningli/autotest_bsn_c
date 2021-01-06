import unittest

from base.get_driver import GetDriver
from base.get_logger import GetLogger
from page.page_login import PageLogin
from page.page_release_create_app import PageRelease


log = GetLogger().get_logger()


class TestReleaseCreateApp(unittest.TestCase):

    def setUp(self):
        log.info('初始化测试程序...')
        self.driver = GetDriver().get_driver()
        self.create_app = PageRelease(self.driver)
        PageLogin(self.driver).page_login_success()

    def tearDown(self):
        log.info('关闭驱动')
        GetDriver.quit_driver()

    def test_create_app(self):
        self.create_app.page_create_app('服务测试0005')