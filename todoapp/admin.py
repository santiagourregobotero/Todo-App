from django.contrib import admin
from todoapp.models import User,Tasks

# Register your models here.
admin.site.register(User)
admin.site.register(Tasks)