# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 13:01:01 2020

@author: dmitr
"""

import os
os.getcwd()
os.chdir('C:/Users/dmitr/OneDrive/Documents/Python_scripts')
from selenium import webdriver
import unittest
import time



from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        self.driver.get("https://www.xeljanz.com/")
        self.driver.find_element_by_id("top-menu-indication").click()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()