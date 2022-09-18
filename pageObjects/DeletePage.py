import time

from selenium.webdriver.common.by import By

from pageObjects.TrimVideo import TrimVideo


class DeletePage:
    button_select_Yes_xpath = (By.XPATH, "//button[contains(text(),'Yes')]")
    button_start_over_xpath = (By.XPATH, "//button[contains(text(),'No')]")

    def __init__(self, driver):
        self.driver = driver

    def Yes(self):
        return self.driver.find_element(*DeletePage.button_select_Yes_xpath).click()
    def NO(self):
        return self.driver.find_element(*DeletePage.button_start_over_xpath).click()

