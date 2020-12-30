import unittest
from parameterized import parameterized
from base.get_driver import GetDriver
from base.get_logger import GetLogger
from page.page_login import PageLogin

log = GetLogger().get_logger()


data = (
    ['18815596963', 'abc123', '登录成功', 'True'],
    ['18815596964', '11111', '密码错误', 'False'],
    ['18815596960', '11111', '账户为空,请先注册', 'False'],
    ['18815596963', 'abc123', '登录成功', 'True'],
)

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
                self.assertEqual(msg, except_result)
            except Exception as e:
                log.error('错误{}'.format(e))
                raise e

