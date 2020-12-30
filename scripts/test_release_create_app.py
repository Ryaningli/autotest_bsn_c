import unittest

from base.get_driver import GetDriver
from base.get_logger import GetLogger
from page.page_release import PageRelease

# rel = PageRelease(GetDriver().get_driver())
# rel.page_create_service('服务名测试0003')

log = GetLogger().get_logger()


class TestReleaseCreateApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info('初始化测试程序...')
        cls.release_create_app = PageRelease(GetDriver.get_driver())