from django.db import models


class Exercise(models.Model):
    CATEGORY_CHOICES = [
        ('chest', 'Chest'),
        ('back', 'Back'),
        ('legs', 'Legs'),
        ('arms', 'Arms'),
        ('shoulders', 'Shoulders'),
        ('abs', 'Abs'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
