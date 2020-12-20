from selenium import webdriver
import page


class GetDriver:
    driver = None

    # 获取driver
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Firefox()
            cls.driver.maximize_window()
            cls.driver.get(page.URL)

        return cls.driver

    # 关闭driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            # 关闭后必须置空
            cls.driver = None

