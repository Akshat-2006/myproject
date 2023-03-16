from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']

'''
class TaskForm(forms.ModelForm):
    class meta:

        model = Task
        title = forms.CharField(label='Task Title', max_length=100)
        dsc = forms.CharField(label='Task Description', max_length=550)
        completed = forms.BooleanField(label='You didnt finish that. did you!', initial=True)
'''