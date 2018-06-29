
import nose
import unittest
from unittest import TestLoader, TestSuite, TextTestRunner
import xmlrunner
from unittest import TestCase
from selenium import webdriver
from nose.plugins.attrib import attr
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.by import By
from locators import *

class nosetest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument("--ignore-certificate-errors")
        self.driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), options=chrome_options)
        #self.driver = webdriver.Chrome('/home/rizkimp/Documents/coba_nose/chromedriver')
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://arena.jog.ojodowo.com/")

    @attr(speed='fast')
    def test(self):
        self.driver.find_element(By.XPATH,locator.landing)
        self.driver.find_element(By.XPATH,locator.landing_getstar).click()
        self.driver.find_element(By.XPATH,locator.button_formlogin).click()
        self.driver.find_element(By.XPATH,locator.form_username).send_keys('rizkimahaputra')
        self.driver.find_element(By.XPATH,locator.form_password).send_keys('rizkimahaputra')
        self.driver.find_element(By.XPATH,locator.button_login).click()
        self.driver.find_element(By.XPATH,locator.slide)
        self.driver.find_element(By.XPATH,locator.imageavatar)
        self.driver.find_element(By.XPATH,locator.button_avatar).click()
        self.driver.find_element(By.XPATH,locator.button_logout).click()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    loader = TestLoader()
    test_suite = TestSuite((
        loader.loadTestsFromTestCase(nosetest),
        ))

    #run test sequentially using simple XMLTestRunner
    testRunner = xmlrunner.XMLTestRunner(verbosity=2, output=os.path.abspath("report")).run(test_suite)
