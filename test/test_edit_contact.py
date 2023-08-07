
from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login( username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="Edited", middlename="Edited", lastname="Edited", nickname="Edited", company_name="Edited", home_phone_number="55-55-55"))
    app.session.logout()
