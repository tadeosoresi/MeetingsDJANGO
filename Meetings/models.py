from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

#Database de usuarios registrados   
class Usuarios(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30) #argumento verbose_name explica como debe aparecer en panel administración
    usuario = models.CharField(max_length=15)
    email = models.EmailField()
    tel = models.IntegerField()
    sex = models.CharField(max_length=1)
    provincia = models.CharField(max_length=30)
    codigo_postal = models.IntegerField()

    def __str__(self):
        return 'El usuario es %s y el email %s' % (self.usuario, self.email)

#Mapeo ORM
class Espacios(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='meetings')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Espacio'
        verbose_name_plural = 'Espacios'
    
    def __str__(self):
        return self.titulo