from datetime import datetime
from django.forms.models import model_to_dict
from rest_framework import mixins, status, viewsets
from rest_framework.authtoken import views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import (Consumable, ConsumableCategory, ConsumableNutrient,
  DailyValue, Intake, Name, Nutrient, Target, Unit)
from .permissions import (OWNER_ACTIONS, OWNER_UPDATE_ACTIONS,
  get_permissions as get_perms)
from .serializers import (ConsumableSerializer, ConsumableCategorySerializer,
  ConsumableNutrientSerializer, DailyValueSerializer, IntakeSerializer,
  NameSerializer, NutrientSerializer, TargetSerializer, UnitSerializer)

class OwnerUpdateViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
  def get_permissions(self):
    return get_perms(self.action, OWNER_UPDATE_ACTIONS)

class ConsumableViewSet(OwnerUpdateViewSet):
  serializer_class = ConsumableSerializer
  queryset = Consumable.objects.all()

class ConsumableCategoryViewSet(OwnerUpdateViewSet):
  serializer_class = ConsumableCategorySerializer
  queryset = ConsumableCategory.objects.all()

class ConsumableNutrientViewSet(OwnerUpdateViewSet):
  serializer_class = ConsumableNutrientSerializer
  queryset = ConsumableNutrient.objects.all()

class DailyValueViewSet(OwnerUpdateViewSet):
  serializer_class = DailyValueSerializer

  def get_permissions(self):
    return get_perms(self.action, OWNER_ACTIONS)

  def get_queryset(self):
    query_set = DailyValue.objects.filter(user=self.request.user)
    getLatest = self.request.query_params.get('getLatest')
    if getLatest:
      return query_set.order_by('-id')[0:1]
    return query_set

class IntakeViewSet(viewsets.ModelViewSet):
  serializer_class = IntakeSerializer

  def get_permissions(self):
    return get_perms(self.action, OWNER_ACTIONS)

  def get_queryset(self):
    start = self.request.query_params.get('start') or datetime.min
    end = self.request.query_params.get('end') or datetime.max
    return Intake.objects.filter(
      user=self.request.user).filter(timestamp__range=(start, end))

class NameViewSet(OwnerUpdateViewSet):
  serializer_class = NameSerializer
  queryset = Name.objects.all()

class NutrientViewSet(OwnerUpdateViewSet):
  serializer_class = NutrientSerializer
  queryset = Nutrient.objects.all()

class TargetViewSet(viewsets.ModelViewSet):
  serializer_class = TargetSerializer

  def get_permissions(self):
    return get_perms(self.action, OWNER_ACTIONS)

  def get_queryset(self):
    query_set = Target.objects.filter(user=self.request.user)
    getLatest = self.request.query_params.get('getLatest')
    if getLatest:
      return query_set.order_by('-id')[0:1]
    return query_set

class UnitViewSet(OwnerUpdateViewSet):
  serializer_class = UnitSerializer
  queryset = Unit.objects.all()

class ObtainTokenView(views.ObtainAuthToken):
  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'user_id': user.pk})
