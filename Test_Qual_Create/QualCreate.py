
import argparse
import datetime
import logging
import sys

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support import expected_conditions
sys.path.insert(0,'..')
from Cumulative_Reporting.BaseClass import BaseClass
from Test_Qual_Create.CATQualPage import CATQualPage
from Test_Qual_Create.CATTestCyclePage import CATTestCyclePage


class QualCreate(BaseClass):
    def __init__(self):
        """In Init function we will initialize loggers and create a log file name"""
        self._current_time = datetime.datetime.now()
        self._current_time = self._current_time.strftime("%Y%m%d")
        self._log_name = "selenium_" + self._current_time + ".log"
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.INFO)
        self._handler = logging.FileHandler(self._log_name)
        self._logger.addHandler(self._handler)
        self._formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
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

        variables = ['--starting_date', '--ending_date', '--days', '--epack']
        args = sys.argv[1:]
        check = all(items in args for items in variables)
        print(check)
        if not check or len(args) < 8:
            self.driver.close()
            self._parse_args = parser.parse_args()
            self._logger.error("User didn't provide correct parameters and values")
            sys.exit("Please Provide all parameter and their respective values")
        
        str_format = "%m/%d/%Y"
        self._parse_args = parser.parse_args()
        self._starting_date = self._parse_args.starting_date
        self._ending_date = self._parse_args.ending_date
        self._epack = self._parse_args.epack
        self._days = self._parse_args.days
        self._logger.info(f'''User has provided Starting _Date as {self._parse_args.starting_date}, 
                                      Ending _Date as {self._parse_args.ending_date},
                                      Epack number as {self._parse_args.epack} and 
                                      Days as {self._parse_args.days}''')
        try:
            if datetime.datetime.strptime(self._parse_args.starting_date, str_format) and \
                    datetime.datetime.strptime(self._parse_args.ending_date, str_format):
                self._logger.info("Format of date inputs is matched")
        except ValueError:
            self._logger.info("Please enter the date in %m/%d/%Y format. Exiting the test")
            sys.exit("Please Provide date in correct format")

    def qual_create(self):
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
            self._logger.info(f' Error ocurred while creating qual and message is {error_message}')
            sys.exit("The Qual name is already selected. Please try with different name")

        except NoSuchElementException as ex:
            self._logger.info("Qual name is unique. Going further with creating qual name")
            qual_description.send_keys(self._epack_text)
            self.wait.until(expected_conditions.presence_of_element_located((CATQualPage.save)))
            save = qual_page.save_button()
            save.click()
            self.driver.close()



    def add_qual_to_test_cycle(self):
        self.driver.get("http://catprd.corp.emc.com/Tests/Cycles/Edit.aspx?sName=cumulative&sIsDynamic=&sActive=2&id"
                        "=3871")
        self._epack_text_new = "\"" + self._epack_text + "\""
        test_cycle_page = CATTestCyclePage(self.driver, self._epack_text_new)

        qual_field = test_cycle_page.qual_field_textbox()
        qual_field.send_keys(self._epack_text)

        select_qual = test_cycle_page.select_qual()
        select_qual.click()

        start_date = test_cycle_page.enter_starting_date()
        start_date.send_keys(self._starting_date)

        end_date = test_cycle_page.enter_starting_date()
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

        save_button = test_cycle_page.add_button_click()
        save_button.click()

        more_actions = test_cycle_page.more_actions_click()
        more_actions.click()

        materialize = test_cycle_page.materialize_qual()
        materialize.click()

        self.driver.close()


qual_create = QualCreate()
qual_create.parse_commandline_args()
qual_create.qual_create()
qual_create.add_qual_to_test_cycle()
























