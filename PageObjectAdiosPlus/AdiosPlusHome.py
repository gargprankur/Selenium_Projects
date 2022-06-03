import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

class AdiosPlusHome:
    def __init__(self, driver):
        self.driver = driver

    user_name = (By.ID, "username")
    user_password = (By.ID, "password")
    submit = (By.XPATH, '//button[@type = "submit"]')

    resources = (By.XPATH, '//a[@href = "/resources"]')

    despatch = (By.XPATH, '//a[@href = "/dispatch"]')

    def get_user_name(self):
        return self.driver.find_element(*AdiosPlusHome.user_name)

    def get_user_password(self):
        return self.driver.find_element(*AdiosPlusHome.user_password)

    def submit_button(self):
        return self.driver.find_element(*AdiosPlusHome.submit)

    def navigate_resources(self):
        return self.driver.find_element(*AdiosPlusHome.resources)

    def navigate_despatch(self):
        return self.driver.find_element(*AdiosPlusHome.despatch)

