
from rest_framework import serializers
from .models import (Consumable, ConsumableCategory, ConsumableNutrient,
  DailyValue, Intake, Name, Nutrient, Target)

class ConsumableSerializer(serializers.ModelSerializer):
  class Meta:
    model = Consumable
    fields = '__all__'

class ConsumableCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = ConsumableCategory
    fields = '__all__'

class ConsumableNutrientSerializer(serializers.ModelSerializer):
  class Meta:
    model = ConsumableNutrient
    fields = '__all__'

class DailyValueSerializer(serializers.ModelSerializer):
  class Meta:
    model = DailyValue
    fields = '__all__'

class IntakeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Intake
    fields = '__all__'

class NameSerializer(serializers.ModelSerializer):
  class Meta:
    model = Name
    fields = '__all__'

class NutrientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Nutrient
    fields = '__all__'

class TargetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Target
    fields = '__all__'
