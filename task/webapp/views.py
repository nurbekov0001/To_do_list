from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from webapp.models import Task, STATUS_CHOICES
from webapp.forms import TaskForm, TaskDeleteForm


def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={'tasks': tasks})


def task_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    return render(request, 'task_view.html', context={'task': task})


def task_create_view(request):
    if request.method == "GET":
        form = TaskForm()
        return render(request, 'task_create.html', {'stat': STATUS_CHOICES})
    elif request.method == "POST":
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                description=form.cleaned_data.get("description"),
                status=form.cleaned_data.get("status"),
                date_done=form.cleaned_data.get("date_done"),
                detailed_description=form.cleaned_data.get("detailed_description")
            )

            return redirect('task_view', pk=task.id)
        return render(request, 'task_create.html', context={'form': form})


def task_update_view(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'GET':
        form = TaskForm(initial={
            'description': task.description,
            'detailed_description': task.detailed_description,
            'status': task.status,
            'date_done': task.date_done
        })
        return render(request, 'task_update.html', context={'form': form, 'task': task})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.description = form.cleaned_data.get("description")
            task.detailed_description = form.cleaned_data.get("detailed_description")
            task.status = form.cleaned_data.get("status")
            task.date_done = form.cleaned_data.get("date_done")
            task.save()
            return redirect('task_view', pk=task.id)
        return render(request, 'task_update.html', context={'form': form, 'task': task})


def task_delete_view(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'GET':
        form = TaskDeleteForm()
        return render(request, 'task_delete.html', context={'task': task, 'form': form})
    elif request.method == 'POST':
        form = TaskDeleteForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['description'] != task.description:
                form.errors['description'] = ['Названия статей не совпадают']
                return render(request, 'task_delete.html', context={'task': task, 'form': form})
            task.delete()
            return redirect('task_list')
        return render(request, 'task_delete.html', context={'task': task, 'form': form})
