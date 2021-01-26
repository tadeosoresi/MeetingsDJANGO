from django.db import models

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
    codigo_postal = models.IntegerField(max_length=4)

    def __str__(self):
        return 'El usuario es %s y el email %s' % (self.usuario, self.email)
