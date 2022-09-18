import time

from selenium.webdriver.common.by import By

from pageObjects.createpage1 import CreatePage1


class TrimVideo:
    button_continue_xpath = (
    By.XPATH, "//body/div[@id='_gifbuz']/main[1]/section[3]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/button[1]")
    button_start_over_xpath = (By.XPATH, "//div[@class= 'col-6 col-sm-5 col-md-4 col-lg-5']/a")

    def __init__(self, driver):
        self.driver = driver

    def Continue(self):
        return self.driver.find_element(*TrimVideo.button_continue_xpath).click()


    def StartOver(self):
        return self.driver.find_element(*TrimVideo.button_start_over_xpath).click()
