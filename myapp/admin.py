from django.contrib.auth import get_user_model
from django.contrib import admin

from .models import  Task

# Register your models here.

admin.site.register(Task)