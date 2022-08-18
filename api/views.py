from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .models import (Consumable, ConsumableCategory, ConsumableNutrient,
  DailyValue, Intake, Name, Nutrient, Target)
from .permissions import (OWNER_ACTIONS, OWNER_UPDATE_ACTIONS,
  get_permissions as get_perms)
from .serializers import (ConsumableSerializer, ConsumableCategorySerializer,
  ConsumableNutrientSerializer, DailyValueSerializer, IntakeSerializer,
  NameSerializer, NutrientSerializer, TargetSerializer)

# TODO: define proper querysets
# TODO: move authentication_classes to settings.py, change to Token
class ConsumableViewSet(viewsets.ModelViewSet):
  serializer_class = ConsumableSerializer
  queryset = Consumable.objects.all()
  authentication_classes = [SessionAuthentication]

  def get_permissions(self):
    return get_perms(self.action, OWNER_UPDATE_ACTIONS)

class ConsumableCategoryViewSet(viewsets.ModelViewSet):
  serializer_class = ConsumableCategorySerializer
  queryset = ConsumableCategory.objects.all()
  authentication_classes = [SessionAuthentication]

  def get_permissions(self):
    return get_perms(self.action, OWNER_UPDATE_ACTIONS)

class ConsumableNutrientViewSet(viewsets.ModelViewSet):
  serializer_class = ConsumableNutrientSerializer
  queryset = ConsumableNutrient.objects.all()
  authentication_classes = [SessionAuthentication]

  def get_permissions(self):
    return get_perms(self.action, OWNER_UPDATE_ACTIONS)

class DailyValueViewSet(viewsets.ModelViewSet):
  serializer_class = DailyValueSerializer
  queryset = DailyValue.objects.all()
  authentication_classes = [SessionAuthentication]

  def get_permissions(self):
    return get_perms(self.action, OWNER_UPDATE_ACTIONS)

class IntakeViewSet(viewsets.ModelViewSet):
  serializer_class = IntakeSerializer
  queryset = Intake.objects.all()
  authentication_classes = [SessionAuthentication]

  def get_permissions(self):
    return get_perms(self.action, OWNER_ACTIONS)

class NameViewSet(viewsets.ModelViewSet):
  serializer_class = NameSerializer
  queryset = Name.objects.all()
  authentication_classes = [SessionAuthentication]

  def get_permissions(self):
    return get_perms(self.action, OWNER_UPDATE_ACTIONS)

class NutrientViewSet(viewsets.ModelViewSet):
  serializer_class = NutrientSerializer
  queryset = Nutrient.objects.all()
  authentication_classes = [SessionAuthentication]

  def get_permissions(self):
    return get_perms(self.action, OWNER_UPDATE_ACTIONS)

class TargetViewSet(viewsets.ModelViewSet):
  serializer_class = TargetSerializer
  queryset = Target.objects.all()
  authentication_classes = [SessionAuthentication]

  def get_permissions(self):
    return get_perms(self.action, OWNER_ACTIONS)
