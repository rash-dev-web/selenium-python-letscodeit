import time
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class HomePage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    log = cl.custom_logger(logging.DEBUG)

    # locators
    _login_link = "//a[text()='Sign In']"
    _email_field = 'email'
    _password_field = 'password'
    _submit_button = "//input[@type='submit']"

    # def get_sign_in_link(self):
    #     return self.driver.find_element(By.XPATH, self._login_link)
    #
    # def get_login_field(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def get_password_field(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def get_submit_button(self):
    #     return self.driver.find_element(By.XPATH, self._submit_button)

    def click_sign_in_link(self):
        self.element_click(self._login_link, locator_type='xpath')

    def enter_email(self, email):
        self.do_send_keys(email, self._email_field)

    def enter_password(self, password):
        self.do_send_keys(password, self._password_field)

    def click_submit(self):
        self.element_click(self._submit_button, 'xpath')

    def login(self, email='', password=''):
        self.click_sign_in_link()
        self.enter_email(email)
        self.enter_password(password)
        time.sleep(5)
        self.click_submit()
        # time.sleep(5)

    def verify_login_success(self):
        result = self.is_element_present("//a[text()='MY COURSES']", 'xpath')
        return result

    def verify_login_fail(self):
        # time.sleep(5)
        result = self.is_element_present("//span[contains(text(), 'invalid')]", 'xpath')
        return result

    def verify_title(self):
        if 'Login' == self.get_title():
            self.log.info('Login*******************', self.get_title())
            return True
        else:
            return False
