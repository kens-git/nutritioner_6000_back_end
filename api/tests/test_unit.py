from .generic_tests import (create, destroy_disabled, list, partial_update,
  retrieve, update)
from ..models import Unit

def create_unit(user, name, description):
  return {'user': user, 'name': name, 'description': description}

class ListUnitTest(list.GenericListTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'unit',
    'username': 'user1',
    'data_length': 3,
    'column_name': 'name',
    'expected_values': [5, 6, 7],
  }

class RetrieveUnitTest(retrieve.GenericRetrieveTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'unit',
    'username': 'user1',
    'pk': 1,
    'column_name': 'name',
    'expected_value': 5,
  }

class CreateUnitTest(create.GenericCreateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'unit',
    'data': create_unit(1, 8, ''),
    'username': 'user1',
    'created_data': lambda: Unit.objects.get(pk=4).name.id,
    'column_name': 'name',
  }

# TODO: duplicate name test

class UpdateUnitTest(update.GenericUpdateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'unit',
    'data': create_unit(1, 8, ''),
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 2,
    'updated_data': lambda: Unit.objects.get(pk=1).name.id,
    'column_name': 'name',
  }

class PartialUpdateUnitTest(partial_update.GenericPartialUpdateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'unit',
    'data': {'name': 8},
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 2,
    'updated_data': lambda: Unit.objects.get(pk=1).name.id,
    'column_name': 'name',
  }

class DestroyUnitTest(destroy_disabled.GenericDestroyDisabledTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'unit',
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 2,
  }
