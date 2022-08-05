from copyreg import add_extension
from datetime import datetime, date, time
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods, require_GET
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import DailyValue, Food, Intake, NutrientUnit, Target
from .forms.add_food import AddFood, NutrientUnitType
from .forms.add_intake import AddIntake
from .forms.get_daily_intake import GetDailyIntake
from .forms.get_target import GetTarget

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

def get_target_data(target):
  return {
    'food_name': 'Target',  # TODO: remember this is here when fixing repeated code
    'category': '',         # TODO
    'serving_size': '',     # TODO
    'unit': '',             # TODO
    'fat': target.fat,
    'saturated_fat': target.saturated_fat,
    'trans_fat': target.trans_fat,
    'cholesterol': target.cholesterol,
    'sodium': target.sodium,
    'carbohydrates': target.carbohydrates,
    'fibre': target.fibre,
    'sugar': target.sugar,
    'protein': target.protein,
    'biotin': target.biotin,
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
def get_intake(user, selected_date: date):
  # TODO
  start_time = datetime.combine(selected_date, time(00, 00, 00))
  end_time = datetime.combine(selected_date, time(23, 59, 59))
  intake_data = []
  intake = Intake.objects.filter(user=user).filter(timestamp__range=(start_time, end_time)).all()
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
  if target := Target.objects.filter(user=user).latest('timestamp'):
    intake_data.append(get_target_data(target))
  return intake_data

@login_required
@require_http_methods(['GET', 'POST'])
def home(request):
  if request.method == 'POST':
    intake_form = GetDailyIntake(request.POST)
    if intake_form.is_valid():
      requested_date = date(
        int(request.POST['date_year']),
        int(request.POST['date_month']),
        int(request.POST['date_day']))
      intake_data = get_intake(request.user, requested_date)
      return render(request, 'app/home.html', { 'intake_data': intake_data,
        'get_daily_intake_form': GetDailyIntake(initial={'date': requested_date}),
        'add_intake_form': AddIntake(initial={'timestamp': datetime.now()}) })
  intake_data = get_intake(request.user, date.today())
  return render(request, 'app/home.html',
    { 'intake_data': intake_data, 'get_daily_intake_form': GetDailyIntake(initial={'date': date.today() }),
      'add_intake_form': AddIntake(initial={'timestamp': datetime.now()}) })

@login_required
@require_http_methods(['GET', 'POST'])
def intake(request):
  if request.method == 'POST':
    intake_form = AddIntake(request.POST)
    if intake_form.is_valid():
      intake = intake_form .save(commit=False)
      intake.user = request.user
      intake.save()
  return redirect(reverse('home'))

# TODO: Maybe use a dict for NutrientUnitType, because the form returns
#       its value as a string, and the values can't be compared for some reason
#       i.e., NutrientUnitType.DAILY_VALUE == a doesn't work
def get_nutrient_value(name: str, value: float, type: NutrientUnitType):
  if type == NutrientUnitType.DAILY_VALUE.value:
    dv = DailyValue.objects.filter(nutrient_name=name).first()
    return (value / 100) * dv.value
  return value

@login_required
@require_http_methods(['GET', 'POST'])
def food(request):
  if request.method == 'POST':
    food_form = AddFood(request.POST)
    if food_form.is_valid():
      food = food_form.save(commit=False)
      food.biotin = get_nutrient_value(
        'biotin', food.biotin, int(food_form['biotin_unit'].data))
      food.calcium = get_nutrient_value(
        'calcium', food.calcium, int(food_form['calcium_unit'].data))
      food.chromium = get_nutrient_value(
        'chromium', food.chromium, int(food_form['chromium_unit'].data))
      food.copper = get_nutrient_value(
        'copper', food.copper, int(food_form['copper_unit'].data))
      food.folacin = get_nutrient_value(
        'folacin', food.folacin, int(food_form['folacin_unit'].data))
      food.iodide = get_nutrient_value(
        'iodide', food.iodide, int(food_form['iodide_unit'].data))
      food.iron = get_nutrient_value(
        'iron', food.iron, int(food_form['iron_unit'].data))
      food.magnesium = get_nutrient_value(
        'magnesium', food.magnesium, int(food_form['magnesium_unit'].data))
      food.manganese = get_nutrient_value(
        'manganese', food.manganese, int(food_form['manganese_unit'].data))
      food.molybdenum = get_nutrient_value(
        'molybdenum', food.molybdenum, int(food_form['molybdenum_unit'].data))
      food.niacin = get_nutrient_value(
        'niacin', food.niacin, int(food_form['niacin_unit'].data))
      food.pantothenate = get_nutrient_value(
        'pantothenate', food.pantothenate, int(food_form['pantothenate_unit'].data))
      food.phosphorous = get_nutrient_value(
        'phosphorous', food.phosphorous, int(food_form['phosphorous_unit'].data))
      food.potassium = get_nutrient_value(
        'potassium', food.potassium, int(food_form['potassium_unit'].data))
      food.riboflavin = get_nutrient_value(
        'riboflavin', food.riboflavin, int(food_form['riboflavin_unit'].data))
      food.selenium = get_nutrient_value(
        'selenium', food.selenium, int(food_form['selenium_unit'].data))
      food.thiamine = get_nutrient_value(
        'thiamine', food.thiamine, int(food_form['thiamine_unit'].data))
      food.vitamin_a = get_nutrient_value(
        'vitamin_a', food.vitamin_a, int(food_form['vitamin_a_unit'].data))
      food.vitamin_b6 = get_nutrient_value(
        'vitamin_b6', food.vitamin_b6, int(food_form['vitamin_b6_unit'].data))
      food.vitamin_b12 = get_nutrient_value(
        'vitamin_b12', food.vitamin_b12, int(food_form['vitamin_b12_unit'].data))
      food.vitamin_c = get_nutrient_value(
        'vitamin_c', food.vitamin_c, int(food_form['vitamin_c_unit'].data))
      food.vitamin_d = get_nutrient_value(
        'vitamin_d', food.vitamin_d, int(food_form['vitamin_d_unit'].data))
      food.vitamin_e = get_nutrient_value(
        'vitamin_e', food.vitamin_e, int(food_form['vitamin_e_unit'].data))
      food.zinc = get_nutrient_value(
        'zinc', food.zinc, int(food_form['zinc_unit'].data))
      food.save()
  food_form = AddFood()
  return render(request, 'app/add_food.html', {'food_form': food_form})

@login_required
@require_http_methods(['GET', 'POST'])
def target(request):
  success = False
  if request.method == 'POST':
    get_target_form = GetTarget(request.POST)
    if get_target_form.is_valid():
      target = get_target_form.save(commit=False)
      target.user = request.user
      target.timestamp = datetime.now()
      target.save()
      success = True
  get_target_form = GetTarget()
  return render(request, 'app/target.html',
    {'get_target_form': get_target_form, 'success': success})

@login_required
@require_GET
def food_category(request):
  return HttpResponse('food_category')
