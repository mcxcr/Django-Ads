from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_success(self):
        """TEST: Create a new user with email."""
        email = 'test@mcx.ink'
        password = 'Test@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """TEST: Case sensitivity."""
        email = 'test@MCX.INK'
        user = get_user_model().objects.create_user(email, 'Test@123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """TEST: Creating user with no email raises error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test@123')

    def test_create_new_superuser(self):
        """TEST: Creating new superuser """
        user = get_user_model().objects.create_superuser(
            'admin@mcx.ink',
            'Test@123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
