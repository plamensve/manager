from django import forms
from .models import Workout, WorkoutExercise
from fitness_manager.exercise.models import Exercise

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class WorkoutExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutExercise
        fields = ['exercise', 'sets', 'reps', 'weight']
        widgets = {
            'exercise': forms.Select(attrs={'class': 'form-control'}),
            'sets': forms.NumberInput(attrs={'class': 'form-control'}),
            'reps': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['exercise'].queryset = Exercise.objects.all()
