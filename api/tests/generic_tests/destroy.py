from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class GenericDestroyTest(APITestCase):
  test_data = {}

  def setUp(self):
    self.url = f'{self.test_data["url_name"]}-detail'
    self.username = self.test_data['username']
    self.anonymous_url = reverse(self.url,
      kwargs={'pk': self.test_data['pk_unowned']})
    self.owned_url = reverse(self.url,
      kwargs={'pk': self.test_data['pk_owned']})
    self.unowned_url = reverse(self.url,
      kwargs={'pk': self.test_data['pk_unowned']})

  def test_anonymous_denied(self):
    response = self.client.delete(self.anonymous_url)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_unowned_denied(self):
    self.client.force_authenticate(
      user=get_user_model().objects.get(username=self.username))
    response = self.client.delete(self.unowned_url)
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

  def test_owned(self):
    self.client.force_authenticate(
      user=get_user_model().objects.get(username=self.username))
    response = self.client.delete(self.owned_url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
