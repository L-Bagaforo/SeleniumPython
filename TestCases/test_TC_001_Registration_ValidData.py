from Base import InitiateDriver
from Pages import RegistrationPage
import time

def test_ValidateRegistration():
    driver = InitiateDriver.startbrowser()
    register = RegistrationPage.RegistrationClass(driver)
    register.enter_username('hello')
    register.enter_email("luel@abc.com")
    register.enter_password("123456789")
    time.sleep(5)

