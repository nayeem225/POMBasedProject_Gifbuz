import time

from selenium.webdriver.common.by import By


class Upload:
    # button_text_xpath = (By.XPATH, "//input[@placeholder ='Enter your text']")
    button_uploadgif_choose_xpath=(By.XPATH,"//input[@name='UploadGifChoseFile']")
    button_title_css = (By.XPATH, "//input[@id='gifTitle']")
    button_tags_xpath = (By.XPATH, "//label[@for='tags']/following-sibling::input")
    button_continueUpload_xpath = (By.XPATH, "//button[contains(text(),'Continue to Upload')]")
    button_category_xpath = (By.XPATH, "//label[contains(text(),'Memes')]")
    button_UploadGif_xpath = (By.XPATH, "//span[normalize-space()='Upload GIF']")

    def __init__(self, driver):
        self.driver = driver


    def ChooseFile(self):
        return self.driver.find_element(*Upload.button_uploadgif_choose_xpath).click()

    def Title(self):
        title = self.driver.find_element(*Upload.button_title_css).send_keys("best")
        return title

    def Tags(self):
        return self.driver.find_element(*Upload.button_tags_xpath).send_keys("This is a test")

    def Upload(self):
        return self.driver.find_element(*Upload.button_continueUpload_xpath).click()

    def Categroy(self):
        return self.driver.find_element(*Upload.button_category_xpath).click()

    def UoloadGif(self):
        return self.driver.find_element(*Upload.button_UploadGif_xpath).click()
