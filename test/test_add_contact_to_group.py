import random


from model.contact import Contact
from model.group import Group

def test_add_contact_to_group(app, db, db_orm, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    contacts = db.get_contact_list()
    # contact = random.choice(contacts)

    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = db.get_group_list()
    # group = random.choice(groups)

    arr = [(contact, group) for contact in contacts for group in groups if contact not in db_orm.get_contacts_in_group(group)]

    if len(arr) == 0: # Проверка, что все контакты добавлены во все группы
        contact_del = random.choice(contacts)
        group_del = random.choice(groups)
        app.contact.del_contact_from_group(contact_del.id, group_del.name)
        contact = contact_del
        group = group_del
    else:
        contact, group = random.choice(arr)
    app.contact.add_contact_to_group(contact.id, group.name)
    l = db_orm.get_contacts_in_group(group)
    assert contact in l
