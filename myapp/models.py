from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='null')
    description = models.CharField(max_length=200, default='null')
    completed = models.BooleanField(default=False)
    #task_holder = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields for the user profile here
    # For example:
    # An additional field added (boolen)
    marital_status = models.BooleanField(default=False)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    '''
    def get_absolute_url(self):
        return reverse_lazy('', args=[str(self.id)])
    '''

    '''
    def __str__(self):
        return self.user.username
    '''

