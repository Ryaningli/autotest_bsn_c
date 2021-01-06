import unittest
from base.get_driver import GetDriver
from page.page_login import PageLogin
from page.page_release_config_upgrade_check_money import PageReleaseConfigUpgradeCheckMoney


class TestReleaseConfigUpgradeCheckMoney(unittest.TestCase):

    def setUp(self):
        self.driver = GetDriver().get_driver()
        self.check_money = PageReleaseConfigUpgradeCheckMoney(self.driver)
        PageLogin(self.driver).page_login_success()

    def tearDown(self):
        GetDriver.quit_driver()

    def test_check_money(self):
        print(self.check_money.page_config_up_check_money())