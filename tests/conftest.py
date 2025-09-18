import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import logging
import os
import time
from pages.login_page import LoginPage


BASE_URL = "https://s8p53070095.accuenergy.io/#/login"


# 使用class级别的夹具将driver作为类属性绑定到测试类,是的每一个测试类自动具有driver属性
# 注意绑定类属性必须将scope定义为class
# 如果是function级别的应用,可以直接在测试脚本中的函数中通过传递实参(家具函数名)的方式进行调用,但是function 级别的夹具只能在一般的function 中使用而且不能在初始化函数中使用

@pytest.fixture(scope="class", autouse=True)
def get_driver(request):
    service = Service(executable_path=ChromeDriverManager().install())
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=service, options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()


#进行登录 登录和driver初始化必须都是同一个scope的比如都是class保证所有的driver中都进行过登录有所有的会话信息
@pytest.fixture(scope="class", autouse=True)
def login(request, get_driver):
    login_page = LoginPage(get_driver)
    get_driver.get(BASE_URL)
    title = login_page.login()
    

@pytest.fixture(scope="session", autouse=True)
def configure_logger(request):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    fh = logging.FileHandler(f"reports/test_loggier_{timestamp}", mode="w", encoding="utf-8")
    fh.setLevel(logging.INFO)
    
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    fh.setFormatter(formatter)
    
    logger.addHandler(fh)
    return logger
    

    
@pytest.fixture(scope="session")
def driver():
    driver = "this driver is used"
    yield driver
    print("driver use is ended")
    

    