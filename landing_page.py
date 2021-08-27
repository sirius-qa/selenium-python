from selenium.webdriver.common.by import By


# Landing Page locators go here
class LandingPageLocators:
    COUNTER = (By.XPATH, "//p[contains(text(), 'Count:')]")
