from django.test import TestCase
from django.contrib.auth import get_user
from django.shortcuts import resolve_url as r
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class HomeTest(TestCase):
    def setUp(self):
        # User = get_user_model()
        self.user = User.objects.create_user(
            username="blackthorne@gmail.com",
            email="blackthorne@gmail.com",
            password="Mariko-san",
            first_name="John",  # Shogun --James Clavell
            last_name="BlackThorne"
        )
        # self.client.login(username='blackthorne@gmail.com', password="Mariko-san")
        self.client.force_login(self.user)
        self.resp = self.client.get(r('home'))

    def test_home(self):
        """Get '('home ') must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_home_redirect_login(self):
        """If USER is AnonymousUser must be redirected by 'login'"""
        self.client.logout()
        resp = self.client.get(r('home'))
        self.assertRedirects(resp, r('/login/?next=%2F'))

    def test_redirect_login_to_home(self):
        """After login must be redirected to 'Home' """
        data = dict(username="blackthorne@gmail.com", password="Mariko-san")
        resp = self.client.post(r('login'), data)
        self.assertRedirects(resp, r('home'))

    # def test_logout(self):
    #     """The User must be AnonymousUser"""
    #     resp = self.client.get('/logout/')
    #     expected = 'AnonymousUser'
    #     user = get_user(resp)
    #     print(user, '************************')
    #     self.assertEqual(expected, user)
