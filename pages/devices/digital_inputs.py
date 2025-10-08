import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils.common_method import CommonMethods
from time import sleep


class DevicesDigitalInputs(BasePage):
    EDIT = (By.CSS_SELECTOR, "#_Edit_switch_")
    
    @classmethod
    def setup_class(cls):
        cls.driver.get("https://s8p53070095.accuenergy.io/#/devices/digital_inputs")
        sleep(10)
    
    def __init__(self, driver):
        super().__init__(driver)
        self.common_methods = CommonMethods()
        
    def enable_edit(self):
        edit = self.find(self.EDIT)
        edit.click()
        sleep(3)
        