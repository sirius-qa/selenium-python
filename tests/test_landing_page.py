import pytest
from pages.landing_page import LandingPage
from utils.custom_logger import LogGen
import time


class TestLandingPage:
    logger = LogGen.loggen()

    # Positive test
    @pytest.mark.parametrize("testcase_id", ["Landing Page - Login"])
    def test_login(self, setup, testcase_id):
        self.logger.info(
            f"******************** {testcase_id} ********************"
        )
        self.driver = setup

        # get the page instance
        landing_page = LandingPage(driver=self.driver)

        # enter email, password and click the submit button
        landing_page.enter_email()
        landing_page.enter_password()
        landing_page.click_submit()

        # verify that we're on the dashboard
        time.sleep(5)
        assert landing_page.is_logged_in()
