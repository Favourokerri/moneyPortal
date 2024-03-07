from django.test import TestCase, Client
from django.db import transaction
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.
class SignUpViewTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.signup_url = reverse('signUp')
    
    def test_SignUp(self):
        data = {
            'firstName': 'okerri',
            'email': 'favour@gmail.com',
            'password': '12345678'
        }

        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, 302) #check if redirection occured
        self.assertTrue(User.objects.filter(username='favour@gmail.com').exists())
    
    def test_DuplicateUser(self):
        User.objects.create(first_name='peter', email='john@gmail.com', username='john@gmail.com', password='12345678')
        data = {
            'firstName': 'john',
            'email': 'john@gmail.com',
            'password': '12345678'
        }
        try:
            with transaction.atomic():
                response = self.client.post(self.signup_url, data)
        except IntegrityError:
            self.fail('user with thie email alredy exits')
        self.assertEqual(response.status_code, 200) #check that there was no redirect
        self.assertFalse(User.objects.filter(first_name='john').exists())