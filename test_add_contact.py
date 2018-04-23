# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact(Contact(firstname="ivan", lastname="taranov", nickname="tara", company="book", address="lenina 1", home_phone="555555", email="123@mail.ru", byear="1985"))
    app.logout()
