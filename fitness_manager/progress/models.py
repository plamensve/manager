from django.db import models
from django.contrib.auth.models import User


class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    weight = models.FloatField(help_text="in kilograms")
    chest = models.FloatField(help_text="in cm", null=True, blank=True)
    waist = models.FloatField(help_text="in cm", null=True, blank=True)
    biceps = models.FloatField(help_text="in cm", null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"


class PersonalRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.CharField(max_length=100)
    weight = models.FloatField(help_text="in kilograms")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.exercise}: {self.weight} kg"
