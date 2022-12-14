from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

# most test codes from team member adryanhaska

class HealthcareTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test1')
        self.user.set_password('passwordtest1')
        self.user.save()

        self.client = Client()
        self.client.login(username='test1', password='passwordtest1')

        self.admin = User.objects.create_superuser(username='test1admin')
        self.admin.set_password('passwordtest1admin')
        self.admin.save()

        self.admin_client = Client()
        self.admin_client.login(username='test1admin', password='passwordtest1admin')

    def test_show(self):
        response = self.client.get(reverse('healthcare:show_healthcare'))
        self.assertEquals(response.status_code, 200)

    def test_add(self):
        self.admin_client.login(username='test1', password='passwordtest1')
        response = self.client.post(reverse('healthcare:add_keluhan'), data={
            'keluhan': 'aids',
            'appointment_date': '2021-01-01',
        })
        self.assertEquals(response.status_code, 201)

        self.admin_client.login(username='test1', password='passwordtest1')
        response = self.client.post(reverse('healthcare:add_keluhan'), data={
            'keluhan': 'aids',
        })
        self.assertEquals(response.status_code, 404)
        #  keluhan = form.cleaned_data['keluhan']
        #     appointment_date = form.cleaned_data['appointment_date']
        #     phone_number = form.cleaned_data['phone_number']
    def test_update(self):
        self.admin_client.login(username='test1admin', password='passwordtest1admin')
        response = self.client.post(reverse('healthcare:update_keluhan', kwargs={ 'id': 1 }), {'pk':1})
        self.assertEquals(response.status_code, 200)

    def test_deleter(self):
        self.admin_client.login(username='test1admin', password='passwordtest1admin')
        response = self.client.post(reverse('healthcare:delete_keluhan', kwargs={ 'id': 1 }), {'pk':1})
        self.assertEquals(response.status_code, 200)