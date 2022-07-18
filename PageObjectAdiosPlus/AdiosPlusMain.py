import sys
import os

path_dir = os.getcwd()
sys.path.insert(0, "..")
#print(sys.path)


"""Selenium Packages"""
import argparse

from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, \
    ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions
""" 
Page Object classes 
Created By: Prankur Garg
Date: 25th May 2022
"""
from Cumulative_Reporting.BaseClass import BaseClass
from PageObjectAdiosPlus.AdiosPlusDespatch import AdiosPlusDespatch
from PageObjectAdiosPlus.AdiosPlusHome import AdiosPlusHome
from PageObjectAdiosPlus.AdiosPlusResourcesPage import AdiosPlusResourcesPage


"""Python Package"""
import time
import datetime
import logging


class AdiosPlusMain(BaseClass):
    def __init__(self):
        self._current_time = datetime.datetime.now()
        self._current_time = self._current_time.strftime("%Y%m%d")
        self._log_name = "Adios_run_" + self._current_time + ".log"
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.INFO)
        self._handler = logging.FileHandler(self._log_name)
        self._logger.addHandler(self._handler)
        self._formatter = logging.Formatter('%(asctime)s-%(message)s')
        self._handler.setFormatter(self._formatter)

    def parse_commandline_args(self):
        parser = argparse.ArgumentParser(description="Need to enter test cycle, qual name and team name")
        parser.add_argument('--test_cycle', type=str, help="Test Cycle", required=True)
        parser.add_argument('--qual', type=str, help="Qual Name", required=True)
        parser.add_argument('--team', type = str, help = "Enter Team Name core/data-services", required= True)
        if len(sys.argv[1:]) < 6 or '--test_cycle' not in sys.argv[1:] or '--qual' not in sys.argv[1:] or '--team' not in sys.argv[1:]:
            self.driver.close()
            self._logger.error("Either parameters were not provided or wrongly given")
            parse_args = parser.parse_args()
            sys.exit("Required Parameters were not provided")
        teams = ["core", "data-services"]
        parse_args = parser.parse_args()
        self._test_cycle = parse_args.test_cycle
        self._qual = parse_args.qual
        self._team = parse_args.team
        if self._team not in teams:
            self._logger.error("Team name entered is wrong. It should be either core or data-sustaining")
            sys.exit("Team name entered is wrong. It should be either core or data-sustaining")
        self._logger.info(f"User has entered Test Cycle name as {self._test_cycle} and qual Name as {self._qual}")


    def adios_plus_login(self):
        self.driver.get("http://adiosplus.cec.lab.emc.com/dashboard")
        self._home_adios_plus = AdiosPlusHome(self.driver)
        user_name = self._home_adios_plus.get_user_name()
        user_name.send_keys("gargp6")
        user_password = self._home_adios_plus.get_user_password()
        user_password.send_keys("June@11jun")
        submit_button = self._home_adios_plus.submit_button()
        submit_button.click()
        self._logger.info("User has entered username and password and logging into Adios Page")

    def navigate_resources_page(self):
        element = self._home_adios_plus.navigate_resources()
        self.driver.execute_script("arguments[0].click();", element)
        self._logger.info("We are resource tab of Adios Page")
        resource_page = AdiosPlusResourcesPage(self.driver)
        time.sleep(30)
        print(AdiosPlusResourcesPage.search_plus)

        self.wait.until(expected_conditions.presence_of_element_located((AdiosPlusResourcesPage.search_plus)))

        self.wait.until(expected_conditions.element_to_be_clickable((AdiosPlusResourcesPage.search_plus)))

        data_services_suites = {
                  "Cumulative_Testing_P2": "10.60.153.253",
                  "Cumulative_Testing_P3": "10.60.153.195",
                  "Defrag_Shrink_SP_Cumulative": "10.60.154.6",
                  "LREP_SP_Cumulative" : "10.60.154.51",
                  "RDF_SP_Cumulative" : "10.60.155.123",
                  "Cumulative_Testing_P1" : "10.60.153.202",
                  "Long_Running_Tests_SP_Cumulative": "10.60.153.132",
                  "Cumulative_Testing_P4": "10.60.153.195"
                  }

        core_suites = {
                    "ACS DataMobility" : "10.60.153.55",
                    "ACT Platform" : "10.60.153.55",
                    "ACT Config" : "10.60.153.55",
                    "ACT Backend" : "10.60.153.55",
                    "ACS_Enginuity Services" : "10.60.153.55"
                    }
        self._suites = {}
        if self._team == "core":
            self._suites = core_suites
        elif self._team == "data-services":
            self._suites = data_services_suites

        self._dict_value = [value for value in self._suites.values()]
        self._dict_keys = [value for value in self._suites.keys()]
        print(self._dict_value)
        print(self._dict_keys)
        for host in self._dict_value:
            try:
                search = resource_page.search_host()
                self.driver.execute_script("arguments[0].click()", search)
                #search.click()
            except ElementClickInterceptedException:
                search = resource_page.search_host()
                search.click()
            time.sleep(2)
            self._logger.info(f"We are adding {host} in resource tab of Adios Page")
            self.wait.until(expected_conditions.presence_of_element_located((AdiosPlusResourcesPage.host_name)))
            try:
                host_name = resource_page.enter_host_name()
                host_name.send_keys(host)
            except NoSuchElementException as ex:
                self.driver.get_screenshot_as_file("Host_error.png")
                host_name = resource_page.enter_host_name()
                host_name.send_keys(host)

            confirm = resource_page.confirm_button()
            confirm.click()
            time.sleep(2)
            self._logger.info(f"Successfully added {host} in resource tab of Adios Page")

    def navigate_dispatch(self):
        element = self._home_adios_plus.navigate_despatch()
        self.driver.execute_script("arguments[0].click();", element)
        self._logger.info(f" Now when we have resources added. Will add suites to Dispatch tab")

        self.wait.until(expected_conditions.presence_of_element_located((AdiosPlusDespatch.search)))
        self.wait.until(expected_conditions.element_to_be_clickable((AdiosPlusDespatch.search)))

        despatch_page = AdiosPlusDespatch(self.driver)
        search_button = despatch_page.search_button()
        search_button.click()

        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])
        self._logger.info("Navigated to dispatch page of Adios Page")
        for suite in self._dict_keys:
            self.wait.until(expected_conditions.element_to_be_clickable((AdiosPlusDespatch.clear_filter)))
            clear_button = despatch_page.clear_filter_button()
            clear_button.click()

            suite_name = despatch_page.enter_suite_name()
            suite_name.send_keys(suite)

            search_suite = despatch_page.search_suite_button()
            search_suite.click()

            self._logger.info(f"Adding suite {suite} to adios Page")

            self.wait.until(expected_conditions.presence_of_element_located((AdiosPlusDespatch.select_suite)))
            time.sleep(4)

            select_suite = despatch_page.select_suite_checkbox()
            select_suite[1].click()

            self.wait.until(expected_conditions.element_to_be_clickable((AdiosPlusDespatch.right_arrow)))

            right_arrow = despatch_page.select_right_arrow()
            right_arrow.click()

        select_suites = despatch_page.select_all_suites()
        select_suites[2].click()

        add_suites = despatch_page.add_suites_button()
        add_suites.click()

        self._logger.info(f"Successfully added all suites to View")

        for key, value in self._suites.items():
            suite_search = despatch_page.search_suite_to_run()
            self._logger.info(f'Selected suite {key} to run on host {value}')
            suite_search.send_keys(key)

            try:
                add_button = despatch_page.suite_add_button()
            except ElementClickInterceptedException as ex:
                add_button = despatch_page.suite_add_button()
            add_button.click()

            try:
                suite_run = despatch_page.select_suite_to_despatch()
                suite_run.click()
            except ElementClickInterceptedException as ex:
                suite_run = despatch_page.select_suite_to_despatch()
                suite_run.click()
            self.wait.until(expected_conditions.presence_of_element_located((AdiosPlusDespatch.test_cycle)))

            test_cycle = despatch_page.test_cycle_input()

            test_cycle.send_keys(self._test_cycle)

            test_cycle.send_keys(Keys.ENTER)
            time.sleep(1)
            qual = despatch_page.qual_input()

            qual.send_keys(self._qual)

            qual.send_keys(Keys.ENTER)
            time.sleep(2)

            host = despatch_page.host_input()
            host.send_keys(value)
            host.send_keys(Keys.ENTER)
            self.wait.until(expected_conditions.presence_of_element_located((AdiosPlusDespatch.host_select_message)))

            message = despatch_page.get_host_message()
            message = message.text
            self._logger.info(f' Currently status of host is {message}')
            if "Currently validating" in message:
                time.sleep(5)
                message = despatch_page.get_host_message()
                message = message.text
                if "ready to run" in message:
                    self._logger.info(f'Despatcher state of Host {value} is ready')
                    time.sleep(8)
                    box = despatch_page.select_symm()
                    box.send_keys("OLKCK")
                    box.send_keys(Keys.ENTER)
                    time.sleep(2)

                    self.wait.until(expected_conditions.element_to_be_clickable((AdiosPlusDespatch.run)))
                    run_button = despatch_page.run_button()
                    run_button.click()

                    handles = self.driver.window_handles
                    self.driver.switch_to.window(handles[0])
                    time.sleep(5)
                    ok_button = despatch_page.ok_button_function()
                    ok_button.click()
                    time.sleep(20)
                    self.wait.until(expected_conditions.presence_of_element_located((AdiosPlusDespatch.after_run_message)))

                    self.driver.get_screenshot_as_file(f'{key}.png')
                    time.sleep(30)

                    search_field = despatch_page.search_suite_text_field()

                    clear_suite = despatch_page.clear_search_suite()
                    clear_suite.click()

                    despatch_page.deselect_suite_link().click()
                    time.sleep(4)

                else:
                    self._logger.info(f'Despatcher state of Host {value} is not in ready state')
                    print("host is not in ready state")
                    clear_suite = despatch_page.clear_search_suite()
                    clear_suite.click()
                    print("Clearing suite")
                    time.sleep(5)

                    deselect_suite = despatch_page.deselect_suite_link()
                    deselect_suite.click()
                    time.sleep(4)
                    continue
        self.driver.close()


obj = AdiosPlusMain()
obj.parse_commandline_args()
obj.adios_plus_login()
obj.navigate_resources_page()
obj.navigate_dispatch()





