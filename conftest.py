import pytest
from selenium import webdriver
from utils.test_data import TestData

@pytest.fixture(params=["firefox"])
# @pytest.fixture(params=["chrome", "firefox", "edge"])
def initialize_driver(request):
    if request.param == "firefox":
        driver = webdriver.Firefox()
    # elif request.param == "firefox":
    #     driver = webdriver.Firefox()
    # elif request.param == "edge":
    #     driver = webdriver.Edge()
    request.cls.driver = driver
    print("Browser: ", request.param)
    driver.get(TestData.url)
    driver.maximize_window()
    yield
    print("Close Driver")
    driver.close()