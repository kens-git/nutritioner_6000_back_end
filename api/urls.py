from rest_framework import routers
from .views import (ConsumableViewSet, ConsumableCategoryViewSet,
  ConsumableNutrientViewSet, DailyValueViewSet, IntakeViewSet,
  NameViewSet, NutrientViewSet, TargetViewSet)

router = routers.SimpleRouter()
router.register(r'consumable', ConsumableViewSet, 'consumable')
router.register(r'consumable-category', ConsumableCategoryViewSet,
  'consumable-category')
router.register(r'consumable-nutrient', ConsumableNutrientViewSet,
  'consumable-nutrient')
router.register(r'daily-value', DailyValueViewSet, 'daily-value')
router.register(r'intake', IntakeViewSet, 'intake')
router.register(r'name', NameViewSet, 'name')
router.register(r'nutrient', NutrientViewSet, 'nutrient')
router.register(r'target', TargetViewSet, 'target')
urlpatterns = router.urls
