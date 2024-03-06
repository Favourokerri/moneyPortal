from django.test import TestCase, Client
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