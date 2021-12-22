from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from model_mommy import mommy

from fono.holders.models import Holder, Pseudonym
from fono.holders.models import Society

class HolderModelTest(TestCase):
    def setUp(self):
        self.holder = mommy.make(Holder, pk=1)

    def test_create_holder(self):
        self.assertTrue(Holder.objects.exists())

class HolderUserModelTest(TestCase):
    """Test the M-One relationship between the Holder and User tables """

    def setUp(self) -> None:
        self.user1 = mommy.make(User, pk=1)
        self.user2 = mommy.make(User, pk=2)
        self.holder1 = mommy.make(Holder, pk=1, owner=self.user1)
        self.holder2 = mommy.make(Holder, pk=1, owner=self.user2)

    def test_create_holder_with_owner(self):
        self.assertTrue(Holder.objects.exists())

    # Acabei não utilizando, mantive como referencia
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

    def test_holder_post_with_user(self):
        user = self.user1
        valid = dict(
            cod_ecad=171,
            name='Tit_valid',
            owner=user
        )
        expected = "/login/?next=%2Ftitular"
        resp = self.client.post(r('holder:new'), valid)
        self.assertRedirects(resp, expected)

class HolderPseudoModelTest(TestCase):
    """Test the M-One relationship between the Holder and Pseudonym tables"""

    def setUp(self):
        self.holder1 = mommy.make(Holder, pk=1)

        self.pseudo1 = mommy.make(Pseudonym, pk=1, holder=self.holder1)
        self.pseudo2 = mommy.make(Pseudonym, pk=2, holder=self.holder1)

    def test_create_holder_with_pseudonym(self):
        self.assertTrue(Holder.objects.exists())
        self.assertTrue(Pseudonym.objects.exists())

    def test_holder_post_with_pseudonym(self):
        user = mommy.make(User)

        valid = dict(
            cod_ecad=171,
            name='Tit_valid',
            owner=user
        )
        expected = "/login/?next=%2Ftitular"
        resp = self.client.post(r('holder:new'), valid)
        self.assertRedirects(resp, expected)

class HolderSocietyTest(TestCase):
    """Test the M-One relationship between the Holder and Society tables"""

    def setUp(self) -> None:
        self.user1 = mommy.make(User, pk=1)
        self.soc = mommy.make(Society, pk=1)
        self.holder = mommy.make(Holder, pk=1, owner=self.user1, society=self.soc)

    def test_create_holder_with_soc(self):
        self.assertTrue(Holder.objects.exists())
