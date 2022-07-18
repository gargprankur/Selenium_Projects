from selenium.webdriver.common.by import By


class CATQualPage:
    def __init__(self, driver):
        self._driver = driver

    more_actions = (By.XPATH, '//a[@class = "more-actions-a"]')
    clone = (By.XPATH, '//div[@class = "more-actions-dropdown opened"]/a[text()="Clone"]')

    qual_name = (By.XPATH, '//input[@value = "Clone of: Cummulative Epack 9537"]')

    qual_description = (By.XPATH, '//textarea[contains(text(), "9537 Cummulative Epack Testin")]')

    qual_exists = (By.XPATH, '//label[@class = "error"]')

    save = (By.XPATH, '//a[contains(text(),"Save")]')


    def more_actions_dropdown(self):
        return self._driver.find_element(*CATQualPage.more_actions)

    def qual_clone(self):
        return self._driver.find_element(*CATQualPage.clone)

    def qual_name_textbox(self):
        return self._driver.find_element(*CATQualPage.qual_name)

    def qual_description_textbox(self):
        return self._driver.find_element(*CATQualPage.qual_description)

    def qual_exists_error(self):
        return self._driver.find_element(*CATQualPage.qual_exists)

    def save_button(self):
        return self._driver.find_element(*CATQualPage.save)


