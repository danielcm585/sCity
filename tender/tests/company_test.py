from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

class CompanyTest(TestCase):
    def test_get_all(self):
        client = Client()
        response = client.get(reverse('tender:all_companies_api'))
        self.assertEquals(response.status_code, 200)

    def test_create(self):
        user = User.objects.create(username='test1')
        user.set_password('passwordtest1')
        user.save()

        client = Client()
        client.login(username='test1', password='passwordtest1')

        response = client.post(reverse('tender:all_companies_api'), data={
            "company_name": "Coba 1",
            "pt_name": 'PT. Coba 1',
            "npwp": "1231231232"
        })
        self.assertEquals(response.status_code, 201)

    def test_get_one(self):
        user = User.objects.create(username='test1')
        user.set_password('passwordtest1')
        user.save()

        client = Client()
        client.login(username='test1', password='passwordtest1')

        client.post(reverse('tender:all_companies_api'), data={
            "company_name": "Coba 1",
            "pt_name": 'PT. Coba 1',
            "npwp": "1231231232"
        })

        response = client.get(reverse('tender:one_company_api', kwargs={ 'id': 1 }))
        self.assertEquals(response.status_code, 200)