from selenium.webdriver.common.by import By


class Profile:
    # Login Page

    button_dashbaord_xpath = (By.XPATH, "//a[contains(text(),'Dashboard')]")
    button_edit_profile_xpath = (By.XPATH, "//a[contains(text(),'Edit Profile')]")
    button_senitive_xpath = (By.XPATH, "//a[contains(text(),'Sensitive Contents')]")
    button_logout_xpath = (By.XPATH, "//button[contains(text(),'Logout')]")

    # link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def Dashboard(self):
        return self.driver.find_element(*Profile.button_dashbaord_xpath).click()

    def EditProfile(self):
        return self.driver.find_element(*Profile.button_edit_profile_xpath).click()

    def SenstiveContents(self):
        return self.driver.find_element(*Profile.button_senitive_xpath).clcik()

    def LogOut(self):
        return self.driver.find_element(*Profile.button_logout_xpath).click()

    # def clickLogout(self):
    #     self.driver.find_element_by_link_text(self.link_logout_linktext).click()
