from django.test import TestCase
from django.contrib.auth.models import User
from model_mommy import mommy

from fono.holders.models import Contact
from fono.holders.models import Holder
from fono.holders.models import Society


class ContacModelTest(TestCase):

    def setUp(self):
        user = mommy.make(User)
        society = mommy.make(Society)
        self.holder = Holder.objects.create(
            owner=user,
            society=society,
            cod_ecad=17171,
            name='John BlackThoner',
        )

    def test_email(self):
        Contact.objects.create(
            holder=self.holder,
            kind=Contact.EMAIL, value='blackthoner@gmail.com'
        )
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        Contact.objects.create(
            holder=self.holder,
            kind=Contact.EMAIL, value='blackthoner@gmail.com'
        )
        self.assertTrue(Contact.objects.exists())


class ContactManagerTest(TestCase):
    def setUp(self):
        user = mommy.make(User)
        society = mommy.make(Society)
        holder = Holder.objects.create(
            owner=user,
            society=society,
            cod_ecad=17171,
            name='John BlackThoner',
        )
        holder.contact_set.create(
            kind=Contact.EMAIL,
            value='blackthoner@gmail.com'
        )
        holder.contact_set.create(
            kind=Contact.PHONE,
            value='21-8995545555'
        )

    def test_emai(self):
        qs = Contact.objects.emails()
        expected = ['blackthoner@gmail.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phone(self):
        qs = Contact.objects.phones()
        expected = ['21-8995545555']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
