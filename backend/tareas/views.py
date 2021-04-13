from django.shortcuts import render
from rest_framework import viewsets,status,permissions
from tareas.models import Tareas
from tareas.serializers import TareasSerializer
# Create your views here.
class TareasViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication,]
    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer