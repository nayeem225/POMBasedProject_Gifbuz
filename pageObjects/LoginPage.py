from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    # Login Page

    textbox_email_xpath = (By.XPATH, "//input[@id='email']")
    textbox_password_css = (By.XPATH, "//input[@id='password']")
    button_login_xpath = (By.XPATH, "//button[@class='login-btn']")
    text_wrong_email_pass_xpath = (By.XPATH, "//p[contains(text(),'Incorrect email or password.')]")

    # link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self):
        return self.driver.find_element(*LoginPage.textbox_email_xpath).send_keys("esdras.henrique@fillnoo.com")

    def setPassword(self):
        return self.driver.find_element(*LoginPage.textbox_password_css).send_keys("Nayeem-225!")

    def clickLogin(self):
        return self.driver.find_element(*LoginPage.button_login_xpath).click()


    def checkEmailWrong(self):
        return self.driver.find_element(*LoginPage.text_wrong_email_pass_xpath).text

#
#
# class LoginPage:
#     textbox_email_address_xpath = "//input[@id='email']"
#     textbox_password_css = "#password"
#     button_login_button_xpath = "//button[@class='login-btn']"
#     button_logout_button_xpath = "//button[contains(text(),'Logout')]"
#
#     def __int__(self, driver):
#         self.driver = driver
#
#     def setEmailAddress(self, emailAddress):
#         self.driver.find_element_by_xpath(self.textbox_email_address_xpath).send_keys(emailAddress)
#
#     def setPassword(self, password):
#         self.driver.find_element_by_xpath(self.textbox_password_css).send_keys(password)
#
#     def LoginButton(self):
#         self.driver.find_element_by_xpath(self.button_login_button_xpath).click()
#
#     # def LogOutButton(self):
#     #     self.driver.find_element_by_xpath(self.button_logout_button_xpath).click()
