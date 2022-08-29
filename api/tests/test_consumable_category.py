from .generic_tests import (create, destroy_disabled, list, partial_update,
  retrieve, update)
from ..models import ConsumableCategory, Name

def create_category(user, name, description):
  return {'user': user, 'name': name, 'description': description}

class ListConsumableCategoryTest(list.GenericListTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'consumable-category',
    'username': 'user1',
    'data_length': 2,
    'column_name': 'name',
    'expected_values': [1, 2],
  }

class RetrieveConsumableCategoryTest(retrieve.GenericRetrieveTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'consumable-category',
    'username': 'user1',
    'pk': 1,
    'column_name': 'name',
    'expected_value': 1,
  }

class CreateConsumableCategoryTest(create.GenericCreateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'consumable-category',
    'data': create_category(1, 8, ''),
    'username': 'user1',
    'created_data': lambda: ConsumableCategory.objects.get(pk=3).name.id,
    'column_name': 'name',
  }

class UpdateConsumableCategoryTest(update.GenericUpdateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'consumable-category',
    'data': create_category(1, 8, ''),
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 2,
    'updated_data': lambda: ConsumableCategory.objects.get(pk=1).name.id,
    'column_name': 'name',
  }

class PartialUpdateConsumableCategoryTest(partial_update.GenericPartialUpdateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'consumable-category',
    'data': {'name': 8},
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 2,
    'updated_data': lambda: ConsumableCategory.objects.get(pk=1).name.id,
    'column_name': 'name',
  }

class DestroyConsumableCategoryTest(destroy_disabled.GenericDestroyDisabledTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'consumable-category',
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 2,
  }
