from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

class RegistrantTest(TestCase):
    def test_create(self):
        user = User.objects.create(username='test1')
        user.set_password('passwordtest1')
        user.save()

        user_client = Client()
        user_client.login(username='test1', password='passwordtest1')

        user_client.post(reverse('tender:all_companies_api'), data={
            "company_name": "Coba 1",
            "pt_name": 'PT. Coba 1',
            "npwp": "1231231232"
        })

        admin = User.objects.create_superuser(username='test1admin')
        admin.set_password('passwordtest1admin')
        admin.save()

        admin_client = Client()
        admin_client.login(username='test1admin', password='passwordtest1admin')

        admin_client.post(reverse('tender:all_projects_api'), data={
            "title": "Coba 1",
            "description": 'Description Coba 1'
        })
        
        response = user_client.post(reverse('tender:one_registrant_api', kwargs={ 'id': 1 }), data={
            "offer_price": 123000000,
            "company": 1,
        })
        self.assertEquals(response.status_code, 201)