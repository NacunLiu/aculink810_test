from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class MainPage(BasePage):
    NAV_LINKS = (By.CSS_SELECTOR, "section#desktop a.router-link")
    # aside和nav都是语义化标签,方便机器理解SOE友好的语义化标签 也是和div一样的 块元素(block-level element)但是语义更清晰
    # 回顾: block-level element 独占一行 可以包含其他块元素和行内元素 常见的有: <div>, <p>, <section>, <article>
    # <header>, <footer>, <aside>, <nav>, <ul>, <li>
    
    # 能用 header/footer/nav/aside/section/article/main 就别全用 div，有利于可访问性与 SEO
    
    
    # 内联元素(inline)不会独占一行, 只占自身宽度, 一般用来修饰文字和小片段内容, 常见的有: <span>, <a>, <img>
    LEFT_MENU = (By.CSS_SELECTOR, "aside.sidebar nav.left_menu ul li a")
    
    # don't use setup_class in the page object like below, it won't work as expect since the setup_class is provided by pytest not python and should only be used in the Test Class in the test scripts
    # def setup_class(cls):
    #     sleep(5)
    #     cls.driver.get("https://s8p53070095.accuenergy.io/#/devices/dashboard")
        
    def main_navigation(self):
        elements = self.find_elements(self.NAV_LINKS)
        return [el.text.strip() for el in elements if el.text.strip()]
    
    def left_menu(self):
        elements = self.find_elements(self.LEFT_MENU)
        return [el.text.strip() for el in elements if el.text.strip()]
    
    def click_left_menu(self, label:str):
        left_nav = self.find_elements(self.LEFT_MENU)
        for el in left_nav:
            if el.text.strip() == label:
                el.click()
                sleep(2)
                return self.driver.current_url
            

        
            


        
    
    