import time

from selenium.webdriver.common.by import By

from pageObjects.TrimVideo import TrimVideo


class UploadFile:
    button_select_video_xpath = (By.XPATH, "//input[@name='UploadGifChoseFile']")
    # button_start_over_xpath =(By.XPATH,"//div[@class= 'col-6 col-sm-5 col-md-4 col-lg-5']/a")

    def __init__(self, driver):
        self.driver = driver

    def SendFile(self):
        return  self.driver.find_element(*UploadFile.button_select_video_xpath).send_keys(
            r"C:\Users\Brain Craft\Desktop\giphy.gif")
        # time.sleep(5)
        # trimvideo = TrimVideo(self.driver)
        # return editname, trimvideo.Continue()




