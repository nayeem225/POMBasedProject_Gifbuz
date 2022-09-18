import time

from selenium.webdriver.common.by import By

from pageObjects.TrimVideo import TrimVideo


class SinglePageGif:
    button_edit_xpath = (By.XPATH, "//ul[@class='SingleDetails_gifActions__OlzrF d-flex align-items-center']//li//a")
    button_delete_xpath = (By.XPATH, "//ul[@class='SingleDetails_gifActions__OlzrF d-flex align-items-center']/li[2]/button")
    gifTitle_xpath = (By.XPATH, "//div[@class='title-view']/h2")
    box_profile_pic_xpath = (By.XPATH, "//div[@class='user-dropdown me-3']/button")

    def __init__(self, driver):
        self.driver = driver

    def GifActionEdit(self):
        return self.driver.find_element(*SinglePageGif.button_edit_xpath).click()

    def GifActionDelete(self):
        return self.driver.find_element(*SinglePageGif.button_delete_xpath).click()

    def GifEdit(self):
        return self.driver.find_element(*SinglePageGif.gifTitle_xpath).text

    def Profile(self):
        return self.driver.find_element(*SinglePageGif.box_profile_pic_xpath).click()
