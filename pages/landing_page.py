from locators.landing_page import LandingPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from pages.page import BasePage


class LandingPage(BasePage):
    """
    Methods to locate HTML elements
    """

    def get_input_email(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(
                *LandingPageLocators.INPUT_EMAIL
            )
        )

    def get_input_password(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(
                *LandingPageLocators.INPUT_PASSWORD
            )
        )

    def get_button_submit(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(
                *LandingPageLocators.BUTTON_SUBMIT
            )
        )

    """
    Methods to simulate user actions
    """

    def enter_email(self):
        element = self.get_input_email()
        self.set_input_text("nicoulmete1@gmail.com", element)

    def enter_password(self):
        self.set_input_text("Arenaza2135!", self.get_input_password())

    def click_submit(self):
        self.click_element(self.get_button_submit())

    """
    Misc
    """

    def is_logged_in(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*LandingPageLocators.HOME_TITLE)
        )

    def is_on_dashboard(self):
        return (
            self.driver.title == "Activity | Burb"
            and self.driver.current_url
            == "https://app.burb-dev.co/dashboard?page=1"
        )
