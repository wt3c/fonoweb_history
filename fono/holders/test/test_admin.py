from django.test import TestCase
from model_mommy import mommy

from fono.holders.admin import Holder, HolderModelAdmin, admin


class HolderModelAdminTest(TestCase):
    def setUp(self):
        self.holder = mommy.make(Holder, pk=1)
        self.model_admin = HolderModelAdmin(self.holder, admin.site)
