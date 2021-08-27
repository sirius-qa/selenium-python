from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def set_input_text(self, value, input_element):
        # remove existing text from input
        input_text = input_element.get_attribute("value")
        for i in range(len(input_text)):
            input_element.send_keys(Keys.BACKSPACE)
        # insert text into input
        input_element.send_keys(value)

    def click_element(self, element):
        element.click()

    def get_element_text(self, element):
        return element.text
