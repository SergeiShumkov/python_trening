from model.contact import Contact
import random

def test_modify_contact_firstname(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)

    contact_mod = Contact(firstname="New firstname")
    contact_mod.id = old_contacts[index].id
    contact_mod.lastname = old_contacts[index].lastname
    app.contact.modify_contact_by_id(contact.id, contact_mod)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact_mod
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

# def test_modify_contact_home_phone_number(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="test"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first_contact(Contact(home_phone_number="11-11-11"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
