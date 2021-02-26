
import traceback

import chromedriver_autoinstaller
from selenium import webdriver


class WebDriverFactory():

    def __init__(self, browser):

        self.browser = browser


    def getWebDriverInstance(self):

        baseURL = "https://github.com/"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            chromedriver_autoinstaller.install()
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver