from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    NAV_LINKS = (By.CSS_SELECTOR, "section#desktop a.router-link")
    
    def setup_class(cls):
        cls.driver.get("https://s8p53070095.accuenergy.io/#/devices/dashboard")
        
    def main_navigation(self):
        elements = self.find_elements(self.NAV_LINKS)
        return [el.text.strip() for el in elements if el.text.strip()]
        
        
    