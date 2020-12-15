from traceback import print_stack

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import utilities.custom_logger as cl
import logging


class SeleniumDriver:
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        print('title...', self.driver.title)
        self.log.info('title....', self.driver.title)
        return str(self.driver.title)

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == 'id':
            return By.ID
        elif locator_type == 'name':
            return By.NAME
        elif locator_type == 'link':
            return By.LINK_TEXT
        elif locator_type == 'partiallink':
            return By.PARTIAL_LINK_TEXT
        elif locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'class':
            return By.CLASS_NAME
        elif locator_type == 'xpath':
            return By.XPATH
        else:
            self.log.info('locator type ' + locator_type + ' is not correct/supported')
        return False

    def get_element(self, locator, locator_type='id'):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info('Element found with the locator ' + locator + ' and locator type: ' + locator_type)
        except:
            self.log.info('Element not found with the locator ' + locator + ' and locator type: ' + locator_type)
        return element

    def element_click(self, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            self.log.info('clicked on the element with locator: ' + locator + ' and locator type: ' + locator_type)
        except:
            self.log.info('can not click element with locator: ' + locator + ' and locator type: ' + locator_type)
            print_stack()

    def do_send_keys(self, data, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info('sent data on the element with locator: ' + locator + ' and locator type: ' + locator_type)
        except:
            self.log.info(
                'can not sent data on element with locator: ' + locator + ' and locator type: ' + locator_type)
            print_stack()

    def is_element_present(self, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info('found element')
                return True
            else:
                return False
        except:
            self.log.info('element not found')
            return False

    def element_presence_check(self, locator, by_type):
        try:
            element_list = self.driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                self.log.info('found element')
                return True
            else:
                self.log.info('element not found')
                return False
        except:
            self.log.info('element not found')
            return False

    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element
