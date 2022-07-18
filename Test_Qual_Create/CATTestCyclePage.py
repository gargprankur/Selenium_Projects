from selenium.webdriver.common.by import By


class CATTestCyclePage:

    def __init__(self, driver, qual_name):
        self._driver = driver
        self._qual_name = qual_name
        self._value = f"//div[@class = 'rcbScroll rcbWidth']/ul[@class='rcbList']/li[text() = {self._qual_name}]"

    qual_field = (By.XPATH, "//td[@class = 'rcbInputCell rcbInputCellLeft']/input[@id = 'ctl00_m_genQual_cb_Input']")

    days_field = (By.XPATH, '//span[text() = "Duration"]/parent::td/input')
    #days_field = (By.XPATH, '//input[@id = "ctl00_m_genQualOccur"]')

    starting_date_field = (By.XPATH, '//input[@id = "ctl00_m_genQualStart_dateInput"]')

    ending_date_field = (By.XPATH, '//input[@id = "ctl00_m_genQualEnd_dateInput"]')

    add_button = (By.XPATH, '//input[@value = "Add"]')

    #save_button = (By.XPATH, '//span[@id = "ctl00_ButtonPanel"]/a[text() = "Save"]')
    save_button = (By.XPATH, '//a[text() = "Save"]')
    more_actions = (By.XPATH, '//a[@class = "more-actions-a"]')

    materialize = (By.XPATH, '//a[text() = "Materialize"]')


    def qual_field_textbox(self):
        return self._driver.find_element(*CATTestCyclePage.qual_field)

    def select_qual(self):
        return self._driver.find_element(By.XPATH, self._value)

    def enter_days(self):
        return self._driver.find_element(*CATTestCyclePage.days_field)

    def enter_starting_date(self):
        return self._driver.find_element(*CATTestCyclePage.starting_date_field)

    def enter_ending_date(self):
        return self._driver.find_element(*CATTestCyclePage.ending_date_field)

    def add_button_click(self):
        return self._driver.find_element(*CATTestCyclePage.add_button)

    def save_button_click(self):
        return self._driver.find_element(*CATTestCyclePage.save_button)

    def more_actions_click(self):
        return self._driver.find_element(*CATTestCyclePage.more_actions)

    def materialize_qual(self):
        return self._driver.find_element(*CATTestCyclePage.materialize)
