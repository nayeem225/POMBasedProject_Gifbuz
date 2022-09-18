import time

from selenium.webdriver.common.by import By


class profilePic:
    # Login Page

    finalPrp_cssSel = (By.XPATH, "//input[@id='profilePic']")
    button_submit_xpath= (By.XPATH,"//div[@class='d-flex align-items-center justify-content-center mt-3']/button")

    def __init__(self, driver):
        self.driver = driver

    def FinalProfPic(self):
        return self.driver.find_element(*profilePic.finalPrp_cssSel).send_keys(
            r"C:\Users\Brain Craft\Desktop\giphy.gif")

    def SubmitButton(self):
        return self.driver.find_element(*profilePic.button_submit_xpath).click()
