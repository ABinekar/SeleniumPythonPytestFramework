import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loogerName = inspect.stack()[1][3]
        logger = logging.getLogger(loogerName)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter((formatter))
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def verify_link_presence(self, text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, text)))
