from django.urls import path
from webapp.views import (
    index_view,
    task_view,
    task_create_view,
    task_update_view,
    task_delete_view
)

urlpatterns = [
    path('', index_view, name='task_list'),
    path('<int:pk>/', task_view, name='task_view'),
    path('add/', task_create_view, name='task_add'),
    path('<int:pk>/update/', task_update_view, name='task_update'),
    path('<int:pk>/delete/', task_delete_view, name='task_delete'),

]