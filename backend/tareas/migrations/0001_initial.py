# Generated by Django 3.1.7 on 2021-04-07 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, max_length=250, null=True, verbose_name='descripcion')),
                ('imagen', models.ImageField(blank=True, max_length=200, null=True, upload_to='tarea/', verbose_name='Logo de la tarea')),
            ],
            options={
                'verbose_name': 'nombre',
                'verbose_name_plural': 'tareas',
            },
        ),
    ]