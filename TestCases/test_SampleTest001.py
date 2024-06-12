from Base import InitiateDriver
from Pages import RegistrationPage
from DataGenerate import DataGen
import pytest
import openpyxl
import time

@pytest.mark.parametrize('data', DataGen.dataGenerator())

def test_registration_invaliddata(data):
   driver = InitiateDriver.startbrowser()
   register = RegistrationPage.RegistrationClass(driver)
   register.enter_username(data[0])
   register.enter_password(data[1])
   driver
