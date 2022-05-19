from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as AC


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def refresh(self):
        self.driver.refresh()


    def open_url(self, url):
        self.driver.get(url)

    
    def get_url(self, url):
        self.open_url(url)
    

    def get_title(self):
        return self.driver.title

    
    def pause(self, seconds = 1):
        AC(self.driver).pause(seconds).perform()

    
    def wait(self, time):
        WebDriverWait(self.driver, time)

    
    def wait_for(self, condition, seconds = 10):
        return WebDriverWait(self.driver, seconds).until(condition)
    

    def click(self, locator, seconds = 10):
        self.wait_for(EC.element_to_be_clickable(locator), seconds).click()

    
    def find(self, locator, seconds = 10):
        element = self.wait_for(EC.visibility_of_element_located(locator), seconds)
        return element

    
    def find_by_id(self, id):
        return self.driver.find_element_by_id(id)


    def find_in_condition(self, condition, seconds = 10):
        element = self.wait_for(condition, seconds=seconds)
        return element

    
    def find_in_presence(self, locator, seconds = 10):
        element = self.wait_for(EC.presence_of_element_located(locator), seconds)
        return element

    
    def elements_by_name(self, locator):
        return self.driver.find_elements_by_name(locator)

    
    def elements_by_class(self, locator):
        return self.driver.find_elements_by_class_name(locator)

    
    def find_elements(self, locator, seconds = 10):
        element = self.wait_for(EC.visibility_of_all_elements_located(locator), seconds)
        return element


    def clear_input(self, locator, index=0):
        if index ==0:
            self.find(locator).clear()
        else:
            self.find_elements(locator)[index].clear


    def clear_input_text(self, locator):
        element = self.find(locator)
        text = element.get_attribute('value')
        text_length = len(text)
        while text_length > 0:
            self.type_in(locator, Keys.BACK_SPACE, set_clear=False)
            text_length = text_length - 1

    
    def type_in(self, locator, text, set_clear = True, set_enter = False, click = False):
        element = self.find(locator)
        if set_clear:
            self.clear_input_text(locator)
        if click:
            self.click(locator)
        if set_enter:
            element.send_keys(text, Keys.ENTER)
        else:
            element.send_keys(text)
    

    def type_in_presence(self, locator, text, set_clear = True, set_enter = False):
        element = self.find_in_presence(locator)
        if set_clear:
            element.clear()
        if set_enter:
            element.send_keys(text, Keys.ENTER)
        else:
            element.send_keys(text)

    
    def type_in_condition(self, condition, text, set_clear = True, set_enter = False):
        element = self.find_in_condition(condition)
        if set_clear:
            element.clear()
        if set_enter:
            element.send_keys(text, Keys.ENTER)
        else:
            element.send_keys(text)