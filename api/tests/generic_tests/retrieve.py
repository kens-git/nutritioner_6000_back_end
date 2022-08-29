from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class GenericRetrieveTest(APITestCase):
  test_data = {}

  def setUp(self):
    self.url = reverse(f'{self.test_data["url_name"]}-detail',
      kwargs={'pk': self.test_data['pk']})
    self.username = self.test_data['username']
    self.column_name = self.test_data['column_name']
    self.expected_value = self.test_data['expected_value']

  def test_anonymous_denied(self):
    response = self.client.get(self.url)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_retrieve(self):
    self.client.force_authenticate(
      user=get_user_model().objects.get(username=self.username))
    response = self.client.get(self.url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data[self.column_name], self.expected_value)
