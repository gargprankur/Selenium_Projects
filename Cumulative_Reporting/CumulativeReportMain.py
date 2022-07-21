import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import StaleElementReferenceException
from BaseClass import BaseClass
from CumulativeReportHome import CumulativeReportHome
import sys
import os

path_dir = os.getcwd()
sys.path.insert(0, "..")

import argparse

class CumulativeReportMain(BaseClass):
    def parse_cmdline_args(self):
        parser = argparse.ArgumentParser("help = Need to provide epack number")
        parser.add_argument('--epack', type = int, required= True)
        parsed_args = parser.parse_args()
        self._epack = parsed_args.epack

    def test_run_automation(self):

        self.driver.get("http://estsqlrptprd001.corp.emc.com/Reports_SSRS/report/CAT/Test%20Cycle%20Details%20("
                        "All%20Results)")
        time.sleep(20)
        #selected_qual = self.driver.find_element(By.XPATH, "\'//label[contains(text(),\' + str(self._epack) + ")]"

        home_page = CumulativeReportHome(self.driver, self._epack)
        self.driver.switch_to.frame(0)
        product = home_page.get_product()
        select = Select(product)
        select.select_by_visible_text("Enginuity")

        try:
            code = home_page.get_code()
            self.wait.until(expected_conditions.element_to_be_clickable((CumulativeReportHome.code)))
            select = Select(code)
            select.select_by_visible_text("5978.711.711")
        except StaleElementReferenceException as ex:
            code = home_page.get_code()
            select = Select(code)
            select.select_by_visible_text("5978.711.711")

        try:
            test_cycle = home_page.get_test_cycle()
            self.wait.until(expected_conditions.element_to_be_clickable((CumulativeReportHome.test_cycle)))
            test_cycle.click()
        except StaleElementReferenceException as ex:
            test_cycle = home_page.get_test_cycle()
            test_cycle.click()

        selected_test_cycle = home_page.select_test_cycle()
        selected_test_cycle.click()

        try:
            qual = home_page.select_qual_input()
            qual.click()

            self.wait.until(expected_conditions.element_to_be_clickable((CumulativeReportHome.qual)))
            qual = home_page.select_qual_input()
            qual.click()
        except StaleElementReferenceException as ex:
            qual = home_page.select_qual_input()
            qual.click()
        select_all = home_page.get_select_all()
        select_all.click()
        selected_qual = self.driver.find_element(By.XPATH, f'//label[contains(text(), \"{str(self._epack)}\")]')
        selected_qual.click()
        approved = home_page.get_approved()
        approved.click()

        approve_all = home_page.get_approve_all()
        approve_all.click()

        submit = home_page.get_submit()
        submit.click()

        self.wait.until(expected_conditions.element_to_be_clickable((CumulativeReportHome.drop_down)))
        self.wait.until(expected_conditions.element_to_be_clickable((CumulativeReportHome.element_to_be_present)))

        down_arrow = home_page.get_down_arrow()
        down_arrow.click()

        download = home_page.get_download()
        download.click()


obj = CumulativeReportMain()
obj.parse_cmdline_args()
obj.test_run_automation()







