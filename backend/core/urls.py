from django.urls import path, include
from django.contrib.auth.decorators import login_required
from core.views import *

 

urlpatterns = [
    path('',login_required(InicioViews.as_view()),name='inicio'),
    
]
