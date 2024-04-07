from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from unittest.mock import patch
from referral.models import *

class RegisterUserTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_user_success(self):
        url = reverse('register_user')
        data = {
            "name": "Test User",
            "email": "test@example.com",
            "password": "testpassword",
            "referral_code": "example-referral-code"
        }
        with patch('requests.post') as mocked_post:
            mocked_post.return_value.status_code = 200
            mocked_post.return_value.json.return_value = {
                "access": "example_access_token",
                "refresh": "example_refresh_token"
            }
            response = self.client.post(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data['app_data']['StatusCode'], 6000)


class ViewDetailsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_view_details_success(self):
        user = Register.objects.create(name="Test User", email="test@example.com", password="testpassword")
        url = reverse('view_details', kwargs={'pk': user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['app_data']['StatusCode'], 6000)


class ViewReferralDataTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_view_referral_data_success(self):
        user = Register.objects.create(name="Test User", email="test@example.com", password="testpassword", referral_code="example-referral-code")
        url = reverse('view_referral_data', kwargs={'pk': user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['app_data']['StatusCode'], 6000)


# Create your tests here.
