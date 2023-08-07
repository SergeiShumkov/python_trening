"""# -*- coding: utf-8 -*-

import pytest

from model.group import Group
from fixture.application import Application

@pytest.fixture
def app():
    fixture = Application()
    yield fixture
    fixture.destroy()


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="new_group", header="header_group", footer="footer_group"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()"""