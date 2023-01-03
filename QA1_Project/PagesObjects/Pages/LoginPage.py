# Import locators
from QA1_Project.PagesObjects.Locators import Locators

class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    # Login page action methods
    def enter_username(self, username):

        self.driver.find_element(Locators.username_field_search, Locators.username_field).clear()
        self.driver.find_element(Locators.username_field_search, Locators.username_field).click()
        self.driver.find_element(Locators.username_field_search, Locators.username_field).send_keys(username)

    def enter_password(self, password):

        self.driver.find_element(Locators.password_field_search, Locators.password_field).clear()
        self.driver.find_element(Locators.password_field_search, Locators.password_field).click()
        self.driver.find_element(Locators.password_field_search, Locators.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(Locators.login_button_search, Locators.login_button).click()
