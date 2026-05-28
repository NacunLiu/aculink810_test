import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from time import sleep

class TestMain:
    LEFT_NAVI = ["Dashboard", "Alarm Logs", "Modbus Devices", "BACnet Devices", 
                         "MBus Devices", "Digital Inputs", "Virtual Devices"]
    LINK_TABS = ["dashboard", "alarm_logs", "modbus_devices", "bacnet_devices", "mbus", "digital_inputs", "virtual_device"]


    #  setup_class is a class level setup method in recognized by pytest
    # setup_class会在其他所有函数执行之前自动执行一次 所以用来创建页面对象供后续的测试方法使用 注意类方法必须使用@classmethod装饰器进行装饰
    # 同理还有 setup_method 这个就会在每个函数执行前自动执行一次还有teardown_class和teardown_method作为后置方法
    
    
    @classmethod
    def setup_class(cls):
        cls.main_page = MainPage(driver=cls.driver, timeout=30) # don't worry about the class-level login fixture
        cls.login_page = LoginPage(driver=cls.driver, timeout=30) # login will not be execute in creation of the POM as the fixture will only be executed in the Test Class of the test scripts
        cls.login_page.login()

    def test_main_navigation(self):
        items = self.main_page.main_navigation()
        assert items == ['Devices', 'Data Log', 'System Settings', 
                         'Protocols', 'Templates', 'Maintenance', 'Diagnostics']
        self.main_page.logger.info("Test Main Navigation Passed")
        
    def test_left_menu(self):
        items = self.main_page.left_menu()
        assert items == self.LEFT_NAVI
        i = 0
        for item in self.LEFT_NAVI:
            linked = self.main_page.click_left_menu(item)  # the click function returns the url of the new page entered
            assert self.LINK_TABS[i] in linked, "Test Left Menu Failed"  # if assert fail then it will return the message and stop this test function and continue with other test functions
            self.main_page.logger.info(f"Test Left Menu {i} Passed, open {linked} works") # no worry to record this log if test failed in previous assert, since it will break the function
            i += 1
      
    