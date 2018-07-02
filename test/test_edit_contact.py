from model.contact import Contact
import random

def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(firstname="ivan", lastname="taranov", nickname="tara", company="book", address="lenina 1", homephone="555555", mobilephone="666666", workphone="777777", secondaryphone="888888", email="123@mail.ru", byear="1985"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    edit_contact = Contact(firstname="ivan2", lastname="taranov2", nickname="tara2", company="book2", address="lenina 12", homephone="5555552", mobilephone="6666662", workphone="7777772", secondaryphone="8888882", email="1232@mail.ru", byear="1986")
    edit_contact.id = contact.id
    app.contact.edit_contact_by_id(edit_contact.id, edit_contact)
    new_contacts = db.get_contact_list()
    index = old_contacts.index(contact)
    old_contacts[index] = edit_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
