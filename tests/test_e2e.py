import pytest
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.PracticePage import PracticePage


class TestOne(BaseClass):

    def test_e2e1(self):
        log = self.getLogger()
        pp = PracticePage(self.driver)
        pp.homeitems().click()
        log.info(("Just clicking on Home button"))
        self.driver.back()
        log.info(("Navigate Back"))
        print("Test 1 started from here")

    def test_e2e2(self):
        log = self.getLogger()
        pp = PracticePage(self.driver)
        log.info(("Just clicking on Practice button"))
        pp.practiceitems().click()
        print("Test 2 started from here")
