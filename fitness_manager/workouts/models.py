from django.db import models
from django.contrib.auth.models import User
from fitness_manager.exercise.models import Exercise


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="exercises")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.FloatField(help_text="in kilograms", null=True, blank=True)

    def __str__(self):
        return f"{self.workout} - {self.exercise.name}"
