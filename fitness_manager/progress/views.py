from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Progress, PersonalRecord
from .forms import ProgressForm, PersonalRecordForm


@login_required
def progress_list(request):
    progress_entries = Progress.objects.filter(user=request.user).order_by('-date')
    personal_records = PersonalRecord.objects.filter(user=request.user).order_by('-date')

    context = {
        'progress_entries': progress_entries,
        'personal_records': personal_records,
    }
    return render(request, 'progress/progress_list.html', context)


@login_required
def add_progress(request):
    if request.method == 'POST':
        form = ProgressForm(request.POST)
        if form.is_valid():
            progress = form.save(commit=False)
            progress.user = request.user
            progress.save()
            messages.success(request, 'Progress entry added successfully!')
            return redirect('progress_list')
    else:
        form = ProgressForm()

    return render(request, 'progress/add_progress.html', {'form': form})


@login_required
def add_personal_record(request):
    if request.method == 'POST':
        form = PersonalRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            messages.success(request, 'Personal record added successfully!')
            return redirect('progress_list')
    else:
        form = PersonalRecordForm()

    return render(request, 'progress/add_personal_record.html', {'form': form})

# --- EDIT PROGRESS ---
@login_required
def edit_progress(request, pk):
    entry = get_object_or_404(Progress, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ProgressForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Progress entry updated successfully!')
            return redirect('progress_list')
    else:
        form = ProgressForm(instance=entry)
    return render(request, 'progress/edit_progress.html', {'form': form})

# --- DELETE PROGRESS ---
@login_required
def delete_progress(request, pk):
    entry = get_object_or_404(Progress, pk=pk, user=request.user)
    if request.method == 'POST':
        entry.delete()
        messages.success(request, 'Progress entry deleted.')
        return redirect('progress_list')
    return render(request, 'progress/confirm_delete.html', {'entry': entry})


# --- EDIT PERSONAL RECORD ---
@login_required
def edit_personal_record(request, pk):
    record = get_object_or_404(PersonalRecord, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PersonalRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Personal record updated successfully!')
            return redirect('progress_list')
    else:
        form = PersonalRecordForm(instance=record)
    return render(request, 'progress/edit_personal_record.html', {'form': form})

# --- DELETE PERSONAL RECORD ---
@login_required
def delete_personal_record(request, pk):
    record = get_object_or_404(PersonalRecord, pk=pk, user=request.user)
    if request.method == 'POST':
        record.delete()
        messages.success(request, 'Personal record deleted.')
        return redirect('progress_list')
    return render(request, 'progress/confirm_delete.html', {'record': record})