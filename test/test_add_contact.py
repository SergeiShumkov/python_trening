# -*- coding: utf-8 -*-
import pytest

from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login( username="admin", password="secret")
    app.contact.create(Contact(firstname="First", middlename="Middle", lastname="Last", nickname="Nickname", company_name="Company", home_phone_number="45-45-45"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", company_name="", home_phone_number=""))
    app.session.logout()

