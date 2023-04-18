from django.test import TestCase

# Create your tests here.

from .models import User

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user= User.objects.create(
            phoneNumber='01012341234',
            password='1234',
        )
    
    def test_user_creation(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertEqual(self.user.__str__(),self.user.phoneNumber)
        self.assertEqual(self.user.password,'1234')