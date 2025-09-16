import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from time import sleep

class TestMain:
    LEFT_NAVI = ["Dashboard", "Alarm Logs", "Modbus Devices", "BACnet Devices", 
                         "MBus Devices", "Digital Inputs", "Virtual Devices"]
    LINK_TABS = ["dashboard", "alarm_logs", "modbus_devices", "bacnet_devices", "mbus", "digital_inputs", "virtual_device"]

    @classmethod
    def setup_class(cls):
        cls.main_page = MainPage(driver=cls.driver, timeout=30)
        cls.login_page = LoginPage(driver=cls.driver, timeout=30)
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
            linked = self.main_page.click_left_menu(item)
            assert self.LINK_TABS[i] in linked, "Test Left Menu Failed"
            self.main_page.logger.info(f"Test Left Menu {i} Passed, open {linked} works")
            i += 1
        
    