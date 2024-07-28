from selenium.webdriver.common.by import By


class PracticePage:

    def __init__(self, driver):
        self.driver = driver

    home = (By.XPATH, "//button[@class='btn btn-primary']")

    def homeitems(self):
        return self.driver.find_element(*PracticePage.home)

    login = (By.XPATH,"//a[normalize-space()='Login']")

    def login_button(self):
        return self.driver.find_element(*PracticePage.login)


    practice = (By.XPATH, "(//button[@class='btn btn-primary'])[2]")

    def practiceitems(self):
        return self.driver.find_element(*PracticePage.practice)
