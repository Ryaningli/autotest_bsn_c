import unittest
from base.get_driver import GetDriver
from page.page_login import PageLogin
from page.page_config_upgrade_check_money import PageConfigUpgradeCheckMoney


class TestReleaseConfigUpgradeCheckMoney(unittest.TestCase):

    def setUp(self):
        self.driver = GetDriver().get_driver()
        self.check_money = PageConfigUpgradeCheckMoney(self.driver)
        PageLogin(self.driver).page_login_success()

    def tearDown(self):
        GetDriver.quit_driver()

    def test_check_money(self):
        self.check_money.page_config_up_check_money()