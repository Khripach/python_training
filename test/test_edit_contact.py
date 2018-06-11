from model.contact import Contact
from random import randrange

def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="ivan", lastname="taranov", nickname="tara", company="book", address="lenina 1", homephone="555555", mobilephone="666666", workphone="777777", secondaryphone="888888", email="123@mail.ru", byear="1985"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="ivan2", lastname="taranov2", nickname="tara2", company="book2", address="lenina 12", homephone="5555552", mobilephone="6666662", workphone="7777772", secondaryphone="8888882", email="1232@mail.ru", byear="1986")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
