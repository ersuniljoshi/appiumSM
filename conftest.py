# Using appium webdriver to automate
from appium import webdriver
import pytest
import os


def pytest_addoption(parser):
    parser.addoption("--device", action="store", default="Android Emulator",
                     help="my option: Android Emulator or Android device")
    parser.addoption("--codexFile", action="store", default="android", help="my option: android")
    parser.addoption("--platformName", action="store", default="Android", help="name: Android")
    parser.addoption("--platformVersion", action="store", default="5.1.1", help="version: 5.1.1")


@pytest.fixture
def device(request):
    return request.config.getoption("--device").lower()


@pytest.fixture
def codexFile(request):
    return request.config.getoption("--codexFile").lower()

@pytest.fixture
def platformName(request):
    return request.config.getoption("--platformName").lower()

@pytest.fixture
def platformVersion(request):
    return request.config.getoption("--platformVersion").lower()




@pytest.fixture(scope="function")
def setUp(device, platformName, platformVersion):
    desired_caps = {}
    desired_caps['platformName'] = platformName
    desired_caps['platformVersion'] = platformVersion
    desired_caps['deviceName'] = device
    desired_caps['appPackage'] = 'com.surveymonkey'
    desired_caps['appActivity'] = 'com.surveymonkey.login.activities.LandingActivity'
    driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps)
    #driver = webdriver.Remote('http://172.16.20.10:4723/wd/hub', desired_caps)
    return driver


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
                if os.path.exists("myfile1"):
                        file = open('myfile1', 'r')
                        screenshot = file.read()
                        os.remove("myfile1")
                        extra.append(pytest_html.extras.image(screenshot, 'Screenshot'))
        report.extra = extra
