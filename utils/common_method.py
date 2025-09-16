import yaml
import json
import os
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
            
    # 读取yaml文件 传入reference数据文件路径 返回json格式数据 
    def load_yaml_test_data(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"YAML file not found: {file_path}")
        with open(file=file_path, mode='r', encoding='utf-8') as f:
            data = yaml.safe_load(f) #转换成python字典
        return data
    
    # 读取json文件 传入reference数据文件路径 返回json格式数据
    def load_json_test_data(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"JSON file not found: {file_path}")
        with open(file=file_path, mode='r', encoding='utf-8') as f:
            data = json.load(f)
            return data