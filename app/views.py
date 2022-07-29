from copyreg import add_extension
from datetime import datetime, date, time
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods, require_GET
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Food, Intake
from .forms.add_food import AddFood
from .forms.add_intake import AddIntake
from .forms.get_daily_intake import GetDailyIntake

# TODO: move
def empty_nutrient_dict():
  return {
    'fat': 0,
    'saturated_fat': 0,
    'trans_fat': 0,
    'cholesterol': 0,
    'sodium': 0,
    'carbohydrates': 0,
    'fibre': 0,
    'sugar': 0,
    'protein': 0,
    'biotin': 0,
    'calcium': 0,
    'chromium': 0,
    'copper': 0,
    'folacin': 0,
    'iodide': 0,
    'iron': 0,
    'magnesium': 0,
    'manganese': 0,
    'molybdenum': 0,
    'niacin': 0,
    'pantothenate': 0,
    'phosphorous': 0,
    'potassium': 0,
    'riboflavin': 0,
    'selenium': 0,
    'thiamine': 0,
    'vitamin_a': 0,
    'vitamin_b6': 0,
    'vitamin_b12': 0,
    'vitamin_c': 0,
    'vitamin_d': 0,
    'vitamin_e': 0,
    'zinc': 0,
  }

# TODO: move
def get_intake(selected_date: date):
  # TODO
  start_time = datetime.combine(selected_date, time(00, 00, 00))
  end_time = datetime.combine(selected_date, time(23, 59, 59))
  intake_data = []
  intake = Intake.objects.filter(timestamp__range=(start_time, end_time)).all()
  total = empty_nutrient_dict()
  for i in intake:
    intake_data.append({
      'food_name': i.food.name,
      'category': i.food.category,
      'serving_size': i.serving_size,
      'unit': i.food.unit.abbreviation,
      'fat': i.food.fat * (i.serving_size / i.food.reference_size),
      'saturated_fat': i.food.saturated_fat * (i.serving_size / i.food.reference_size),
      'trans_fat': i.food.trans_fat * (i.serving_size / i.food.reference_size),
      'cholesterol': i.food.cholesterol * (i.serving_size / i.food.reference_size),
      'sodium': i.food.sodium * (i.serving_size / i.food.reference_size),
      'carbohydrates': i.food.carbohydrates * (i.serving_size / i.food.reference_size),
      'fibre': i.food.fibre * (i.serving_size / i.food.reference_size),
      'sugar': i.food.sugar * (i.serving_size / i.food.reference_size),
      'protein': i.food.protein * (i.serving_size / i.food.reference_size),
      'biotin': i.food.biotin * (i.serving_size / i.food.reference_size),
      'calcium': i.food.calcium * (i.serving_size / i.food.reference_size),
      'chromium': i.food.chromium * (i.serving_size / i.food.reference_size),
      'copper': i.food.copper * (i.serving_size / i.food.reference_size),
      'folacin': i.food.folacin * (i.serving_size / i.food.reference_size),
      'iodide': i.food.iodide * (i.serving_size / i.food.reference_size),
      'iron': i.food.iron * (i.serving_size / i.food.reference_size),
      'magnesium': i.food.magnesium * (i.serving_size / i.food.reference_size),
      'manganese': i.food.manganese * (i.serving_size / i.food.reference_size),
      'molybdenum': i.food.molybdenum * (i.serving_size / i.food.reference_size),
      'niacin': i.food.niacin * (i.serving_size / i.food.reference_size),
      'pantothenate': i.food.pantothenate * (i.serving_size / i.food.reference_size),
      'phosphorous': i.food.phosphorous * (i.serving_size / i.food.reference_size),
      'potassium': i.food.potassium * (i.serving_size / i.food.reference_size),
      'riboflavin': i.food.riboflavin * (i.serving_size / i.food.reference_size),
      'selenium': i.food.selenium * (i.serving_size / i.food.reference_size),
      'thiamine': i.food.thiamine * (i.serving_size / i.food.reference_size),
      'vitamin_a': i.food.vitamin_a * (i.serving_size / i.food.reference_size),
      'vitamin_b6': i.food.vitamin_b6 * (i.serving_size / i.food.reference_size),
      'vitamin_b12': i.food.vitamin_b12 * (i.serving_size / i.food.reference_size),
      'vitamin_c': i.food.vitamin_c * (i.serving_size / i.food.reference_size),
      'vitamin_d': i.food.vitamin_d * (i.serving_size / i.food.reference_size),
      'vitamin_e': i.food.vitamin_e * (i.serving_size / i.food.reference_size),
      'zinc': i.food.zinc * (i.serving_size / i.food.reference_size),
    })
    total['fat'] += intake_data[-1]['fat']
    total['saturated_fat'] += intake_data[-1]['saturated_fat']
    total['trans_fat'] += intake_data[-1]['trans_fat']
    total['cholesterol'] += intake_data[-1]['cholesterol']
    total['sodium'] += intake_data[-1]['sodium']
    total['carbohydrates'] += intake_data[-1]['carbohydrates']
    total['fibre'] += intake_data[-1]['fibre']
    total['sugar'] += intake_data[-1]['sugar']
    total['protein'] += intake_data[-1]['protein']
    total['biotin'] += intake_data[-1]['biotin']
    total['calcium'] += intake_data[-1]['calcium']
    total['chromium'] += intake_data[-1]['chromium']
    total['copper'] += intake_data[-1]['copper']
    total['folacin'] += intake_data[-1]['folacin']
    total['iodide'] += intake_data[-1]['iodide']
    total['iron'] += intake_data[-1]['iron']
    total['magnesium'] += intake_data[-1]['magnesium']
    total['manganese'] += intake_data[-1]['manganese']
    total['molybdenum'] += intake_data[-1]['molybdenum']
    total['niacin'] += intake_data[-1]['niacin']
    total['pantothenate'] += intake_data[-1]['pantothenate']
    total['phosphorous'] += intake_data[-1]['phosphorous']
    total['potassium'] += intake_data[-1]['potassium']
    total['riboflavin'] += intake_data[-1]['riboflavin']
    total['selenium'] += intake_data[-1]['selenium']
    total['thiamine'] += intake_data[-1]['thiamine']
    total['vitamin_a'] += intake_data[-1]['vitamin_a']
    total['vitamin_b6'] += intake_data[-1]['vitamin_b6']
    total['vitamin_b12'] += intake_data[-1]['vitamin_b12']
    total['vitamin_c'] += intake_data[-1]['vitamin_c']
    total['vitamin_d'] += intake_data[-1]['vitamin_d']
    total['vitamin_e'] += intake_data[-1]['vitamin_e']
    total['zinc'] += intake_data[-1]['zinc']
  if(len(intake_data)):
    intake_data.append(total)
  return intake_data

