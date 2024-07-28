import pytest
from testData.LoginPageData import LoginPageData
from selenium import webdriver
from pageObjects.PracticePage import PracticePage
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestLogin(BaseClass):

    def test_e2e_login(self, get_data):
        pp = PracticePage(self.driver)
        lp = LoginPage(self.driver)
        log = self.getLogger()
        print("Test 1 started from here")
        pp.homeitems().click()
        log.info(" Just click on Home button")
        pp.login_button().click()
        log.info(" Just click on Login button")
        lp.set_email().clear()
        lp.set_email().send_keys(get_data["email"])
        log.info(" Just enter email as " + get_data["email"])
        lp.set_password().clear()
        lp.set_password().send_keys(get_data["password"])
        log.info(" Just enter password as " + get_data["password"])
        lp.click_log_in()
        assert 1 == "Incorrect"
        print("Test 1 ended here")

    @pytest.fixture(params=LoginPageData.test_LoginPage_Data)
    def get_data(self, request):
        return request.param

    @pytest.fixture(params=LoginPageData.get_data_excel("TestCase1"))
    def get_data_excel(self, request):
        return request.param
