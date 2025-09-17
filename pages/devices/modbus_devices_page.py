import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from utils.common_method import CommonMethods
from time import sleep


class ModbusDevices(BasePage):
    BUTTONS = (By.CSS_SELECTOR, ".btn.position-relative.btn-success.btn-md")
    ADD_DEVICE_NAME = (By.CSS_SELECTOR, "#_Device_Name_input")
    ADD_SERIAL_NUM = (By.CSS_SELECTOR, "#_Serial_Number_input")
    TEMPLATE = (By.CSS_SELECTOR, "#_Template_input")
    RTU_RADIO = (By.ID, "_Protocol_input_0")
    TCP_RADIO = (By.ID, "_Protocol_input_1")
    PORT = (By.ID, "_Port_input")
    MODBUS_ID = (By.ID, "_Modbus_ID_input")
    
    SAVE_BTN = (By.CSS_SELECTOR, ".btn.position-relative.btn-success.btn-md")
    
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout=timeout)
        self.common_methods = CommonMethods()
        
    def click_to_enter_test_page(self):
        tab = self.common_methods.get_left_menu_tabs(pom=self, target_tab="Modbus Devices")
        self.logger.info(f"{tab.text.strip()}")
        tab.click()
        
    def add_device(self):
        add_button = self.find_elements(self.BUTTONS)[0]
        actions = self.get_actions()
        actions.move_to_element(add_button).perform()
        sleep(2)
        actions.click(add_button).perform()
        sleep(2)
        
        # 进入添加设备页面进行新电表的添加测试
        
        # 首先定位获取输入框和选择等元素
        add_device_name_input = self.find(self.ADD_DEVICE_NAME)
        add_serial_number_input = self.find(self.ADD_SERIAL_NUM)
        templates = self.find(self.TEMPLATE)
        
        # 使用actions进行操作输入设备名称
        actions = self.get_actions()
        actions.click(add_device_name_input).perform()
        sleep(2)
        actions.send_keys("abcdef").perform()
        sleep(1)
        add_device_name_input.clear()
        add_device_name_input.send_keys("AHB20250917")  
        sleep(1)
        
        # 输入设备序列号
        add_serial_number_input.send_keys("AHB20250917")
        sleep(1)
        
        # 获取所有templates options
        templates = Select(self.find(self.TEMPLATE))
        options = self.common_methods.get_options(templates)
        self.logger.info(f"templates are {options}")
        templates.select_by_value("Acuvim IIV3")
        sleep(1)
        
        # 获取Protocol input元素
        rtu = self.find(self.RTU_RADIO)
        tcp = self.find(self.TCP_RADIO)
        
        actions.click(rtu).perform()
        sleep(1)
        
        actions.click(tcp).perform()
        sleep(1)
        
        actions.click(rtu).perform()
        sleep(1)
        
        # 获取Port
        port = Select(self.find(self.PORT))
        options_port = self.common_methods.get_options(port)
        self.logger.info(f"the ports options are {options_port}")
        port.select_by_index(1)
        sleep(1)
        
        modbus_id_input = self.find(self.MODBUS_ID)
        modbus_id_input.send_keys("9")
        sleep(1)
        
        save_btn = self.find(self.SAVE_BTN)
        save_btn.click()
        sleep(3)