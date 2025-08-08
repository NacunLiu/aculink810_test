import pytest
from pages.login_page import LoginPage


class TestLogin:
    @classmethod
    def setup_class(cls):
        cls.login_page = LoginPage(cls.driver, timeout=30)

    def test_login(self):
        title = self.login_page.login()
        self.login_page.logger.info(title)
        assert title
        
    