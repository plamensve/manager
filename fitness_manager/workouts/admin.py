from django.contrib import admin
from .models import Workout, WorkoutExercise

class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutExercise
    extra = 1

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'notes']
    list_filter = ['date', 'user']
    search_fields = ['user__username', 'notes']
    date_hierarchy = 'date'
    inlines = [WorkoutExerciseInline]

@admin.register(WorkoutExercise)
class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ['workout', 'exercise', 'sets', 'reps', 'weight']
    list_filter = ['exercise__category', 'workout__date']
    search_fields = ['workout__user__username', 'exercise__name']
    list_editable = ['sets', 'reps', 'weight']
