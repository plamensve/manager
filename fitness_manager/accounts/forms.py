from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'height', 'weight', 'goal']
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'goal': forms.Select(attrs={'class': 'form-control'}),
        }
