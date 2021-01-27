import unittest
from time import sleep

from base.get_driver import GetDriver
from page.page_login import PageLogin
from page.page_config_upgrade_check_money import PageConfigUpgradeCheckMoney


class TestReleaseConfigUpgradeCheckMoney(unittest.TestCase):

    def setUp(self):
        self.driver = GetDriver().get_driver()
        self.check_money = PageConfigUpgradeCheckMoney(self.driver)
        PageLogin(self.driver).page_login_success(username='18815596966', password='abc123')

    def tearDown(self):
        GetDriver.quit_driver()

    def test_check_money(self):
        self.check_money.page_config_up_check_money('app_test_600024')