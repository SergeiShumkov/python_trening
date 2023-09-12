# -*- coding: utf-8 -*-
import re

from model.contact import Contact


def test_add_contact(app, db, json_contacts):
    contact = json_contacts
    contact.all_emails_from_home_page = merge_emails([contact.email1, contact.email2, contact.email3])
    contact.all_phones_from_home_page = merge_phones([contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone])
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    # assert len(old_contacts) + 1 == len(new_contacts)
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

