from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from utils.common_method import CommonMethods
from time import sleep

class AlarmLogs(BasePage):
    Interval = (By.ID, "_Interval_input")
    LEFT_CAL = (By.CSS_SELECTOR, "div.drp-calendar.left th.prev.available")
    RIGHT_CAL = (By.CSS_SELECTOR, "div.drp-calendar.right th.next.available")
    LEFT_MONTH = (By.CSS_SELECTOR, "div.drp-calendar.left th.month")
    RIGHT_MONTH = (By.CSS_SELECTOR, "div.drp-calendar.right th.month")
    SELECT_TIME = (By.CSS_SELECTOR, ".calendar-time")
    CLEAR_BUTTON = (By.CSS_SELECTOR, ".cancelBtn.btn.btn-sm.btn-default")
    APPLY_BUTTON = (By.CSS_SELECTOR, ".applyBtn.btn.btn-sm.btn-primary")
    SerialNumber = (By.ID, "_Serial_Number_input")
    MonitorID = (By.ID, "_Monitor_ID_input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".btn.position-relative.btn-success.btn-md")
    RESET_BUTTON = (By.CSS_SELECTOR, ".btn.position-relative.btn-warning.btn-md")
    ALARM_LOG_TABLE = (By.CSS_SELECTOR, ".table.table-striped.no-border.table-hover")
    
    
    
    def __init__(self, driver, timeout=20):
        super().__init__(driver, timeout=timeout)
        self.common_methods = CommonMethods()
        
    def click_tab_enter_test_page(self):
        tab = self.common_methods.get_left_menu_tabs(self, "Alarm Logs")
        sleep(3)
        tab.click()
        
    def interval_select_date(self):
        interval = self.find(self.Interval)
        interval.click()
        interval.send_keys("abcd")
        sleep(3)
        interval.clear()
        # 定位日历左右按键
        left_cal  = self.find(self.LEFT_CAL)
        right_cal = self.find(self.RIGHT_CAL)
        
        # 定位日历的左右当前日期月份
        left_month_before_click = self.find(self.LEFT_MONTH).text
    
        
        # 定位触发按键前背景颜色
        left_cal_background_color_before_click = left_cal.value_of_css_property("background-color")
        right_cal_background_color_before_click = right_cal.value_of_css_property("background-color")
        
        # 移动鼠标到左侧按键悬停3并获取背景色
        actions = self.get_actions()
        actions.move_to_element(left_cal).perform()
        sleep(2)
        left_cal_background_color_after_click = right_cal.value_of_css_property("background-color")
        
        # 点击按键并获取月份信息
        actions.click(left_cal).perform()
        left_month_after_click = self.find(self.LEFT_MONTH).text
        sleep(2)
        
        # 点击左侧按钮之后calendar会刷新 必须从新获取右侧按钮元素
        right_cal = self.find(self.RIGHT_CAL)
        
        # 移动鼠标到右侧按键并悬停2秒
        actions.move_to_element(right_cal).perform()
        sleep(2)
        right_cal_background_color_after_click = right_cal.value_of_css_property("background-color")
        
        # 点击右侧按钮并获取月份信息
        actions.click_and_hold(right_cal).perform()
        sleep(2)
        actions.release()
        right_month_after_click = right_cal.value_of_css_property("background-color")
        right_month_before_click = self.find(self.RIGHT_MONTH)
        
        
        return (left_cal_background_color_before_click, left_cal_background_color_after_click, left_month_before_click, left_month_after_click, 
                right_cal_background_color_before_click, right_cal_background_color_after_click, right_month_before_click, right_month_after_click)
      
    def interval_select_time(self):
        select_left_time = self.find_elements(self.SELECT_TIME)[0]
        select_right_time = self.find_elements(self.SELECT_TIME)[-1]
        select_hour = Select(select_left_time.find_element(By.CSS_SELECTOR, ".hourselect"))
        
        
        option_hours = [opt.text.strip() for opt in select_hour.options]
        select_hour.select_by_value("8")
        sleep(1)
        
        select_minute = Select(select_left_time.find_element(By.CSS_SELECTOR, ".minuteselect"))
        option_minutes = [opt.text.strip() for opt in select_minute.options]
        select_minute.select_by_value("30")
        sleep(1)
        
        select_ampm = Select(select_left_time.find_element(By.CSS_SELECTOR, ".ampmselect"))
        option_ampm = [opt.text.strip() for opt in select_ampm.options]
        select_ampm.select_by_value("AM")
        sleep(1)
        return option_hours, option_minutes, option_ampm
    
    def interval_select_clear_apply_button(self):
        clear_btn = self.find(self.CLEAR_BUTTON)
        actions = self.get_actions()
        actions.click(clear_btn).perform()
        sleep(3)
        interval = self.find(self.Interval)
        interval.click()
        sleep(1)
        apply_btn = self.find(self.APPLY_BUTTON)
        actions.click(apply_btn).perform()
        interval = self.find(self.Interval)
        sleep(1)
        return interval.get_attribute("value")
        
    
    def interval_select_search(self):
        search_btn = self.find(self.SEARCH_BUTTON)
        actions = self.get_actions()
        actions.move_to_element(search_btn)
        sleep(2)
        actions.click(search_btn).perform()
        
        
    def alarm_log_table(self):
        alarm_table = self.find(self.ALARM_LOG_TABLE)
        table_data = self.common_methods.get_table_data(alarm_table)
        return table_data