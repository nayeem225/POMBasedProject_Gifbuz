import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresenenceUploadXpath(self,text):
        myElem = WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.XPATH, text)))

    def verifyLinkPresenenceUploadCSS(self,text):
        myElem = WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, text)))

    def verifyLinkPresenenceUploadID(self,text):
        myElem = WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.ID, text)))

    def elementIsClickable(self,text):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, text))).click()

    def click_on_using_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)
