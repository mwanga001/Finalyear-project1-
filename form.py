from django import forms
from . models import application
from bootstrap_datepicker_plus.widgets import DatePickerInput

class DataForm(forms.ModelForm):
    class Meta:
        model=application
        fields="__all__"
        widgets={
            'date_registered':DatePickerInput()
        }