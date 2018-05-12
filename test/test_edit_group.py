from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_first(Group(name="1", header="2", footer="3"))

def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_first(Group(name="New name"))

def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_first(Group(header="New header"))
