import pytest
from django.test import Client
from django.shortcuts import resolve_url as r

def test_home():
    client = Client()

    response = client.get(r('home'))

    assert response.status_code == 200
