from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email = (By.XPATH, "//input[@id='email']")

    def set_email(self):
        return self.driver.find_element(*LoginPage.email)

    password = (By.XPATH, "//input[@id='password']")

    def set_password(self):
        return self.driver.find_element(*LoginPage.password)

    log_in = (By.XPATH, "//input[@name='commit']")

    def click_log_in(self):
        return self.driver.find_element(*LoginPage.log_in)
