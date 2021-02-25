from django.shortcuts import render
from task.models import Task


def index_view(request):
    return render(request, 'index.html')

def task_view(request):
    """
    Представление для отображение одной статьи
    """
    task_id = request.GET.get('id')
    task = Task.objects.get(id=task_id)
    return render(request, 'task_view.html', context={'task': task})


def task_create_view(request):
    """
    Представление для создания статьи
    """
    if request.method == "GET":  # Если метод запроса GET - будет отображена форма создания статьи
        return render(request, 'task_create.html')
    elif request.method == "POST":  # Если метод запроса POST - будет отображён шаблон просмотра деталей статьи
        description = request.POST.get("title")
        status = request.POST.get("content")
        date_done = request.POST.get("author")

        article = Task.objects.create(
            description=description,
            status=status,
            date_done=date_done
        )

        return render(request, 'task_view.html', context={'task': task})

# Create your views here.
