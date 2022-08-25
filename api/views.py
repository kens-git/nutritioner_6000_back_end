from rest_framework import mixins, viewsets
from .models import (Consumable, ConsumableCategory, ConsumableNutrient,
  DailyValue, Intake, Name, Nutrient, Target)
from .permissions import (OWNER_ACTIONS, OWNER_UPDATE_ACTIONS,
  get_permissions as get_perms)
from .serializers import (ConsumableSerializer, ConsumableCategorySerializer,
  ConsumableNutrientSerializer, DailyValueSerializer, IntakeSerializer,
  NameSerializer, NutrientSerializer, TargetSerializer)

class OwnerUpdateViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
  pass

# TODO: define proper querysets
class ConsumableViewSet(OwnerUpdateViewSet):
  serializer_class = ConsumableSerializer
  queryset = Consumable.objects.all()

  def get_permissions(self):
    return get_perms(self.action, OWNER_UPDATE_ACTIONS)

class ConsumableCategoryViewSet(OwnerUpdateViewSet):
  serializer_class = ConsumableCategorySerializer
  queryset = ConsumableCategory.objects.all()

  def get_permissions(self):
    return get_perms(self.action, OWNER_UPDATE_ACTIONS)

class ConsumableNutrientViewSet(OwnerUpdateViewSet):
  serializer_class = ConsumableNutrientSerializer
  queryset = ConsumableNutrient.objects.all()

  def get_permissions(self):
    return get_perms(self.action, OWNER_UPDATE_ACTIONS)

class DailyValueViewSet(OwnerUpdateViewSet):
  serializer_class = DailyValueSerializer
  queryset = DailyValue.objects.all()

  def get_permissions(self):
    return get_perms(self.action, OWNER_UPDATE_ACTIONS)

class IntakeViewSet(viewsets.ModelViewSet):
  serializer_class = IntakeSerializer
  queryset = Intake.objects.all()

  def get_permissions(self):
    return get_perms(self.action, OWNER_ACTIONS)

class NameViewSet(OwnerUpdateViewSet):
  serializer_class = NameSerializer
  queryset = Name.objects.all()

  def get_permissions(self):
    return get_perms(self.action, OWNER_UPDATE_ACTIONS)

class NutrientViewSet(OwnerUpdateViewSet):
  serializer_class = NutrientSerializer
  queryset = Nutrient.objects.all()

  def get_permissions(self):
    return get_perms(self.action, OWNER_UPDATE_ACTIONS)

class TargetViewSet(viewsets.ModelViewSet):
  serializer_class = TargetSerializer
  queryset = Target.objects.all()

  def get_permissions(self):
    return get_perms(self.action, OWNER_ACTIONS)
