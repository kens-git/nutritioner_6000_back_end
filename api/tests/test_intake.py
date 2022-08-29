from datetime import datetime
from .generic_tests import (create, destroy, list, partial_update,
  retrieve, update)
from ..models import Intake

def create_intake(user, timestamp, consumable, serving_size):
  return {'user': user, 'timestamp': timestamp, 'consumable': consumable,
    'serving_size': serving_size}

# TODO: tests for current user only
class ListIntakeTest(list.GenericListTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'intake',
    'username': 'user1',
    'data_length': 4,
    'column_name': 'user',
    'expected_values': [1, 1, 2, 2],
  }

class RetrieveIntakeTest(retrieve.GenericRetrieveTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'intake',
    'username': 'user1',
    'pk': 1,
    'column_name': 'user',
    'expected_value': 1,
  }

class CreateIntakeTest(create.GenericCreateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'intake',
    'data': create_intake(1, datetime.now(), 1, 100),
    'username': 'user1',
    'created_data': lambda: Intake.objects.get(pk=5).serving_size,
    'column_name': 'serving_size',
  }

# TODO: duplicate name test

class UpdateIntakeTest(update.GenericUpdateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'intake',
    'data': create_intake(1, datetime.now(), 1, 10000),
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 3,
    'updated_data': lambda: Intake.objects.get(pk=1).serving_size,
    'column_name': 'serving_size',
  }

class PartialUpdateIntakeTest(partial_update.GenericPartialUpdateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'intake',
    'data': {'serving_size': 1000},
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 3,
    'updated_data': lambda: Intake.objects.get(pk=1).serving_size,
    'column_name': 'serving_size',
  }

class DestroyConsumableTest(destroy.GenericDestroyTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'intake',
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 3,
  }
