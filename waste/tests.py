from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.

class WasteTest(TestCase):
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
        response = self.client.get(reverse('waste:show_waste'))
        self.assertEquals(response.status_code, 200)
        
    def test_show_admin(self):
        response = self.admin_client.get(reverse('waste:show_admin'))
        self.assertEquals(response.status_code, 200)    

    def test_show_admin2(self):
        self.client.login(username='test1', password='passwordtest1')
        response = self.client.get(reverse('waste:show_admin'))
        self.assertEquals(response.status_code, 200)    


    def test_get_all(self):
        response = self.client.get(reverse('waste:get_waste_json'))
        self.assertEquals(response.status_code, 200)

    def test_get_admin(self):
        response = self.client.get(reverse('waste:get_waste_json_admin'))
        self.assertEquals(response.status_code, 200)


    def test_add(self):
        self.admin_client.login(username='test1', password='passwordtest1')
        response = self.client.post(reverse('waste:add_waste'), data={
            "waste_type": "Plastic",
            "weight": '2',
        })
        self.assertEquals(response.status_code, 201)

        self.admin_client.login(username='test1', password='passwordtest1')
        response = self.client.post(reverse('waste:add_waste'), data={
            "waste_type": "Plastic",
        })
        self.assertEquals(response.status_code, 404)

    def test_update(self):
        self.admin_client.login(username='test1admin', password='passwordtest1admin')
        response = self.client.post(reverse('waste:update_waste', kwargs={ 'id': 1 }), {'pk':1})
        self.assertEquals(response.status_code, 200)

    def test_deleter(self):
        self.admin_client.login(username='test1admin', password='passwordtest1admin')
        response = self.client.post(reverse('waste:delete_waste', kwargs={ 'id': 1 }), {'pk':1})
        self.assertEquals(response.status_code, 200)
        

    
