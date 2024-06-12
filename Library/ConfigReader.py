import configparser

def readConfigData(section, key):
    config = configparser.ConfigParser()
    config.read('C:\\Users\\luelb\\PycharmProjects\\PythonBasicProgramming\\EndtoEndAutomation\\ConfigurationFiles\\Config.cfg')
    return config.get(section,key)

def fetchElementLocators (section, key):
    config = configparser.ConfigParser()
    config.read('C:\\Users\\luelb\\PycharmProjects\\PythonBasicProgramming\\EndtoEndAutomation\\ConfigurationFiles\\Elements.cfg')
    return config.get(section,key)