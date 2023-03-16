from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.views.generic.edit import CreateView, UpdateView
from .models import Task
from .forms import TaskForm
from django.views.generic.edit import DeleteView
from .forms import TaskForm
from django import forms

# Create your views here.
def Style_test(request):
    return render(request, 'myapp/styling.html')

#form view
class MyFormView(FormView):
    template_name = 'myapp/mypage.html'
    form_class = TaskForm


# This one would bring all in one page (view inheritance)
# thats one way to do that
class CreateCumListView(CreateView, ListView):
    template_name='myapp/mypage.html'
    form_class = TaskForm
    model = Task
    success_url = '/'

    def form_valid(self, form):

        inst = super().form_valid(form)
        return inst

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