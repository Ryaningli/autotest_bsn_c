import unittest
from base.get_driver import GetDriver
from base.get_logger import GetLogger
from page.page_app_release import PageAppRelease
from page.page_login import PageLogin

log = GetLogger().get_logger()


class TestAppRelease(unittest.TestCase):

    def setUp(self):
        log.info('初始化测试程序...')
        self.driver = GetDriver().get_driver()
        self.app_release = PageAppRelease(self.driver)
        PageLogin(self.driver).page_login_success()

    def tearDown(self):
        log.info('关闭驱动')
        # GetDriver.quit_driver()

    def test_app_release(self):
        self.app_release.page_app_release('发一个图hi就欧佩克')
        commit_msg = self.app_release.page_get_commit_msg()
        try:
            self.assertIn(commit_msg, '已提交')
        except AssertionError as e:
            log.error('错误：{}'.format(e))
            raise e
        finally:
            self.app_release.page_click_commit_enter()
