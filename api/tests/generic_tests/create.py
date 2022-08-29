from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class GenericCreateTest(APITestCase):
  test_data = {}

  def setUp(self):
    self.url = reverse(f'{self.test_data["url_name"]}-list')
    self.data = self.test_data['data']
    self.username = self.test_data['username']
    self.created_data = self.test_data['created_data']
    self.expected_data = self.test_data['data'][self.test_data['column_name']]

  def test_anonymous_denied(self):
    response = self.client.post(self.url, data=self.data)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_create(self):
    self.client.force_authenticate(
      user=get_user_model().objects.get(username=self.username))
    response = self.client.post(self.url, data=self.data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(self.created_data(), self.expected_data)
