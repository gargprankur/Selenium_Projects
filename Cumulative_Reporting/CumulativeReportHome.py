from selenium.webdriver.common.by import By


class CumulativeReportHome:

    def __init__(self, driver):
        self.driver = driver

    iframe = (By.XPATH, '"iframe"')
    product = (By.XPATH, '//div[@data-parametername = "Product"]/select')
    code = (By.XPATH, '//div[@data-parametername = "ProductVersionID"]/select')
    test_cycle = (By.XPATH, '//div[@data-parametername = "TestCycleID"]/div/table/tbody/tr/td/input')
    selected_test_cycle = (By.XPATH, '//label[contains(text(), "Cumulative")]')
    select_all = (By.XPATH, '//label[contains(text(), "(Select All)")]')
    qual = (By.XPATH, '//div[@data-parametername = "QualIDs"]/div/table/tbody/tr/td/input')
    selected_qual = (By.XPATH, '//label[contains(text(), "9605")]')
    approved = (By.XPATH, '//div[@data-parametername = "Approved"]/div/table/tbody/tr/td/input')
    approve_all = (By.XPATH, '//label[contains(text(), "(Select All)")]')
    submit = (By.XPATH, '//input[@type = "submit"]')

    drop_down = (By.XPATH, '//a[@title = "Export drop down menu"]')

    element_to_be_present = (By.XPATH, '//span[text() = "Test Cycle"]')

    down_arrow = (By.XPATH, '//a[@title =  "Export drop down menu"]/span[contains(@class, "glyphui-save")]')

    download = (By.LINK_TEXT, 'Excel')

    def get_iframe(self):
        return self.driver.find_element(*CumulativeReportHome.iframe)

    def get_product(self):
        return self.driver.find_element(*CumulativeReportHome.product)

    def get_code(self):
        return self.driver.find_element(*CumulativeReportHome.code)

    def get_test_cycle(self):
        return self.driver.find_element(*CumulativeReportHome.test_cycle)

    def select_test_cycle(self):
        return self.driver.find_element(*CumulativeReportHome.selected_test_cycle)

    def select_qual_input(self):
        return self.driver.find_element(*CumulativeReportHome.qual)

    def get_select_all(self):
        return self.driver.find_element(*CumulativeReportHome.select_all)

    def select_qual(self):
        return self.driver.find_element(*CumulativeReportHome.selected_qual)

    def get_approved(self):
        return self.driver.find_element(*CumulativeReportHome.approved)

    def get_approve_all(self):
        return self.driver.find_element(*CumulativeReportHome.approve_all)

    def get_submit(self):
        return self.driver.find_element(*CumulativeReportHome.submit)

    def get_down_arrow(self):
        return self.driver.find_element(*CumulativeReportHome.down_arrow)

    def get_download(self):
        return self.driver.find_element(*CumulativeReportHome.download)