from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

class CompanyTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test1')
        self.user.set_password('passwordtest1')
        self.user.save()

        self.client = Client()
        self.client.login(username='test1', password='passwordtest1')

    def test_get_all(self):
        response = self.client.get(reverse('tender:all_companies_api'))
        self.assertEquals(response.status_code, 200)

    def test_create(self):
        self.client.login(username='test1', password='passwordtest1')
        response = self.client.post(reverse('tender:all_companies_api'), data={
            "company_name": "Coba 1",
            "pt_name": 'PT. Coba 1',
            "npwp": "1231231232"
        })
        self.assertEquals(response.status_code, 201)

    def test_get_one(self):
        self.client.post(reverse('tender:all_companies_api'), data={
            "company_name": "Coba 1",
            "pt_name": 'PT. Coba 1',
            "npwp": "1231231232"
        })
        response = self.client.get(reverse('tender:one_company_api', kwargs={ 'id': 1 }))
        self.assertEquals(response.status_code, 200)