from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from model_mommy import mommy

from fono.holders.forms import HolderForm
from fono.holders.models import Holder


class HolderModelTest(TestCase):
    def setUp(self):
        self.holder = mommy.make(Holder, pk=1)

    def test_create_holder(self):
        self.assertTrue(Holder.objects.exists())


class HolderUserModelTest(TestCase):
    def setUp(self) -> None:
        self.user1 = mommy.make(User, pk=1)
        self.user2 = mommy.make(User, pk=1)
        self.holder1 = mommy.make(Holder, pk=1, owner=self.user1)
        self.holder2 = mommy.make(Holder, pk=1, owner=self.user2)

    def test_create_holder_with_owner(self):
        self.assertTrue(Holder.objects.exists())

    # Acabei não presindo, mantve como referencia
    # def make_valited_form(self, **kwargs):
    #     user = self.user1
    #     valid = dict(
    #         cod_ecad=171,
    #         name='Tit_valid',
    #         owner=user
    #     )
    #     data = dict(valid, **kwargs)
    #     form = HolderForm(data)
    #     form.is_valid()
    #     return form

    def test_holder_post(self):
        user = self.user1
        valid = dict(
            cod_ecad=171,
            name='Tit_valid',
            owner=user
        )
        expected = "/login/?next=%2Ftitular"
        resp = self.client.post(r('holder:new'), valid)
        self.assertRedirects(resp, expected)
