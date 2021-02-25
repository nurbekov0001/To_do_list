from django.db import models


STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class Task(models.Model):
    description = models.TextField(max_length=3000, null=False, blank=False,verbose_name="Описание задачи")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, null=True, blank=True, default='new',verbose_name="Статус задачи")
    date_done = models.DateField(null=True, blank=True,verbose_name="Время создания задачи")

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.id}. {self.description}: {self.status} {self.date_done}'
# Create your models here.
