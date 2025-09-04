from django import forms
from .models import Exercise

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'category', 'description', 'video_url']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'video_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://youtube.com/watch?v=...'}),
        }
