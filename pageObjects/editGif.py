import time

from selenium.webdriver.common.by import By


class EditGif:
    # button_text_xpath = (By.XPATH, "//input[@placeholder ='Enter your text']")
    button_title_css = (By.XPATH, "//input[@id='gifTitle']")
    button_tags_xpath = (By.XPATH, "//label[@for='tags']/following-sibling::input")
    button_continueUpload_xpath = (By.XPATH, "//button[contains(text(),'Continue to Upload')]")
    button_category_xpath = (By.XPATH, "//label[contains(text(),'Memes')]")
    button_SaveButton_xpath = (By.XPATH, "//span[contains(text(),'Save')]")

    def __init__(self, driver):
        self.driver = driver

    def Title(self):
        title = self.driver.find_element(*EditGif.button_title_css)
        title.clear()
        time.sleep(5)
        return title

    def Tags(self):
        return self.driver.find_element(*EditGif.button_tags_xpath).send_keys("This is a test")

    def Upload(self):
        return self.driver.find_element(*EditGif.button_continueUpload_xpath).click()

    def Categroy(self):
        return self.driver.find_element(*EditGif.button_category_xpath).click()

    def SaveButton(self):
        return self.driver.find_element(*EditGif.button_SaveButton_xpath).click()
