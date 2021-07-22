from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

import unittest
import xmlrunner
import HtmlTestRunner
import datetime
import os

def wait_get_by_xpath(self, xpath):
        try:
            element = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
        except TimeoutException:
            print(xpath + " is not loaded")
    
        return element

def screen_counter(self):
    self.n += 1
    return self.n

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        # setting chrome
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")

        # setting selenium web driver
        self.driver = webdriver.Chrome(executable_path=r"C:\\Users\\cborgesn\\Documents\\auto\\chromedriver.exe", options=chrome_options)
        self.driver.get("https://www.google.com/")
        self.actions = ActionChains(self.driver)

        # creating folder to screenshots
        folder_ss = str(datetime.datetime.now().timestamp())
        if not os.path.exists('test_evidences'):
            os.mkdir('test_evidences')
        os.mkdir('test_evidences\\' + folder_ss)
        self.full_folder_ss = os.getcwd() + '\\test_evidences\\' + folder_ss + '\\'
        self.n = 0

    def test_result_list(self):
        logo = wait_get_by_xpath(self, "//img[@alt='Google']")
        self.assertTrue(logo.is_displayed())
        self.driver.save_screenshot(self.full_folder_ss + 'screenshot' + str(screen_counter(self)) + '.png')

        field_search = self.driver.find_element_by_xpath("//input[@name='q']")
        if(field_search.is_enabled() and field_search.is_displayed()):
            field_search.send_keys("python")

        option_list = wait_get_by_xpath(self, "(//ul/li//span[text()='python'])[1]")
        self.assertTrue(option_list.is_displayed() and option_list.is_enabled())
        self.driver.save_screenshot(self.full_folder_ss + 'screenshot' + str(screen_counter(self)) + '.png')
        option_list.click()

        python_result = wait_get_by_xpath(self, "//h3[text()='Welcome to Python.org']/../../..")
        self.actions.move_to_element(python_result).perform()
        self.assertTrue(python_result.is_displayed() and python_result.is_enabled())
        self.driver.save_screenshot(self.full_folder_ss + 'screenshot' + str(screen_counter(self)) + '.png')
    
    @unittest.skip("Skipping sample test")
    def test_another_test(self):
        # another test in the module
        pass

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    # with HtmlTestRunner
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())

    """
    WITH XMLRUNNER
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)
    """