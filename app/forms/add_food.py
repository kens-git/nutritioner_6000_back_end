from typing import Type
from django import forms
from ..models import Food, NutrientUnit

def make_unit_choices(unit: str):
  return [(1, 'DV%'), (2, unit)]

class AddFood(forms.ModelForm):
  biotin_unit = forms.ChoiceField(choices=make_unit_choices('ug'),
    initial=1, widget=forms.RadioSelect)
  calcium_unit = forms.ChoiceField(choices=make_unit_choices('mg'),
    initial=1, widget=forms.RadioSelect)
  chromium_unit = forms.ChoiceField(choices=make_unit_choices('ug'),
    widget=forms.RadioSelect, initial=1)
  copper_unit = forms.ChoiceField(choices=make_unit_choices('mg'),
    widget=forms.RadioSelect, initial=1)
  folacin_unit = forms.ChoiceField(choices=make_unit_choices('ug'),
    widget=forms.RadioSelect, initial=1)
  iodide_unit = forms.ChoiceField(choices=make_unit_choices('ug'),
    widget=forms.RadioSelect, initial=1)
  iron_unit = forms.ChoiceField(choices=make_unit_choices('mg'),
    widget=forms.RadioSelect, initial=1)
  magnesium_unit = forms.ChoiceField(choices=make_unit_choices('mg'),
    widget=forms.RadioSelect, initial=1)
  manganese_unit = forms.ChoiceField(choices=make_unit_choices('mg'),
    widget=forms.RadioSelect, initial=1)
  molybdenum_unit = forms.ChoiceField(choices=make_unit_choices('ug'),
    widget=forms.RadioSelect, initial=1)
  niacin_unit = forms.ChoiceField(choices=make_unit_choices('NE'),
    widget=forms.RadioSelect, initial=1)
  pantothenate_unit = forms.ChoiceField(choices=make_unit_choices('mg'),
    widget=forms.RadioSelect, initial=1)
  phosphorous_unit = forms.ChoiceField(choices=make_unit_choices('mg'),
    widget=forms.RadioSelect, initial=1)
  potassium_unit = forms.ChoiceField(choices=make_unit_choices('mg'),
    widget=forms.RadioSelect, initial=1)
  riboflavin_unit = forms.ChoiceField(choices=make_unit_choices('mg'),
    widget=forms.RadioSelect, initial=1)
  selenium_unit = forms.ChoiceField(choices=make_unit_choices('ug'),
    widget=forms.RadioSelect, initial=1)
  thiamine_unit = forms.ChoiceField(choices=make_unit_choices('mg'),
    widget=forms.RadioSelect, initial=1)
  vitamin_a_unit = forms.ChoiceField(choices=make_unit_choices('RE'),
    widget=forms.RadioSelect, initial=1)
  vitamin_b6_unit = forms.ChoiceField(choices=make_unit_choices('mg'),
    widget=forms.RadioSelect, initial=1)
  vitamin_b12_unit = forms.ChoiceField(choices=make_unit_choices('ug'),
    widget=forms.RadioSelect, initial=1)
  vitamin_c_unit = forms.ChoiceField(choices=make_unit_choices('mg'),
    widget=forms.RadioSelect, initial=1)
  vitamin_d_unit = forms.ChoiceField(choices=make_unit_choices('ug'),
    widget=forms.RadioSelect, initial=1)
  vitamin_e_unit = forms.ChoiceField(choices=make_unit_choices('mg'),
    widget=forms.RadioSelect, initial=1)
  zinc_unit = forms.ChoiceField(choices=make_unit_choices('mg'),
    widget=forms.RadioSelect, initial=1)

  class Meta:
    model = Food
    fields = '__all__'
    widgets = {
      'name': forms.TextInput(),
    }

  def __init__(self, *args, **kwargs):
    super(forms.ModelForm, self).__init__(*args, **kwargs)
    for name, field in self.fields.items():
      abbreviation = NutrientUnit.objects.filter(nutrient_name=name).first()
      if abbreviation:
        # TODO: store nutrient display names in a model
        field.label = (name.replace('_', ' ').title() +
          ' ({})'.format(abbreviation.unit.abbreviation))
      if name != 'name' and field.initial != 1:
        field.initial = 0
      field.widget.attrs['placeholder'] = ''
