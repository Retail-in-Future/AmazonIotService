from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class ApiTest(TestCase):

    def setUp(self):
        self.client = APIClient();
        self.base_url = 'http://127.0.0.1:8000/'

    def should_get_thing_shadow(self):
        response = self.client.get(self.base_url+'things');
        self.assertEqual(response.status_code, status.HTTP_200_OK)