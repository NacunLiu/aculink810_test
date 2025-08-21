import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage

class TestMain:
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