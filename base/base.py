from time import strftime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from base.get_logger import GetLogger
from base.wait_loading import WaitLoading

# 获取日志类实例化对象
log = GetLogger().get_logger()


class Base:
    # 初始化
    def __init__(self, driver):
        log.info('获取初始化driver对象:{}'.format(driver))
        self.driver = driver

    # 查找元素封装（默认超时时间30s，每0.5秒刷新寻找一次）
    def base_find(self, loc,  timeout=30, poll=0.5):
        log.info('定位元素:{}，超时时间={}s，每{}s刷新一次'.format(loc, timeout, poll))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 查找多个元素封装（默认超时时间30s，每0.5秒刷新寻找一次）
    def base_find_elements(self, loc,  timeout=30, poll=0.5):
        log.info('定位元素:{}，超时时间={}s，每{}s刷新一次'.format(loc, timeout, poll))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc))

    # 点击元素方法封装
    def base_click(self, loc):
        log.info('对元素:{}实行点击'.format(loc))
        self.base_find(loc).click()

    # 输入元素方法封装
    def base_input(self, loc, value):
        el = self.base_find(loc)
        log.info('对元素:{}实行清空'.format(loc))
        el.clear()
        log.info('向元素:{}输入:{}'.format(loc, value))
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
            self.base_find(loc, timeout=5)
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

    '''下面三个关于下拉框dropdown的方法专用为tag名为select的标准下拉框'''

    # 判断下拉框是否包含指定选项（准备舍弃此方法，没必要啊）
    def base_dropdown_is_have_option(self, loc, value):
        if value in self.base_get_text(loc):
            log.info('判断下拉框"{}"所有选项包含"{}"'.format(loc, value))
            return True
        else:
            log.info('判断下拉框"{}"所有选项不包含"{}"'.format(loc, value))
            return False

    # 获取当前下拉框选项
    def base_dropdown_get_current_option(self, loc):
        sl = Select(self.base_find(loc))
        text = sl.first_selected_option.text
        log.info('获取当前下拉框"{}"选项为"{}"'.format(loc, text))
        return text

    # 下拉框选择方法封装（三种选择方式，通过给select_method传参选择，默认select_by_visible_text）
    def base_dropdown_select(self, loc, value, select_method='text'):
        # 实例化Select
        sl = Select(self.base_find(loc))
        log.info('下拉框"{}"根据"{}"选择"{}"'.format(loc, select_method, value))
        if select_method == 'text':
            sl.select_by_visible_text(value)

        if select_method == 'index':
            sl.select_by_index(value)

        if select_method == 'value':
            sl.select_by_value(value)

    '''下面三个关于下拉框dropdown的方法专用为tag名为input的非标准下拉框'''

    # 获取下拉框所有选项（点击下拉框箭头打开选项，获取选项文本，再次点击下拉框箭头关闭选项。参数分别为下拉框箭头和选项元素）
    def base_dropdown_input_get_options(self, arrow_loc, options_loc):
        self.base_click(arrow_loc)
        text = self.base_get_text(options_loc)
        self.base_click(arrow_loc)
        options_list = text.split('\n')
        log.info('下拉框"{}"所有选项为"{}"，共{}个'.format(options_loc, options_list, len(options_list)))
        return options_list

    # 获取当前下拉框选项（点击下拉框箭头展开选项，获取多个选项元素，遍历元素判断if 'selected' in class的属性值里，点击下箭头关闭选项）
    def base_dropdown_input_get_current_option(self, arrow_loc, options):
        self.base_click(arrow_loc)
        elements = self.base_find_elements(options)
        log.info('遍历多个元素"{}"，判断每个元素的class属性值里是否包含"selected"'.format(options))

        for element in elements:
            if 'selected' in element.get_attribute('class'):
                self.base_click(arrow_loc)
                element_text = element.text
                log.info('判断成功，遍历结束。元素"{}"的class属性值包含"selected"，当前下拉框选项为"{}"'.format(element, element_text))
                return element_text

        log.info('遍历结束，没有元素的class属性值包含"selected"，当前选项为空')
        self.base_click(arrow_loc)

    # 下拉框选择方法封装（先点击下拉框的下箭头，展开下拉框，再点击指定选项。此方法的两个参数分别对应下拉框箭头和要点击的选项元素）
    def base_dropdown_input_select(self, locs):
        log.info('开始在下拉框"{}"中选择选项"{}"'.format(locs[0], locs[1]))
        self.base_click(locs[0])
        self.base_loading()
        self.base_click(locs[1])

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

    # 截图方法封装
    def base_get_image(self):
        image_path = '../image/{}.png'.format(strftime('%Y-%m-%d_%H-%M-%S'))
        log.info('调用截图，文件路径：{}'.format(image_path))
        self.driver.get_screenshot_as_file(image_path)

    # 添加cookie
    def base_add_cookie(self, cookie):
        self.driver.add_cookie(cookie)
        log.info('添加cookie {}'.format(cookie))
        self.driver.refresh()

    # tab（没必要）
    def base_push_tab(self, loc):
        self.base_find(loc).send_keys(Keys.TAB)

    # 等待加载页面
    def base_loading(self, timeout=20, wait_first=0.3, poll_frequency=0.5):
        log.info('等待loading加载结束......')
        WaitLoading(self.driver, timeout=timeout, wait_first=wait_first, poll_frequency=poll_frequency).until_not(
            lambda x: x.find_element_by_css_selector('.el-loading-text')
        )
