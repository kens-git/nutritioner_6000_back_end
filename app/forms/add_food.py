from django import forms
from ..models import Food, NutrientUnit

class AddFood(forms.ModelForm):
  field_order = ['name', 'category', 'unit', 'reference_size']

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
      field.widget.attrs['placeholder'] = ''
