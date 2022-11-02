from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

class RegistrantTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test1')
        self.user.set_password('passwordtest1')
        self.user.save()

        self.user_client = Client()
        self.user_client.login(username='test1', password='passwordtest1')

        self.user_client.post(reverse('tender:all_companies_api'), data={
            "company_name": "Coba 1",
            "pt_name": 'PT. Coba 1',
            "npwp": "1231231232"
        })

        self.admin = User.objects.create_superuser(username='test1admin')
        self.admin.set_password('passwordtest1admin')
        self.admin.save()

        self.admin_client = Client()
        self.admin_client.login(username='test1admin', password='passwordtest1admin')

    def test_create(self):
        self.admin_client.post(reverse('tender:all_projects_api'), data={
            "title": "Coba 1",
            "description": 'Description Coba 1'
        })
        response = self.user_client.post(reverse('tender:one_registrant_api', kwargs={ 'id': 1 }), data={
            "offer_price": 123000000,
            "company": 1,
        })
        self.assertEquals(response.status_code, 201)