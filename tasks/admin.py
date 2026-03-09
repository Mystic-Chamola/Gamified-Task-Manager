from django.contrib import admin
from .models import Task, Points, Streak

# Register your models here.
admin.site.register(Task)
admin.site.register(Points)
admin.site.register(Streak)
