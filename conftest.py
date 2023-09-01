import json
import pytest
import os.path

from fixture.application import Application

fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open (config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])
    fixture.session.ensure_login(username=target["username"], password=target["password"])
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
    # parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")



"""@pytest.fixture
def app():
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(username="admin", password="secret")
    yield fixture
    fixture.session.logout()
    fixture.destroy()"""