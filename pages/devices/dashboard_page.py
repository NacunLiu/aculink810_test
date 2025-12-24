from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage
# 将通用方法进行封装，并且在POM类内通过对象初始化方法直接添加到对象属性中
from utils.common_method import CommonMethods


class DevicesDashboard(BasePage):
    OFFLINE_DEVICES_TABLE = (By.CSS_SELECTOR, "table.table.table-striped.no-border.table-hover")
    ALARMS = (By.CSS_SELECTOR, "table.table.table-striped.no-border.table-hover")
    
    
    # 这个setup方法是pytest的方法而不是python的方法，只有写在test脚本内才会在执行测试的时候首先自动执行
    # 放在POM类除非手动调用, 否则不会自动执行
    @classmethod
    def setup_class(cls):
        cls.driver.get("https://s8p53070095.accuenergy.io/#/devices/dashboard")
        sleep(10)
    
    #初始化方法直接添加到对象属性，如果不初始化添加到对象属性，那么需要在CommonMethods类中将其写成static method否则就必须实例化传递self
    # super().父类方法名的作用有两个:第一是当子类方法与父类方法同名时可以不直接覆盖会先调用父类方法之后进行扩展
    # 第二就是如果不使用super那么父类的初始化方法 def __init__(self) 不会被自动调用就无法传递driver
    # super就是相当于调用了一次父类中的初始化方法就等同于BasePage.__init__(self, driver) 
    
    def __init__(self, driver):
        super().__init__(driver) #将driver属性传递到父类也就是BasePage类中,这样之后所有的调用都可以在父类中找到driver， driver的传递过程是 TestClass->This Page Object -> BasePage 
        self.common_methods = CommonMethods() #将一些通用方法的类作为属性绑定到页面对象，后面可以直接使用
    
    def offline_devices(self):
         table = self.find_elements(self.OFFLINE_DEVICES_TABLE)[0]
         return self.common_methods.get_table_data(table)
     
    def alarms(self):
         table = self.find_elements(self.ALARMS)[-1]        
         return self.common_methods.get_table_data(table)
     
 
        