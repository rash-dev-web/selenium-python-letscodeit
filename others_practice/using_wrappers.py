from selenium import webdriver
from others_practice.handy_wrappers import HandyWrappers
import time
from selenium.webdriver.common.by import By


class UsingWrappers:

    def get_text_method(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\rashe\\Documents\\AutomationFiles\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        text_field1 = hw.get_element('name')
        text_field1.send_keys('testing')
        time.sleep(3)
        text_field2 = hw.get_element("//input[@id='name']", locator_type='xpath')
        text_field2.clear()

        element_result1 = hw.is_element_present('name', By.ID)
        print(element_result1)

        element_result2 = hw.element_presence_check("//input[@id='name']", By.XPATH)
        print(element_result2)
        time.sleep(5)
        driver.quit()


ch = UsingWrappers()
ch.get_text_method()
