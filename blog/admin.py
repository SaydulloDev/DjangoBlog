from django.contrib import admin
from django.contrib.admin.models import LogEntry

from . import models

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Post)
admin.site.register(models.Author)
admin.site.register(models.Tag)
LogEntry.objects.all().delete()
