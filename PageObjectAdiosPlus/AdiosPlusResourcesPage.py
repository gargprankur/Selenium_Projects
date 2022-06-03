from selenium.webdriver.common.by import By


class AdiosPlusResourcesPage:

    def __init__(self, driver):
        self.driver = driver

    resources = (By.XPATH, '//a[@href = "/resources"]')
    search_plus = (By.XPATH, '//div[@class = "resource-action-bar"]/span[contains(@class, "search-plus")]')

    host_name = (By.XPATH, '//span[text() = "hostname"]/parent::div/span/input')

    confirm = (By.XPATH, '//button[@title = "confirm"]')

    search_plus_icon = (By.XPATH, '//span[contains(@class, "search-plus")]/svg[@data-icon = "search"]')



    def search_host(self):
        return self.driver.find_element(*AdiosPlusResourcesPage.search_plus)

    def enter_host_name(self):
        return self.driver.find_element(*AdiosPlusResourcesPage.host_name)

    def confirm_button(self):
        return self.driver.find_element(*AdiosPlusResourcesPage.confirm)




