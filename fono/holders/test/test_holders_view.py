from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r


class HolderView(TestCase):
    def setUp(self) -> None:
        data = {'csrfmiddlewaretoken': ['wJJA8jykTObFZ1y8XgYpzr8yTeKshxGtvwlnTE42Em1mULc7lj7lUWN7Gwjy9YbX'],
                'pseudonym_set-TOTAL_FORMS': ['2'],
                'pseudonym_set-INITIAL_FORMS': ['0'],
                'pseudonym_set-MIN_NUM_FORMS': ['0'],
                'pseudonym_set-MAX_NUM_FORMS': ['1000'],
                'pseudonym_set-0-pseudonym': ['danda'],
                'pseudonym_set-1-pseudonym': ['patalogica'],
                'cod_ecad': ['555642'],
                'society': ['2'],
                'name': ['ROSANGELA MAGALI P.GROSSO'],
                'type_doc': ['F'],
                'cpf': ['12345646545'],
                'cnpj': ['333333'],
                'ifpi': ['RMG'],
                'radical_ifpi': ['BX'],
                'contact_set-TOTAL_FORMS': ['3'],
                'contact_set-INITIAL_FORMS': ['0'],
                'contact_set-MIN_NUM_FORMS': ['0'],
                'contact_set-MAX_NUM_FORMS': ['1000'],
                'contact_set-0-kind': ['E'],
                'contact_set-0-value': ['danda@gmail.com'],
                'contact_set-1-kind': ['P'],
                'contact_set-1-value': ['45454554'],
                'contact_set-2-kind': ['E'],
                'contact_set-2-value': ['angel@gmail.com'],
                'is_interpreter': ['on'],
                'note': ['']}

        self.user = User.objects.create_user(
                username="blackthorne@gmail.com",
                email="blackthorne@gmail.com",
                password="Mariko-san",
                first_name="John",  # Shogun --James Clavell
                last_name="BlackThorne"
        )
        # self.client.login(username='blackthorne@gmail.com', password="Mariko-san")
        self.client.force_login(self.user)
        self.resp = self.client.post(r('holder:new'), data)

    def test_post(self):
        self.assertEqual(200, self.resp.status_code)
