import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import StaleElementReferenceException
from Cumulative_Reporting.BaseClass import BaseClass
from Cumulative_Reporting.CumulativeReportHome import CumulativeReportHome


class CumulativeReportMain(BaseClass):

    def test_run_automation(self):
        self.driver.get("http://estsqlrptprd001.corp.emc.com/Reports_SSRS/report/CAT/Test%20Cycle%20Details%20("
                        "All%20Results)")
        time.sleep(20)
        home_page = CumulativeReportHome(self.driver)
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
            self.driver.get_screenshot_as_file("first_qual_click.png")
            self.wait.until(expected_conditions.element_to_be_clickable((CumulativeReportHome.qual)))
            qual = home_page.select_qual_input()
            qual.click()
        except StaleElementReferenceException as ex:
            qual = home_page.select_qual_input()
            qual.click()
            self.driver.get_screenshot_as_file("second_qual_click.png")

        select_all = home_page.get_select_all()
        select_all.click()

        qual = home_page.select_qual()
        qual.click()

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
obj.test_run_automation()







