from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .models import (Consumable, ConsumableCategory, ConsumableNutrient,
  DailyValue, Intake, Name, Nutrient, Target)
from .serializers import (ConsumableSerializer, ConsumableCategorySerializer,
  ConsumableNutrientSerializer, DailyValueSerializer, IntakeSerializer,
  NameSerializer, NutrientSerializer, TargetSerializer)

OWNER_UPDATE_ACTIONS = ('update', 'partial_update')
OWNER_ACTIONS = ('update', 'partial_update', 'destroy')

class ObjectOwnerPermission(permissions.BasePermission):
  def has_permission(self, request, view):
    return True

  def has_object_permission(self, request, view, obj):
    return obj.user == request.user

def get_permissions(action, acceptable_actions):
  if action in acceptable_actions:
    return [permissions.IsAuthenticated(), ObjectOwnerPermission()]
  return [permissions.IsAuthenticated()]

# TODO: define proper querysets
# TODO: move authentication_classes to settings.py, change to Token
class ConsumableViewSet(viewsets.ModelViewSet):
  serializer_class = ConsumableSerializer
  queryset = Consumable.objects.all()
  authentication_classes = [SessionAuthentication]

  def get_permissions(self):
    return get_permissions(self.action, OWNER_UPDATE_ACTIONS)

class ConsumableCategoryViewSet(viewsets.ModelViewSet):
  serializer_class = ConsumableCategorySerializer
  queryset = ConsumableCategory.objects.all()
  authentication_classes = [SessionAuthentication]

  def get_permissions(self):
    return get_permissions(self.action, OWNER_UPDATE_ACTIONS)

class ConsumableNutrientViewSet(viewsets.ModelViewSet):
  serializer_class = ConsumableNutrientSerializer
  queryset = ConsumableNutrient.objects.all()
  authentication_classes = [SessionAuthentication]

  def get_permissions(self):
    return get_permissions(self.action, OWNER_UPDATE_ACTIONS)

class DailyValueViewSet(viewsets.ModelViewSet):
  serializer_class = DailyValueSerializer
  queryset = DailyValue.objects.all()
  authentication_classes = [SessionAuthentication]

  def get_permissions(self):
    return get_permissions(self.action, OWNER_UPDATE_ACTIONS)

class IntakeViewSet(viewsets.ModelViewSet):
  serializer_class = IntakeSerializer
  queryset = Intake.objects.all()
  authentication_classes = [SessionAuthentication]

  def get_permissions(self):
    return get_permissions(self.action, OWNER_ACTIONS)

class NameViewSet(viewsets.ModelViewSet):
  serializer_class = NameSerializer
  queryset = Name.objects.all()
  authentication_classes = [SessionAuthentication]

  def get_permissions(self):
    return get_permissions(self.action, OWNER_UPDATE_ACTIONS)

class NutrientViewSet(viewsets.ModelViewSet):
  serializer_class = NutrientSerializer
  queryset = Nutrient.objects.all()
  authentication_classes = [SessionAuthentication]

  def get_permissions(self):
    return get_permissions(self.action, OWNER_UPDATE_ACTIONS)

class TargetViewSet(viewsets.ModelViewSet):
  serializer_class = TargetSerializer
  queryset = Target.objects.all()
  authentication_classes = [SessionAuthentication]

  def get_permissions(self):
    return get_permissions(self.action, OWNER_ACTIONS)
