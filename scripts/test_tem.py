import unittest
from base.get_driver import GetDriver
from page.page_login import PageLogin
from page.page_tem import PageTem


class TestTem(unittest.TestCase):

    def setUp(self):
        self.driver = GetDriver().get_driver()
        self.tem = PageTem(self.driver)
        PageLogin(self.driver).page_login_success()

    def tearDown(self):
        # GetDriver.quit_driver()
        pass

    def test_create_app(self):
        self.tem.page_get()