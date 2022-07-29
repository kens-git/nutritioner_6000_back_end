from django import forms
from ..models import Intake

class AddIntake(forms.ModelForm):
  class Meta:
    model = Intake
    fields = ['food', 'serving_size', 'timestamp']
