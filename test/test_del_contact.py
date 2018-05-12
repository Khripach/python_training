from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="ivan", lastname="taranov", nickname="tara", company="book", address="lenina 1", home_phone="555555", email="123@mail.ru", byear="1985"))
    app.contact.delete_first_contact()
