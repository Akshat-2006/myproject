from django.shortcuts import render, redirect
from django.shortcuts import reverse
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.views.generic.edit import CreateView, UpdateView
from .models import Task, UserProfile
from .forms import TaskForm, UserProfileForm, UserDetailForm
from django.views.generic.edit import DeleteView
from .forms import TaskForm
from django import forms
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def create_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('/know') #redirection... To login...
    else:
        form = UserProfileForm()
    return render(request, 'myapp/create_user_profile.html', {'form': form})

class more_details(CreateView):
    template_name = 'myapp/more.html'
    model = UserProfile
    form_class = UserDetailForm
    success_url = 'login/'
    
    def form_valid(self, form):
        detail = form.save(commit=False)
        detail.save()

        form.instance.owner = self.request.user
        inst = super().form_valid(form)
        return inst

class LoginView(View):
    form_class = AuthenticationForm
    template_name = 'myapp/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        return render(request, self.template_name, {'form': form})

def Style_test(request):
    return render(request, 'myapp/styling.html')

#form view
class MyFormView(FormView):
    template_name = 'myapp/mypage.html'
    form_class = TaskForm

# This one would bring all in one page (view inheritance)
# thats one way to do that
class CreateCumListView(CreateView, ListView, LoginRequiredMixin):
    template_name='myapp/mypage.html'
    form_class = TaskForm
    model = Task
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        if form.instance.user is not None:
            inst = super().form_valid(form)
            return inst

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            # Add user-specific content to the context
            context['user_content'] = 'Hello, ' + self.request.user.username
        return context

class TaskDetailView(DetailView):
    model = Task
    template_name = 'myapp/task_detail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'myapp/task_form.html'
    success_url = '/'

'''
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = self.get_queryset()
        return context

def post(self, request, *args, **kwargs):
        if 'delete' in request.POST:
            return self.delete(request, *args, **kwargs)
        else:    
            return super().post(request, *args, **kwargs)
    
def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        self.get_object().delete()
        return self.get(request, *args, **kwargs)

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'myapp/mypage.html'
    success_url = reverse_lazy('myapp:task-list')        
'''