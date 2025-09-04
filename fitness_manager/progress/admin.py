from django.contrib import admin
from .models import Progress, PersonalRecord

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'weight', 'chest', 'waist', 'biceps']
    list_filter = ['date', 'user']
    search_fields = ['user__username']
    list_editable = ['weight', 'chest', 'waist', 'biceps']
    date_hierarchy = 'date'

@admin.register(PersonalRecord)
class PersonalRecordAdmin(admin.ModelAdmin):
    list_display = ['user', 'exercise', 'weight', 'date']
    list_filter = ['date', 'user', 'exercise']
    search_fields = ['user__username', 'exercise']
    list_editable = ['weight']
    date_hierarchy = 'date'
