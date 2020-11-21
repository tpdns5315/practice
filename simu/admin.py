from django.contrib import admin

# Register your models here.

from .models import Simu, Comment

admin.site.register(Simu)
admin.site.register(Comment)