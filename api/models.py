from django.conf import settings
from django.db import models

class Name(models.Model):
  name = models.CharField(unique=True, max_length=200) # TODO: case insensitive
  abbreviation = models.CharField(max_length=15)
  plural = models.CharField(max_length=50)

class Nutrient(models.Model):
  name = models.ForeignKey(
    Name, on_delete=models.PROTECT, related_name='nutreint_name')
  description = models.TextField()
  unit = models.ForeignKey(
    Name, on_delete=models.PROTECT, related_name='nutrient_unit')

class DailyValue(models.Model):
  # TODO: instead of nullable, maybe add admin user as creator
  user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE, null=True, blank=True)
  nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
  value = models.FloatField()

class ConsumableCategory(models.Model):
  name = models.ForeignKey(Name, on_delete=models.PROTECT)
  description = models.TextField()

class Consumable(models.Model):
  name = models.TextField()
  category = models.ForeignKey(ConsumableCategory, on_delete=models.PROTECT)
  unit = models.ForeignKey(Name, on_delete=models.PROTECT)
  reference_size = models.FloatField()
  nutrients = models.ManyToManyField(Nutrient)

class Target(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  timestamp = models.DateTimeField()
  name = models.CharField(unique=True, max_length=200)
  description = models.TextField()
  nutrients = models.ManyToManyField(Nutrient)

class Intake(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  timestamp = models.DateTimeField()
  consumable = models.ForeignKey(Consumable, on_delete=models.PROTECT)
  serving_size = models.FloatField()
