from .generic_tests.create import GenericCreateTest
from .generic_tests.destroy_disabled import GenericDestroyDisabledTest
from .generic_tests.list import GenericListTest
from .generic_tests.partial_update import GenericPartialUpdateTest
from .generic_tests.retreive import GenericRetrieveTest
from .generic_tests.update import GenericUpdateTest
from ..models import Consumable

def create_consumable(user, name, category_pk, unit_pk, reference_size,
    nutrient_pks):
  return {'user': user, 'name': name, 'category': category_pk, 'unit': unit_pk,
    'reference_size': reference_size, 'nutrients': nutrient_pks}

class ListConsumableTest(GenericListTest):
  GenericListTest.fixtures = ['test_data.json']

  GenericListTest.test_data = {
    'url_name': 'consumable',
    'username': 'user1',
    'data_length': 2,
    'column_name': 'name',
    'expected_values': ['Test Food 1', 'Test Food 2'],
  }

class RetrieveConsumableTest(GenericRetrieveTest):
  GenericRetrieveTest.fixtures = ['test_data.json']

  GenericRetrieveTest.test_data = {
    'url_name': 'consumable',
    'username': 'user1',
    'pk': 1,
    'column_name': 'name',
    'expected_value': 'Test Food 1',
  }

class CreateConsumableTest(GenericCreateTest):
  GenericCreateTest.fixtures = ['test_data.json']

  GenericCreateTest.test_data = {
    'url_name': 'consumable',
    'data': create_consumable(1, 'Apple', 1, 1, 1, [1, 2]),
    'username': 'user1',
    'created_data': lambda: Consumable.objects.get(pk=3).name,
    'pk': 3,
    'column_name': 'name',
  }

class UpdateConsumableTest(GenericUpdateTest):
  GenericUpdateTest.fixtures = ['test_data.json']

  GenericUpdateTest.test_data = {
    'url_name': 'consumable',
    'data': create_consumable(1, 'Banana', 1, 1, 1, [1, 2]),
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 2,
    'updated_data': lambda: Consumable.objects.get(pk=1).name,
    'column_name': 'name',
  }

class PartialUpdateConsumableTest(GenericPartialUpdateTest):
  GenericPartialUpdateTest.fixtures = ['test_data.json']

  GenericPartialUpdateTest.test_data = {
    'url_name': 'consumable',
    'data': {'name': 'New Name'},
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 2,
    'updated_data': lambda: Consumable.objects.get(pk=1).name,
    'column_name': 'name',
  }

class DestroyConsumableTest(GenericDestroyDisabledTest):
  GenericDestroyDisabledTest.fixtures = ['test_data.json']

  GenericDestroyDisabledTest.test_data = {
    'url_name': 'consumable',
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 2,
  }
