from model.group import Group
import random

#def test_edit_first_group(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first(Group(name="1", header="2", footer="3"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

def test_edit_some_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    edit_group = Group(name="New name")
    edit_group.id = group.id
    app.group.edit_group_by_id(edit_group.id, edit_group)
    new_groups = db.get_group_list()
    index = old_groups.index(group)
    old_groups[index] = edit_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#def test_edit_first_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
