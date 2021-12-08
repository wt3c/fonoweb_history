from django.test import TestCase
from django.contrib.auth.models import User
from model_mommy import mommy
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
