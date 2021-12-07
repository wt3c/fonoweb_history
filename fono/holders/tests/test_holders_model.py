from django.test import TestCase
from model_mommy import mommy
from fono.holders.models import Holder


class HolderModelTest(TestCase):
    def setUp(self):
        self.holder = mommy.make(Holder, pk=1)

    def test_create_holder(self):
        self.assertTrue(Holder.objects.exists())
