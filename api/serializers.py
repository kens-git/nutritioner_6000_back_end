from rest_framework import serializers
from .models import (Consumable, ConsumableCategory, ConsumableNutrient,
  DailyValue, Intake, Name, Nutrient, Target, Unit)

class NameSerializer(serializers.ModelSerializer):
  class Meta:
    model = Name
    fields = '__all__'

class ConsumableCategorySerializer(serializers.ModelSerializer):
  name = NameSerializer()
  
  def to_internal_value(self, data):
    self.fields['name'] = serializers.PrimaryKeyRelatedField(
      queryset=Name.objects.all())
    return super(
      ConsumableCategorySerializer, self).to_internal_value(data)

  class Meta:
    model = ConsumableCategory
    fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
  name = NameSerializer()

  def to_internal_value(self, data):
    self.fields['name'] = serializers.PrimaryKeyRelatedField(
      queryset=Name.objects.all())
    return super(UnitSerializer, self).to_internal_value(data)

  class Meta:
    model = Unit
    fields = '__all__'

class NutrientSerializer(serializers.ModelSerializer):
  name = NameSerializer()
  unit = UnitSerializer()

  def to_internal_value(self, data):
    self.fields['name'] = serializers.PrimaryKeyRelatedField(
      queryset=Name.objects.all())
    self.fields['unit'] = serializers.PrimaryKeyRelatedField(
      queryset=Unit.objects.all())
    return super(NutrientSerializer, self).to_internal_value(data)

  class Meta:
    model = Nutrient
    fields = '__all__'

class ConsumableNutrientSerializer(serializers.ModelSerializer):
  nutrient = NutrientSerializer()

  def to_internal_value(self, data):
    self.fields['nutrient'] = serializers.PrimaryKeyRelatedField(
      queryset=Nutrient.objects.all())
    return super(ConsumableNutrientSerializer, self).to_internal_value(data)

  class Meta:
    model = ConsumableNutrient
    fields = '__all__'

class ConsumableSerializer(serializers.ModelSerializer):
  category = ConsumableCategorySerializer()
  unit = UnitSerializer()
  nutrients = ConsumableNutrientSerializer(many=True)

  def create(self, validated_data):
    consumable = Consumable.objects.create(name=validated_data['name'],
      category=validated_data['category'], unit=validated_data['unit'],
      reference_size=validated_data['reference_size'], user=validated_data['user'])
    for cn in validated_data['nutrients']:
      created_cn = ConsumableNutrient.objects.create(nutrient=cn['nutrient'],
        value=cn['value'], user=validated_data['user'])
      consumable.nutrients.add(created_cn.pk)
    return consumable

  def to_internal_value(self, data):
    self.fields['category'] = serializers.PrimaryKeyRelatedField(
      queryset=ConsumableCategory.objects.all())
    self.fields['unit'] = serializers.PrimaryKeyRelatedField(
      queryset=Unit.objects.all())
    for nutrient in data['nutrients']:
      nutrient['user'] = self.context['request'].user.pk
    return super(ConsumableSerializer, self).to_internal_value(data)

  class Meta:
    model = Consumable
    fields = '__all__'

class DailyValueSerializer(serializers.ModelSerializer):
  nutrients = ConsumableNutrientSerializer(many=True)

  def create(self, validated_data):
    values = DailyValue.objects.create(
      user=validated_data['user'])
    for cn in validated_data['nutrients']:
      created_cn = ConsumableNutrient.objects.create(
        nutrient=cn['nutrient'],
        value=cn['value'], user=validated_data['user'])
      values.nutrients.add(created_cn.pk)
    return values

  def to_internal_value(self, data):
    for nutrient in data['nutrients']:
      nutrient['user'] = self.context['request'].user.pk
    return super(DailyValueSerializer, self).to_internal_value(data)

  class Meta:
    model = DailyValue
    fields = '__all__'

class IntakeSerializer(serializers.ModelSerializer):
  consumable = ConsumableSerializer()

  def to_internal_value(self, data):
    self.fields['consumable'] = serializers.PrimaryKeyRelatedField(
      queryset=Consumable.objects.all())
    return super(IntakeSerializer, self).to_internal_value(data)

  class Meta:
    model = Intake
    fields = '__all__'

class TargetSerializer(serializers.ModelSerializer):
  nutrients = ConsumableNutrientSerializer(many=True)

  def create(self, validated_data):
    target = Target.objects.create(timestamp=validated_data['timestamp'],
      name=validated_data['name'], description=validated_data['description'],
      user=validated_data['user'])
    for cn in validated_data['nutrients']:
      created_cn = ConsumableNutrient.objects.create(nutrient=cn['nutrient'],
        value=cn['value'], user=validated_data['user'])
      target.nutrients.add(created_cn.pk)
    return target

  def to_internal_value(self, data):
    for nutrient in data['nutrients']:
      nutrient['user'] = self.context['request'].user.pk
    return super(TargetSerializer, self).to_internal_value(data)

  class Meta:
    model = Target
    fields = '__all__'
