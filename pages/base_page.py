import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging
import os
import time


# 对于810这种先登录才能访问所有内容的设置，只需要传递driver就能获取所有cookie，token信息，所有内容会被保存在这个driver里面
# 只要不关闭driver driver.quit()可以在一次登录之后继续使用这个driver

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.logger = logging.getLogger(__name__)
        
    def find(self, locator):
        wait = WebDriverWait(self.driver, timeout=self.timeout, poll_frequency=0.5)
        try:
            element = wait.until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException as e:
            self.logger.error("element not found {e}")
            self._take_screenshot("find_failure")
            raise
        
    def find_elements(self, locator):
        wait = WebDriverWait(self.driver, timeout=self.timeout, poll_frequency=0.5)
        try:
            elements = wait.until(EC.presence_of_all_elements_located(locator))
            return elements
        except TimeoutException as e:
            self.logger.error("element not found {e}")
            self._take_screenshot("find_failure")
            raise
        
        
    def get_actions(self):
        actions = ActionChains(self.driver)
        return actions
    
    def click(self, locator):
        try:
            element = self.find(locator)
            element.click()
        except Exception as e:
            self.logger.error(f"click {locator} failed")
            raise
        
    def input_text(self, locator, text):
        try:
            element = self.find(locator)
            element.send_keys(text)
        except Exception as e:
            self.logger.error(f"input text failed {e}")
            raise
        
    def get_text(self, locator):
        try:
            element = self.find(locator)
            return element.text
        except Exception as e:
            self.logger.error(f"get {locator} text failed due to {e}")
        
        
    def _take_screenshot(self, name):
        os.makedirs("screenshots", exist_ok=True)
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        self.driver.save_screenshot(f"screenshots/{name}_{timestamp}.png")
        self.logger.info(f"Screenshot saved")
        

        
        
            
        