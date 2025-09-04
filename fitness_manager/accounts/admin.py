from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'height', 'weight', 'goal']
    list_filter = ['goal', 'age']
    search_fields = ['user__username', 'user__email']
    list_editable = ['age', 'height', 'weight', 'goal']
