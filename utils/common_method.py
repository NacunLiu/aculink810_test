import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class CommonMethods:
    def get_table_data(self, table: WebElement):
        table_data = []
        rows = table.find_elements(By.XPATH, ".//tbody/tr")
        for row in rows:
            cells = [td.text.strip() for td in row.find_elements(By.TAG_NAME, "td")]
            table_data.append(cells)
        return table_data
    
    # 用来提取左侧导航栏中的目标元素，在每一个POM页面开始的时候进行点击进入页面开始测试
    def get_left_menu_tabs(self, pom, target_tab):
        tabs = pom.find_elements((By.CSS_SELECTOR, ".left_menu ul li"))
        for tab in tabs:
            pom.logger.info(f"{tab.text.strip()}")
            if tab.text.strip() == target_tab:
                return tab
            
    