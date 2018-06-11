from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="ivan", lastname="taranov", nickname="tara", company="book", address="lenina 1", homephone="555555", mobilephone="666666", workphone="777777", secondaryphone="888888", email="123@mail.ru", byear="1985"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
