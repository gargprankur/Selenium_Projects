
"""
Created By: Prankur Garg
Email Id: prankur.garg1@emc.com, p.garg@dell.com
Date: 18th July 2022
"""

# Base Imports
import argparse
import logging
import sys
import datetime

sys.path.insert(0 , '..')

# Imports Selenium Packages
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support import expected_conditions

# Page Object classes of CAT functionality Imports
from Cumulative_Reporting.BaseClass import BaseClass
from Test_Qual_Create.CATQualPage import CATQualPage
from Test_Qual_Create.CATTestCyclePage import CATTestCyclePage

"""
This class is for creating a qual based on the epack number given by user.
Once qual is created, it adds it to the Cumulative epack test cycle and then materialize the cycle
"""

class QualCreate(BaseClass):
    def __init__(self):
        """In Init function we will initialize loggers and create a log file name, will get today's date and date
        after 7 days """
        self._current_time = datetime.datetime.now()
        self._current_time = self._current_time.strftime("%Y%m%d")
        self._log_name = "selenium_" + self._current_time + ".log"
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.INFO)
        self._handler = logging.FileHandler(self._log_name)
        self._logger.addHandler(self._handler)
        self._formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
        self._handler.setFormatter(self._formatter)
        self._starting_date_1 = datetime.datetime.now()
        self._starting_date = self._starting_date_1.strftime("%m/%d/%Y")
        time_delta = datetime.timedelta(days=7)
        self._ending_date = self._starting_date_1 + time_delta
        self._ending_date = self._ending_date.strftime("%m/%d/%Y")
        self._days = 7

    def parse_commandline_args(self):
        """ In this function, we will parse command line arguments provided by user and check if there are in correct
        format """
        parser = argparse.ArgumentParser(description="""This Program will need 1 parameter to be passed by user
                                                     1. Epack Number(Integer) """)

        parser.add_argument('--epack', type=int, help="EPack Number(Integer)", required=True)
        self._parse_args = parser.parse_args()
        self._epack = self._parse_args.epack

    def qual_create(self):
        """
        This is the function which creates the qual. Checks if qual name already exists.
        """
        self.driver.get('http://catprd.corp.emc.com/Tests/Quals/View.aspx?name=cummulative&sActive=2&sPublicPrivate'
                        '=&id=13791')

        self._epack_text = "Cumulative_Epack" + "_" + str(self._epack)
        self._logger.info(f'We are going to create Qual with name {self._epack_text}')
        qual_page = CATQualPage(self.driver)

        more_actions = qual_page.more_actions_dropdown()
        more_actions.click()

        clone = qual_page.qual_clone()
        clone.click()

        qual_name = qual_page.qual_name_textbox()
        qual_name.clear()

        qual_name.send_keys(self._epack_text)

        qual_description = qual_page.qual_description_textbox()
        qual_description.clear()

        try:
            qual_exists = qual_page.qual_exists_error()
            error_message = qual_exists.text
            self._logger.error(f' Error occurred while creating qual and message is {error_message}')
            self.driver.close()
            sys.exit("The Qual name is already selected. Please try with different name")

        except NoSuchElementException as ex:
            self._logger.info("Qual name is unique. Going further with creating qual name")
            qual_description.send_keys(self._epack_text)
            self.wait.until(expected_conditions.presence_of_element_located((CATQualPage.save)))
            save = qual_page.save_button()
            save.click()
            self.driver.close()

    def add_qual_to_test_cycle(self):
        """
        This is the function to add qual to test cycle and then materialize it.
        :return:
        """
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://catprd.corp.emc.com/Tests/Cycles/Edit.aspx?sName=cumulative&sIsDynamic=&sActive=2&id"
                        "=3871")

        self._epack_text_new = "\"" + self._epack_text + "\""

        test_cycle_page = CATTestCyclePage(self.driver, self._epack_text_new)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        qual_field = test_cycle_page.qual_field_textbox()

        qual_field.send_keys(self._epack_text)

        select_qual = test_cycle_page.select_qual()

        select_qual.click()

        start_date = test_cycle_page.enter_starting_date()

        start_date.send_keys(self._starting_date)

        end_date = test_cycle_page.enter_ending_date()

        end_date.send_keys(self._ending_date)

        days = test_cycle_page.enter_days()

        days.send_keys(self._days)

        add_button = test_cycle_page.add_button_click()

        add_button.click()

        try:
            alert = self.driver.switch_to.alert
            self._logger.info(f' There is an alert popped up and the message of alert is {alert.text}')
            alert.accept()
            sys.exit("Qual seems to already added to cycle.")

        except NoAlertPresentException:
            self._logger.info("Qual was not added to test cycle previously. Proceeding further with adding it the "
                              "test cycle ")

        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

        save_button = test_cycle_page.save_button_click()

        save_button.click()

        more_actions = test_cycle_page.more_actions_click()

        more_actions.click()

        materialize = test_cycle_page.materialize_qual()

        materialize.click()

        self.driver.close()


if __name__ == '__main__':
    qual_create = QualCreate()
    qual_create.parse_commandline_args()
    qual_create.qual_create()
    qual_create.add_qual_to_test_cycle()

























