from model.contact import Contact

def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="New firstname"))

def test_modify_contact_home_phone_number(app):
    app.contact.modify_first_contact(Contact(home_phone_number="11-11-11"))
