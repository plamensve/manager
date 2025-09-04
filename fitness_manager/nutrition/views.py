from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from datetime import date, timedelta
from .models import Meal
from .forms import MealForm

@login_required
def meal_list(request):
    meals = Meal.objects.filter(user=request.user).order_by('-date')
    today = date.today()
    today_meals = meals.filter(date=today)
    
    # Calculate daily totals
    daily_totals = today_meals.aggregate(
        total_calories=Sum('calories'),
        total_protein=Sum('protein'),
        total_carbs=Sum('carbs'),
        total_fat=Sum('fat')
    )
    
    context = {
        'meals': meals,
        'today_meals': today_meals,
        'daily_totals': daily_totals,
        'today': today,
    }
    return render(request, 'nutrition/meal_list.html', context)

@login_required
def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            messages.success(request, 'Meal added successfully!')
            return redirect('meal_list')
    else:
        form = MealForm()
    
    return render(request, 'nutrition/add_meal.html', {'form': form})
