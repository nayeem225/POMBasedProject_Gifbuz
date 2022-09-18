import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # browser_name = request.config.getoption("browser_name")
    # if browser_name == "chrome":
    #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #
    # elif browser_name == "edge":
    #     driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    #
    # elif browser_name == "firefox":
    #     driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    driver.get("https://gifbuz.com/")
    driver.maximize_window()
    driver.execute_script("""
        var foo = 'this is a test';
        console.log(foo);
    """)
    time.sleep(5)
    request.cls.driver = driver
    yield
    driver.close()
