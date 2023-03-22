from django.urls import path
from .views import TaskDetailView, TaskUpdateView, CreateCumListView, create_user_profile, Style_test
from .views import LoginView, more_details
app_name = 'myapp'
urlpatterns = [
    path('', CreateCumListView.as_view(), name='task-list'),
    #path('', TaskListView.as_view(), name='task-list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    #path('create', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    #path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('style/', Style_test, name='style-test'),
    path('register/', create_user_profile, name='create_user_profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('know/', more_details.as_view(), name='know')
]
