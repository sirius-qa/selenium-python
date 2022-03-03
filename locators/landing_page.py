from selenium.webdriver.common.by import By


# Landing Page locators go here
class LandingPageLocators:
    INPUT_EMAIL = (By.NAME, "email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    BUTTON_SUBMIT = (
        By.XPATH,
        "//button[@type='submit']/span[contains(text(), 'Log In')]",
    )

    HOME_TITLE = (By.XPATH, "//h3[contains(text(), 'Home')]")
