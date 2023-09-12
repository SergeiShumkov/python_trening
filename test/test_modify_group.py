from model.group import Group
import random

def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)

    group_mod = Group(name="New group")
    group_mod.id = old_groups[index].id
    app.group.modify_group_by_id(group.id, group_mod)
    new_groups = db.get_group_list()
    # assert len(old_groups) == len(new_groups)
    old_groups[index] = group_mod
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)





# def test_modify_group_name(app, db):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = db.get_group_list()
#     index = randrange(len(old_groups))
#     group = Group(name="New group")
#     group.id = old_groups[index].id
#     app.group.modify_group_by_index(index, group)
#     new_groups = db.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[index] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




