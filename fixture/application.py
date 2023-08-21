import os

from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper

DRIVER_FOLDER = os.path.expanduser("~\Downloads\drivers")

options = webdriver.ChromeOptions()

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome(executable_path=f"{DRIVER_FOLDER}\chromedriver\chromedriver.exe",
                         options=options
                         )
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()