#
# class HomePage():
#     url = "https://gifbuz.com/dashboard/my-uploads"
#     button_cookie_accept_id = "rcc-confirm-button"
#     button_login_xpath = "//button[contains(text(),'Login')]"
#
#     def __int__(self, driver):
#         self.driver = driver
#
#     def CookieAccept(self,cookie):
#         self.driver.find_element_by_xpath(self.button_cookie_accept_id).click()
#
#     def LogIn(self,LOGIN):
#         self.driver.find_element_by_xpath(self.button_login_xpath).click()

from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.EditProfiles import EditProfiles


class HomePage:
    # Home Page
    button_cookie_id = (By.ID, "rcc-confirm-button")
    button_login_xpath = (By.XPATH, "//button[contains(text(),'Login')]")
    box_profile_pic_xpath = (By.XPATH, "//div[@class='user-dropdown me-3']")
    button_creategif_xpath = (By.XPATH, "//span[contains(text(),'Create')]")
    button_upload_xpath =(By.XPATH,"//span[contains(text(),'Upload')]")

    def __init__(self, driver):
        self.driver = driver

    def CookieAccept(self):
        return self.driver.find_element(*HomePage.button_cookie_id).click()

    def LogIn(self):
        return self.driver.find_element(*HomePage.button_login_xpath).click()
        # lp = LoginPage(self.driver)
        # return lp

    def Profile(self):
        return self.driver.find_element(*HomePage.box_profile_pic_xpath).click()
        # return EditProfiles(self.driver)
        # return editProf

    def Title(self):
        return self.driver.title

    def CreateGif(self):
        return self.driver.find_element(*HomePage.button_creategif_xpath).click()
        # return self.driver.title

    def Upload(self):
        return self.driver.find_element(*HomePage.button_upload_xpath).click()
        # return self.driver.title

