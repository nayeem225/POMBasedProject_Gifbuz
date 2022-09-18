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

        url = "https://gifbuz.com/dashboard/my-uploads"

        assert self.driver.current_url == url, "Not Logged In"

        wrongemailtext = "Incorrect email or password."

        if wrongemailtext == lp.text_wrong_email_pass_xpath:
            print("perfect")

        time.sleep(10)

    # def test_4_profileButton(self):
    #     # Home-Page
    #     hp = HomePage(self.driver)
    #     # Log-In Page
    #     lp = LoginPage(self.driver)
    #
    #     profile = Profile(self.driver)
    #     hp.Profile()
    #     profile.EditProfile()
    #     self.verifyLinkPresenenceUploadXpath(
    #         "//body/div[@id='_gifbuz']/main[1]/section[3]/div[1]/div[1]/div[1]/form[1]/div[5]/button[1]")

    def test_5_editProfile(self):
        # js = JavascriptExecutor(self.driver)
        dashboard = Dashboard(self.driver)
        hp = HomePage(self.driver)
        editProf = EditProfiles(self.driver)
        profile = Profile(self.driver)
        dashboard.Profile()
        profile.EditProfile()
        self.verifyLinkPresenenceUploadCSS("form[class='chanel-settings mt-3'] button[type='submit']")
        editProf.DisplayName()
        time.sleep(25)
        About = self.driver.find_element(By.XPATH, " //textarea[ @ id = 'about']")
        # self.click_on_using_js(About)
        # self.driver.execute_script("some javascript code here")
        # we need to work on this to send keys
        editProf.SaveButton()
        time.sleep(12)

    def test_6_CreateGif_createFile(self):
        # Home-Page
        hp = HomePage(self.driver)
        db = Dashboard(self.driver)
        createpage = CreatePage(self.driver)
        crGif = CreateGif(self.driver)
        db.HomePage()
        time.sleep(25)
        hp.CreateGif()
        time.sleep(5)
        self.verifyLinkPresenenceUploadXpath("//input[@type='file']")
        trimvideo = TrimVideo(self.driver)
        crGif.SendFile()
        self.verifyLinkPresenenceUploadXpath('//div[@class= "col-6 col-sm-7 col-md-8 col-lg-7"]/button')

    def test_7_CreateGif_TrimVideo(self):
        trimvideo = TrimVideo(self.driver)
        trimvideo.Continue()
        self.verifyLinkPresenenceUploadXpath("//button[contains(text(),'Continue to Upload')]")

    def test_8_CreateGif_CreatePage1(self):
        crGif = CreateGif(self.driver)
        createpage = CreatePage(self.driver)
        self.click_on_using_js(self.driver.find_element(By.XPATH,"//button[contains(text(),'Continue to Upload')]"))
        # createpage.Upload()
        time.sleep(35)
        self.verifyLinkPresenenceUploadXpath("//span[contains(text(),'Upload GIF')]")

    def test_9_CreateGif_CreatePage2(self):
        dashboard = Dashboard(self.driver)
        createpage = CreatePage(self.driver)
        createpage.Title()
        time.sleep(5)
        createpage.Tags()
        time.sleep(5)
        self.click_on_using_js(self.driver.find_element(By.XPATH,"//label[contains(text(),'Places')]"))
        # createpage.Categroy()
        time.sleep(5)
        createpage.UoloadGif().click()
        self.verifyLinkPresenenceUploadXpath("//div[@class='react-toast-notifications__toast__content css-1ad3zal']")
        print(dashboard.GifCreateMessage())
        assert dashboard.GifCreateMessage() == "Gif created successfully", "Something is wrong"
        # dashboard.HomePage()
        time.sleep(15)

    def test_10_UploadGif_Upload_File(self):
        dashboard = Dashboard(self.driver)
        homepage = HomePage(self.driver)
        uploadgif = UploadFile(self.driver)
        upload=Upload(self.driver)
        # homepage.Upload()
        self.click_on_using_js(self.driver.find_element(By.XPATH, "// span[contains(text(), 'Upload')]"))
        self.verifyLinkPresenenceUploadXpath("//div[@class='col-lg-8 order-0 order-lg-2']/div/label")
        # self.driver.execute_script("window.scrollTo(0, Y)")
        uploadgif.SendFile()
        self.verifyLinkPresenenceUploadXpath("//span[normalize-space()='Upload GIF']")
        upload = Upload(self.driver)
        time.sleep(2)
        upload.Title()
        time.sleep(2)
        upload.Tags()
        time.sleep(2)
        upload.Categroy()
        time.sleep(2)
        self.click_on_using_js(self.driver.find_element(By.XPATH, "//span[normalize-space()='Upload GIF']"))
    #     # myLoad = self.driver.find_element(By.XPATH("//span[contains(text(),'Upload')]"))
    #     # self.driver.execute_script("arguments[0].scrollIntoView();", myLoad)
    #     self.driver.execute_script("window.scrollTo(0, 1000)")
    #     self.elementIsClickable("//span[contains(text(),'Upload GIF')]")
        self.verifyLinkPresenenceUploadXpath("//div[@class='react-toast-notifications__toast__content css-1ad3zal']")
        print(dashboard.GifCreateMessage())
        time.sleep(10)
    #
    def test_12_LogOut(self):
        dashboard = Dashboard(self.driver)
        self.click_on_using_js(self.driver.find_element(By.XPATH, "//img[@alt='User']"))
        # time.sleep(5)
        # self.verifyLinkPresenenceUploadXpath("//button[contains(text(),'Logout')]")
        self.click_on_using_js(self.driver.find_element(By.XPATH, "//button[contains(text(),'Logout')]"))
        # profile = Profile(self.driver)
        # profile.LogOut()
        self.verifyLinkPresenenceUploadXpath("//button[contains(text(),'Login')]")
