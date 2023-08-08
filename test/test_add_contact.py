# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login( username="admin", password="secret")
    app.contact.create(Contact(firstname="First", middlename="Middle", lastname="Last", nickname="Nickname", company_name="Company", home_phone_number="45-45-45"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", company_name="", home_phone_number=""))
    app.session.logout()

