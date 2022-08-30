from datetime import datetime
from rest_framework import status
from .generic_tests import (create, destroy, list, partial_update,
  retrieve, update)
from ..models import Target

def create_target(user, timestamp, name, description, nutrients):
  return {'user': user, 'timestamp': timestamp, 'name': name,
    'description': description, 'nutrients': nutrients}

class ListTargetTest(list.GenericListTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'target',
    'username': 'user1',
    'data_length': 1,
    'column_name': 'name',
    'expected_values': ['Current'],
  }

class RetrieveTargetTest(retrieve.GenericRetrieveTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'target',
    'username': 'user1',
    'pk': 1,
    'column_name': 'name',
    'expected_value': 'Current',
  }

# TODO: retrieve unowned

class CreateTargetTest(create.GenericCreateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'target',
    'data': create_target(1, datetime.now(), 'New Name', '', [1, 2]),
    'username': 'user1',
    'created_data': lambda: Target.objects.get(pk=3).name,
    'column_name': 'name',
  }

# TODO: duplicate name test

class UpdateTargetTest(update.GenericUpdateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'target',
    'data': create_target(1, datetime.now(), 'New Name', '', [1, 2]),
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 2,
    'updated_data': lambda: Target.objects.get(pk=1).name,
    'column_name': 'name',
    'denied_status': status.HTTP_404_NOT_FOUND,
  }

class PartialUpdateTargetTest(partial_update.GenericPartialUpdateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'target',
    'data': {'name': 'New Name'},
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 2,
    'updated_data': lambda: Target.objects.get(pk=1).name,
    'column_name': 'name',
    'denied_status': status.HTTP_404_NOT_FOUND,
  }

class DestroyTargetTest(destroy.GenericDestroyTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'target',
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 2,
    'denied_status': status.HTTP_404_NOT_FOUND,
  }
