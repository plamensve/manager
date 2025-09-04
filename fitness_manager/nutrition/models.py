from django.db import models
from django.contrib.auth.models import User


class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    protein = models.FloatField(help_text="in grams", null=True, blank=True)
    carbs = models.FloatField(help_text="in grams", null=True, blank=True)
    fat = models.FloatField(help_text="in grams", null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.name} ({self.calories} kcal)"
