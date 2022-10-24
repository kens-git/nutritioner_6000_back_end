from django.conf import settings
from django.db import models

# TODO: separate files
class UserCascade(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  class Meta:
    abstract = True

class UserProtect(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

  class Meta:
    abstract = True

class Name(UserProtect):
  name = models.CharField(unique=True, max_length=200) # TODO: case insensitive
  abbreviation = models.CharField(max_length=15)
  plural = models.CharField(max_length=200)

  def __str__(self):
    return f'{self.name} ({self.abbreviation})'

class Unit(UserProtect):
  name = models.OneToOneField(Name, on_delete=models.PROTECT)
  description = models.TextField(blank=True)

  def __str__(self):
    return f'{self.name}'

class Nutrient(UserProtect):
  name = models.OneToOneField(
    Name, on_delete=models.PROTECT, related_name='nutrient_name')
  description = models.TextField(blank=True)
  unit = models.ForeignKey(
    Unit, on_delete=models.PROTECT, related_name='nutrient_unit')
  is_macronutrient = models.BooleanField(default=False)

  def __str__(self):
    return f'{self.name} ({self.unit})'

class ConsumableCategory(UserProtect):
  name = models.OneToOneField(Name, on_delete=models.PROTECT)
  description = models.TextField(blank=True)

  def __str__(self):
    return f'{self.name}'

class ConsumableNutrient(UserProtect):
  nutrient = models.ForeignKey(Nutrient, on_delete=models.PROTECT)
  value = models.FloatField()

  def __str__(self):
    return f'{self.nutrient} ({self.value})'

class DailyValue(UserProtect):
  nutrients = models.ManyToManyField(ConsumableNutrient)

  def __str__(self):
    return f'{self.nutrient} ({self.value})'

class Consumable(UserProtect):
  name = models.TextField(unique=True)
  category = models.ForeignKey(ConsumableCategory, on_delete=models.PROTECT)
  unit = models.ForeignKey(Unit, related_name='unit', on_delete=models.PROTECT)
  reference_size = models.FloatField()
  nutrients = models.ManyToManyField(ConsumableNutrient)

  def __str__(self):
    return f'{self.name}'

class Target(UserCascade):
  timestamp = models.DateTimeField()
  name = models.CharField(unique=True, max_length=200)
  description = models.TextField(blank=True)
  nutrients = models.ManyToManyField(ConsumableNutrient)

  def __str__(self):
    return f'{self.user}: {self.name}'

class Intake(UserCascade):
  timestamp = models.DateTimeField()
  consumable = models.ForeignKey(Consumable, on_delete=models.PROTECT)
  serving_size = models.FloatField()

  def __str__(self):
    return f'{self.user}, {self.timestamp}, {self.consumable}, {self.serving_size}'
