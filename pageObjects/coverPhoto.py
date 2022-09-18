from selenium.webdriver.common.by import By


class CoverPhoto:
    # Login Page

    finalCoverPhto_Xpath = (By.XPATH, "//input[@id='coverPic']")
    button_submit_xpath= (By.XPATH,"//div[@class='d-flex align-items-center justify-content-center mt-3']/button")

    def __init__(self, driver):
        self.driver = driver

    def FinalCoverPhto(self):
        return self.driver.find_element(*CoverPhoto.finalCoverPhto_Xpath).send_keys(
            r"C:\Users\Brain Craft\Desktop\giphy (1).gif")

    def SubmitButton(self):
        return self.driver.find_element(*CoverPhoto.button_submit_xpath).click()