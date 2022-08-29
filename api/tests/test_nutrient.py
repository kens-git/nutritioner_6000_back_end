from .generic_tests import (create, destroy_disabled, list, partial_update,
  retrieve, update)
from ..models import Nutrient

def create_nutrient(user, name, description, unit):
  return {'user': user, 'name': name, 'description': description, 'unit': unit}

class ListNutrientTest(list.GenericListTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'nutrient',
    'username': 'user1',
    'data_length': 2,
    'column_name': 'name',
    'expected_values': [3, 4],
  }

class RetrieveNutrientTest(retrieve.GenericRetrieveTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'nutrient',
    'username': 'user1',
    'pk': 1,
    'column_name': 'name',
    'expected_value': 3,
  }

class CreateNutrientTest(create.GenericCreateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'nutrient',
    'data': create_nutrient(1, 8, '', 1),
    'username': 'user1',
    'created_data': lambda: Nutrient.objects.get(pk=3).name.id,
    'column_name': 'name',
  }

class UpdateNutrientTest(update.GenericUpdateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'nutrient',
    'data': create_nutrient(1, 8, '', 1),
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 2,
    'updated_data': lambda: Nutrient.objects.get(pk=1).name.id,
    'column_name': 'name',
  }

class PartialUpdateNutrientTest(partial_update.GenericPartialUpdateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'nutrient',
    'data': {'name': 8},
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 2,
    'updated_data': lambda: Nutrient.objects.get(pk=1).name.id,
    'column_name': 'name',
  }

class DestroyNameTest(destroy_disabled.GenericDestroyDisabledTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'name',
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 2,
  }
