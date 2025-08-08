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
    
@pytest.fixture(scope="class")
def login(request, get_driver):
    login_page = LoginPage(get_driver)
    get_driver.get(BASE_URL)
    title = login_page.login()

    
    