from .generic_tests import (create, destroy_disabled, list, partial_update,
  retrieve, update)
from ..models import Consumable

def create_consumable(user, name, category_pk, unit_pk, reference_size,
    nutrient_pks):
  return {'user': user, 'name': name, 'category': category_pk, 'unit': unit_pk,
    'reference_size': reference_size, 'nutrients': nutrient_pks}

class ListConsumableTest(list.GenericListTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'consumable',
    'username': 'user1',
    'data_length': 2,
    'column_name': 'name',
    'expected_values': ['Test Food 1', 'Test Food 2'],
  }

class RetrieveConsumableTest(retrieve.GenericRetrieveTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'consumable',
    'username': 'user1',
    'pk': 1,
    'column_name': 'name',
    'expected_value': 'Test Food 1',
  }

class CreateConsumableTest(create.GenericCreateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'consumable',
    'data': create_consumable(1, 'Apple', 1, 1, 1, [1, 2]),
    'username': 'user1',
    'created_data': lambda: Consumable.objects.get(pk=3).name,
    'column_name': 'name',
  }

# TODO: duplicate name test

class UpdateConsumableTest(update.GenericUpdateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'consumable',
    'data': create_consumable(1, 'Banana', 1, 1, 1, [1, 2]),
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 2,
    'updated_data': lambda: Consumable.objects.get(pk=1).name,
    'column_name': 'name',
  }

class PartialUpdateConsumableTest(partial_update.GenericPartialUpdateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'consumable',
    'data': {'name': 'New Name'},
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 2,
    'updated_data': lambda: Consumable.objects.get(pk=1).name,
    'column_name': 'name',
  }

class DestroyConsumableTest(destroy_disabled.GenericDestroyDisabledTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'consumable',
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 2,
  }
