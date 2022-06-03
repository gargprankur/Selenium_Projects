from selenium.webdriver.common.by import By

class AdiosPlusDespatch:
    def __init__(self, driver):
        self.driver = driver

    search = (By.XPATH, '//span[contains(@class, "search-plus")]')

    clear_filter = (By.XPATH, '//span[text() = "Clear Filters"]')

    suite_name = (By.XPATH, '//input[@id = "NAME"]')

    search_suite = (By.XPATH, '//div[@class = "resource-search-btns"]/button/span[text() = "Search"]')

    select_suite = (By.XPATH, '//input[@class = "ant-checkbox-input"]')

    right_arrow = (By.XPATH, '//div[@class = "ant-transfer-operation"]/button[contains(@class, "ant-btn")]')

    all_suites = (By.XPATH, '//input[@class = "ant-checkbox-input"]')

    add_suites = (By.XPATH, '//span[text() = "Add Suites To View"]/parent::button')

    run_suite = (By.XPATH, '//input[@class = "ant-input"]')

    search_run_suite = (By.XPATH, '//button[contains(@class,"ant-input-search-button")]')

    select_suite_to_run = (By.XPATH, '//span[@class = "ant-tree-checkbox-inner"]')

    test_cycle = (By.XPATH, '//span[text() = "Select test cycle"]/parent::div/span/input')

    select_test_cycle = (By.XPATH, '//div[@title = "Cumulative ePack test cycle"]')

    qual = (By.XPATH, '//span[text() = "Select qualification"]/parent::div/span/input')

    select_qual = (By.XPATH, '//div[@title = "Cumulative_Epack_9911"]')

    host = (By.XPATH, '//span[text() = "Select a host"]/parent::div/span/input')

    symm = (By.XPATH, '//span[text() = "Select a primary storage"]/parent::div/span/input')

    host_select_message = (By.XPATH, '//span[contains(@class, "host-badge-message")]/span[2]')

    run = (By.XPATH, '//span[text() = "Run"]/parent::button')

    ok_button = (By.XPATH, '//span[text() = "OK"]/parent::button')

    clear_suite = (By.XPATH, '//span[contains(@class, "ant-input-clear-icon")]')

    deselect_suite = (By.XPATH, '//a[text() = "Deselect All"]')

    after_run_message = (By.XPATH, '//a[text() = "See detailed report"]')

    close = (By.XPATH, '//span[@aria-label = "close"]')
    def search_button(self):
        return self.driver.find_element(*AdiosPlusDespatch.search)

    def clear_filter_button(self):
        return self.driver.find_element(*AdiosPlusDespatch.clear_filter)

    def enter_suite_name(self):
        return self.driver.find_element(*AdiosPlusDespatch.suite_name)

    def search_suite_button(self):
        return self.driver.find_element(*AdiosPlusDespatch.search_suite)

    def select_suite_checkbox(self):
        return self.driver.find_elements(*AdiosPlusDespatch.select_suite)

    def select_right_arrow(self):
        return self.driver.find_element(*AdiosPlusDespatch.right_arrow)

    def select_all_suites(self):
        return self.driver.find_elements(*AdiosPlusDespatch.all_suites)

    def add_suites_button(self):
        return self.driver.find_element(*AdiosPlusDespatch.add_suites)

    def search_suite_to_run(self):
        return self.driver.find_element(*AdiosPlusDespatch.run_suite)

    def suite_add_button(self):
        return self.driver.find_element(*AdiosPlusDespatch.search_run_suite)

    def select_suite_to_despatch(self):
        return self.driver.find_element(*AdiosPlusDespatch.select_suite_to_run)

    def test_cycle_input(self):
        return self.driver.find_element(*AdiosPlusDespatch.test_cycle)

    def click_test_cycle(self):
        return self.driver.find_element(*AdiosPlusDespatch.select_test_cycle)

    def qual_input(self):
        return self.driver.find_element(*AdiosPlusDespatch.qual)

    def click_test_qual(self):
        return self.driver.find_element(*AdiosPlusDespatch.select_qual)

    def host_input(self):
        return self.driver.find_element(*AdiosPlusDespatch.host)

    def select_symm(self):
        return self.driver.find_element(*AdiosPlusDespatch.symm)

    def get_host_message(self):
        return self.driver.find_element(*AdiosPlusDespatch.host_select_message)

    def run_button(self):
        return self.driver.find_element(*AdiosPlusDespatch.run)

    def ok_button_function(self):
        return self.driver.find_element(*AdiosPlusDespatch.ok_button)

    def clear_search_suite(self):
        return self.driver.find_element(*AdiosPlusDespatch.clear_suite)

    def deselect_suite_link(self):
        return self.driver.find_element(*AdiosPlusDespatch.deselect_suite)

    def get_after_run_message(self):
        return self.driver.find_element(*AdiosPlusDespatch.after_run_message)

    def close_button(self):
        return self.driver.find_element(*AdiosPlusDespatch.close)