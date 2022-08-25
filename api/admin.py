from django.contrib import admin
from .models import (Consumable, ConsumableCategory, ConsumableNutrient,
  DailyValue, Intake, Name, Nutrient, Target, Unit)

admin.site.register(Consumable)
admin.site.register(ConsumableCategory)
admin.site.register(ConsumableNutrient)
admin.site.register(DailyValue)
admin.site.register(Intake)
admin.site.register(Name)
admin.site.register(Nutrient)
admin.site.register(Target)
admin.site.register(Unit)
