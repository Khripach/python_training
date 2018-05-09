# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.contact.add_new(Contact(firstname="ivan", lastname="taranov", nickname="tara", company="book", address="lenina 1", home_phone="555555", email="123@mail.ru", byear="1985"))
