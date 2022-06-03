""" These are base Python Packages which we imported."""
import argparse
import sys
import datetime
import time
import logging

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""Following are Python Selenium Packages"""
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class QualCreate:
    def __init__(self):
        """In Init function we will initialize loggers and create a log file name"""
        self._current_time = datetime.datetime.now()
        self._current_time = self._current_time.strftime("%Y%m%d")
        self._log_name = "selenium_" + self._current_time + ".log"
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.INFO)
        self._handler = logging.FileHandler(self._log_name)
        self._logger.addHandler(self._handler)
        self._formatter = logging.Formatter('%(asctime)s-%(message)s')
        self._handler.setFormatter(self._formatter)


    def parse_commandline_args(self):
        """ In this function, we will parse command line arguments provided by user and check if there are in correct
        format """
        parser = argparse.ArgumentParser(description="""This Program will need 4 parameters to be passed by user
                                                     1. Epack Number \n 2. Starting date(mm/dd/yyyy format) \n 3. End
                                                     Date \n 4. Days""")
        parser.add_argument('--epack', type=int, help="EPack Number(Integer)", required=True)
        parser.add_argument('--starting_date', type=str, help="Starting Date(Date)", required=True)
        parser.add_argument('--ending_date', type=str, help="End Date(Date)", required=True)
        parser.add_argument('--days', type=int, help="Days(Integer)", required=True)
        parse_args = parser.parse_args()
        self._logger.info(f'''User has provided Starting _Date as {parse_args.starting_date}, 
                              Ending _Date as {parse_args.ending_date},
                              Epack number as {parse_args.epack} and 
                              Days as {parse_args.days}''')
        str_format = "%m/%d/%Y"
        try:
            if datetime.datetime.strptime(parse_args.starting_date, str_format) and \
                    datetime.datetime.strptime(parse_args.ending_date, str_format):
                self._logger.info("Format of date inputs is matched")
        except ValueError:
            self._logger.info("Please enter the date in %m/%d/%Y format. Exiting the test")
            sys.exit("Please Provide date in correct format")
        else:
            return parse_args.epack, parse_args.starting_date, parse_args.ending_date, parse_args.days


    def qual_clone(self):
        """ We will create qual here. If qual already exists, program will fail. Else it will create a qual name
        based on the inputs user provided """
        epack, starting_date, ending_date, days = self.parse_commandline_args()
        services = Service("C:\\Users\\gargp6\\OneDrive - Dell Technologies\Documents\\chromedriver.exe")
        driver = webdriver.Chrome(service=services)
        epack_text = "Cumulative_Epack" + "_" + str(epack)
        """ This is the qual, which we will be cloning"""
        driver.get('http://catprd.corp.emc.com/Tests/Quals/View.aspx?name=cummulative&sActive=2&sPublicPrivate=&id=13791')
        driver.maximize_window()
        driver.implicitly_wait(10)

        self._logger.info(f'We are going to create Qual with name {epack_text}')
        driver.find_element(by=By.XPATH, value='//a[@class = "more-actions-a"]').click()
        driver.find_element(by=By.XPATH, value='//div[@class = "more-actions-dropdown opened"]/a[text()="Clone"]').click()
        driver.find_element(by=By.XPATH, value='//input[@value = "Clone of: Cummulative Epack 9537"]').clear()
        driver.find_element(by=By.XPATH, value='//input[@value = "Clone of: Cummulative Epack 9537"]').send_keys(epack_text)
        driver.find_element(by=By.XPATH, value='//textarea[contains(text(),"9537 Cummulative Epack Testin")]').clear()
        try:
            error_message = driver.find_element(by=By.XPATH, value='//label[@class = "error"]').text
            self._logger.info(f' Error ocurred while creating qual and message is {error_message}')
            sys.exit("The Qual name is already selected. Please try with different name")


        except NoSuchElementException as ex:
            self._logger.info("Qual name is unique. Going further with creating qual name")
            driver.find_element(by=By.XPATH, value='//textarea[contains(text(),"9537 Cummulative Epack Testin")]').send_keys(epack_text)
            wait = WebDriverWait(driver, 5)
            wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//a[contains(text(),"Save")]')))
            driver.find_element(by=By.XPATH, value='//a[contains(text(),"Save")]').click()
            driver.close()
            return epack_text, starting_date, ending_date, days


    def add_qual_to_test_cycle(self):
        epack_text, starting_date, ending_date, days = self.qual_clone()
        services = Service("C:\\Users\\gargp6\\OneDrive - Dell Technologies\Documents\\chromedriver.exe")
        driver = webdriver.Chrome(service=services)
        driver.get("http://catprd.corp.emc.com/Tests/Cycles/Edit.aspx?sName=cumulative&sIsDynamic=&sActive=2&id=3871")
        driver.maximize_window()
        driver.implicitly_wait(10)

        epack_text_new = "\"" + epack_text + "\""
        self._logger.info(epack_text_new)
        self._logger.info("Now when Qual is created, we will now add it to Test Cycle")
        driver.find_element(by=By.XPATH, value="//td[@class = 'rcbInputCell rcbInputCellLeft']/input[@id = 'ctl00_m_genQual_cb_Input']").send_keys(epack_text)
        value_xpath = f"//div[@class = 'rcbScroll rcbWidth']/ul[@class='rcbList']/li[text() = {epack_text_new}]"

        driver.find_element(by=By.XPATH, value=value_xpath).click()

        driver.find_element(by=By.XPATH, value='//input[@id = "ctl00_m_genQualOccur"]').send_keys(days)

        driver.find_element(by=By.XPATH, value='//input[@id = "ctl00_m_genQualStart_dateInput"]').send_keys(starting_date)
        driver.find_element(by=By.XPATH, value='//input[@id = "ctl00_m_genQualEnd_dateInput"]').send_keys(ending_date)
        driver.find_element(by=By.XPATH, value='//input[@value = "Add"]').click()
        try:
            alert = driver.switch_to.alert
            self._logger.info(f' There is an alert popped up and the message of alert is {alert.text}')
            sys.exit("Qual seems to already added to cycle.")
        # alert.accept()
        except NoAlertPresentException:
            self._logger.info("Qual was not added to test cycle previously. Proceeding further with adding it the test cycle ")

        driver.find_element(by=By.XPATH, value='//span[@id = "ctl00_ButtonPanel"]/a[text() = "Save"]').click()
        driver.find_element(by=By.XPATH, value='//a[@class = "more-actions-a"]').click()
        driver.find_element(by=By.XPATH, value='//a[text() = "Materialize"]').click()


qual = QualCreate()
qual.add_qual_to_test_cycle()
