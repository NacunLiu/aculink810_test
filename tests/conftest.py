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


# request is a pytest built-in fixture object and is used to access information about the test context(pytest 内置夹具用来获取测试脚本的上下文信息,哪个脚本在使用这个夹具就获取哪个脚本的上下文信息)
# 比如获取测试函数名称,测试类等等 所以在下面中request.cls就是在获取当前测试类对象，并且赋予它类属性为driver这个过程就是一个类级别的注入(class level injection)
# 当我们在测试脚本中打印这些信息的时候就可以看到 比如 print(request.cls) print(request.function) print(request.node) 就会得到这些信息
# CLS: <class 'tests.test_login.TestLogin'> FUNC: <function TestLogin.test_valid_login at 0x000001...>  NODE: <Function test_valid_login>
# 总之就是谁在使用这个夹具，那么request 就可以获取它的所有信息

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
    

# logging是一个模块可以看成是一个类,而logger是一个object,是负责具体记录日志的对象
# 当我们使用logger = logging.getLogger()的时候是使用的root logger
# 当我们使用logger = logging.getLogger(name)的时候是一个普通的logger,所有其他的logger都继承(inherit from) root logger
# 所以在BasePage中直接使用logger(__name__)就可以了
@pytest.fixture(scope="session", autouse=True)
def configure_logger(request):
    logger = logging.getLogger() # root logger
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
    

    