@require_http_methods(['GET', 'POST'])
def home(request):
  if request.method == 'POST':
    intake_form = GetDailyIntake(request.POST)
    if intake_form.is_valid():
      intake_data = get_intake(date(
        int(request.POST['date_year']),
        int(request.POST['date_month']),
        int(request.POST['date_day'])))
      return render(request, 'app/home.html', { 'intake_data': intake_data,
        'get_daily_intake_form': GetDailyIntake(),
        'add_intake_form': AddIntake(initial={'timestamp': datetime.now()}) })
  return render(request, 'app/home.html',
    {'get_daily_intake_form': GetDailyIntake(),
      'add_intake_form': AddIntake(initial={'timestamp': datetime.now()}) })

@require_http_methods(['GET', 'POST'])
def intake(request):
  if request.method == 'POST':
    intake_form = AddIntake(request.POST)
    if intake_form.is_valid():
      intake = intake_form .save(commit=False)
      intake.user = request.user
      intake.save()
  return redirect(reverse('home'))

@require_http_methods(['GET', 'POST'])
def food(request):
  if request.method == 'POST':
    food_form = AddFood(request.POST)
    if food_form.is_valid():
      food_form.save()
  food_form = AddFood()
  return render(request, 'app/add_food.html', {'food_form': food_form})

@require_http_methods(['GET', 'POST'])
def target(request):
  return HttpResponse('target')

@require_GET
def food_category(request):
  return HttpResponse('food_category')
