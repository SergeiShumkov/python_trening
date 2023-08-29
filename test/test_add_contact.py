# -*- coding: utf-8 -*-
import re
import pytest
import random
import string
from model.contact import Contact


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_for_name(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# string.punctuation +  +  " "*10
def random_string_for_phone(maxlen):
    symbols = string.digits + "- ()+"
    return  "".join([random.choice(symbols) for i in range(random.randrange(4, maxlen))])


def random_string_for_email(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(2, maxlen))]) + "@" + "".join([random.choice(symbols) for i in range(random.randrange(2, maxlen))]) + ".com"


testdata = [Contact(firstname="", lastname="", homephone="", mobilephone="", workphone="", secondaryphone="", address="",
                 email1="", email2="", email3="")] + [
        Contact(firstname=random_string_for_name("firstname", 10), lastname=random_string_for_name("lastname", 10),
                homephone=random_string_for_phone(10),  mobilephone=random_string_for_phone(10),
                workphone=random_string_for_phone(10), secondaryphone=random_string_for_phone(10),
                address=random_string("address", 20), email1=random_string_for_email(7),
                email2=random_string_for_email(7), email3=random_string_for_email(7))

        for i in range(5)
    ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    contact.all_emails_from_home_page = merge_emails([contact.email1, contact.email2, contact.email3])
    contact.all_phones_from_home_page = merge_phones([contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone])
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones(phones):
    return "\n".join(filter(lambda x: x != "",map(lambda x: clear(x),
                                                  filter(lambda x: x is not None,
                                                         phones))))

def merge_emails(emails):
    return "\n".join(filter(lambda x: x != "",map(lambda x: clear(x),
                                                  filter(lambda x: x is not None,
                                                         emails))))

