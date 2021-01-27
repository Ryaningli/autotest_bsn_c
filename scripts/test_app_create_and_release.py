import unittest

from parameterized import parameterized

from base.get_driver import GetDriver
from base.get_logger import GetLogger
from page.page_app_create_and_release import PageAppCreateAndRelease
from page.page_login import PageLogin

log = GetLogger().get_logger()


def get_data(number):
    app_name = []
    with open('../data/app_create_and_release_app_name.txt', 'r') as f:
        current_name = f.readline()

    for i in range(number):
        name = 'app_test_' + str(int(current_name[-6:]) + i + 1)
        app_name.append((name,))

    with open('../data/app_create_and_release_app_name.txt', 'w') as f:
        f.write(app_name[-1][0])

    return app_name


class TestAppCreateAndRelease(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log.info('初始化测试程序...')
        cls.driver = GetDriver().get_driver()
        cls.app_cr = PageAppCreateAndRelease(cls.driver)
        PageLogin(cls.driver).page_login_success(username='18815596966', password='abc123')

    @classmethod
    def tearDownClass(cls):
        log.info('关闭驱动')
        GetDriver.quit_driver()

    @parameterized.expand(get_data(4))
    def test_app_create_and_release(self, app_name):
        self.app_cr.page_app_create_and_release(app_name)
        self.app_cr.page_get_home_page()
