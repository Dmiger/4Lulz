# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 13:48:24 2020

@author: dmitr
"""

#QA attempt number 1
import os
os.getcwd()
os.chdir('C:/Users/dmitr/OneDrive/Documents/Python_scripts')
from selenium import webdriver
import unittest
import time

class Xeljanz(unittest.TestCase):
    
    @classmethod
    
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        #cls.driver.implicitly_wait(10)
        #cls.driver.maximize_window()
        
    def test_click_top_indication(self):
        self.driver.get("https://www.xeljanz.com/")
        self.driver.find_element_by_id("top-menu-indication").click()
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/ul/li[3]/a").click()
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/ul/li[5]/a").click()
        
#    def test_click_header_isi(self):
#       self.driver.get("https://www.xeljanz.com/")
#        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/ul/li[3]/a").click()

        
#    def test_click_header_medication_guide(self):
#        self.driver.get("https://www.xeljanz.com/")
#        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/ul/li[5]/a").click()
    

    
    @classmethod
    
    

    def tearDownClass(cls):
        cls.driver.close()
        #cls.driver.quit()
        print("\n -> Test completed <-")
        

if __name__ == "__main__":
    unittest.main()
    

#//*[@id="mCSB_10_container"]/p[23]/span[1]/a
#driver.set_page_load_timeout(10)
#driver.get("https://www.xeljanz.com/")
#driver.find_element_by_id("top-menu-indication").send_keys("idi nahui") --
#That one fills in text
#driver.find_element_by_id("top-menu-indication").click()
#time.sleep(5)
#driver.quit()
