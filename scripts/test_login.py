import unittest
from parameterized import parameterized
from base.get_driver import GetDriver
from base.get_logger import GetLogger
from page.page_login import PageLogin
from tools.get_data_txt import get_data_txt

log = GetLogger().get_logger()
data = get_data_txt('data_login.txt')


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info('初始化程序')
        cls.login = PageLogin(GetDriver().get_driver())

    @classmethod
    def tearDownClass(cls):
        log.info('关闭driver驱动')
        GetDriver.quit_driver()
        log.info('程序运行结束，拜了个拜！！！')

    # 测试方法
    @parameterized.expand(data)
    def test_login(self, username, password, except_result, status):
        log.info('开始执行测试用例')
        self.login.page_login(username, password)

        if status == 'True':
            try:
                self.assertTrue(self.login.page_login_if_success(username))
            except Exception as e:
                log.error('错误：{}'.format(e))
                raise e
            finally:
                self.login.page_click_logout()

        if status == 'False':
            msg = self.login.page_get_error_msg()
            try:
                self.assertIn(except_result, msg)
            except Exception as e:
                log.error('错误{}'.format(e))
                raise e

