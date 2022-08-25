from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate
from ..models import Consumable

def create_consumable(user, name, category_pk, unit_pk, reference_size,
    nutrient_pks):
  return {'user': user, 'name': name, 'category': category_pk, 'unit': unit_pk,
    'reference_size': reference_size, 'nutrients': nutrient_pks}

class ListConsumableTest(APITestCase):
  fixtures = ['test_data.json']

  def test_anonymous_denied(self):
    response = self.client.get(reverse('consumable-list'))
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_list(self):
    self.client.force_authenticate(
      user=get_user_model().objects.get(username='user1'))
    response = self.client.get(reverse('consumable-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 2)
    response_names = [response.data[0]['name'], response.data[1]['name']]
    expected_names = ['Test Food 1', 'Test Food 2']
    self.assertEqual(sorted(response_names), sorted(expected_names))

class RetrieveConsumableTest(APITestCase):
  fixtures = ['test_data.json']

  def test_anonymous_denied(self):
    response = self.client.get(
      reverse('consumable-detail', kwargs={'pk': 1}))
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_retrieve(self):
    self.client.force_authenticate(
      user=get_user_model().objects.get(username='user1'))
    response = self.client.get(
      reverse('consumable-detail', kwargs={'pk': 1}))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['name'], 'Test Food 1')

class CreateConsumableTest(APITestCase):
  fixtures = ['test_data.json']

  def test_anonymous_denied(self):
    consumable = create_consumable(1, 'Apple', 1, 1, 1, [1, 2])
    response = self.client.post(reverse('consumable-list'),
      data=consumable, content_type='application/json')
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_create(self):
    self.client.force_authenticate(
      user=get_user_model().objects.get(username='user1'))
    consumable = create_consumable(1, 'Apple', 1, 1, 1, [1, 2])
    response = self.client.post(reverse('consumable-list'), data=consumable)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    new_consumable = Consumable.objects.get(pk=3)
    self.assertEqual(new_consumable.name, 'Apple')

class UpdateConsumableTest(APITestCase):
  fixtures = ['test_data.json']

  def test_anonymous_denied(self):
    put_data = create_consumable(1, 'Banana', 1, 1, 1, [1, 2])
    response = self.client.patch(
      reverse('consumable-detail', kwargs={'pk': 1}), data=put_data)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_unowned_denied(self):
    self.client.force_authenticate(
      user=get_user_model().objects.get(username='user1'))
    put_data = create_consumable(1, 'Banana', 1, 1, 1, [1, 2])
    response = self.client.put(
      reverse('consumable-detail', kwargs={'pk': 2}), data=put_data)
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

  def test_update(self):
    self.client.force_authenticate(
      user=get_user_model().objects.get(username='user1'))
    put_data = create_consumable(1, 'Banana', 1, 1, 1, [1, 2])
    response = self.client.put(
      reverse('consumable-detail', kwargs={'pk': 1}), data=put_data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    updated_consumable = Consumable.objects.get(pk=1)
    self.assertEqual(updated_consumable.name, 'Banana')

class PartialUpdateConsumableTest(APITestCase):
  fixtures = ['test_data.json']

  def test_anonymous_denied(self):
    patch_data = {'name': 'New Name'}
    response = self.client.patch(
      reverse('consumable-detail', kwargs={'pk': 1}), data=patch_data)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_unowned_denied(self):
    self.client.force_authenticate(
      user=get_user_model().objects.get(username='user1'))
    patch_data = {'name': 'New Name'}
    response = self.client.patch(
      reverse('consumable-detail', kwargs={'pk': 2}), data=patch_data)
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

  def test_partial_update(self):
    self.client.force_authenticate(
      user=get_user_model().objects.get(username='user1'))
    patch_data = {'name': 'New Name'}
    response = self.client.patch(
      reverse('consumable-detail', kwargs={'pk': 1}), data=patch_data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    updated_consumable = Consumable.objects.get(pk=1)
    self.assertEqual(updated_consumable.name, 'New Name')

class DestroyConsumableTest(APITestCase):
  fixtures = ['test_data.json']

  def test_anonymous_denied(self):
    patch_data = {'name': 'New Name'}
    response = self.client.delete(
      reverse('consumable-detail', kwargs={'pk': 1}))
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_unowned_denied(self):
    self.client.force_authenticate(
      user=get_user_model().objects.get(username='user1'))
    response = self.client.delete(
      reverse('consumable-detail', kwargs={'pk': 2}))
    self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

  def test_owned_denied(self):
    self.client.force_authenticate(
      user=get_user_model().objects.get(username='user1'))
    response = self.client.delete(
      reverse('consumable-detail', kwargs={'pk': 1}))
    self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
