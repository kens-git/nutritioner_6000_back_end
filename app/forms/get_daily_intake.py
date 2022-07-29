from tkinter.tix import Form
from django import forms

class GetDailyIntake(forms.Form):
  date = forms.DateField(widget=forms.SelectDateWidget)
