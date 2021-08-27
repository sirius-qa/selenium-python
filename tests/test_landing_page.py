import pytest
from pages.landing_page import LandingPage
from utils.custom_logger import LogGen
from selenium.common.exceptions import TimeoutException


class TestLandingPage:
    logger = LogGen.loggen()

    DECREMENT_BTN_TEXT = "-1"
    RESET_BTN_TEXT = "Reset"
    INCREMENT_BTN_TEXT = "+1"

    # Positive test
    @pytest.mark.parametrize(
        "testcase_id", ["Landing Page counter - positive"]
    )
    def test_landing_page_counter(self, setup, testcase_id):
        self.logger.info(
            f"******************** {testcase_id} ********************"
        )
        self.driver = setup
        landing_page = LandingPage(driver=self.driver)
        assert landing_page.get_button_by_text(self.DECREMENT_BTN_TEXT)
        assert landing_page.get_button_by_text(self.RESET_BTN_TEXT)
        assert landing_page.get_button_by_text(self.INCREMENT_BTN_TEXT)

    # Negative test
    @pytest.mark.parametrize(
        "testcase_id", ["Landing Page counter - negative"]
    )
    def test_landing_page_counter_negative(self, setup, testcase_id):
        self.logger.info(
            f"******************** {testcase_id} ********************"
        )
        self.driver = setup
        landing_page = LandingPage(driver=self.driver)
        with pytest.raises(TimeoutException):
            landing_page.get_button_by_text("Dummy text")

    @pytest.mark.parametrize("testcase_id", ["Landing Page counter - click"])
    def test_counter_click(self, setup, testcase_id):
        self.logger.info(
            f"******************** {testcase_id} ********************"
        )
        self.driver = setup
        landing_page = LandingPage(driver=self.driver)
        assert landing_page.get_counter_text() == "Count: 0"
        landing_page.click_element(
            landing_page.get_button_by_text(self.DECREMENT_BTN_TEXT)
        )
        assert landing_page.get_counter_text() == "Count: -1"
        landing_page.click_element(
            landing_page.get_button_by_text(self.RESET_BTN_TEXT)
        )
        assert landing_page.get_counter_text() == "Count: 0"
        landing_page.click_element(
            landing_page.get_button_by_text(self.INCREMENT_BTN_TEXT)
        )
        assert landing_page.get_counter_text() == "Count: 1"
        landing_page.click_element(
            landing_page.get_button_by_text(self.RESET_BTN_TEXT)
        )
        assert landing_page.get_counter_text() == "Count: 0"
