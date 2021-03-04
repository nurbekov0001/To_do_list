from django import forms
from webapp.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('description', 'detailed_description', 'status', 'date_done')


class TaskDeleteForm(forms.Form):
    description = forms.CharField(max_length=120, required=True, label='Введите название задачи, чтобы удалить её')
