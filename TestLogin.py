# Login Test Case

# Import packages, Modules
from time import sleep
import unittest
from selenium import webdriver

# Import locators, test data
from QA1_Project.PagesObjects.Locators import Locators
from QA1_Project.PagesObjects.TestData import TestData

# import pages
from QA1_Project.PagesObjects.Pages.HomePage import HomePage
from QA1_Project.PagesObjects.Pages.LoginPage import LoginPage


class TestLogin(unittest.TestCase):

    def SetUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(Locators.home_page_url)

    def TestLogin(self):

        # login credentials
        username = TestData.testuser1_username
        password = TestData.testuser1_password

        # Click login link
        homepage = HomePage(self.driver)
        homepage.click_login_link()

        # Enter credential and log in
        loginpage = LoginPage(self.driver)
        loginpage.enter_username(username)
        loginpage.enter_password(password)
        loginpage.click_login()

    def teardown(self):

        sleep(3)
        self.driver.close()
        self.driver.quit()
        print('Test successful completed')
