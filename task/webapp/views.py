from django.shortcuts import render
from webapp.models import Task, STATUS_CHOICES


def index_view(request):

    tasks = Task.objects.all()
    return render(request, 'index.html', context={'tasks': tasks})


def task_view(request):
    task_id = request.GET.get('id')
    task = Task.objects.get(id=task_id)
    return render(request, 'task_view.html', context={'task': task})


def task_create_view(request):
    if request.method == "GET":  # Если метод запроса GET - будет отображена форма создания статьи
        return render(request, 'task_create.html', {'stat': STATUS_CHOICES})
    elif request.method == "POST":  # Если метод запроса POST - будет отображён шаблон просмотра деталей статьи
        description = request.POST.get("description")
        status = request.POST.get("status")
        date_done = request.POST.get("date_done")

        task = Task.objects.create(
            description=description,
            status=status,
            date_done=date_done
        )

        return render(request, 'task_view.html', context={'task': task})

# Create your views here.
