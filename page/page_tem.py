import random
from time import sleep
import page
from base.base import Base


class PageTem(Base):
    def page_get(self):
        self.driver.get('http://192.168.0.158/service/uploadservice?type=1&appTypeName=Fabric-secp256r1-1.4.3&appInfoId=12327&frameType=fabric&payType=1')
        self.driver.refresh()
        sleep(2)
        js = 'document.querySelector("#editor>div:nth-child(2)>div>p").innerText="这是服务的描述"'
        self.driver.execute_script(js)