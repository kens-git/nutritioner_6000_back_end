from django.conf import settings
from django.db import models
from django.forms import JSONField

class UnitOfMeasure(models.Model):
  name = models.TextField(unique=True) # TODO: case insensitive
  abbreviation = models.TextField(unique=True) # TODO: case insensitive

class Nutrient(models.Model):
  name = models.TextField(unique=True) # TODO: case insensitive
  unit = models.ForeignKey(UnitOfMeasure, on_delete=models.CASCADE) # TODO: cascade or nothing?
  daily_value = models.FloatField(default=0)

class Consumable(models.Model):
  # stores a dictionary of Nutrient ids and values, e.g. {nutrient_id: nutrient_amount, ...}
  nutrients = JSONField() # TODO: custom field instead?

  class Meta:
    abstract = True

class UserConsumable(Consumable):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  timestamp = models.DateTimeField()

class FoodCategory(models.Model):
  name = models.TextField(unique=True)

class Food(Consumable):
  name = models.TextField(unique=True)
  category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
  unit = models.ForeignKey(UnitOfMeasure, on_delete=models.CASCADE)

class Target(Consumable):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  timestamp = models.DateTimeField()
  name = models.TextField(unique=True)

class Intake(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  timestamp = models.DateTimeField()
  food = models.ForeignKey(Food, on_delete=models.CASCADE)
  serving_size = models.FloatField()
