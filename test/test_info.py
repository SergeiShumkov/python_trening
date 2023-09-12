import re


def test_info_on_home_page(app, db):
    contacts = app.contact.get_contact_list()
    contacts_db = db.get_contact_list()
    for contact_from_home_page in contacts:
        id = contact_from_home_page.id
        contact_db = list(filter(lambda s: s.id == id, contacts_db))[0]
        assert contact_from_home_page.firstname == contact_db.firstname
        assert contact_from_home_page.lastname == contact_db.lastname
        assert contact_from_home_page.address == contact_db.address
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_db(contact_db)
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_db(contact_db)


# def test1_info_on_home_page(app):
#     contacts = app.contact.get_contact_list()
#     index = randrange(len(contacts))
#     contact_from_home_page = contacts[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
#     assert contact_from_home_page.firstname == contact_from_edit_page.firstname
#     assert contact_from_home_page.lastname == contact_from_edit_page.lastname
#     assert contact_from_home_page.address == contact_from_edit_page.address
#     assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_db(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
                                                   filter(lambda x: x is not None,
                                                          [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_emails_like_on_db(contact):
    return "\n".join(filter(lambda x: x is not None and x != "",
                                                         [contact.email1, contact.email2, contact.email3]))

