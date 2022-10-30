from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

class ProjectTest(TestCase):
    def test_get_all(self):
        client = Client()
        response = client.get(reverse('tender:all_projects_api'))
        self.assertEquals(response.status_code, 200)

    def test_create(self):
        admin = User.objects.create_superuser(username='test1')
        admin.set_password('passwordtest1')
        admin.save()

        client = Client()
        client.login(username='test1', password='passwordtest1')

        response = client.post(reverse('tender:all_projects_api'), data={
            "title": "Coba 1",
            "description": 'Description Coba 1'
        })
        self.assertEquals(response.status_code, 201)

    def test_get_one(self):
        admin = User.objects.create_superuser(username='test1')
        admin.set_password('passwordtest1')
        admin.save()

        client = Client()
        client.login(username='test1', password='passwordtest1')

        client.post(reverse('tender:all_projects_api'), data={
            "title": "Coba 1",
            "description": 'Description Coba 1'
        })

        response = client.get(reverse('tender:one_project_api', kwargs={ 'id': 1 }))
        self.assertEquals(response.status_code, 200)