from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class GenericUpdateTest(APITestCase):
  test_data = {}

  def setUp(self):
    self.url = f'{self.test_data["url_name"]}-detail'
    self.data = self.test_data['data']
    self.username = self.test_data['username']
    self.pk_owned = self.test_data['pk_owned']
    self.pk_unowned = self.test_data['pk_unowned']
    self.anonymous_url = reverse(self.url, kwargs={'pk': self.pk_unowned})
    self.owned_url = reverse(self.url, kwargs={'pk': self.pk_owned})
    self.unowned_url = reverse(self.url, kwargs={'pk': self.pk_unowned})
    self.updated_data = self.test_data['updated_data']
    self.column_name = self.test_data['column_name']
    self.denied_status = self.test_data.get('denied_status',
      status.HTTP_403_FORBIDDEN)

  def test_anonymous_denied(self):
    response = self.client.patch(self.anonymous_url, data=self.data)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_unowned_denied(self):
    self.client.force_authenticate(
      user=get_user_model().objects.get(username=self.username))
    response = self.client.put(self.unowned_url, data=self.data)
    self.assertEqual(response.status_code, self.denied_status)

  def test_update(self):
    self.client.force_authenticate(
      user=get_user_model().objects.get(username=self.username))
    response = self.client.put(self.owned_url, data=self.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(self.updated_data(), self.data[self.column_name])
