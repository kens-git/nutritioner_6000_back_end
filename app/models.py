from django.conf import settings
from django.db import models
from django.forms import JSONField

class UnitOfMeasure(models.Model):
  name = models.TextField(unique=True) # TODO: case insensitive
  abbreviation = models.TextField(unique=True) # TODO: case insensitive

  def __str__(self):
    return self.name

class NutrientUnit(models.Model):
  nutrient_name = models.TextField()
  unit = models.ForeignKey(UnitOfMeasure, on_delete=models.CASCADE)

class DailyValue(models.Model):
  nutrient_name = models.TextField()
  value = models.FloatField()

class Consumable(models.Model):
  fat = models.FloatField()
  saturated_fat = models.FloatField()
  trans_fat = models.FloatField()
  cholesterol = models.FloatField()
  sodium = models.FloatField()
  carbohydrates = models.FloatField()
  fibre = models.FloatField()
  sugar = models.FloatField()
  protein = models.FloatField()
  biotin = models.FloatField()
  calcium = models.FloatField()
  chromium = models.FloatField()
  copper = models.FloatField()
  folacin = models.FloatField()
  iodide = models.FloatField()
  iron = models.FloatField()
  magnesium = models.FloatField()
  manganese = models.FloatField()
  molybdenum = models.FloatField()
  niacin = models.FloatField()
  pantothenate = models.FloatField()
  phosphorous = models.FloatField()
  potassium = models.FloatField()
  riboflavin = models.FloatField()
  selenium = models.FloatField()
  thiamine = models.FloatField()
  vitamin_a = models.FloatField()
  vitamin_b6 = models.FloatField()
  vitamin_b12 = models.FloatField()
  vitamin_c = models.FloatField()
  vitamin_d = models.FloatField()
  vitamin_e = models.FloatField()
  zinc = models.FloatField()

  class Meta:
    abstract = True

class FoodCategory(models.Model):
  name = models.TextField(unique=True)

  def __str__(self):
    return self.name

class Food(Consumable):
  name = models.TextField(unique=True)
  category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
  unit = models.ForeignKey(UnitOfMeasure, on_delete=models.CASCADE)
  reference_size = models.FloatField()

  def __str__(self):
    return self.name

class Target(Consumable):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  timestamp = models.DateTimeField()
  name = models.TextField(unique=True)

  def __str__(self):
    return '{}: {}'.format(self.user, self.name)

class Intake(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  timestamp = models.DateTimeField()
  food = models.ForeignKey(Food, on_delete=models.CASCADE)
  serving_size = models.FloatField()

  def __str__(self):
    return '{}: {} of {} at {}'.format(
      self.user, self.serving_size, self.food, self.timestamp)
