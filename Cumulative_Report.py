import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

"""Following are Python Selenium Packages"""
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

services = Service("C:\\Users\\gargp6\\OneDrive - Dell Technologies\\Documents\\chromedriver")
driver = webdriver.Chrome(service=services)
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("http://estsqlrptprd001.corp.emc.com/Reports_SSRS/report/CAT/Test%20Cycle%20Details%20(All%20Results)")
element = driver.find_element(by = By.TAG_NAME, value = "iframe")
print(element)
driver.switch_to.frame(0)

select = Select(driver.find_element(by = By.XPATH, value = '//div[@data-parametername = "Product"]/select'))
select.select_by_visible_text("Enginuity")

wait = WebDriverWait(driver, 20)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//div[@data-parametername = "ProductVersionID"]/select')))
select = Select(driver.find_element(by = By.XPATH, value = '//div[@data-parametername = "ProductVersionID"]/select'))
select.select_by_visible_text("5978.711.711")

wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//div[@data-parametername = "TestCycleID"]/div/table/tbody/tr/td/input')))

driver.find_element(by = By.XPATH, value = '//div[@data-parametername = "TestCycleID"]/div/table/tbody/tr/td/input').click()
driver.find_element(by = By.XPATH, value = '//label[contains(text(), "Cumulative")]').click()

driver.find_element(by = By.XPATH, value = '//div[@data-parametername = "QualIDs"]/div/table/tbody/tr/td/input').click()
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//div[@data-parametername = "QualIDs"]/div/table/tbody/tr/td/input')))
driver.find_element(by = By.XPATH, value = '//div[@data-parametername = "QualIDs"]/div/table/tbody/tr/td/input').click()
driver.find_element(by = By.XPATH, value = '//label[contains(text(), "(Select All)")]').click()
driver.find_element(by = By.XPATH, value = '//label[contains(text(), "9605")]').click()

driver.find_element(by = By.XPATH, value = '//div[@data-parametername = "Approved"]/div/table/tbody/tr/td/input').click()
driver.find_element(by = By.XPATH, value = '//label[contains(text(), "(Select All)")]').click()

driver.find_element(by = By.XPATH, value = '//div[@data-parametername = "groupids"]/div/table/tbody/tr/td/input').click()
#driver.find_element(by = By.XPATH, value = '//label[contains(text(), "(Select All)")]').click()

driver.find_element(by = By.XPATH, value = '//input[@type = "submit"]').click()
#driver.switch_to.default_content()
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//a[@title = "Export drop down menu"]')))
wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//div[contains(text() , "CAT Report")]')))
time.sleep(20)
element = driver.find_element(by = By.XPATH, value = '//a[@title =  "Export drop down menu"]/span[contains(@class, "glyphui-save")]')
#driver.execute_script("arguments[0].click();", element)
assert element.is_enabled()
element.click()
driver.find_element(by = By.LINK_TEXT, value ="Excel").click()










