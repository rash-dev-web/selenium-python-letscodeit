from selenium import webdriver


class GetTextTest:

    def get_text_method(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\rashe\\Documents\\AutomationFiles\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        # Text of an element
        open_tab = driver.find_element_by_id('opentab')
        print('Text:: ', open_tab.text)

        # value of an attribute
        ele = driver.find_element_by_id('name')
        print('Attributes: ', ele.get_attribute('placeholder'))
        driver.quit()


ch = GetTextTest()
ch.get_text_method()
