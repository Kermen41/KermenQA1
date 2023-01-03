# Home Page Object

# Import locators
from QA1_Project.PagesObjects.Locators import Locators

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Home page action methods
    def click_login_link(self):

        self.driver.find_element(Locators.login_link_search, Locators.login_link).click()
