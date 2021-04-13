from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import User,Generales



# Register your models here.

admin.site.register(Generales)

admin.site.register(User, UserAdmin)