import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Dashboard:
    # Login Page

    GifCreateMessage_xpath = (By.XPATH, "//div[@class='react-toast-notifications__toast__content css-1ad3zal']")
    profilePicture_xpath = (By.XPATH, "//div[@class='user-thumbnail']")
    coverphoto_xpath = (By.XPATH, "//button[@class='edit-cover-btn']")
    finalPrp_cssSel = (By.XPATH, "//input[@id='profilePic']")
    toast_profilePicChangeMessage_xpath = (By.XPATH,"//*[contains(text(),'Profile photo updated successfully')]")
    toast_coverPicChangeMessage_xpath = (By.XPATH, "//*[contains(text(),'Cover photo updated successfully')]")
    myGifs_xpath = (By.XPATH, "//ul[@class='cardList']/li[1]/a")
    myGifs2_xpath = (By.XPATH, "//ul[@class='cardList']/li[2]/a")
    button_homepage_xpath = (By.XPATH, "//body/div[@id='_gifbuz']/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[1]/img[1]")
    box_profile_pic_xpath = (By.XPATH, "//div[@class='user-dropdown me-3']")

    def __init__(self, driver):
        self.driver = driver

    def GifCreateMessage(self):
        return self.driver.find_element(*Dashboard.GifCreateMessage_xpath).text

    def profilePicChange(self):
        return self.driver.find_element(*Dashboard.profilePicture_xpath).click()

    def CoverPhotoPicChange(self):
        return self.driver.find_element(*Dashboard.coverphoto_xpath).click()

    def ProfilePicChangeMessage(self):
        return self.driver.find_element(*Dashboard.toast_profilePicChangeMessage_xpath)

    def CoverPhotoChangeMessage(self):
        return self.driver.find_element(*Dashboard.toast_coverPicChangeMessage_xpath)

    def MyGifCollections(self):
        return self.driver.find_element(*Dashboard.myGifs_xpath)

    def Profile(self):
        return self.driver.find_element(*Dashboard.box_profile_pic_xpath).click()

    def HomePage(self):
        return self.driver.find_element(*Dashboard.button_homepage_xpath).click()
