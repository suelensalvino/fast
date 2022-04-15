from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from Pages.PageObject import PageObject

class LoginPage(PageObject):
    url = 'https://www.saucedemo.com/'
    id_login_btn = 'login-button'
    class_error_msg = 'error-message-container'
    txt_error_login_message = 'Epic sadface: Username is required'
    id_username = 'user-name'
    id_password = 'password'

    def __init__(self):
        super(LoginPage, self).__init__()
        self.driver.get(self.url)

    def click_login_button(self):
        self.driver.find_element(By.ID, self.id_login_btn).click()

    def is_login_page(self):
        is_url_login = self.driver.current_url == self.url
        try:
            login_btn = self.driver.find_element(By.ID, self.id_login_btn)
        except NoSuchElementException:
            login_btn = False

        return is_url_login and login_btn

    def has_login_message_error(self):
        error_msg = self.driver.find_element(By.CLASS_NAME, self.class_error_msg).text
        return error_msg == self.txt_error_login_message

    def make_login(self, user_name='standard_user', password='secret_sauce'):
        self.driver.find_element(By.ID, self.id_username).send_keys(user_name)
        self.driver.find_element(By.ID, self.id_password).send_keys(password)
        self.click_login_button()