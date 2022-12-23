import pytest
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User
from django.contrib import auth
from pytest_django.asserts import assertTemplateUsed


@pytest.fixture
@pytest.mark.django_db
def get_user():
    return User.objects.create_user(username="blackthorne@gmail.com",
                                    email="blackthorne@gmail.com",
                                    password="Mariko-san",
                                    first_name="John",
                                    last_name="BlackThorne")  # Shogun --James Clavell



@pytest.mark.django_db
def test_home(client, get_user):
    """Get home must return status code 200"""

    client.force_login(get_user)
    response = client.get(r('home'))

    assert response.status_code == 200


def test_home_redirect_login(client):
    """If USER is AnonymousUser must be redirected by 'login'"""
    response = client.get(r('home'))
    assert response.status_code == 302



@pytest.mark.django_db
def test_has_template(client, get_user):
    """Must use index.html"""

    client.force_login(get_user)
    response = client.get(r('home'))
    assertTemplateUsed(response, 'index.html')


@pytest.mark.django_db
def test_logout(client, get_user):
    """The USER must be AnonymouUSer or empty
        and the status_code must be 302 """

    # Step one, login
    client.force_login(get_user)

    # Step two, calling logout function
    client.get(r('logout'))

    # Response should return 302 as status_code
    response = client.get(r('home'))

    assert response.status_code == 302
    assert auth.get_user(client).username == ''
