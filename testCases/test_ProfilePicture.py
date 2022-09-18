import time
import unittest
import pytest
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
from pageObjects.EditProfiles import EditProfiles
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.Profile import Profile
# from pageObjects.trimVideo import TrimVideo
from pageObjects.SinglePageGif import SinglePageGif
from pageObjects.TrimVideo import TrimVideo
from pageObjects.coverPhoto import CoverPhoto
from pageObjects.profilePic import profilePic
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

        url = "https://gifbuz.com/dashboard/my-uploads"

        assert self.driver.current_url == url, "Not Logged In"

        wrongemailtext = "Incorrect email or password."

        if wrongemailtext == lp.text_wrong_email_pass_xpath:
            print("perfect")

        time.sleep(10)



    def test_5_profilepictureChange(self):
        dashboard = Dashboard(self.driver)
        dashboard.profilePicChange()
        self.click_on_using_js(self.driver.find_element(By.XPATH, "//div[@class='user-dropdown me-3']"))
        self.verifyLinkPresenenceUploadXpath("//div[@class='d-flex align-items-center justify-content-center mt-3']/button")
        profilepic = profilePic(self.driver)
        time.sleep(5)
        self.click_on_using_js(self.driver.find_element(By.XPATH, "//div[@class='user-dropdown me-3']"))
        profilepic.FinalProfPic()
        time.sleep(15)
        profilepic.SubmitButton()
        time.sleep(5)
        self.verifyLinkPresenenceUploadXpath("//*[contains(text(),'Profile photo updated successfully')]")

        # assert dashboard.ProfilePicChangeMessage() == "Profile photo updated successfully" , "ProfilePicture not changed"
        #
        # print(dashboard.ProfilePicChangeMessage().text)

    def test_6_profileCoverPhotoChange(self):
        dashboard = Dashboard(self.driver)
        self.click_on_using_js(self.driver.find_element(By.XPATH, "//button[@class='edit-cover-btn']"))
        self.verifyLinkPresenenceUploadXpath( "//div[@class='d-flex align-items-center justify-content-center mt-3']/button")
        coverPhoto = CoverPhoto(self.driver)
        time.sleep(5)
        coverPhoto.FinalCoverPhto()
        time.sleep(3)
        coverPhoto.SubmitButton()
        time.sleep(5)
        self.verifyLinkPresenenceUploadXpath("//*[contains(text(),'Cover photo updated successfully')]")

        # assert dashboard.CoverPhotoChangeMessage() == "Cover photo updated successfully" , "Cover Picture not changed"

        print(dashboard.CoverPhotoChangeMessage().text)
    #
    def test_7_LogOut(self):
        dashboard = Dashboard(self.driver)
        singlepage = SinglePageGif(self.driver)
        time.sleep(15)
        hp = HomePage(self.driver)
        profile = Profile(self.driver)
        hp.Profile()
        profile.LogOut()
        self.verifyLinkPresenenceUploadXpath("//button[contains(text(),'Login')]")
