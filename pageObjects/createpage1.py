from selenium.webdriver.common.by import By


class CreatePage1:
    button_continueUpload_xpath = (By.XPATH, "//button[contains(text(),'Continue to Upload')]")

    def __init__(self, driver):
        self.driver = driver

    def Upload(self):
        return self.driver.find_element(*CreatePage1.button_continueUpload_xpath).click()
