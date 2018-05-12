from model.contact import Contact

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="ivan", lastname="taranov", nickname="tara", company="book", address="lenina 1", home_phone="555555", email="123@mail.ru", byear="1985"))
    app.contact.edit_first(Contact(firstname="ivan2", lastname="taranov2", nickname="tara2", company="book2", address="lenina 12", home_phone="5555552", email="1232@mail.ru", byear="1986"))
