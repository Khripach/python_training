from model.contact import Contact

def test_edit_first_contact(app):
    app.contact.edit_first(Contact(firstname="ivan2", lastname="taranov2", nickname="tara2", company="book2", address="lenina 12", home_phone="5555552", email="1232@mail.ru", byear="1986"))
