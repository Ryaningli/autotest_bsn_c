import random
from time import strftime, sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.get_logger import GetLogger
from base.wait_loading import WaitLoading
from PIL import Image, ImageDraw, ImageFont

# 获取日志类实例化对象
log = GetLogger().get_logger()


class Base:
    # 初始化
    def __init__(self, driver):
        log.info('获取初始化driver对象:{}'.format(driver))
        self.driver = driver

    # 查找元素（默认超时时间30s，每0.5秒刷新寻找一次）
    def base_find(self, loc,  timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
            lambda x: x.find_element(By.CSS_SELECTOR, loc)
        )

    # 查找多个元素（默认超时时间30s，每0.5秒刷新寻找一次）
    def base_find_elements(self, loc,  timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
            lambda x: x.find_elements(By.CSS_SELECTOR, loc)
        )

    # 点击元素
    def base_click(self, loc):
        log.info('点击元素{}'.format(loc))
        self.base_find(loc).click()

    # 输入元素方法封装
    def base_input(self, loc, value):
        log.info('向元素:{}输入:{}'.format(loc, value))
        el = self.base_find(loc)
        el.clear()
        el.send_keys(value)

    # 获取元素文本信息方法封装
    def base_get_text(self, loc, timeout=30):
        log.info('获取元素:{}文本'.format(loc))
        msg = self.base_find(loc, timeout=timeout).text
        log.info('文本信息:{}'.format(msg))
        return msg

    # 获取当前页面title方法
    def base_get_title(self):
        title = self.driver.title
        log.info('获取当前页面title:{}'.format(title))
        return title

    # 判断元素是否存在
    def base_element_is_exist(self, loc):
        log.info('判断元素 {} 是否存在'.format(loc))
        try:
            self.base_find(loc, timeout=3)
            log.info('元素查找成功')
            return True
        except:
            log.info('元素查找失败')
            return False

    # 判断元素是否被选中
    def base_if_select(self, loc):
        log.info('判断元素:{}是否被选中'.format(loc))
        if self.base_find(loc).is_selected():
            log.info('元素：{} 被选中'.format(loc))
            return True
        else:
            log.info('元素:{} 未被选中'.format(loc))
            return False

    '''下面三个关于下拉框dropdown的方法专用为tag名为input的非标准下拉框'''
    # 获取当前下拉框选项（点击下拉框箭头展开选项，获取多个选项元素，遍历元素判断if 'selected' in class的属性值里，点击下箭头关闭选项）
    def base_dropdown_get_current_option(self, locs, timeout=30):
        self.base_click(locs[0])
        try:
            elements = self.base_find_elements(locs[1], timeout=timeout)
        except:
            self.base_click(locs[0])
            return 0

        log.info('遍历多个元素"{}"，判断每个元素的class属性值里是否包含"selected"'.format(locs[1]))

        for element in elements:
            if 'selected' in element.get_attribute('class'):
                element_text = element.text
                self.base_click(locs[0])
                log.info('判断成功，遍历结束，元素"{}"的class属性值包含"selected"，当前下拉框选项为"{}"'.format(element, element_text))
                return element_text

        log.info('遍历结束，没有元素的class属性值包含"selected"，当前选项为空')
        self.base_click(locs[0])
        return 0

    # 下拉框选择方法封装（先点击下拉框的下箭头，展开下拉框，再点击指定选项。此方法的两个参数分别对应下拉框箭头和要点击的选项元素）
    def base_dropdown_select(self, locs):
        log.info('开始在下拉框"{}"中选择选项"{}"'.format(locs[0], locs[1]))
        self.base_click(locs[0])
        sleep(0.3)
        self.base_click(locs[1])

    # 下拉框随机选择
    def base_dropdown_random_select(self, locs):
        log.info('开始在下拉框"{}"中随机选择选项'.format(locs[0]))
        self.base_click(locs[0])
        sleep(0.3)
        try:
            els = self.base_find_elements(locs[1], timeout=1)
            el = random.choice(els)
            log.info('已随机选择到元素{}'.format(el))
            el.click()
            sleep(0.3)
        except:
            log.info('元素不存在，未选择{}')
            self.base_click(locs[0])

    # 鼠标悬停
    def base_mouse_hover(self, loc):
        log.info('鼠标悬停至{}'.format(loc))
        mouse = self.base_find(loc)
        ActionChains(self.driver).move_to_element(mouse).perform()

    # 从多个元素中获取指定元素的文字信息(例如：elements为一个列表，元素class属性包含selected，key='class', value='selected')
    def base_get_text_by_attribute(self, loc, key='class', value='selected'):
        log.info('从多个元素中选择属性{}={}的元素')
        try:
            elements = self.base_find_elements(loc, timeout=1)
        except:
            log.info('元素未找到，返回0')
            return 0

        for element in elements:
            if value in element.get_attribute(key):
                element_text = element.text
                log.info('判断成功，遍历结束，元素"{}"的class属性值包含"selected"，当前下拉框选项为"{}"'.format(element, element_text))
                return element_text

        log.info('遍历结束，没有元素的class属性值包含"selected"，当前选项为空，返回0')
        return 0

    # 前往指定页面
    def base_go_to_page(self, page_url):
        log.info('前往指定页面:{}'.format(page_url))
        self.driver.get(page_url)

    # 切换Frame表单
    def base_switch_frame(self, frame_id):
        log.info('切换表单:{}'.format(frame_id))
        self.driver.switch_to.frame(frame_id)

    # 回到默认表单目录
    def base_default_content(self):
        log.info('回到默认表单目录')
        self.driver.switch_to.default_content()

    # 切换至指定title窗口方法
    def base_switch_title_window(self, title):
        log.info('调用切换句柄至title包含"{}"窗口的方法'.format(title))
        # 获取当前所有句柄
        handles = self.driver.window_handles

        # 遍历所有句柄，判断当前title是否包含指定文字
        for handle in handles:
            log.info('正在遍历窗口句柄"{}" --> 切换至{}'.format(handles, handle))
            self.driver.switch_to.window(handle)
            current_title = self.driver.title

            if title in current_title:
                log.info('当前窗口为"{}",包含指定的"{}"，判断成功，遍历结束'.format(current_title, title))
                break
            else:
                log.info('当前窗口为"{}",不包含指定的"{}"，判断失败，继续遍历下一个句柄'.format(current_title, title))

        # 遍历结束，判断当前title是否包含指定文字，如果不包含，则表明找不到指定的窗口，发起错误
        if title in self.driver.title:
            pass
        else:
            log.error('判断失败，所有窗口的title都不包含"{}"'.format(title))
            raise ValueError('判断失败，所有窗口的title都不包含"{}"'.format(title))

    # 截图
    def base_get_image(self, name='', full_screen=0, text='', position=(), ):
        image_path = '../image/{}.png'.format(strftime('%Y-%m-%d_%H-%M-%S{}'.format(name)))
        log.info('调用截图，文件路径：{}'.format(image_path))

        if full_screen == 0:
            self.driver.get_screenshot_as_file(image_path)
        elif full_screen == 1:
            width = self.driver.execute_script(
                'return Math.max(document.body.scrollWidth, document.body.offsetWidth, document.documentElement.'
                'clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth);')
            height = self.driver.execute_script(
                'return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.'
                'clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);')
            self.driver.set_window_size(width + 100, height + 100)
            self.driver.get_screenshot_as_file(image_path)
            self.driver.maximize_window()
        else:
            raise ValueError('shot_type只可为0或1')

        if text == '':
            pass
        else:
            img = Image.open(image_path)
            draw = ImageDraw.Draw(img)
            front = ImageFont.truetype('simhei.ttf', 25)  # 字体大小
            draw.text(position, text, fill=(84, 139, 84), font=front)  # 文字位置，内容，字体
            img.save(image_path)

    # 添加cookie
    def base_add_cookie(self, cookie):
        self.driver.add_cookie(cookie)
        log.info('添加cookie {}'.format(cookie))
        self.driver.refresh()

    # 等待加载页面
    def base_loading(self, css='[class^="el-loading"]', timeout=20, poll_frequency=0.5):
        log.info('等待loading加载结束......')

        # 尝试捕获loading，找到或1s找不到loading则继续下一步
        try:
            WebDriverWait(self.driver, timeout=1, poll_frequency=0.1).until(lambda x: x.find_element_by_css_selector(css))
        except:
            pass

        # 等待loading加载结束
        WaitLoading(self.driver, timeout=timeout, poll_frequency=poll_frequency).until_not(
            lambda x: x.find_element_by_css_selector(css)
        )

