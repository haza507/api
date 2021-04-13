from rest_framework import serializers
from tareas.models import Tareas

class TareasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = ('id','nombre','descripcion','imagen')

