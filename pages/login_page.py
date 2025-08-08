from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class LoginPage(BasePage):
    USER = (By.ID, "_User_Name_input")
    PASSWORD = (By.ID, "_Password_input")
    SIGN_IN = (By.XPATH, "//button[normalize-space()='Sign In']")

    def login(self, username="admin", password="admin"):
        self.driver.get("https://s8p53070095.accuenergy.io/#/login")
        self.input_text(locator=self.USER, text=username)
        sleep(1)
        self.input_text(locator=self.PASSWORD, text=password)
        sleep(1)
        self.find(self.SIGN_IN).click()
        sleep(1)
        return self.driver.title