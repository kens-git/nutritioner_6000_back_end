from .generic_tests import (create, destroy_disabled, list, partial_update,
  retrieve, update)
from ..models import Name

def create_name(user, name, abbreviation, plural):
  return {'user': user, 'name': name, 'abbreviation': abbreviation,
    'plural': plural}

class ListNameTest(list.GenericListTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'name',
    'username': 'user1',
    'data_length': 8,
    'column_name': 'name',
    'expected_values': ['Dairy', 'Meat', 'Biotin', 'Calcium', 'Microgram',
      'Milligram', 'Gram', 'Candy'],
  }

class RetrieveNameTest(retrieve.GenericRetrieveTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'name',
    'username': 'user1',
    'pk': 1,
    'column_name': 'name',
    'expected_value': 'Dairy',
  }

class CreateNameTest(create.GenericCreateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'name',
    'data': create_name(1, 'Test Name', 'T. N.', 'Test Name'),
    'username': 'user1',
    'created_data': lambda: Name.objects.get(pk=9).name,
    'column_name': 'name',
  }

# TODO: duplicate name test

class UpdateNameTest(update.GenericUpdateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'name',
    'data': create_name(1, 'Test Name', 'T. N.', 'Test Name'),
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 2,
    'updated_data': lambda: Name.objects.get(pk=1).name,
    'column_name': 'name',
  }

class PartialUpdateNameTest(partial_update.GenericPartialUpdateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'name',
    'data': {'name': 'New Name'},
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 2,
    'updated_data': lambda: Name.objects.get(pk=1).name,
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
