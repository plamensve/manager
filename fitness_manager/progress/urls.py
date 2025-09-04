from django.urls import path
from . import views

urlpatterns = [
    # Главна страница с прогрес + записи
    path('', views.progress_list, name='progress_list'),

    # Добавяне
    path('add/', views.add_progress, name='add_progress'),
    path('personal-record/add/', views.add_personal_record, name='add_personal_record'),

    # Edit / Update
    path('edit/<int:pk>/', views.edit_progress, name='edit_progress'),
    path('personal-record/edit/<int:pk>/', views.edit_personal_record, name='edit_personal_record'),

    # Delete
    path('delete/<int:pk>/', views.delete_progress, name='delete_progress'),
    path('personal-record/delete/<int:pk>/', views.delete_personal_record, name='delete_personal_record'),
]
