import time
import unittest
import pytest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
# from pageObjects.CreateGif import CreateGif
from pageObjects.CreateGif import CreateGif
from pageObjects.CreatePage import CreatePage
from pageObjects.Dashboard import Dashboard
from pageObjects.DeletePage import DeletePage
from pageObjects.EditProfiles import EditProfiles
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.Profile import Profile
# from pageObjects.trimVideo import TrimVideo
from pageObjects.SinglePageGif import SinglePageGif
from pageObjects.TrimVideo import TrimVideo
from pageObjects.Upload import Upload
from pageObjects.editGif import EditGif
from pageObjects.uploadfile import UploadFile
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")

class Test_LoginTest(BaseClass):

    def test_1_cookie(self):
        hp = HomePage(self.driver)
        # Log-In Page
        lp = LoginPage(self.driver)

        # Tasks........
        self.verifyLinkPresenenceUploadID("rcc-confirm-button")
        hp.CookieAccept()

    def test_2_TitleCheck(self):
        hp = HomePage(self.driver)
        # Log-In Page
        lp = LoginPage(self.driver)

    def test_3_login(self):
        # Home-Page
        hp = HomePage(self.driver)
        # Log-In Page
        lp = LoginPage(self.driver)

        # Tasks........
        # hp.CookieAccept()

        hp.LogIn()
        self.verifyLinkPresenenceUploadXpath("//button[@class='login-btn']")
        lp.setEmail()
        time.sleep(1)
        lp.setPassword()
        time.sleep(2)
        lp.clickLogin()
        self.verifyLinkPresenenceUploadXpath("//div[@class='user-dropdown me-3']")
        time.sleep(15)

        url = "https://gifbuz.com/dashboard/my-uploads"

        assert self.driver.current_url == url, "Not Logged In"

        wrongemailtext = "Incorrect email or password."

        if wrongemailtext == lp.text_wrong_email_pass_xpath:
            print("perfect")



    def test_04_UploadedGif_Action1(self):
        dashboard = Dashboard(self.driver)
        singlepage = SinglePageGif(self.driver)
        editgif = EditGif(self.driver)
        # dashboard.ScrolTo()
        time.sleep(25)
        self.click_on_using_js(self.driver.find_element(By.XPATH,"//ul[@class='cardList']/li[1]/a"))
        time.sleep(19)
        self.verifyLinkPresenenceUploadXpath(
            "//ul[@class='SingleDetails_gifActions__OlzrF d-flex align-items-center']//li//a")
        time.sleep(20)
        self.click_on_using_js(self.driver.find_element(By.XPATH,"//ul[@class='SingleDetails_gifActions__OlzrF d-flex align-items-center']//li//a"))
        self.verifyLinkPresenenceUploadXpath("//span[contains(text(),'Save')]")

    def test_05_UploadedGif_Action2_editing(self):
        dashboard = Dashboard(self.driver)
        singlepage = SinglePageGif(self.driver)
        editgif = EditGif(self.driver)
        editgif.Title()
        # editgif.Title().clear()
        # time.sleep(5)
        newTitle = "This is an error"
        editgif.Title().click()
        editgif.Title().send_keys(newTitle)
        time.sleep(5)
        self.click_on_using_js(self.driver.find_element(By.XPATH,"//span[normalize-space()='Save']"))
        self.verifyLinkPresenenceUploadXpath(
            "//*[contains(text(),'Resource updated successfully.')]")
        assert singlepage.GifEdit() == newTitle, "SOMETHING IS WRONG"
        time.sleep(10)

    def test_06_UploadedGif_Action_deleting(self):
        profile = Profile(self.driver)
        singlepage = SinglePageGif(self.driver)
        singlepage.Profile()
        time.sleep(5)
        profile.Dashboard()
        # self.verifyLinkPresenenceUploadXpath("//div[@class='user-info-wrap']/h2")
        # dashboard = Dashboard(self.driver)
        time.sleep(10)
        # Gifclick= dashboard.MyGifCollections().click()
        self.click_on_using_js(self.driver.find_element(By.XPATH,"//ul[@class='cardList']/li[1]/a"))
        deletepage = DeletePage(self.driver)
        time.sleep(5)
        self.click_on_using_js(self.driver.find_element(By.XPATH, "//div[@class='related-tags mt-3 mt-md-5']/ul/li/button"))
        self.verifyLinkPresenenceUploadXpath("//button[contains(text(),'Yes')]")
        self.click_on_using_js(self.driver.find_element(By.XPATH,"//button[contains(text(),'Yes')]"))
        # deletepage.Yes()
        self.verifyLinkPresenenceUploadXpath("//*[contains(text(),'Gif deleted successfully.')]")

    def test_8_LogOut(self):
        dashboard = Dashboard(self.driver)
        singlepage = SinglePageGif(self.driver)
        time.sleep(15)
        hp = HomePage(self.driver)
        profile = Profile(self.driver)
        hp.Profile()
        profile.LogOut()
        self.verifyLinkPresenenceUploadXpath("//button[contains(text(),'Login')]")
