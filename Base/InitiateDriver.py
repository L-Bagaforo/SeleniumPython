from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from Library import ConfigReader
def startbrowser():
    global driver
    if((ConfigReader.readConfigData('Details', 'Browser')) == 'chrome'):
        path = "C:\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
        driver = Chrome()

    elif((ConfigReader.readConfigData('Details', 'Browser')) == 'firefox'):
        path = "C:\\geckodriver-v0.34.0-win64\\geckodriver.exe"
        driver = Firefox()

    else: #if firefox failed, Chrome Browser will run instead
        path = "C:\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
        driver = Firefox()

    driver.get(ConfigReader.readConfigData('Details', 'Application_URL'))
    driver.maximize_window()
    return driver

def closebrowser():
    driver.close