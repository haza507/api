from django.db import models
# Create your models here.
class Tareas(models.Model):
    nombre = models.CharField('Nombre',max_length=150)
    descripcion = models.TextField("descripcion", max_length=250,null=True,blank=True)
    imagen = models.ImageField('Logo de la tarea', upload_to='tarea/', max_length=200,blank = True,null = True)
    
    class Meta:
        verbose_name = 'nombre'
        verbose_name_plural = 'tareas'
       

    def __str__(self):
        return self.nombre
    
class Tareas2(models.Model):
    nombre = models.CharField('Nombre',max_length=150)
    descripcion = models.TextField("descripcion", max_length=250,null=True,blank=True)
    
    
    class Meta:
        verbose_name = 'nombre'
        verbose_name_plural = 'tareas2'
       

    def __str__(self):
        return self.nombre

def get_image_filename(instance, filename):
        name = instance.tarea.nombre
        return "imagen/{}/{}/". format(name,filename)

class Images(models.Model):
    tarea = models.ForeignKey(Tareas2,default=None,
        on_delete=models.CASCADE,)
    image = models.ImageField(upload_to=get_image_filename,blank = True,null = True)
    
    class Meta:
        verbose_name = 'imagen'
        verbose_name_plural = 'images'
       

    