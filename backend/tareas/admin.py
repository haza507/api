
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tareas.models import Tareas, Tareas2, Images



# Register your models here.

admin.site.register(Tareas)
admin.site.register(Tareas2)
admin.site.register(Images)