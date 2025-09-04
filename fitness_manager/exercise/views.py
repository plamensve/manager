from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Exercise
from .forms import ExerciseForm

def exercise_list(request):
    exercises = Exercise.objects.all()
    categories = Exercise.CATEGORY_CHOICES
    selected_category = request.GET.get('category')
    
    if selected_category:
        exercises = exercises.filter(category=selected_category)
    
    context = {
        'exercises': exercises,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'exercise/exercise_list.html', context)

def exercise_detail(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    return render(request, 'exercise/exercise_detail.html', {'exercise': exercise})

@login_required
def add_exercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Exercise added successfully!')
            return redirect('exercise_list')
    else:
        form = ExerciseForm()
    
    return render(request, 'exercise/add_exercise.html', {'form': form})

@login_required
def edit_exercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            messages.success(request, 'Exercise updated successfully!')
            return redirect('exercise_detail', exercise_id=exercise.id)
    else:
        form = ExerciseForm(instance=exercise)
    
    return render(request, 'exercise/edit_exercise.html', {'form': form, 'exercise': exercise})
