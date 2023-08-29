import os

from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper

DRIVER_FOLDER = os.path.expanduser("~\Downloads\drivers")

options = webdriver.ChromeOptions()

class Application:

    def __init__(self, browser, base_url):

        # self.wd = webdriver.Chrome(executable_path=f"{DRIVER_FOLDER}\chromedriver\chromedriver.exe",
        #                  options=options
        #                  )

        if browser == "chrome":
            self.wd = webdriver.Chrome(executable_path=f"{DRIVER_FOLDER}\chromedriver\chromedriver.exe")
        elif browser == "opera":
            self.wd = webdriver.Opera(executable_path=f"{DRIVER_FOLDER}\operadriver\operadriver.exe")
        else:
            raise ValueError(f"Unrecognized browser {browser}")

        # self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not wd.current_url.endswith("addressbook/"):
            wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()