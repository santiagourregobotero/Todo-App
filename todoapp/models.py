from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
    



class Priority(models.TextChoices):
    HIGH = "1"
    MEDIUM = "2"
    LOW = "3"





class Tasks(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_tasks")
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10,choices=Priority.choices,default=Priority.LOW)
    due_date = models.DateField(blank=True,null=True)




