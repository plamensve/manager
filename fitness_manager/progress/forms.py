from django import forms
from .models import Progress, PersonalRecord

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['weight', 'chest', 'waist', 'biceps']
        widgets = {
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'chest': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'waist': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'biceps': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
        }

class PersonalRecordForm(forms.ModelForm):
    class Meta:
        model = PersonalRecord
        fields = ['exercise', 'weight']
        widgets = {
            'exercise': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
        }
