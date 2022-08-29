from .generic_tests import (create, destroy_disabled, list, partial_update,
  retrieve, update)
from ..models import DailyValue

def create_daily_value(user, nutrient, value):
  return {'user': user, 'nutrient': nutrient, 'value': value}

class ListDailyValueTest(list.GenericListTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'daily-value',
    'username': 'user1',
    'data_length': 4,
    'column_name': 'value',
    'expected_values': [1.0, 1.0, 100.0, 10.0],
  }

class RetrieveDailyValueTest(retrieve.GenericRetrieveTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'daily-value',
    'username': 'user1',
    'pk': 1,
    'column_name': 'value',
    'expected_value': 10.0,
  }

class CreateDailyValueTest(create.GenericCreateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'daily-value',
    'data': create_daily_value(1, 1, 1000),
    'username': 'user1',
    'created_data': lambda: DailyValue.objects.get(pk=5).value,
    'column_name': 'value',
  }

class UpdateDailyValueTest(update.GenericUpdateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'daily-value',
    'data': create_daily_value(1, 1, 1000),
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 3,
    'updated_data': lambda: DailyValue.objects.get(pk=1).value,
    'column_name': 'value',
  }

class PartialUpdateDailyValueTest(partial_update.GenericPartialUpdateTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'daily-value',
    'data': {'value': 1000.0},
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 3,
    'updated_data': lambda: DailyValue.objects.get(pk=1).value,
    'column_name': 'value',
  }

class DestroyDailyValueTest(destroy_disabled.GenericDestroyDisabledTest):
  fixtures = ['test_data.json']

  test_data = {
    'url_name': 'daily-value',
    'username': 'user1',
    'pk_owned': 1,
    'pk_unowned': 3,
  }
