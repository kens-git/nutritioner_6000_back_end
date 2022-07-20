from django.conf import settings
from django.db import models
from django.forms import JSONField

NUTRIENT_DAILY_VALUES = {
  "biotin": 30,
  "calcium": 1100,
  "chromium": 120,
  "copper": 2,
  "folacin": 220,
  "iodide": 160,
  "iron": 14,
  "magnesium": 250,
  "manganese": 2,
  "molybdenum": 75,
  "niacin": 23,
  "pantothenate": 7,
  "phosphorous": 1100,
  "potassium": 3500,
  "riboflavin": 1.6,
  "selenium": 50,
  "thiamine": 1.3,
  "vitamin_a": 1000,
  "vitamin_b6": 1.8,
  "vitamin_b12": 2,
  "vitamin_c": 60,
  "vitamin_d": 5,
  "vitamin_e": 10,
  "zinc": 9,
}

class UnitOfMeasure(models.Model):
  name = models.TextField(unique=True) # TODO: case insensitive
  abbreviation = models.TextField(unique=True) # TODO: case insensitive

  def __str__(self):
    return self.name

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
