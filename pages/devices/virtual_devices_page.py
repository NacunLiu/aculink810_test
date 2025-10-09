import selenium
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.common_method import CommonMethods
from time import sleep 

class VirtualDevices(BasePage):
    VIRTUAL_DEVICES_TAB = (By.XPATH, "//a[normalize-space()='Virtual Devices']")
    VIRTUAL_DEVICE_TABLE = (By.XPATH, "//table[contains(@class, 'table-striped')]")
    ADD_VIRTUAL_DEVICE_BUTTON = (By.CSS_SELECTOR, ".btn.position-relative.btn-success.btn-md")
    INPUT_DEVICE_NAME = (By.ID, "_Device_Name_input")
    ADD_VIRTUAL_DEVICE_PARAMETER_BUTTON = (By.XPATH, "//button[normalize-space()='Add Virtual Device Parameter']")
    # difference between / and // in Xpath: // means starts anywhere and find the dependent children while not necessary the direct one more like the relative path
    # / means starts from the root and must be the direct child 
    # // 在XPath中会自上而下找到所有的要求元素,但是返回一个还是多个取决于在selenium中使用的方法是find_element 还是find_elements
    # //button[normalized-space() =""]是查找元素并且其中的text等于规定的内容 //button[@class="col-12"]查找特定属性值的button
    # //button[contains(string, substring)] if substring appear anywhere in the string it returns true. So we can use it like //button[contains(@class, 'class_name')]
    
    PARAMETER_NAME = (By.ID, "1_Parameter_Name_input")
    UNIT = (By.ID, "1_Unit_input")
    REALTIME = (By.CSS_SELECTOR, "label[for='1_Parameter_Type_input_0']")
    ACCUMULATIVE = (By.ID, "1_Parameter_Type_input_1")
    SELECT_DEVICE_PARAMETER_BUTTON = (By.XPATH, "//button[normalize-space()='Select Device Parameter']")
    MODAL = (By.CLASS_NAME, 'modal-content')
    FIRST_DEVICE_MENU = (By.CLASS_NAME, "multiselect__tags")
    FIRST_DEVICE = (By.CSS_SELECTOR, 'ul.multiselect__content li > span.multiselect__option')
    
    
    
    def __init__(self, driver):
        super().__init__(driver)
        self.common_methods = CommonMethods()
        
    def click_to_enter_test_page(self):
        self.click(self.VIRTUAL_DEVICES_TAB)
    
    def get_virtual_device_list(self):
        virtual_device_table = self.find(self.VIRTUAL_DEVICE_TABLE)
        device_list = self.common_methods.get_table_data(virtual_device_table)
        return device_list
        sleep(3)
        
    def click_add_device(self):
        self.click(self.ADD_VIRTUAL_DEVICE_BUTTON)
        sleep(3)
        
    def add_virtual_device(self):
        self.click(self.ADD_VIRTUAL_DEVICE_BUTTON)
        sleep(2)
        self.input_text(self.INPUT_DEVICE_NAME, "test")
        sleep(2)
        
        self.click(self.ADD_VIRTUAL_DEVICE_PARAMETER_BUTTON)
        
        self.input_text(self.PARAMETER_NAME, "Power")
        sleep(1)
        self.input_text(self.UNIT, "KW")
        sleep(1)
        
        radio = self.find(self.REALTIME)
        radio.click()
        sleep(2)
        
        self.click(self.SELECT_DEVICE_PARAMETER_BUTTON)
        sleep(2)
        
        self.click(self.FIRST_DEVICE_MENU)
        sleep(2)
        
        modal = self.find(self.MODAL)
        first_device_options = modal.find_elements(*self.FIRST_DEVICE)
        list = [option.text for option in first_device_options]
        return list
    
    