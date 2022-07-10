from django.test import TestCase


class PostTestCase(TestCase):

    def test_failure(self):
        self.assertTrue(False)
