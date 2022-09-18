import time

from selenium.webdriver.common.by import By

from pageObjects.TrimVideo import TrimVideo


class CreateGif:
    button_select_video_xpath = (By.XPATH, "//input[@type='file']")


    def __init__(self, driver):
        self.driver = driver

    def SendFile(self):
        return self.driver.find_element(*CreateGif.button_select_video_xpath).send_keys(
            r"C:\Users\Brain Craft\Desktop\VID20220825163012.mp4")
        # time.sleep(5)
        # trimvideo = TrimVideo(self.driver)
        # return editname, trimvideo.Continue()
