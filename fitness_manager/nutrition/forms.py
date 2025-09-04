from django import forms
from .models import Meal

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'calories', 'protein', 'carbs', 'fat']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'calories': forms.NumberInput(attrs={'class': 'form-control'}),
            'protein': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'carbs': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'fat': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
        }
