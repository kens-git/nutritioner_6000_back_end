from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# TODO: exclude this folder from testing so they don't show up as runnable tests
class GenericListTest(APITestCase):
  test_data = {}

  def setUp(self):
    self.url = reverse(f'{GLT.test_data["url_name"]}-list')
    self.username = GLT.test_data['username']
    self.data_length = GLT.test_data['data_length']
    self.column_name = GLT.test_data['column_name']
    self.expected_values = GLT.test_data['expected_values']

  def test_anonymous_denied(self):
    response = self.client.get(self.url)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_list(self):
    self.client.force_authenticate(
      user=get_user_model().objects.get(username=self.username))
    response = self.client.get(self.url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), self.data_length)
    response_names = [
      response.data[0][self.column_name],
      response.data[1][self.column_name]]
    self.assertEqual(sorted(response_names), sorted(self.expected_values))

GLT = GenericListTest
