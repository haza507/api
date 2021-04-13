from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
  
class User(AbstractUser):
    imagen = models.ImageField('Imagen de Perfil', upload_to='perfil',default='perfil/usuario.png', max_length=200,blank = True,null = True)
    opciones_sexo = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    sexo = models.CharField(max_length=1, choices=opciones_sexo,blank = True,null = True)
    # Sexo
    opciones_tipo = (
        ('Administrador', 'Administrador'),
        ('Docente', 'Docente'),
        ('Estudiante', 'Estudiante'),
        ('Padre', 'Padre'),
    )
    tipo = models.CharField('Tipo',max_length=50,choices=opciones_tipo,blank = True,null = True)
    # Tipo de usuario
     
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
        

    def __str__(self):
        return f'{self.username}'

class Generales(models.Model):
    nombre = models.CharField('Nombre',max_length=150)
    correo = models.EmailField("correo", max_length=100,null=True,blank=True)
    web = models.URLField('Pagina web', max_length=100,null=True,blank=True)
    imagen = models.ImageField('Logo de la institución', upload_to='logo/', max_length=200,blank = True,null = True)
    
    class Meta:
        verbose_name = 'Institución'
        verbose_name_plural = 'General'
       

    def __str__(self):
        return self.nombre

