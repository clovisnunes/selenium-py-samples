from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")
#chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path=r"C:\\Users\\cborgesn\\Documents\\auto\\chromedriver.exe", options=chrome_options)
driver.get("https://www.google.com/")

def wait_get_by_xpath(xpath):
    try:
        element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    except TimeoutException:
        print(xpath + " is not loaded")
    
    return element


wait_get_by_xpath("//img[@alt='Google']")

field_search = driver.find_element_by_xpath("//input[@name='q']")

if(field_search.is_enabled() and field_search.is_displayed()):
    field_search.send_keys("python")

option_list = wait_get_by_xpath("(//ul/li//span[text()='python'])[1]")
option_list.click()

python_result = wait_get_by_xpath("//h3[text()='Welcome to Python.org']")

driver.quit()