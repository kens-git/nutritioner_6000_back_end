from django.conf import settings
from django.db import models

class Name(models.Model):
  name = models.CharField(unique=True, max_length=200) # TODO: case insensitive
  abbreviation = models.CharField(max_length=15)
  plural = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.name} ({self.abbreviation})'

class Nutrient(models.Model):
  name = models.ForeignKey(
    Name, on_delete=models.PROTECT, related_name='nutrient_name')
  description = models.TextField(blank=True)
  unit = models.ForeignKey(
    Name, on_delete=models.PROTECT, related_name='nutrient_unit')

  def __str__(self):
    return f'{self.name} ({self.unit})'

class DailyValue(models.Model):
  # TODO: instead of nullable, maybe add admin user as creator
  user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE, null=True, blank=True)
  nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
  value = models.FloatField()

  def __str__(self):
    return f'{self.nutrient} ({self.value})'

class ConsumableCategory(models.Model):
  name = models.ForeignKey(Name, on_delete=models.PROTECT)
  description = models.TextField(blank=True)

  def __str__(self):
    return f'{self.name}'

class ConsumableNutrient(models.Model):
  nutrient = models.ForeignKey(Nutrient, on_delete=models.PROTECT)
  value = models.FloatField()

  def __str__(self):
    return f'{self.nutrient} ({self.value})'

class Consumable(models.Model):
  name = models.TextField()
  category = models.ForeignKey(ConsumableCategory, on_delete=models.PROTECT)
  unit = models.ForeignKey(Name, on_delete=models.PROTECT)
  reference_size = models.FloatField()
  nutrients = models.ManyToManyField(ConsumableNutrient)

  def __str__(self):
    return f'{self.name}'

class Target(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  timestamp = models.DateTimeField()
  name = models.CharField(unique=True, max_length=200)
  description = models.TextField(blank=True)
  nutrients = models.ManyToManyField(Nutrient)

  def __str__(self):
    return f'{self.user}: {self.description}'

class Intake(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  timestamp = models.DateTimeField()
  consumable = models.ForeignKey(Consumable, on_delete=models.PROTECT)
  serving_size = models.FloatField()

  def __str__(self):
    return f'{self.user}, {self.timestamp}, {self.consumable}, {self.serving_size}'
