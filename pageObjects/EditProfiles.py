import time

from selenium.webdriver.common.by import By


class EditProfiles:
    # Login Page

    button_Save_xpath = (By.XPATH, "//body/div[@id='_gifbuz']/main[1]/section[3]/div[1]/div[1]/div[1]/form[1]/div["
                                   "5]/button[1]")
    box_displayName_xpath = (By.XPATH, "//input[@id='displayName']")

    box_about_xpath = (By.XPATH, "//textarea[@id='about']")

    box_website_xpath = (By.XPATH, "//input[@id='blogUrl']")

    box_fblink_xpath = (By.XPATH, "///input[@id='facebookProfile']")

    box_insta_xpath = (By.XPATH, "//input[@id='instagramProfile']")

    box_twitter_xpath = (By.XPATH, "//input[@id='twitterProfile']")

    # link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def DisplayName(self):
        editname = self.driver.find_element(*EditProfiles.box_displayName_xpath)
        editname.clear()
        # time.sleep()
        editname.send_keys("this is mi")
        return editname

    def SaveButton(self):
        return self.driver.find_element(*EditProfiles.button_Save_xpath).click()

    def About(self):
        editAbout = self.driver.find_element(*EditProfiles.box_about_xpath)
        editAbout.clear()
        time.sleep(5)
        editAbout.send_keys("this is mi")
        time.sleep(7)
        return editAbout

    def Website(self):
        editname = self.driver.find_element(*EditProfiles.box_displayName_xpath)
        editname.clear()
        time.sleep(5)
        editname.send_keys("this is mi")
        time.sleep(7)
        return editname

    def FaceBook(self):
        editname = self.driver.find_element(*EditProfiles.box_displayName_xpath)
        editname.clear()
        time.sleep(5)
        editname.send_keys("this is mi")
        time.sleep(7)
        return editname

    def Instagram(self):
        editname = self.driver.find_element(*EditProfiles.box_displayName_xpath)
        editname.clear()
        time.sleep(5)
        editname.send_keys("this is mi")
        time.sleep(7)
        return editname

    def Twitter(self):
        editname = self.driver.find_element(*EditProfiles.box_displayName_xpath)
        editname.clear()
        time.sleep(5)
        editname.send_keys("this is mi")
        time.sleep(7)
        return editname
