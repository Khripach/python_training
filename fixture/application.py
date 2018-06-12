from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.navigation import NavigationHelper

class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = WebDriver(capabilities={"marionette": False}, firefox_binary="C:/Program Files/MozillaFirefox2/firefox.exe")
            #self.wd = webdriver.FireFox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome(executable_path='C:\Devel\chromedriver.exe')
        elif browser == "ie":
            self.wd = webdriver.Ie(executable_path='C:\Devel\IEDriverServer.exe')
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.navigation = NavigationHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
