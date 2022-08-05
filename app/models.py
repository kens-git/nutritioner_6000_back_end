from django.conf import settings
from django.db import models
from django.forms import JSONField

class Abbreviation(models.Model):
  name = models.TextField(unique=True) # TODO: case insensitive
  abbreviation = models.TextField()

class UnitOfMeasure(models.Model):
  name = models.TextField(unique=True, blank=False)

class Nutrient(models.Model):
  name = models.TextField(unique=True)
  abbreviation = models.ForeignKey(Abbreviation, on_delete=models.PROTECT)
  description = models.TextField()
  unit_of_measure = models.ForeignKey(UnitOfMeasure, on_delete=models.PROTECT)

class DailyValue(models.Model):
  user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE, null=True, blank=True)
  nutrient = models.OneToOneField(Nutrient, unique=True, on_delete=models.CASCADE)
  value = models.FloatField()

class ConsumableCategory(models.Model):
  name = models.TextField()
  abbreviation = models.ForeignKey(Abbreviation, on_delete=models.PROTECT)
  description = models.TextField()

class Consumable(models.Model):
  name = models.TextField()
  category = models.ForeignKey(ConsumableCategory, on_delete=models.PROTECT)
  unit = models.ForeignKey(UnitOfMeasure, on_delete=models.PROTECT)
  reference_size = models.FloatField()
  nutrients = models.ManyToManyField(Nutrient)

class Target(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  timestamp = models.DateTimeField()
  name = models.TextField()
  description = models.TextField()
  nutrients = models.ManyToManyField(Nutrient)

class Intake(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  timestamp = models.DateTimeField()
  consumable = models.ForeignKey(Consumable, on_delete=models.PROTECT)
  serving_size = models.FloatField()
