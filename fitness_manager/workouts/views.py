from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Workout, WorkoutExercise
from .forms import WorkoutForm, WorkoutExerciseForm
from fitness_manager.exercise.models import Exercise

@login_required
def workout_list(request):
    workouts = Workout.objects.filter(user=request.user).order_by('-date')
    return render(request, 'workouts/workout_list.html', {'workouts': workouts})

@login_required
def workout_detail(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)
    exercises = workout.exercises.all()
    return render(request, 'workouts/workout_detail.html', {
        'workout': workout,
        'exercises': exercises
    })

@login_required
def add_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            messages.success(request, 'Workout created successfully!')
            return redirect('workout_detail', workout_id=workout.id)
    else:
        form = WorkoutForm()
    
    return render(request, 'workouts/add_workout.html', {'form': form})

@login_required
def add_exercise_to_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)
    
    if request.method == 'POST':
        form = WorkoutExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.workout = workout
            exercise.save()
            messages.success(request, 'Exercise added to workout!')
            return redirect('workout_detail', workout_id=workout.id)
    else:
        form = WorkoutExerciseForm()
    
    return render(request, 'workouts/add_exercise.html', {
        'form': form,
        'workout': workout
    })
