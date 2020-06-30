# @File  : pytest_log6.py
# @Author: leipei
# @Date  :  2020/06/18

import  pytest
from selenium import webdriver
import  logging

log = logging.getLogger(__name__)

#每个方法都截图，在所有方法之前初始化

class TestClass:

    @pytest.fixture(scope="module", autouse = True)#文件级的，初始化方法执行一次
    def init_driver(self):
        log.info('setup_class()')
        self.browser = webdriver.Firefox()
        self.browser.get('http://www.baidu.com')
        log.info('成功打开百度')
        #遇到yield开始执行测试用例，执行完成之后回来再执行下面的代码
        yield
        log.info('teardown_class()')

    @pytest.fixture()#方法级的，遇到方法就执行
    def init_data(self):
        log.info('test_data_setup')
        yield
        log.info('teardown test_data')

    @pytest.fixture(autouse = True)
    def screen_shot(self):
        log.info('screen_shot')

    @pytest.mark.usefixtures
    def test_qqq(self, init_data):
        log.info('xxxxxqqqq')
        assert 4 == 5

    @pytest.mark.slow
    def test_7(self):
        import time
        time.sleep(2)
        log.info('- test_7()')

    def test_5(self):
        log.debug('不等')
        assert 4 == 5


