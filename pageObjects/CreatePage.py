import time

from selenium.webdriver.common.by import By


class CreatePage:
    button_text_xpath = (By.XPATH, "//input[@placeholder ='Enter your text']")
    button_title_css = (By.CSS_SELECTOR, "#gifTitle")
    button_tags_xpath = (By.XPATH, "//label[@for='tags']/following-sibling::input")
    button_continueUpload_xpath = (By.XPATH, "//button[contains(text(),'Continue to Upload')]")
    button_category_xpath = (By.XPATH, "//label[contains(text(),'Places')]")
    button_UploadGif_xpath = (By.XPATH, "//span[contains(text(),'Upload GIF')]")

    def __init__(self, driver):
        self.driver = driver

    def TextBox(self):
        return self.driver.find_element(*CreatePage.button_text_xpath).send_keys("This test")

    def Title(self):
        title = self.driver.find_element(*CreatePage.button_title_css).send_keys("best")
        return title

    def Tags(self):
        return self.driver.find_element(*CreatePage.button_tags_xpath).send_keys("This is a test")

    def Upload(self):
        return self.driver.find_element(*CreatePage.button_continueUpload_xpath).click()

    def Categroy(self):
        return self.driver.find_element(*CreatePage.button_category_xpath).click()

    def UoloadGif(self):
        return self.driver.find_element(*CreatePage.button_UploadGif_xpath)
