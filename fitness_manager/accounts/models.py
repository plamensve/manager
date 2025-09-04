from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    GOAL_CHOICES = [
        ('lose_weight', 'Lose Weight'),
        ('gain_muscle', 'Gain Muscle'),
        ('endurance', 'Endurance'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    height = models.FloatField(help_text="in centimeters", null=True, blank=True)
    weight = models.FloatField(help_text="in kilograms", null=True, blank=True)
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.user.username
