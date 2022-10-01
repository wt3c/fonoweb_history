from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User
from fono.holders.forms import HolderForm


class HolderNewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="blackthorne@gmail.com",
            email="blackthorne@gmail.com",
            password="Mariko-san",
            first_name="John",  # Shogun --James Clavell
            last_name="BlackThorne"
        )
        self.client.force_login(self.user)
        self.resp = self.client.get(r('holder:new'))

    def test_get(self):
        """Get /titular/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_has_template(self):
        """Must use holders/holders_form.html"""
        self.assertTemplateUsed(self.resp, 'holders/holders_form.html')

    def test_has_form(self):
        """Test if exist in the Get Form"""
        form = self.resp.context['form']
        self.assertEqual(form, HolderForm)
        
ded test2(self):
    
    hdghgdhgd
    print("tetse")
#

#
#
#
#
#
# TESTE
