from django.urls import path
from . import views

urlpatterns = [
    path('', views.exercise_list, name='exercise_list'),
    path('add/', views.add_exercise, name='add_exercise'),
    path('<int:exercise_id>/', views.exercise_detail, name='exercise_detail'),
    path('<int:exercise_id>/edit/', views.edit_exercise, name='edit_exercise'),
]
