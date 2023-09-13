import random


from model.contact import Contact
from model.group import Group


def test_del_contact_from_group(app, db, db_orm, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    contacts = db.get_contact_list()
    contact = random.choice(contacts)

    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = db.get_group_list()
    group = random.choice(groups)

    if len(db_orm.get_contacts_in_group(group)) == 0:
        app.contact.add_contact_to_group(contact.id, group.name)

    contact_del = random.choice(db_orm.get_contacts_in_group(group))

    app.contact.del_contact_from_group(contact_del.id, group.name)
    l = db_orm.get_contacts_in_group(group)
    assert contact_del not in l

