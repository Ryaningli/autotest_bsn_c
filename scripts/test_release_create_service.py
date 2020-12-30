from base.get_driver import GetDriver
from page.page_release import PageRelease

rel = PageRelease(GetDriver().get_driver())
rel.page_create_service('服务名测试0001')