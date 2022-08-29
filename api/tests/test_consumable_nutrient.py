from .generic_tests import (create, destroy_disabled, list, partial_update,
  retrieve, update)
from ..models import ConsumableNutrient

def create_consumable_nutrient(user, nutrient, value):
  return {'user': user, 'nutrient': nutrient, 'value': value}

class ListConsumableNutrientTest(list.GenericListTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'consumable-nutrient',
    'username': 'user1',
    'data_length': 4,
    'column_name': 'value',
    'expected_values': [10.0, 10.0, 100.0, 100.0],
  }

class RetrieveConsumableNutrientTest(retrieve.GenericRetrieveTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'consumable-nutrient',
    'username': 'user1',
    'pk': 1,
    'column_name': 'value',
    'expected_value': 10.0,
  }

class CreateConsumableNutrientTest(create.GenericCreateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'consumable-nutrient',
    'data': create_consumable_nutrient(1, 1, 1000),
    'username': 'user1',
    'created_data': lambda: ConsumableNutrient.objects.get(pk=5).value,
    'column_name': 'value',
  }

class UpdateConsumableNutrientTest(update.GenericUpdateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'consumable-nutrient',
    'data': create_consumable_nutrient(1, 1, 1000),
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 3,
    'updated_data': lambda: ConsumableNutrient.objects.get(pk=1).value,
    'column_name': 'value',
  }

class PartialUpdateConsumableNutrientTest(partial_update.GenericPartialUpdateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'consumable-nutrient',
    'data': {'value': 1000},
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 3,
    'updated_data': lambda: ConsumableNutrient.objects.get(pk=1).value,
    'column_name': 'value',
  }

class DestroyConsumableNutrientTest(destroy_disabled.GenericDestroyDisabledTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'consumable-nutrient',
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 3,
  }
