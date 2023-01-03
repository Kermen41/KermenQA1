# Locators

from selenium.webdriver.common.by import By

class Locators:
    # Home Page

    # Home page Url and title
    home_page_url = 'https://52.33.5.136'
    home_page_title = 'Moodle Test Server 2'

    # Home page locators
    login_link_search = By.LINK_TEXT
    login_link = 'log in'

    # Login Page

    # Login page URL and title
    login_page_url = 'https://52.33.5.136/login/index.php'
    login_page_title = 'Moodle Test Server 2: Log in to the site'

    #Login page Locators
    username_field_search = By.ID
    username_field = 'username'

    password_field_search = By.ID
    password_field = 'password'

    # Dashboard Page

    # Dashboard URL and title
