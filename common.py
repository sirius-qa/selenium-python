# Common Locators go here
class CustomButtonLocators:
    BUTTON = """
        //button[starts-with(@class, 'MuiButtonBase-root')]
        /span[@class='MuiButton-label'][contains(text(), '{}')]
    """
