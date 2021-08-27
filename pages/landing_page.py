from locators.landing_page import LandingPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from pages.page import BasePage
from locators.common import CustomButtonLocators


class LandingPage(BasePage):
    def get_counter(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*LandingPageLocators.COUNTER)
        )

    def get_counter_text(self):
        return self.get_element_text(self.get_counter())

    def get_button_by_text(self, text: str):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_xpath(
                CustomButtonLocators.BUTTON.format(text)
            )
        )
