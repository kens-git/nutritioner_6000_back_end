from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class GenericListTest(APITestCase):
  test_data = {}

  def setUp(self):
    self.url = reverse(f'{self.test_data["url_name"]}-list')
    self.username = self.test_data['username']
    self.data_length = self.test_data['data_length']
    self.column_name = self.test_data['column_name']
    self.expected_values = self.test_data['expected_values']

  def test_anonymous_denied(self):
    response = self.client.get(self.url)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_list(self):
    self.client.force_authenticate(
      user=get_user_model().objects.get(username=self.username))
    response = self.client.get(self.url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), self.data_length)
    response_data = [item[self.column_name] for item in response.data]
    self.assertEqual(sorted(response_data), sorted(self.expected_values))
