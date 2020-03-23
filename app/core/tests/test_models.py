from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    def test_create_user_with_email_successfull(self):
    
        """Test create a new user with an email address"""
        email = 'mf1378mf@yahoo.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email, 
            password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalized(self):
        
        """Test the email for a new user is normalized"""
        
        email = 'mf1378mf@yahoo.com'
        user = get_user_model().objects_create_user(email=email , password="test123")
        
        self.assertEqual(user.email, email.lower())
        
    