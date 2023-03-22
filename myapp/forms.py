from django import forms
from .models import Task, UserProfile #UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']

# shall use a generic one!
class UserProfileForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username']
    def save(self, commit=True):
        user = super(UserProfileForm, self).save(commit=False)
        if commit:
            user.save()
        return user

class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"

'''
class TaskForm(forms.ModelForm):
    class meta:

        model = Task
        title = forms.CharField(label='Task Title', max_length=100)
        dsc = forms.CharField(label='Task Description', max_length=550)
        completed = forms.BooleanField(label='You didnt finish that. did you!', initial=True)
'''