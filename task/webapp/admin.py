from django.contrib import admin
from task.models import Task


class TasksAdmin(admin.ModelAdmin):
    list_display = ['id','description','status',' date_done']
    list_filter = ['status']
    fields = ['id','description','status','date_done']

admin.site.register(Task, TasksAdmin)
# Register your models here.
