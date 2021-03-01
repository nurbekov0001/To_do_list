from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.models import Task, STATUS_CHOICES


def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={'tasks': tasks})


def task_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    return render(request, 'task_view.html', context={'task': task})


def task_create_view(request):
    if request.method == "GET":  # Если метод запроса GET - будет отображена форма создания статьи
        return render(request, 'task_create.html', {'stat': STATUS_CHOICES})
    elif request.method == "POST":  # Если метод запроса POST - будет отображён шаблон просмотра деталей статьи
        description = request.POST.get("description")
        status = request.POST.get("status")
        date_done = request.POST.get("date_done")
        detailed_description = request.POST.get("detailed_description")

        task = Task.objects.create(
            description=description,
            detailed_description=detailed_description,
            status=status,
            date_done=date_done
        )

        return redirect(reverse('task_view', kwargs={'pk': task.id}))
# Create your views here.
