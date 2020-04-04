from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Person)
admin.site.register(models.Gate)
admin.site.register(models.Log)
admin.site.register(models.Image)
