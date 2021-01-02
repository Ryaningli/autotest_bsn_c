import unittest

from base.get_driver import GetDriver
from page.page_login import PageLogin
from page.page_login_log import PageLoginLog


class TestLoginLog(unittest.TestCase):

    def setUp(self):
        self.driver = GetDriver().get_driver()
        self.login_log = PageLoginLog(self.driver)
        PageLogin(self.driver).page_login_success()

    def tearDown(self):
        GetDriver.quit_driver()

    def test_login_log(self):
        self.login_log.page_click_login_log()
        self.login_log.page_all2()