import os
import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome(executable_path=(os.path.abspath(os.path.join(os.getcwd(), 'chromedriver.exe'))))
    yield driver
    driver.quit()
