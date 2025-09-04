from django.contrib import admin
from .models import Meal

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'date', 'calories', 'protein', 'carbs', 'fat']
    list_filter = ['date', 'user']
    search_fields = ['user__username', 'name']
    list_editable = ['calories', 'protein', 'carbs', 'fat']
    date_hierarchy = 'date'
