from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('intake/', views.intake, name='intake'),
  path('food/', views.food, name='food'),
  path('target/', views.target, name='target'),
  path('food_category/', views.food_category, name='food_category'),
]
