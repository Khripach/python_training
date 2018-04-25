# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new(Contact(firstname="ivan", lastname="taranov", nickname="tara", company="book", address="lenina 1", home_phone="555555", email="123@mail.ru", byear="1985"))
    app.session.logout()
